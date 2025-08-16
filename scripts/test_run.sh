#!/bin/bash

# 스크립트가 있는 디렉토리의 상위 디렉토리를 프로젝트 루트로 설정
PROJECT_ROOT=$(dirname "$0")/..
cd "$PROJECT_ROOT" || exit

# 날짜 및 시간 기반 리포트 디렉토리 이름 생성
DATE_DIR=$(date +%y%m%d)
TIMESTAMP_DIR=$(date +%y%m%d_%H%M%S)

# Allure 결과 및 리포트 디렉토리 설정
ALLURE_RESULTS_DIR="results/allure-results"
ALLURE_REPORT_DIR="results/allure-report/$DATE_DIR/$TIMESTAMP_DIR"

# 리포트 디렉토리 생성
mkdir -p $ALLURE_REPORT_DIR

# Pytest 마커 설정 (첫 번째 인자가 있으면 사용)
MARKER=$1
PYTEST_ARGS="-v --alluredir=$ALLURE_RESULTS_DIR --clean-alluredir"

if [ -n "$MARKER" ]; then
  echo "Running tests with marker: $MARKER"
  PYTEST_ARGS="$PYTEST_ARGS -m $MARKER"
else
  echo "Running all tests"
fi

# Pytest 실행
echo "=================================="
echo "       Running pytest..."
echo "=================================="
poetry run pytest $PYTEST_ARGS

# Allure 리포트 생성
echo "=================================="
echo "   Generating Allure report..."
echo "=================================="
poetry run allure generate $ALLURE_RESULTS_DIR -o $ALLURE_REPORT_DIR --clean

# Allure 리포트 열기
echo "=================================="
echo "     Opening Allure report..."
echo "=================================="
poetry run allure open $ALLURE_REPORT_DIR
