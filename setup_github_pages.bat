@echo off
REM GitHub Pages Deployment Setup Script for Windows

echo.
echo ========================================
echo  Churn Prediction - GitHub Pages Setup
echo ========================================
echo.

REM Step 1: Check if Git is installed
echo [1/5] Checking Git installation...
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed. Please install Git from https://git-scm.com/
    pause
    exit /b 1
)
echo ✓ Git is installed

REM Step 2: Check if docs folder exists
echo.
echo [2/5] Checking docs folder...
if not exist "docs" (
    echo ERROR: docs folder not found. Please ensure you are in the project root.
    pause
    exit /b 1
)
echo ✓ docs folder found

REM Step 3: Check for required files
echo.
echo [3/5] Checking required files...
if not exist "docs\index.html" (
    echo ERROR: docs\index.html not found
    pause
    exit /b 1
)
if not exist ".nojekyll" (
    echo ERROR: .nojekyll file not found
    pause
    exit /b 1
)
echo ✓ All required files present

REM Step 4: Verify images folder
echo.
echo [4/5] Checking images folder...
if not exist "docs\assets\images" (
    mkdir "docs\assets\images"
    echo ⚠ Created docs\assets\images folder
    echo   Please add dashboard.png and churn.png to this folder
) else (
    echo ✓ images folder exists
    dir /b "docs\assets\images" 2>nul | find /c /v "" > nul
    if not errorlevel 1 (
        echo   Images found:
        dir /b "docs\assets\images"
    ) else (
        echo ⚠ WARNING: No images found in docs\assets\images
        echo   You can add them later
    )
)

REM Step 5: Git status
echo.
echo [5/5] Git repository status...
git status >nul 2>&1
if errorlevel 1 (
    echo ERROR: Not a Git repository. Run: git init
    pause
    exit /b 1
)
echo ✓ Git repository verified

echo.
echo ========================================
echo  ✓ SETUP COMPLETE!
echo ========================================
echo.
echo Next steps:
echo   1. Add your images to: docs\assets\images\
echo      - dashboard.png
echo      - churn.png
echo.
echo   2. Commit changes:
echo      git add .
echo      git commit -m "Deploy to GitHub Pages"
echo      git push origin Readytogo
echo.
echo   3. Go to GitHub Settings ^> Pages
echo      - Source: GitHub Actions
echo      - Save
echo.
echo   4. Wait 1-2 minutes for deployment
echo.
echo   5. Your site will be at:
echo      https://yourusername.github.io/Churn_Prediction
echo.
echo Documentation: See DEPLOYMENT_GUIDE.md
echo.
pause
