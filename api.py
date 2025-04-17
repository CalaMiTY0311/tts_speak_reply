import uvicorn
from fastapi import APIRouter, Request
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse

from contextlib import asynccontextmanager
from src.setup import load_nltk, load_models

from router.character.character import character
from router.category import category
from router.character.getdata import data

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

manager = ModelManager()

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        load_nltk('taggers/averaged_perceptron_tagger_eng')
    except Exception as e:
        print(f"NLTK 리소스 초기화 중 오류 발생: {str(e)}")
    try:
        await manager.load_all_models()
        print("🔧 모든 모델 로드 완료")
    except Exception as e:
        print(f"❌ 모델 로드 실패: {str(e)}")
    yield
    print("애플리케이션 종료 중...")

import asyncio

app = FastAPI(lifespan=lifespan)

app.include_router(character, prefix="/character")
app.include_router(category, prefix="/category")

#test just getdata
app.include_router(data, prefix="/getdata")

# @app.post("/")
# async def test():
#     return {"asdf" : "asdf"}

import psutil
import time
import threading

if __name__ == "__main__":
    # threading.Thread(target=print_memory_diff).start()
    uvicorn.run(app, host=host, port=port, workers=1)