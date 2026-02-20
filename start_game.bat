@echo off
echo Starting Digital Prison Game...

:: Start Backend in a new window
start "Digital Prison Backend" cmd /k "python server.py"

:: Start Frontend in a new window
cd frontend
start "Digital Prison Frontend" cmd /k "npm run dev"

echo servers started! Access the game at the URL shown in the Frontend window (usually http://localhost:5173).
pause
