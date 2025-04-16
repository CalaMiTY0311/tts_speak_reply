import uvicorn
from fastapi import APIRouter, Request
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse

import nltk
from contextlib import asynccontextmanager

from router.character.character import character
from router.category import category

from src.loadModel import ModelManager

import argparse
import src.config as global_config
g_config = global_config.Config()

# 获取参数
parser = argparse.ArgumentParser(description="GPT-SoVITS api")
parser.add_argument("-a", "--bind_addr", type=str, default="0.0.0.0", help="default: 0.0.0.0")
parser.add_argument("-p", "--port", type=int, default=g_config.api_port, help="default: 9880")

args = parser.parse_args()
port = args.port
host = args.bind_addr

model_manager = ModelManager()

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
    # 애플리케이션 시작 시
    print("애플리케이션 시작: NLTK 리소스 확인 중...")
    try:
        check_nltk_resource('taggers/averaged_perceptron_tagger_eng')
    except Exception as e:
        print(f"NLTK 리소스 초기화 중 오류 발생: {str(e)}")

    # 모델 로드
    try:
        await model_manager.load_all_models()
        print("🔧 모든 모델 로드 완료")
    except Exception as e:
        print(f"❌ 모델 로드 실패: {str(e)}")

    yield

    # 애플리케이션 종료 시
    print("애플리케이션 종료 중...")

import asyncio

# app = FastAPI()
app = FastAPI(lifespan=lifespan)

app.include_router(character, prefix="/character")
app.include_router(category, prefix="/category")

@app.post("/")
async def test():
    return {"asdf" : "asdf"}

@app.post("/test")
async def test():
    character_name = "KusanagiNene"  # 여기에 확인하고 싶은 캐릭터 이름 넣어줘
    is_loaded = model_manager.is_model_loaded(character_name)
    return {"character": character_name, "is_model_loaded": is_loaded}


if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port, workers=1)