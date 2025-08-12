# API 자동화 테스트 프로젝트

## 🚀 프로젝트 개요
이 프로젝트는 API 테스트 자동화 구현 및 테스트 케이스 문서화를 목표로 합니다.

## 🛠️ 주요 기술 스택 및 라이브러리
- **코드 환경**: Poetry
- **언어**: Python 3
- **테스트 프레임워크**: Pytest
- **리포트**: Allure
- **API 호출**: Requests
- **코드 포맷터**: Black

## 📂 프로젝트 구조
```
.
├── app/
│   ├── codes/          # Enum들로 고정된 값들을 정의하는 패키지
│   ├── common/         # 공통 함수를 정의하는 패키지
│   ├── core/           # requests 호출 및 주요 모듈에 대한 패키지 (ApiClient 포함)
│   ├── api/            # API 호출 및 관련 로직을 정의하는 패키지
│   ├── models/         # DTO, Model 등을 저장 및 관리
│   └── tests/          # 테스트 케이스
├── scripts/            # 테스트 실행 배치 파일
├── config/             # 설정 파일
├── task/               # 시험 문제
├── results/            # 테스트 케이스를 저장하는 폴더, 결과파일
├── pyproject.toml      # Poetry 프로젝트 설정 및 의존성 관리
├── poetry.lock         # Poetry 의존성 잠금 파일
├── README.md           # 프로젝트 설명 문서
└── .gitignore          # Git 무시 파일 설정
```

## ⚙️ 설치 및 설정 방법

### 1. Poetry 설치 (선택 사항)
Poetry가 설치되어 있지 않다면, 다음 명령어를 사용하여 설치할 수 있습니다:
```bash
curl -sSL https://install.python-poetry.org | python -
```
또는 공식 문서를 참조하세요: [Poetry Installation](https://python-poetry.org/docs/#installation)

### 2. 프로젝트 클론
```bash
git clone [프로젝트_레포지토리_URL]
cd [프로젝트_디렉토리명]
```

### 3. 의존성 설치
프로젝트의 모든 의존성을 설치합니다.
```bash
poetry install
```

### 4. 개발 의존성 설치 (Black 등)
코드 포맷팅 도구인 Black과 같은 개발 환경에 필요한 의존성을 설치합니다.
```bash
poetry install --with dev
```
또는 개별적으로 추가:
```bash
poetry add --group dev black
```

## 📏 코딩 컨벤션
이 프로젝트는 `black`을 사용하여 코드 포맷팅을 관리합니다. `pyproject.toml` 파일에 설정이 정의되어 있습니다.
- **라인 길이**: 88자
- **타겟 Python 버전**: 3.12

## 🧪 테스트 실행
테스트는 `pytest` 프레임워크를 사용합니다.
```bash
poetry run pytest
```
Allure 리포트를 생성하려면:
```bash
poetry run pytest --alluredir=allure-results
```
Allure 리포트를 확인하려면:
```bash
allure serve allure-results
```
(Allure Commandline 도구가 설치되어 있어야 합니다.)