@echo off
echo Starting the process...

rem Run the input_getter.py script to get user input
python input_getter.py

rem Compile and run the C++ program for sorting
g++ main.cpp -o main
main.exe

rem Run the visualizer.py script to visualize sorting
python visualiser.py

pause
