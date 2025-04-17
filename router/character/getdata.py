import os,sys

now_dir = os.getcwd()
sys.path.append(now_dir)
print(now_dir)

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse, Response
from pydantic import BaseModel
from typing import Optional

from src.util import get_character_models, get_emotion
from src.generator import get_tts_data, cut_text, media_type
from src.loadModel import ModelManager
# from src.generator import change_gpt_weights, change_sovits_weights

import traceback

manager = ModelManager()

class ttsBase(BaseModel):
    emotion:Optional[str] = None
    prompt_text: Optional[str] = ""
    text: str
    text_language:str
    cut_punc: bool

# models_base = router_config.models_base

def handle(name, refer_wav_path, prompt_text, text, text_language, cut_punc):
    try:
        loadModel = manager.loaded_models[name]
        
        t2s_model = loadModel["t2s_model"]
        config = loadModel["config"]
        hz = loadModel["hz"]
        max_sec = loadModel["max_sec"]
        vq_model = loadModel["vq_model"]
        hps = loadModel["hps"]

        # if cut_punc == None: 
        #     text = cut_text(text,default_cut_punc)
        # else:
        #     text = cut_text(text,cut_punc)

        text = cut_text(text, cut_punc)

        audio_data = get_tts_data(
            refer_wav_path, 
            prompt_text, 
            text, 
            text_language,
            t2s_model,
            config,
            hz,
            max_sec,
            vq_model,
            hps
        )
        
        # 바이트 변환이 필요하면 이 부분에서 처리
        # audio_data가 이미 바이트 형식이라면 그대로 사용
        
        # StreamingResponse 대신 Response 사용하여 데이터 반환
        import base64
        base64_audio = base64.b64encode(audio_data).decode('utf-8')
        return {"audio_data" : base64_audio}
    
    except Exception as e:
        # raise HTTPException(status_code=500, detail="Internal Server Error")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Server Error")

data = APIRouter()

@data.post("/{name}")
async def default(data: ttsBase, name):
    if data.emotion == "" or data.emotion is None:
        refer_wav_path = get_emotion(manager.models_base, name)
    else:
        refer_wav_path = get_emotion(manager.models_base, name, data.emotion)
    
    return handle(
        name,
        refer_wav_path,
        data.prompt_text,
        data.text,
        data.text_language,
        data.cut_punc,
    )
