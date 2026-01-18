@echo off
setlocal
cd "c:\Users\K.Raj Kumar\Documents\project"

echo Adding files...
git add .

echo Committing changes...
git commit -m "Add predict another button and localStorage persistence to GitHub Pages site"

echo Pulling latest changes...
git pull origin main --rebase

echo Pushing to GitHub...
git push origin main

echo Done!
pause
