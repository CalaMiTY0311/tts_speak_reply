import nltk
import psutil
from src.loadModel import ModelManager

#########################################################영어 추론 시 필수 패키지 체크
def load_nltk(path):
    """NLTK 패키지 확인"""
    print("애플리케이션 시작: NLTK 리소스 확인 중...")
    try:
        # 리소스 존재 여부 확인
        file = nltk.data.find(path)
        print(f"NLTK 리소스 '{path}'가 이미 설치되어 있습니다: {file}")
    except LookupError:
        # 리소스가 없으면 다운로드
        print(f"NLTK 리소스 '{path}'가 설치되어 있지 않습니다. 설치를 시작합니다...")
        
        # 리소스 경로에서 패키지 이름 추출
        if '/' in path:
            package_name = path.split('/')[-1]
        else:
            package_name = path
            
        nltk.download('averaged_perceptron_tagger_eng')
        print(f"NLTK 리소스 '{path}' 설치가 완료되었습니다.")
    
#########################################################서버 실행 전 메모리 체크
def get_current_memory_mb():
    process = psutil.Process()
    mem = process.memory_info().rss
    return mem / (1024 * 1024)