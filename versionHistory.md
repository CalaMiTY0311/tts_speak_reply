### v1.0
- 일본어 텍스트(한자 포함)를 TTS 모델을 사용하여 음성으로 변환 
- emotion에 저장된 참조 오디오를 활용하여 사용자가 여러 감정 상태의 음성 변환 구성 

### v1.1
- tts모델(캐릭터) 목록 조회하는 엔드포인트 구성   /category/characters
- tts모델의 참조(감정)오디오 파일 리스트 조회하는  엔드포인트 구성 /category/{캐릭터이름}/emotions <- (확장자인 .mp3는 제거하여 감정 이름만 반환)

### v1.2
- 원신 캐릭터 산고노미야코코미 캐릭터 ttsmodel추가 (huggingface 에서 가져옴)
- KusanagiNene 캐릭터 모델 퀄리티 업그레이드

### v1.3
- 영어 추론을 하기 위한 nltk의 averaged_perceptron_tagger_eng 패키지 감지 및 미설치되어있을 시 자동 설치 구현 
- text_language 기본값을 "en"으로 설정하여, v1.3부터 영어 텍스트에 대한 추론 가능

