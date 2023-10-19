import sys
from cx_Freeze import setup, Executable

icon_file = "logo/rubiks.ico"
appName = "RubiksFrescoMaker"

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI"

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "excludes": ["result0", "result1", "result2", "result3", "result4", "result5"],
    "include_files": "logo/"
}

setup(
    name=appName,
    version="0.1",
    description="Rubiks fresco maker made by team 6 of Algosup Students",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "main.py",
            base=base,
            target_name=appName,
            icon=icon_file
        )
    ]
)