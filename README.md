# DocGen FastAPI

DocGen FastAPI는 AI 기반 프로젝트 문서 자동 생성 서비스의 백엔드 API 서버입니다. 요구사항 정의서, 기능 명세서, 정책 정의서 등의 프로젝트 문서를 AI를 활용하여 자동으로 생성하고 관리하는 기능을 제공합니다.

## 📚 기술 스택

### 핵심 프레임워크 및 런타임

- **Python** `v3.11` - 프로그래밍 언어
- **FastAPI** `v0.104.1` - 고성능 웹 프레임워크
- **Uvicorn** `v0.24.0` - ASGI 서버
- **MongoDB** - NoSQL 문서 데이터베이스

### AI 및 머신러닝

- **LangChain** `v0.1.0` - LLM 애플리케이션 프레임워크
  - `langchain-openai` `v0.0.5` - OpenAI 모델 연동
  - `langchain-google-genai` `v0.0.6` - Google Gemini 모델 연동
  - `langchain-anthropic` `v0.1.1` - Anthropic Claude 모델 연동
- **OpenAI** `v1.3.0` - GPT 모델 API
- **CrewAI** `v0.28.8` - AI 에이전트 프레임워크
- **Pydantic** `v2.5.0` - 데이터 검증 및 직렬화

### 데이터베이스 및 저장소

- **Motor** `v3.3.2` - MongoDB 비동기 드라이버
- **MongoDB** - 문서 기반 NoSQL 데이터베이스

### 파일 처리 및 유틸리티

- **openpyxl** `v3.1.2` - Excel 파일 생성 및 처리
- **python-multipart** `v0.0.6` - 멀티파트 폼 데이터 처리
- **requests** `v2.31.0` - HTTP 클라이언트
- **python-dotenv** `v1.0.0` - 환경 변수 관리

### 배포 및 운영

- **Gunicorn** `v21.2.0` - WSGI HTTP 서버
- **Docker** - 컨테이너화
- **Jenkins** - CI/CD 파이프라인

## 🤖 AI 문서 생성 시스템

### 1. 지원하는 LLM 모델

DocGen FastAPI는 다양한 LLM 모델을 지원하여 최적의 문서 생성 성능을 제공합니다:

#### OpenAI 모델

- **GPT-3.5 Turbo**: 빠른 응답과 비용 효율성
- **GPT-4o**: 고품질 문서 생성

#### Google Gemini 모델

- **Gemini 2.0 Flash Lite**: 경량화된 고속 처리
- **Gemini 2.5 Flash**: 균형잡힌 성능과 품질
- **Gemini 2.5 Flash Lite**: 최적화된 성능

#### Anthropic Claude 모델

- **Claude 3 Haiku**: 빠른 응답과 효율성
- **Claude 3.7 Sonnet**: 고품질 문서 생성

### 2. AI 에이전트 아키텍처

```python
# AI 에이전트 구조
class DocumentGenerator:
    - QuestionGenerator: 질문 생성 에이전트
    - ListGenerator: 목록 생성 에이전트
    - DetailGenerator: 상세 내용 생성 에이전트
    - SummaryGenerator: 요약 생성 에이전트
    - RoleGenerator: 역할 정의 에이전트
```

### 3. 문서 생성 플로우

```
사용자 요구사항 입력
    ↓
QuestionGenerator: 초기 질문 생성
    ↓
ListGenerator: 요구사항 목록 생성
    ↓
DetailGenerator: 상세 내용 생성
    ↓
SummaryGenerator: 요약 생성
    ↓
RoleGenerator: 역할 정의 (정책 문서용)
    ↓
최종 문서 생성 및 저장
```

## 📁 소스 구조

```
docgen-fastapi/
├── ai/                           # AI 문서 생성 모듈
│   ├── product_requirement_document/    # 요구사항 정의서
│   │   ├── agent/                       # AI 에이전트
│   │   │   ├── detail_generator.py      # 상세 내용 생성
│   │   │   ├── list_generator.py        # 목록 생성
│   │   │   ├── question_generator.py    # 질문 생성
│   │   │   └── requirement_summary.py   # 요구사항 요약
│   │   └── prd_generator.py             # PRD 생성기
│   ├── functional_specification_document/  # 기능 명세서
│   │   ├── agent/                       # AI 에이전트
│   │   │   ├── detail_generator.py      # 상세 내용 생성
│   │   │   └── list_generator.py        # 목록 생성
│   │   └── fsd_generator.py             # FSD 생성기
│   ├── service_policy_document/         # 정책 정의서
│   │   ├── agent/                       # AI 에이전트
│   │   │   ├── detail_generator.py      # 상세 내용 생성
│   │   │   ├── list_generator.py        # 목록 생성
│   │   │   └── role_generator.py        # 역할 생성
│   │   └── spd_generator.py             # SPD 생성기
│   ├── llm_models.py                    # LLM 모델 설정
│   ├── models.py                        # 데이터 모델
│   └── utils.py                         # 유틸리티 함수
│
├── api/                        # API 엔드포인트
│   ├── endpoints/              # API 라우터
│   │   ├── requirement_document.py    # 요구사항 문서 API
│   │   ├── functional_document.py     # 기능 명세서 API
│   │   ├── policy_document.py         # 정책 문서 API
│   │   ├── project.py                 # 프로젝트 관리 API
│   │   └── users.py                   # 사용자 관리 API
│   └── routers.py              # 라우터 설정
│
├── schemas/                    # Pydantic 스키마
│   └── document.py             # 문서 스키마 정의
│
├── utility/                    # 유틸리티 함수
│   └── excel_util.py           # Excel 파일 생성
│
├── deploy/                     # 배포 설정
│   ├── dockerfile              # Docker 설정
│   └── jenkinsfile             # Jenkins 설정
│
├── main.py                     # 애플리케이션 진입점
├── mongo_db.py                 # MongoDB 연결 설정
├── models.py                   # 데이터 모델
├── environment.yml             # Conda 환경 설정
└── README.md                   # 프로젝트 문서
```

### 주요 디렉토리 설명

#### `ai/`

- **product_requirement_document/**: 요구사항 정의서 생성 로직
- **functional_specification_document/**: 기능 명세서 생성 로직
- **service_policy_document/**: 정책 정의서 생성 로직
- **llm_models.py**: 다양한 LLM 모델 설정 및 초기화

#### `api/endpoints/`

- **requirement_document.py**: 요구사항 문서 CRUD API
- **functional_document.py**: 기능 명세서 CRUD API
- **policy_document.py**: 정책 문서 CRUD API
- **project.py**: 프로젝트별 문서 관리 API
- **users.py**: 사용자별 문서 관리 API

#### `schemas/`

- **document.py**: Pydantic 기반 데이터 검증 스키마

## 🔄 기본적인 소스 플로우

### 1. 애플리케이션 시작

```
main.py
  ├── FastAPI 앱 초기화
  ├── CORS 미들웨어 설정
  ├── MongoDB 연결 초기화
  ├── API 라우터 등록
  └── 서버 시작 (Uvicorn)
```

### 2. 일반적인 API 요청 플로우

```
클라이언트 요청
    ↓
[CORS 검증]
    ↓
[FastAPI Router] - 엔드포인트 라우팅
    ↓
[Pydantic Validation] - 요청 데이터 검증
    ↓
[AI Document Generator] - 문서 생성 로직
    ↓
[MongoDB] - 비동기 데이터 저장
    ↓
[Response] - JSON 형식 응답
```

### 3. AI 문서 생성 플로우

```
문서 생성 요청
    ↓
AI Agent 초기화
    ↓
QuestionGenerator: 초기 질문 생성
    ↓
ListGenerator: 요구사항/기능 목록 생성
    ↓
DetailGenerator: 상세 내용 생성
    ↓
SummaryGenerator: 요약 생성
    ↓
MongoDB에 문서 저장
    ↓
Excel 파일 생성 (선택사항)
    ↓
응답: 문서 ID 및 상태
```

### 4. 비동기 문서 생성 플로우

```
문서 생성 요청
    ↓
MongoDB에 진행 상태로 저장
    ↓
백그라운드 태스크 시작
    ↓
AI 에이전트 실행
    ↓
문서 생성 완료
    ↓
MongoDB 상태 업데이트 (finished/error)
    ↓
태스크 완료
```

### 5. Excel 파일 생성 플로우

```
Excel 생성 요청
    ↓
MongoDB에서 문서 데이터 조회
    ↓
openpyxl을 사용한 Excel 생성
    ↓
워크시트 설정 및 데이터 입력
    ↓
셀 병합 및 포맷팅
    ↓
파일 다운로드 제공
```

## 🚀 동작 방법

### 1. 환경 설정

#### 필수 요구사항

- **Python** v3.11 이상
- **MongoDB** v4.4 이상
- **Conda** 또는 **pip**

#### 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 다음 정보를 입력합니다:

```bash
# MongoDB 설정
MONGO_URI=mongodb://localhost:27017
MONGO_DB=docgen

# OpenAI API (GPT 기능 사용 시)
OPENAI_API_KEY=your_openai_api_key

# Google Gemini API (Gemini 기능 사용 시)
GEMINI_API_KEY=your_gemini_api_key

# Anthropic Claude API (Claude 기능 사용 시)
CLAUDE_API_KEY=your_claude_api_key
```

### 2. 설치 및 실행

#### Conda 환경 설정

```bash
# Conda 환경 생성 및 활성화
conda env create -f environment.yml
conda activate docgen-fastapi
```

#### pip 설치

```bash
# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

#### 개발 서버 실행

```bash
# 개발 모드 (자동 재시작)
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 프로덕션 모드
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

서버가 정상적으로 시작되면 다음 메시지가 출력됩니다:

```
INFO:     Uvicorn running on http://0.0.0.0:8000
✅ MongoDB connected: mongodb://localhost:27017
```

### 3. 데이터베이스 설정

MongoDB에서 다음 컬렉션들이 자동으로 생성됩니다:

- `requirement_document` - 요구사항 정의서
- `functional_document` - 기능 명세서
- `policy_document` - 정책 정의서

### 4. API 테스트

#### FastAPI 자동 문서 접근

```
http://localhost:8000/docs          # Swagger UI
http://localhost:8000/redoc         # ReDoc
```

#### 요구사항 문서 생성 테스트

```bash
POST http://localhost:8000/api/document/requirement/
Content-Type: application/json

{
  "owner_id": "user123",
  "project_id": "project456",
  "requirement": "길찾기 사이트를 만들어 일반인을 대상으로 현재 위치와 찾는 위치를 입력하여 경로와 소요시간을 확인할 수 있도록 해야 합니다."
}
```

#### 문서 조회 테스트

```bash
GET http://localhost:8000/api/document/requirement/{document_id}
```

### 5. Excel 파일 다운로드

생성된 Excel 문서는 다음 경로로 접근 가능합니다:

```
GET http://localhost:8000/api/document/requirement/file/{document_id}
GET http://localhost:8000/api/document/functional/file/{document_id}
GET http://localhost:8000/api/document/policy/file/{document_id}
```

## 🔧 주요 API 엔드포인트

### 요구사항 문서 관리

- `POST /api/document/requirement/` - 요구사항 문서 생성
- `GET /api/document/requirement/{id}` - 요구사항 문서 조회
- `POST /api/document/requirement/question` - 질문 생성
- `DELETE /api/document/requirement/{id}` - 요구사항 문서 삭제

### 기능 명세서 관리

- `POST /api/document/functional/` - 기능 명세서 생성
- `GET /api/document/functional/{id}` - 기능 명세서 조회
- `DELETE /api/document/functional/{id}` - 기능 명세서 삭제

### 정책 문서 관리

- `POST /api/document/policy/` - 정책 문서 생성
- `GET /api/document/policy/{id}` - 정책 문서 조회
- `DELETE /api/document/policy/{id}` - 정책 문서 삭제

### 프로젝트 관리

- `GET /api/project/{project_id}` - 프로젝트별 문서 목록 조회

### 사용자 관리

- `GET /api/users/{user_id}` - 사용자별 문서 목록 조회

## 📝 개발 가이드

### 새로운 AI 에이전트 추가하기

1. **에이전트 클래스 생성** (`ai/{document_type}/agent/`)

```python
from langchain_openai import ChatOpenAI
from ai.llm_models import llm_openai_turbo

async def generate_custom_content(input_data):
    llm = llm_openai_turbo
    prompt = f"Generate content for: {input_data}"
    response = await llm.ainvoke(prompt)
    return response.content
```

2. **문서 생성기 업데이트** (`ai/{document_type}/generator.py`)

```python
from .agent.custom_generator import generate_custom_content

async def generate_document(input_data):
    custom_content = await generate_custom_content(input_data)
    # 문서 생성 로직
    return document
```

3. **API 엔드포인트 추가** (`api/endpoints/`)

```python
@router.post("/custom", response_model=CustomDocumentResponse)
async def create_custom_document(request: CustomDocumentRequest):
    document = await generate_custom_document(request.data)
    return document
```

### 새로운 LLM 모델 추가하기

1. **모델 설정 추가** (`ai/llm_models.py`)

```python
from langchain_new_provider import NewProviderLLM

llm_new_model = NewProviderLLM(
    model_name="new-model",
    temperature=0.7,
    api_key=os.getenv("NEW_API_KEY")
)
```

2. **문서 생성기에 적용**

```python
from ai.llm_models import llm_new_model

async def generate_with_new_model(prompt):
    response = await llm_new_model.ainvoke(prompt)
    return response.content
```

### MongoDB 쿼리 실행

```python
# 컬렉션에서 문서 조회
document = await db.collection_name.find_one({"_id": ObjectId(document_id)})

# 여러 문서 조회
documents = await db.collection_name.find({"project_id": project_id}).to_list()

# 문서 생성
result = await db.collection_name.insert_one(document_data)

# 문서 업데이트
result = await db.collection_name.update_one(
    {"_id": ObjectId(document_id)},
    {"$set": {"status": "finished"}}
)
```

## 🛡️ 보안 고려사항

- ✅ 환경 변수를 통한 API 키 관리
- ✅ CORS 정책으로 허용된 도메인만 접근 가능
- ✅ Pydantic을 통한 입력 데이터 검증
- ✅ MongoDB 인젝션 방지 (ObjectId 사용)
- ✅ 비동기 처리로 서버 성능 최적화
- ✅ 에러 핸들링 및 로깅
- ✅ API 키 로테이션 지원

## 📄 라이선스

UNLICENSED

## 👥 기여자

DocGen FastAPI 개발팀

---

**DocGen FastAPI** - AI 기반 프로젝트 문서 자동 생성 서비스
