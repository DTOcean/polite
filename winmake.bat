@ECHO OFF
SET curdir=%cd%


IF "%1" == "install" CALL :Install
IF "%1" == "test" CALL :Test
IF "%1" == "pylint" CALL :Pylint

:Return
CD %curdir%
EXIT /B %ERRORLEVEL%

:: Function to install the program
:Install
CD %~dp0 && (
    CALL python setup.py clean --all
    CALL python setup.py install
    CALL :Test
) || ( GOTO Return )
EXIT /B 0

:: Function to test the program
:Test
CD %~dp0 && (
    CALL python setup.py cleanpyc
    CALL python setup.py test -a "-rsx tests"
) || ( GOTO Return )
EXIT /B 0

:: Function to run pylint
:Pylint
CD %~dp0
setlocal enableDelayedExpansion
SET result=
FOR /f "tokens=*" %%a in ('dir tests\*.py /B') DO SET result=!result!tests\%%a 
CALL pylint setup.py polite %result%
GOTO Return
