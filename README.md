# For Users:
If after trying to launch the application, you get an error "braw2mov can`t be opened because Apple canno tcheck it for malicioues software", follow these steps:

- In the Finder on Mac, find the app you want to open.
- Hold down the Control key, click on the application icon, then select "Open" in the context menu.
- Click "Open".

> The application is saved in the list of exceptions from the security settings, and it can be opened at any time by double-clicking, like any normal application..

# For Devs:

Command for pyinstaller:
```
pyinstaller --noconfirm --onedir --windowed --name braw2mov --icon "b2m.icns" --add-data "./song.mp3:." --add-data "./speaker.png:."  "./app.py"
```

U also can install with `pyinstaller brew2mov.spec`
