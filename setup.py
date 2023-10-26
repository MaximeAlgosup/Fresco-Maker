import sys
from cx_Freeze import setup, Executable

icon_file = "assets/rubiks.ico"
appName = "Fresco Maker"

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI"

# Dependencies are automatically detected, but it might need fine-tuning.
build_exe_options = {
    "excludes": ["fresco_Installer.iit"],
    "include_files": "assets"
}

setup(
    name=appName,
    version="1.0",
    description="Rubik's cube fresco maker made by team 6 of ALGOSUP Students",
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