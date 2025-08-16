# API 자동화 테스트 프로젝트

## 🚀 프로젝트 개요
이 프로젝트는 `pytest`를 이용한 API 테스트 자동화 프레임워크입니다. Allure 리포트를 통해 테스트 결과를 시각적으로 확인할 수 있습니다.

## 🛠️ 주요 기술 스택
- **코드 환경**: Poetry
- **언어**: Python 3
- **테스트 프레임워크**: Pytest
- **API 호출**: Requests
- **리포트**: Allure

## 📁 프로젝트 구조
```
.
├── api_test/          # 테스트 프레임워크
│   ├── tests/         # 테스트 코드가 저장되는 곳
│   ├── core/          # 테스트 실행에 필요한 공통 모듈
│   └── run.py         # 테스트 실행 스크립트
├── scripts/           # 테스트 실행 스크립트 폴더
├── results/           # Allure 리포트 등 결과 파일 저장
├── pyproject.toml     # Poetry 프로젝트 설정 및 의존성 관리
└── README.md          # 프로젝트 설명 문서
```

## ⚙️ 사전 준비

### 1. Python 설치
Python 3.9 이상 버전이 필요합니다. [공식 웹사이트](https://www.python.org/downloads/)에서 설치할 수 있습니다.

### 2. Poetry 설치
이 프로젝트는 Poetry를 사용하여 의존성을 관리합니다. Poetry가 설치되어 있지 않다면, 다음 명령어로 설치하세요.
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
자세한 내용은 [Poetry 공식 문서](https://python-poetry.org/docs/#installation)를 참고하세요.

### 3. Allure Commandline 설치
테스트 결과를 Allure 리포트로 생성하기 위해 Allure Commandline 도구가 필요합니다.

- **macOS (Homebrew 사용):**
  ```bash
  brew install allure
  ```
- **Windows (Scoop 사용):**
  ```bash
  scoop install allure
  ```
- **Linux (수동 설치):**
  자세한 내용은 [Allure 공식 문서](https://allurereport.org/docs/getting-started-installation-commandline/)를 참고하여 설치를 진행하세요.


## ⚙️ 설치 및 실행 방법

### 1. 프로젝트 의존성 설치
프로젝트에 필요한 모든 Python 라이브러리를 설치합니다.
```bash
poetry install
```

### 2. 테스트 실행 및 리포트 확인
아래 스크립트를 실행하여 테스트를 진행하고 Allure 리포트를 생성합니다.
```bash
# Windows
scripts\\test_run.bat

# Linux/macOS
./scripts/test_run.sh
```
테스트가 완료되면 `results/allure-report` 디렉토리에서 리포트를 확인할 수 있습니다.

