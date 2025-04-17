# TTS-SPEAK_Reply API v1.4

## 소개 
- 👆 GPT-Sovits로 만든 TTS모델과 모델의 참조 오디오만 있다면 텍스트를 캐릭터의 음성으로 변환해 주는 API입니다. 
- **TTS모델은 일본어로 학습된 모델이어야합니다.** (추후 영어와 한국어로 학습된 모델로도 적용할 수 있도록 업데이트 예정) 
- v1.3 이후로 영어로 언어 추론(음성 변환)이 가능해졌습니다.

## 요구 사항
```bash
- OS: Windows
- Python: 3.8
- FFmpeg (직접 설치 필요)
```

## 준비물
1. 캐릭터 TTS모델과 참조 오디오 (없다면 아래 제공된 캐릭터 모델을 사용해주세요)
2. 좋은 CPU (성능이 낮으면 처리 속도가 느립니다)
   - 참고: i5-11세대 CPU 기준, 104자(특수부호 포함) 텍스트 추론 시간 약 16초
   - 첫 추론 시에는 22초 정도 소요되며, 이후 추론은 더 빠릅니다

## 사용 방법
1. 터미널에서 프로젝트 클론하기:
   ```bash
   git clone https://github.com/CalaMiTY0311/tts_speak_reply.git
   ```
   (클론 후 C: 또는 D: 드라이브 루트와 같은 적절한 위치에 이동시키는 것을 권장합니다)

2. [모델 폴더 다운로드](https://drive.google.com/file/d/1u9ockMEWKw1iTulXYzRGk8pq3DCS9MZb/view?usp=drive_link)(구글 드라이브 URL)에서 tts_models 폴더를 다운받아 프로젝트 최상위 디렉토리에 위치시킵니다 (api.py와 같은 위치)

3. 필요한 패키지 설치:
   ```bash
   pip install -r requirements.txt
   ```

4. 서버 실행:
   ```bash
   python api.py
   ```

## API 명세서
- 자세한 API 사용법은 [깃북 문서](https://expressauthkit.gitbook.io/tts-speak-reply/)를 참고하세요.

## 참고 사항
- 텍스트(`text`)가 길어질수록 음성 퀄리티가 낮아질 수 있습니다 (추후 개선 예정).

## 업데이트 내역
### v1.4 (최신)
#### loadModel.py
- 서버 실행 시 tts_models의 모든 캐릭터 모델을 사전에 메모리에 로드합니다.
- 싱글톤 패턴을 도입하여 각 캐릭터별 모델 가중치를 딕셔너리에 체계적으로 관리함으로써 모델 로딩 경쟁 상태를 방지했습니다.
- 이전 버전에서는 캐릭터를 변경할 때마다 `change_sovits_weights(sovits_path)`와 `change_gpt_weights(gpt_path)` 함수가 전역 변수를 덮어쓰는 방식이라 마지막으로 로드된 캐릭터의 모델만 활성화되는 문제가 있었으나, 이제는 각 캐릭터별로 독립적인 모델 인스턴스를 유지하여 해결했습니다.
- 코드 전반의 가독성을 개선하고 구조를 최적화했습니다.

## 추후 업데이트 예정
- 필자 외 일반 사용자를 위한 코드 리팩토링 및 간편화
- 한국어 지원 업데이트 예정
- 일정 글자 수 초과 시 병렬 처리로 속도 개선

## Special Thanks
### [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS?tab=MIT-1-ov-file)
