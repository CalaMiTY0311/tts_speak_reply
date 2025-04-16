import os,sys
from pydantic import BaseModel
from typing import Optional,Dict,Any

import asyncio

now_dir = os.getcwd()
sys.path.append(now_dir)

from src.generator import change_gpt_weights, change_sovits_weights
from src.generator import get_character_models

models_base = os.path.abspath("tts_models")
characters = [
        name for name in os.listdir(models_base)
        if os.path.isdir(os.path.join(models_base, name))
    ]

class ttsBase(BaseModel):
    emotion:Optional[str] = None
    prompt_text: Optional[str] = ""
    text: str
    text_language:str
    cut_punc: bool

class Config:
    def __init__(self):
        self.models_base = models_base

# class ModelManager:
#     def __init__(self):
#         self.models_base = models_base
#         self.loaded_models: Dict[str, Dict[str, Any]] = {}
#         self.characters = characters

#         print(self.characters)
    
#     async def load_all_models(self):
#         """모든 캐릭터의 모델을 로드하고 저장"""
#         for character in self.characters:
#             try:
#                 print(f"Attempting to load models for {character}...")

#                 # 모델 경로 가져오기
#                 gpt_path = os.environ.get("gpt_path", get_character_models(self.models_base, character, ".ckpt"))
#                 sovits_path = os.environ.get("sovits_path", get_character_models(self.models_base, character, ".pth"))

#                 print(f"gpt_path: {gpt_path}")
#                 print(f"sovits_path: {sovits_path}")

#                 # 모델 가중치 변경 함수 호출
#                 print(f"Loading GPT weights for {character}...")
#                 change_gpt_weights(gpt_path)

#                 print(f"Loading SoVITS weights for {character}...")
#                 change_sovits_weights(sovits_path)

#                 # 로드된 모델 정보 저장
#                 self.loaded_models[character] = {
#                     "gpt_path": gpt_path,
#                     "sovits_path": sovits_path,
#                     "loaded": True
#                 }
#                 print(f"loaded_models updated: {self.loaded_models}")

#                 print(f"Models for {character} loaded successfully")
#             except Exception as e:
#                 print(f"Error loading models for {character}: {str(e)}")
    
#     ###############
#     def is_model_loaded(self, character: str) -> bool:
#         """특정 캐릭터의 모델이 로드되었는지 확인"""
#         if character not in self.loaded_models:
#             return False
#         return self.loaded_models[character]["loaded"]
    
#     def are_all_models_loaded(self) -> bool:
#         """모든 캐릭터의 모델이 로드되었는지 확인"""
#         for character in self.characters:
#             if not self.is_model_loaded(character):
#                 return False
#         return True

#     def load_model_for_character(self, character: str):
#         """특정 캐릭터의 모델만 로드"""
#         if character not in self.characters:
#             raise ValueError(f"Character {character} not found")
            
#         gpt_path = os.environ.get("gpt_path", get_character_models(self.models_base, character, ".ckpt"))
#         sovits_path = os.environ.get("sovits_path", get_character_models(self.models_base, character, ".pth"))
        
#         change_gpt_weights(gpt_path)
#         change_sovits_weights(sovits_path)
        
#         self.loaded_models[character] = {
#             "gpt_path": gpt_path,
#             "sovits_path": sovits_path,
#             "loaded": True
#         }
        
#         print(f"Models for {character} loaded successfully")
