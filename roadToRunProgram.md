# roadToRun

## 1. pretrained_models 다운로드
```bash
git clone https://huggingface.co/lj1995/GPT-SoVITS
```
다운로드된 폴더 내용물을 `GPT_SoVITS_tools/GPT_SoVITS/pretrained_models`에 복사
![ㅇㅇ](https://github.com/CalaMiTY0311/tts_speak_reply/blob/main/guideImg/img1.jpg)

## 2. ffmpeg, ffprobe 설치
[ffmpeg 다운로드 페이지](https://ffmpeg.org/download.html)에서 다운로드 후 실행 파일을 최상위 디렉토리(api.py와 같은 위치)에 배치

## 3. TTS 모델 준비
**1: 필자의 모델을 사용 시**
- [제공된 모델](https://drive.google.com/file/d/1u9ockMEWKw1iTulXYzRGk8pq3DCS9MZb/view?usp=drive_link) 다운로드
- 압축 해제 후 `tts_models` 폴더를 최상위 디렉토리에 배치

**2: 사용자(자신)의 모델 사용 시**
```
tts_models/
└── 캐릭터이름/
    ├── 모델파일.pth
    ├── 모델파일.ckpt
    └── emotion/
        ├── default/
        │   └── default.mp3
        ├── angry/
        │   └── angry.wav
        └── sad/
            └── sad.mp3
```
- `emotion` 폴더 내 각 감정 폴더에는 해당 감정의 오디오 파일 하나만 존재해야 함
- 감정 폴더명과 오디오 파일명은 동일하게 설정
- 또한 tts_models, emotion 디렉토리는 이름을 바꾸면 에러 발생으로 주의해야 및 모든 디렉토리는 영어로 해야함

### 배치 완료 구조
![ㅇㅇ](https://github.com/CalaMiTY0311/tts_speak_reply/blob/main/guideImg/img2.jpg)

