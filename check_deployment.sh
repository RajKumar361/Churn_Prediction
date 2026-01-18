#!/bin/bash
# GitHub Pages Deployment Verification Script for Mac/Linux

echo ""
echo "========================================="
echo "  Churn Prediction - Deployment Check"
echo "========================================="
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check 1: Git
echo -n "[1/7] Checking Git... "
if command -v git &> /dev/null; then
    echo -e "${GREEN}✓${NC} $(git --version | cut -d' ' -f3)"
else
    echo -e "${RED}✗${NC} Git not installed"
    exit 1
fi

# Check 2: docs folder
echo -n "[2/7] Checking docs folder... "
if [ -d "docs" ]; then
    echo -e "${GREEN}✓${NC} Found"
else
    echo -e "${RED}✗${NC} Not found"
    exit 1
fi

# Check 3: index.html
echo -n "[3/7] Checking docs/index.html... "
if [ -f "docs/index.html" ]; then
    echo -e "${GREEN}✓${NC} Found ($(wc -c < docs/index.html) bytes)"
else
    echo -e "${RED}✗${NC} Not found"
    exit 1
fi

# Check 4: .nojekyll
echo -n "[4/7] Checking .nojekyll... "
if [ -f ".nojekyll" ]; then
    echo -e "${GREEN}✓${NC} Found"
else
    echo -e "${RED}✗${NC} Not found"
    exit 1
fi

# Check 5: CSS
echo -n "[5/7] Checking docs/assets/css/style.css... "
if [ -f "docs/assets/css/style.css" ]; then
    echo -e "${GREEN}✓${NC} Found ($(wc -c < docs/assets/css/style.css) bytes)"
else
    echo -e "${RED}✗${NC} Not found"
    exit 1
fi

# Check 6: JS
echo -n "[6/7] Checking docs/assets/js/main.js... "
if [ -f "docs/assets/js/main.js" ]; then
    echo -e "${GREEN}✓${NC} Found ($(wc -c < docs/assets/js/main.js) bytes)"
else
    echo -e "${RED}✗${NC} Not found"
    exit 1
fi

# Check 7: Images
echo -n "[7/7] Checking docs/assets/images/... "
if [ -d "docs/assets/images" ]; then
    IMG_COUNT=$(find docs/assets/images -type f | wc -l)
    if [ $IMG_COUNT -gt 0 ]; then
        echo -e "${GREEN}✓${NC} Found $IMG_COUNT image(s)"
    else
        echo -e "${YELLOW}!${NC} Folder empty (add dashboard.png and churn.png)"
    fi
else
    echo -e "${RED}✗${NC} Folder not found"
    exit 1
fi

echo ""
echo "========================================="
echo -e "${GREEN}✓ All checks passed!${NC}"
echo "========================================="
echo ""
echo "Ready to deploy. Run these commands:"
echo ""
echo "  git add ."
echo "  git commit -m 'Deploy to GitHub Pages'"
echo "  git push origin Readytogo"
echo ""
echo "Then go to:"
echo "  GitHub → Settings → Pages → Source: GitHub Actions"
echo ""
