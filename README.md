# Graph 프로젝트

## 소개
Graph 프로젝트는 LangGraph, pymongo, graphviz 등을 활용하여 그래프 기반의 데이터를 처리하고 시각화하는 프로젝트입니다.

## 설치 방법

### 1. 필수 요구 사항
- Python 3.8 이상
- pip
- 가상 환경 설정 (권장)

### 2. 의존성 설치
```sh
pip install -r requirements.txt
```

## 사용 방법

### 1. 프로젝트 실행
```sh
python app/main.py
```

### 2. MongoDB 설정
MongoDB를 실행하고 설정 파일을 업데이트한 후 실행해야 합니다.

## 프로젝트 구조
```
graph/
├── .langgraph_api/               # LangGraph 관련 임시 파일 및 빌드 산출물이 생성될 수 있는 디렉토리
├── .venv/                        # Python 가상환경 폴더 (개발 시 생성)
├── src/                          
│   ├── api/                     # FastAPI 애플리케이션 관련 코드
│   │   ├── endpoints/           # API 엔드포인트 모듈들
│   │   │   └── chat.py          # 예시: 채팅 관련 엔드포인트 정의
│   │   ├── models/              # Pydantic 모델 정의
│   │   │   └── chat.py          # ChatRequest, ChatResponse 클래스 정의
│   │   ├── services/            # API와 관련된 비즈니스 로직
│   │   │   └── chat_service.py  # 예시: process_chat 함수 등
│   │   └── main.py              # FastAPI 애플리케이션 진입점 (app = FastAPI() 등)
│   └── graph/                   # LangGraph 및 대화 처리 관련 코드
│       ├── nodes/             # LangGraph 노드 함수들
│       │   ├── get_chat_history.py        # MongoDB에서 대화 기록 조회
│       │   ├── save_chat_history.py         # 대화 기록과 생성/요약 데이터를 MongoDB에 저장
│       │   └── summarize_conversation.py    # OpenAI GPT-4를 호출해 대화 요약 생성 (함수명: summarize_conversation)
│       ├── agent.py             # LangGraph 에이전트 생성 및 노드/엣지 설정
│       ├── conversation_state.py# 대화 상태 (ChatState) 정의 (Pydantic 모델)
│       └── langgraph.json       # LangGraph 설정 파일
├── docker-compose.yml            # 여러 서비스(Redis, MongoDB, FastAPI, LangGraph, ChromaDB 등) 실행을 위한 Compose 파일
├── Dockerfile.fastapi            # FastAPI 서버를 위한 Dockerfile (소스 전체 복사, PYTHONPATH 설정 등)
├── Dockerfile.langgraph          # LangGraph 서비스를 위한 Dockerfile (소스 전체 복사, CMD 실행 시 langgraph dev 등)
├── .env                          # 환경변수 파일 (예: MONGO_URI, OPENAI_API_KEY 등)
├── requirements.txt              # Python 의존성 목록 (FastAPI, pymongo, langchain, python-dotenv, 등)
└── README.md                     # 프로젝트 소개 및 사용법 등 문서

```

## 주요 기능
- LangGraph를 활용한 그래프 구조 데이터 관리
- pymongo를 사용한 MongoDB 연동
- graphviz를 이용한 데이터 시각화

## 기여 방법
1. 저장소를 포크합니다.
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature-branch`).
3. 변경 사항을 커밋합니다 (`git commit -m '설명 추가'`).
4. 원격 저장소에 푸시합니다 (`git push origin feature-branch`).
5. Pull Request를 생성합니다.

## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.

## 문의
궁금한 점이 있다면 이슈를 등록하거나 프로젝트 관리자에게 문의하세요.

