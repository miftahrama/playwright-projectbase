@echo off
REM ============================================
REM Allure Report Generator
REM Generates report from latest test run folder
REM Uses matching date_counter subfolder structure
REM ============================================

setlocal enabledelayedexpansion

REM Find the latest date_counter folder
set "LATEST_FOLDER="
for /f "delims=" %%F in ('dir /b /ad /o-n allure-results\????????_? 2^>nul') do (
    set "LATEST_FOLDER=%%F"
    goto :found
)

if not defined LATEST_FOLDER (
    echo ERROR: No test run folders found in allure-results!
    echo Run tests first: pytest
    exit /b 1
)

:found
REM Create matching report folder
set "REPORT_FOLDER=allure-report\%LATEST_FOLDER%"
mkdir "%REPORT_FOLDER%" 2>nul

echo ============================================
echo Generating Allure Report
echo ============================================
echo Results folder: allure-results\%LATEST_FOLDER%
echo Report folder:  %REPORT_FOLDER%
echo ============================================

REM Generate report in date_counter subfolder
C:\allure\allure-2.32.0\bin\allure generate allure-results\%LATEST_FOLDER% -o "%REPORT_FOLDER%" --clean

if %errorlevel% equ 0 (
    echo.
    echo ============================================
    echo Report generated successfully!
    echo ============================================
    echo.
    echo Opening report in browser...
    C:\allure\allure-2.32.0\bin\allure open "%REPORT_FOLDER%"
) else (
    echo ERROR: Failed to generate report!
    exit /b 1
)
