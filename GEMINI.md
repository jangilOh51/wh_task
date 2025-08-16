# 프로젝트 개요
이 프로젝트는 API 테스트 자동화 구현 및 테스트 케이스 문서에 대한 내용입니다.
AI 에이전트를 사용하여 API 명세서로부터 테스트 코드를 자동 생성하고, 생성된 코드를 실행하는 2-part 구조를 가집니다.

- **`api_test_gen`**: Gradio 웹 UI를 통해 API 명세서(PDF)를 입력받아, LangChain/LangGraph 기반의 AI 에이전트가 테스트 코드를 생성하는 애플리케이션입니다.
- **`api_test`**: `api_test_gen`에 의해 생성된 `pytest` 코드를 저장하고, 실행하고, 관리하는 테스트 프레임워크입니다.

# 주요 지침
- 모든 답변은 한글로 답변해주세요.
- git에 commit할때도 한글로 comment를 입력해줘 이해할 수 쉽게.

# 주요 라이브러리
- poetry : 코드 환경
- python3 : 코드 언어
- pytest : 테스트 프레임워크
- allure : 리포트
- requests : api 호출
- gradio : 웹 UI
- langchain, langgraph : AI 에이전트

# 실행 방법
- **테스트 코드 생성기 실행:**
  ```bash
  poetry run python api_test_gen/main.py
  ```
- **테스트 코드 실행:**
  ```bash
  poetry run python api_test/run.py
  ```

# TODO List

- [ ] **환경 설정**
    - [ ] `pyproject.toml`에 신규 라이브러리 추가 (완료)
    - [ ] `poetry install` 실행하여 의존성 설치 (사용자 실행 필요)
- [ ] **`api_test_gen` (코드 생성기) 개발**
    - [ ] `api_test_gen/docs`에 API 명세서 위치 (완료)
    - [ ] LLM을 위한 프롬프트 정의 (`api_test_gen/agent/prompts.py`)
    - [ ] LangChain 체인 정의 (`api_test_gen/agent/chains.py`)
    - [ ] LangGraph 워크플로우 정의 (`api_test_gen/agent/graph.py`)
    - [ ] Gradio UI 개발 및 에이전트 연동 (`api_test_gen/main.py`)
- [ ] **`api_test` (테스트 프레임워크) 개발**
    - [ ] 테스트 실행에 필요한 공통 모듈 개발 (`api_test/core/`)
    - [ ] `pytest`를 호출하고 리포트를 생성하는 실행기 개발 (`api_test/run.py`)
- [ ] **프로젝트 구조 변경**
    - [ ] `app` 폴더 삭제 (완료)
    - [ ] `api_test_gen`, `api_test` 패키지 구조 생성 (완료)
    - [ ] 기본 파일 생성 (완료)