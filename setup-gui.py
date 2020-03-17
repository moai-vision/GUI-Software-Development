from cx_Freeze import setup,Executable
import sys
#import all your used library
import cv2
import numpy as np



base=None #platform base
program="testgui.py" #.py file
logo="logo.ico" #application logo

if sys.platform=="win32": #platform search
   base="Win32GUI"
   

fetch=[Executable(program,base=base,icon=logo)] #executable setups


#setup used packages and module and extra useful resources
build_exe_options = {"packages": ["cv2","numpy"],"include_files":["tcl86t.dll","tk86t.dll"]}


#application environment setup
setup(name="testgui",
      version="1.0",
      description="GUI based software development test",
      options={"build_exe": build_exe_options},
      executables=fetch
      )
