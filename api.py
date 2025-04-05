import uvicorn
from fastapi import APIRouter, Request
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse

from router.character.kusanagi_nene import kusanagi_nene
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

app = FastAPI()

app.include_router(kusanagi_nene, prefix="/character")
app.include_router(category, prefix="/category")

@app.post("/")
async def test():
    return {"asdf" : "asdf"}

if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port, workers=1)


