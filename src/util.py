import os, sys

now_dir = os.getcwd()
sys.path.append(now_dir)

# 사용할 캐릭터 모델 설정
def get_character_models(base, name, model):               
    character = os.path.join(base, name)
    if not os.path.isdir(character):
        return {
            "status": 404,
            "data" : {
                "msg" : "존재하지않는 캐릭터 모델"  
            } 
        }
    else:
        for file in os.listdir(character):
            if file.endswith(model):
                return os.path.join(character, file)#캐릭터 .ckpt .pth 참조

# 참조할 캐릭터의 감정
# def get_emotion(base, character, type):
#     refer_wav_path = os.path.join(base, character, "emotion", type)
#     return refer_wav_path
            
def get_emotion(base, character, emotion="default"):

    emotion_folder_path = os.path.join(base, character, "emotion", emotion)
    
    if not os.path.isdir(emotion_folder_path):
        return f"Error : {character} 의 감정 파일을 추가해 주세요"
    
    for refer_file in [".wav", ".mp3"]:
        path = os.path.join(emotion_folder_path, f"{emotion}{refer_file}")
        if os.path.isfile(path):
            return path
    
    return f"Error : {character}의 {emotion} 감정 파일을 찾을 수 없습니다"

if __name__ == "__main__":
    models_base = models_base = os.path.abspath("tts_models")
    models_base = os.path.abspath("tts_models")
    characters = [
        name for name in os.listdir(models_base)
        if os.path.isdir(os.path.join(models_base, name))
    ]

    for character in characters:
        ckpt_path = get_character_models(models_base, character, ".ckpt")
        pth_path = get_character_models(models_base, character, ".pth")

        if not ckpt_path and not pth_path:
            print(f"{character}: 모델 파일 (.ckpt / .pth) 없음")
        else:
            if ckpt_path:
                print(f"{character}: CKPT 모델 → {ckpt_path}")
            if pth_path:
                print(f"{character}: PTH 모델 → {pth_path}")
    
    print(get_emotion(models_base, characters[0]))

