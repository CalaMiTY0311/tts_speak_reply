import os,sys

now_dir = os.getcwd()
sys.path.append(now_dir)

from fastapi import APIRouter

from router.router_config import Config

router_config = Config()
models_base = router_config.models_base

# lst = [
#         name for name in os.listdir(models_base)
#         if os.path.isdir(os.path.join(models_base, name))
#     ]

category = APIRouter()

@category.get("/characters")
async def characters():
    characters = [
        name for name in os.listdir(models_base)
        if os.path.isdir(os.path.join(models_base, name))
    ]
    return {"characters": characters}

@category.get("/{name}/emotions")
async def emotions(name):
    category = os.path.join(models_base, name, "emotion")
    print("category : ", category)
    emotion_dirs = [
        dir_name for dir_name in os.listdir(category)
        if os.path.isdir(os.path.join(category, dir_name))
    ]

    return {"emotions": emotion_dirs}