import os,sys

now_dir = os.getcwd()
sys.path.append(now_dir)
print(now_dir)

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional

from src.generator import get_character_models, get_emotion, get_tts_wav, cut_text, media_type
from src.generator import change_gpt_weights, change_sovits_weights
from src.router_config import Config, ttsBase

router_config = Config()

class ttsBase(BaseModel):
    emotion:Optional[str] = None
    prompt_text: Optional[str] = ""
    text: str
    text_language:str
    cut_punc: bool

models_base = router_config.models_base

def handle(refer_wav_path, prompt_text, text, text_language, cut_punc):
    try:
        refer_wav_path = refer_wav_path
        # if cut_punc == None: 
        #     text = cut_text(text,default_cut_punc)
        # else:
        #     text = cut_text(text,cut_punc)
        text = cut_text(text,cut_punc)
        return StreamingResponse(get_tts_wav(refer_wav_path, prompt_text, text, text_language), media_type="audio/"+media_type)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


character = APIRouter()

@character.post("/{name}")
async def default(data: ttsBase, name):
    model_manager = ModelManager(models_base, name)
    if name not in model_manager.characters:
        raise HTTPException(status_code=404, detail=f"Character '{name}' not found")
    
    # Check if model is loaded, if not, load it
    if not model_manager.is_model_loaded(name):
        try:
            model_manager.load_model_for_character(name)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to load model for {name}: {str(e)}")
    
    # Get emotion reference
    if data.emotion == "" or data.emotion is None:
        refer_wav_path = get_emotion(models_base, name)
    else:
        refer_wav_path = get_emotion(models_base, name, data.emotion)
    
    return handle(
        refer_wav_path,
        data.prompt_text,
        data.text,
        data.text_language,
        data.cut_punc,
    )

@character.get("/test/1")
async def test():
    return {"asdf" : "asdf"}