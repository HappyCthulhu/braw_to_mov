# For Users:

## Instalation steps
1. Download braw2mov.zip from [releases page](https://github.com/HappyCthulhu/braw_to_mov/releases/tag/latest)
2. Unzip file
3. Click it

If after trying to launch the application, you get an error "braw2mov can`t be opened because Apple canno tcheck it for malicioues software", follow these steps:

- In the Finder on Mac, find the app you want to open.
- Hold down the Control key, click on the application icon, then select "Open" in the context menu.
- Click "Open".

> The application is saved in the list of exceptions from the security settings, and it can be opened at any time by double-clicking, like any normal application..

# For Devs:

Commands for pyinstaller:
### OS X:
```
pyinstaller --noconfirm --onedir --windowed --name braw2mov --icon "b2m.icns" --add-data "./song.mp3:." --add-data "./resource.rcc:." "./app.py"
```

### Linux:
```
pyinstaller --noconfirm --onefile  --name braw2mov --icon "b2m.icns" --add-data "./song.mp3:." --add-data "./resource.rcc:." "./app.py"
```

### Windows:
```
pyinstaller --noconfirm --onefile --windowed --name braw2mov --icon "b2m.ico" --add-data "./song.mp3:." --add-data "./resource.rcc:." "./app.py"
```

U also can install with `pyinstaller brew2mov.spec`
