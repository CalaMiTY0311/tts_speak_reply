import os,sys

now_dir = os.getcwd()
sys.path.append(now_dir)
print(now_dir)

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse, JSONResponse
from router.options import get_character_models, get_emotion, get_tts_wav, cut_text, media_type
from router.options import change_gpt_weights, change_sovits_weights
from router.router_config import Config, ttsBase

router_config = Config()
models_base = router_config.models_base
character = "SangonomiyaKokomi"

gpt_path = os.environ.get("gpt_path", get_character_models(models_base, character, ".ckpt"))
sovits_path = os.environ.get("sovits_path", get_character_models(models_base, character, ".pth"))

change_sovits_weights(sovits_path)
change_gpt_weights(gpt_path)

def handle(refer_wav_path, prompt_text, text, text_language, cut_punc):
    refer_wav_path = refer_wav_path
    # if cut_punc == None: 
    #     text = cut_text(text,default_cut_punc)
    # else:
    #     text = cut_text(text,cut_punc)
    text = cut_text(text,cut_punc)

    # wav_data_list = list(get_tts_wav(refer_wav_path, prompt_text, prompt_language, text, text_language))
    # # print("list : ", wav_data_list)
    # wav_data = b"".join(wav_data_list)
    # print("wav_data : ", wav_data) 
    
    return StreamingResponse(get_tts_wav(refer_wav_path, prompt_text, text, text_language), media_type="audio/"+media_type)

SangonomiyaKokomi = APIRouter()

@SangonomiyaKokomi.post("/SangonomiyaKokomi")
async def default(data: ttsBase):
    if data.emotion == "" or data.emotion is None:
        print("asdf : ", data.emotion)
        refer_wav_path = get_emotion(models_base, character)
    else:
        refer_wav_path = get_emotion(models_base, character, data.emotion)
    
    return handle(
        refer_wav_path,
        data.prompt_text,
        data.text,
        data.text_language,
        data.cut_punc,
    )