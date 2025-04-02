# FastAPI 프로젝트

이 프로젝트는 [FastAPI](https://fastapi.tiangolo.com/)를 사용한 웹 API입니다.

## 설치 방법

### 필수 요구사항

- Python 3.7+
- pip (Python 패키지 관리자)

### 설치 단계

1. 프로젝트를 클론하거나 다운로드합니다.

```bash
git clone https://github.com/username/project-name.git
cd project-name
```

2. 가상환경을 생성하고 활성화합니다.

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. 필요한 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

requirements.txt 파일이 없는 경우, 다음과 같이 직접 필수 패키지를 설치할 수 있습니다:

```bash
pip install fastapi uvicorn
```

## 실행 방법

### 개발 서버 실행

```bash
# main.py가 있는 디렉토리에서
uvicorn main:app --reload
```

- `main`: Python 파일 이름 (main.py)
- `app`: FastAPI 인스턴스를 생성한 변수 이름
- `--reload`: 코드 변경 시 자동으로 서버 재시작 (개발 시 유용)

### 프로덕션 환경 실행

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API 사용법

서버가 실행되면 다음 URL에서 API를 사용할 수 있습니다:

- API 엔드포인트: http://localhost:8000/
- 자동 생성된 API 문서: http://localhost:8000/docs
- 대체 API 문서: http://localhost:8000/redoc

## 프로젝트 구조

```
project-name/
│
├── main.py           # FastAPI 앱과 라우트 정의
├── requirements.txt  # 필요한 패키지 목록
├── app/
│   ├── __init__.py
│   ├── models.py     # 데이터 모델
│   ├── schemas.py    # Pydantic 스키마
│   ├── database.py   # 데이터베이스 연결 설정
│   ├── crud.py       # CRUD 작업 함수
│   └── routers/      # 라우트를 모듈로 분리
│       ├── __init__.py
│       ├── users.py
│       └── items.py
├── tests/            # 테스트 코드
└── venv/             # 가상환경 (버전 관리에서 제외됨)
```

## 환경 변수 설정

`.env` 파일을 프로젝트 루트에 생성하여 환경 변수를 설정할 수 있습니다:

```
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your_secret_key
DEBUG=True
```

## 자주 발생하는 문제 해결

- **ModuleNotFoundError**: 가상환경이 활성화되어 있는지 확인하고, 필요한 패키지가 모두 설치되어 있는지 확인하세요.
- **Address already in use**: 8000번 포트가 이미 사용 중입니다. 다른 포트를 지정하세요: `uvicorn main:app --port 8001`
- **Database connection error**: 데이터베이스 연결 설정을 확인하세요.
