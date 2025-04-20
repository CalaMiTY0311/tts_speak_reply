# TTS-SPEAK_Reply API v1.4

## 소개 
- 👆 GPT-Sovits로 만든 TTS모델과 모델의 참조 오디오만 있다면 텍스트를 캐릭터의 음성으로 변환해 주는 API입니다. 
- **TTS모델은 일본어로 학습된 모델이어야합니다.** (추후 영어와 한국어로 학습된 모델로도 적용할 수 있도록 업데이트 예정) 
- v1.3 이후로 영어로 언어 추론(음성 변환)이 가능해졌습니다.

## 실행 환경
```bash
- OS: Windows
- Python: 3.8
```

### 
```bash
   # 프로젝트 다운로드
   git clone https://github.com/CalaMiTY0311/tts_speak_reply.git
   # 의존성 설치
   pip install -r requirements.txt
   ```

### [준비부터 실행, 추론까지 가이드는 여기](https://github.com/CalaMiTY0311/tts_speak_reply/blob/main/roadToRunProgram.md)

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
