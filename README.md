## TTS-SPEAK_Reply JP API v1.0

## 소개 
- GPT-Sovits로 만든 TTS모델(일본어)을 활용하여 텍스트를 wav형태로 스트리밍하여 결과를 보여주는 API입니다. 
- TTS 모델을 사용하여 일본어 텍스트(한자 포함)를 추론하여 음성으로 변환합니다.

## Special Thanks
### [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS?tab=MIT-1-ov-file)

## 요구 사항
```bash
- os: window
- python: 3.8
```

## 준비물
1. 필자가 미리 만들어 둔 Project Sekai의 Kusanagi Nene 캐릭터 TTS모델 ( 사용 방법에서 필자가 만든 모델과 사용 방법 알려드리니 참고)
2. 좋은 CPU (안좋으면 느려요...)
    2-1 필자는 i5-11세대
    2-2 글자수104(특수부호포함)의 길이를 추론했을 때 16초 (처음 추론할때는 시간이 좀 소모되서 22초인데 그 후는 더 빠름)
3. (Window)ffmpeg를 직접 가져와야함

### 사용 방법
1. 터미널에 git clone https://github.com/CalaMiTY0311/tts_speak_reply.git 으로 프로젝트 가져옵니다 ( 구동은 가능하면 바탕화면이아닌 드라이브에서 하는게 좋아요 ex-> C: )
2. [모델 폴더 다운URL](https://drive.google.com/drive/folders/1Wo7fvbUPaI-DoRUZaMEfcjGvNg7WKz-z?usp=drive_link)에서 필자의 tts_models폴더를 다운받아서 api.py와 같은 위치에 놓으면 OK
3. pip install -r requirements.txt 로 패키지 다운로드
4. python api.py로 서버 실행

## 엔드포인트
**POST** `/character/kusanagiNene`

## 요청(Request)
### 헤더
- `Content-Type`: `application/json`

### 요청 본문 (JSON)
```json
{
    "emotion": "",          // (선택) 감정 설정 angry, sad, surprise ...
    "prompt_text": "",       // (선택) 추가 프롬프트
    "text": "<음성 변환할 텍스트>",  // (필수) 변환할 텍스트
    "text_language": "ja",   // (필수) ja로 고정해주세요
    "cut_punc": true          // (선택) 문장 부호를 제거할지 여부 (기본값: false)
}
```

## 응답(Response)
### 성공 (HTTP 200)
- **Content-Type**: `audio/mpeg`
- **Body**: MP3 스트리밍 데이터

## 참고 사항
- 감정(`emotion`)는 선택 사항입니다.
- 텍스트(`text`)는 필수 입력값이며, 최대 길이 제한이 있을 수 있습니다.
- 응답은 MP3 오디오 스트리밍 형식이며, 클라이언트는 이를 파일로 저장하거나 직접 재생할 수 있습니다.

### 추후 업데이트 예정
- 필자 외 일반 사용자를 위한 코드 리팩토링 및 간편화
- 다국어 지원 예정(영어, 한국어)
- GPU를 자동 탐지하여 추론 지원
- 일정 글자 수 초과 시 병렬 처리로 속도 개선