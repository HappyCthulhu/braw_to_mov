from pathlib import PurePath, Path

import pygame
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog

from braw_to_mov import Ui_MainWindow
from logic import rename_files


class MainController:
    # TODO: сделать надпись в духе "Success"
    def __init__(self, ui):
        self.ui = ui
        self.connect_slots()
        self.music_status = False

    def connect_slots(self):
        self.ui.select_button.clicked.connect(self.select_files)
        self.ui.convert_button.clicked.connect(self.rename_files)
        self.ui.speaker_button.clicked.connect(self.control_music)

    def select_files(self):
        f_ps, _ = QFileDialog.getOpenFileNames(caption='Navigation', filter=".braw files (*.braw);;All Files (*)")

        if f_ps:
            self.display_files(f_ps)
            self.ui.convert_button.setEnabled(True)

    def display_files(self, f_ps):
        self.f_names = [PurePath(fp).parts[-1] for fp in f_ps]
        self.dp = Path(f_ps[0]).parent.absolute()
        self.ui.files_label.setText(', '.join(self.f_names))

    def rename_files(self):
        # TODO: добавить проверку, что файлы действительно .bmow
        rename_files(self.f_names, self.dp)

    def control_music(self):
        if not self.music_status:
            pygame.mixer.music.play()
            self.music_status = True
        else:
            pygame.mixer.music.stop()
            self.music_status = False


if __name__ == "__main__":
    import sys

    search_string_file = 'search_query.yaml'

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    reactions = MainController(ui)

    pygame.mixer.init()
    pygame.mixer.music.load('song.mp3')
    MainWindow.show()

    sys.exit(app.exec())
