# Active Mouse
Simple script to move the mouse every 10 minutes

## Requirements
 - [Pyinstaller](https://github.com/pyinstaller/pyinstaller)
   - If creating an executable

## Install
- `$ git clone git@github.com:techb/Active-Mouse.git`
- `$ pipenv install`

## Build Executable
- `$ pyinstaller -F active_mouse.py`

## Binaries
I've included a Windows binary found in `dist/active_mouse.exe`. It uses screen locations `100x100` and `200x200`. Mouse moves every 10 minutes. To change these settings, edit `active_mouse.py` and build a new binary using Pyinstaller.
