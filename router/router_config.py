import os,sys
from pydantic import BaseModel
from typing import Optional

now_dir = os.getcwd()
sys.path.append(now_dir)

models_base = os.path.abspath("tts_models")

class ttsBase(BaseModel):
    emotion:Optional[str] = None
    prompt_text: Optional[str] = ""
    text: str
    text_language:str
    cut_punc: bool

class Config:
    def __init__(self):
        self.models_base = models_base

