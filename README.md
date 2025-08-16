# AI 기반 API 테스트 자동화 프로젝트

## 🚀 프로젝트 개요
이 프로젝트는 AI 에이전트를 사용하여 API 명세서로부터 테스트 코드를 자동 생성하고, 생성된 코드를 실행 및 관리하는 것을 목표로 합니다.

프로젝트는 두 개의 주요 애플리케이션으로 구성됩니다:
- **`api_test_gen`**: 코드 생성기. Gradio 웹 UI를 통해 API 명세서(PDF)를 입력받아, LangChain/LangGraph와 Ollama 기반의 AI 에이전트가 테스트 코드를 생성합니다.
- **`api_test`**: 테스트 프레임워크. `api_test_gen`이 생성한 `pytest` 코드를 저장하고, 실행하며, Allure 리포트를 통해 결과를 시각화합니다.

## 🛠️ 주요 기술 스택
- **코드 환경**: Poetry
- **언어**: Python 3
- **AI**: LangChain, LangGraph, Ollama
- **웹 UI**: Gradio
- **테스트**: Pytest, Requests
- **리포트**: Allure

## 📂 프로젝트 구조
```
.
├── api_test_gen/      # AI 코드 생성기
│   ├── main.py          # Gradio UI 실행 파일
│   ├── agent/           # LangChain/LangGraph 에이전트
│   └── docs/            # API 명세서 저장 폴더
├── api_test/          # 테스트 프레임워크
│   ├── tests/         # 생성된 테스트 코드가 저장되는 곳
│   ├── core/          # 테스트 실행에 필요한 공통 모듈
│   └── run.py           # 테스트 실행 스크립트
├── results/           # Allure 리포트 등 결과 파일 저장
├── pyproject.toml     # Poetry 프로젝트 설정 및 의존성 관리
└── README.md          # 프로젝트 설명 문서
```

## ⚙️ 설치 및 실행 방법

### 1. 사전 준비: Ollama 설치 및 모델 다운로드
이 프로젝트는 로컬 AI 모델을 사용하므로 Ollama 설치가 반드시 필요합니다.

- **Ollama 설치**: [ollama.com](https://ollama.com/) 공식 홈페이지의 가이드에 따라 설치를 진행합니다.
- **AI 모델 다운로드**: Ollama 설치 후, 터미널에서 다음 명령어를 실행하여 프로젝트에서 사용할 모델을 다운로드합니다.
  ```bash
  ollama pull gpt-oss:20b
  ```
- **Ollama 실행**: 모델 다운로드 후, Ollama 애플리케이션이 백그라운드에서 실행 중인지 확인합니다.

### 2. 프로젝트 의존성 설치
프로젝트에 필요한 모든 Python 라이브러리를 설치합니다.
```bash
poetry install
```

### 3. 테스트 코드 생성기 실행
다음 명령어를 실행하여 Gradio 기반의 웹 UI를 시작합니다.
```bash
poetry run python api_test_gen/main.py
```
웹 브라우저에서 UI가 열리면, API 명세서 PDF 파일을 업로드하여 테스트 코드 생성을 시작할 수 있습니다.

### 4. 테스트 실행 및 리포트 확인
생성된 테스트를 실행하고 Allure 리포트를 확인합니다.
```bash
poetry run python api_test/run.py
```
테스트가 완료되면 Allure 리포트가 자동으로 생성되어 웹 브라우저에서 열립니다.
