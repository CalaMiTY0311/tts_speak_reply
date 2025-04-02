import os,sys

now_dir = os.getcwd()
sys.path.append(now_dir)

models_base = os.path.abspath("tts_models")

class Config:
    def __init__(self):
        self.models_base = models_base

