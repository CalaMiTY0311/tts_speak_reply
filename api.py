import uvicorn
from fastapi import APIRouter, Request
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse

import nltk
from contextlib import asynccontextmanager

from router.character.KusanagiNene import KusanagiNene
from router.character.SangonomiyaKokomi import SangonomiyaKokomi
from router.category import category

import argparse
import config as global_config
g_config = global_config.Config()

# 获取参数
parser = argparse.ArgumentParser(description="GPT-SoVITS api")
parser.add_argument("-a", "--bind_addr", type=str, default="0.0.0.0", help="default: 0.0.0.0")
parser.add_argument("-p", "--port", type=int, default=g_config.api_port, help="default: 9880")

args = parser.parse_args()
port = args.port
host = args.bind_addr


# 일본어 문장 나누는 함수
# import MeCab
# def split_text_by_mecab(text, length=30):
#     tagger = MeCab.Tagger("-Owakati")  # 단어 단위로 띄어쓰기
#     words = tagger.parse(text).strip().split()
    
#     result, current = [], ""
#     for word in words:
#         if len(current) + len(word) > length:
#             result.append(current)
#             current = word
#         else:
#             current += (" " if current else "") + word

#     if current:
#         result.append(current)

#     return result

# print(type(kusanagi_nene))

def check_nltk_resource(resource_path):
    """NLTK 리소스 확인 및 필요시 다운로드"""
    try:
        # 리소스 존재 여부 확인
        resource_file = nltk.data.find(resource_path)
        print(f"NLTK 리소스 '{resource_path}'가 이미 설치되어 있습니다: {resource_file}")
    except LookupError:
        # 리소스가 없으면 다운로드
        print(f"NLTK 리소스 '{resource_path}'가 설치되어 있지 않습니다. 설치를 시작합니다...")
        
        # 리소스 경로에서 패키지 이름 추출
        if '/' in resource_path:
            package_name = resource_path.split('/')[-1]
        else:
            package_name = resource_path
            
        nltk.download('averaged_perceptron_tagger_eng')
        print(f"NLTK 리소스 '{resource_path}' 설치가 완료되었습니다.")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 애플리케이션 시작 시 실행할 코드
    print("애플리케이션 시작: NLTK 리소스 확인 중...")
    try:
        check_nltk_resource('taggers/averaged_perceptron_tagger_eng')
        # 다른 NLTK 리소스도 필요하다면 여기에 추가
    except Exception as e:
        print(f"NLTK 리소스 초기화 중 오류 발생: {str(e)}")
    
    yield  # 애플리케이션 실행 중
    
    # 애플리케이션 종료 시 실행할 코드
    print("애플리케이션 종료 중...")

# app = FastAPI()
app = FastAPI(lifespan=lifespan)

app.include_router(KusanagiNene, prefix="/character")
app.include_router(SangonomiyaKokomi, prefix="/character")
app.include_router(category, prefix="/category")

@app.post("/")
async def test():
    return {"asdf" : "asdf"}

if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port, workers=1)