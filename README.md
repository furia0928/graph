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
/graph
├── app
│   ├── main.py  # 메인 실행 파일
│   ├── utils.py  # 유틸리티 함수
│   ├── db.py  # MongoDB 연결 및 데이터 처리
│   ├── graph.py  # 그래프 데이터 처리 및 시각화
├── requirements.txt  # 필요한 라이브러리 목록
├── .gitignore  # Git에서 제외할 파일 목록
└── README.md  # 프로젝트 문서
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

