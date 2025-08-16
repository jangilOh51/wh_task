@echo off
chcp 65001 > nul

cd /d "%~dp0..\"

for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /format:list') do set datetime=%%I
set DATE_DIR=%datetime:~2,6%
set TIMESTAMP_DIR=%datetime:~2,6%_%datetime:~8,6%

set ALLURE_RESULTS_DIR=results\allure-results
set ALLURE_REPORT_DIR=results\allure-report\%DATE_DIR%\%TIMESTAMP_DIR%

mkdir %ALLURE_REPORT_DIR%


set MARKER_ARG=
if not "%~1"=="" (
    echo Running tests with marker: %1
    set MARKER_ARG=-m %1
) else (
    echo Running all tests
)
echo ==================================
echo        Running pytest...
echo ==================================
poetry run pytest -v %MARKER_ARG% --alluredir=%ALLURE_RESULTS_DIR% --clean-alluredir

echo ==================================
echo    Generating Allure report...
echo ==================================
poetry run allure generate %ALLURE_RESULTS_DIR% -o %ALLURE_REPORT_DIR% --clean

echo ==================================
echo      Opening Allure report...
echo ==================================
poetry run allure open %ALLURE_REPORT_DIR%

set datetime=
set DATE_DIR=
set TIMESTAMP_DIR=
set ALLURE_RESULTS_DIR=
set ALLURE_REPORT_DIR=
set MARKER_ARG=
