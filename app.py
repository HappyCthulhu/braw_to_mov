import time
from pathlib import PurePath, Path

import pygame
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog

from braw_to_mov import Ui_MainWindow
from logic import rename_files


class Reactions:
    # TODO: сделать надпись в духе "Success"
    def __init__(self, ui):
        self.ui = ui

    def ui_reactions(self):
        self.ui.select_button.clicked.connect(self.select_files)
        self.ui.convert_button.clicked.connect(self.rename_files)

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
        # TODO: сделать некликабельным, пока не появятся переменные f_names, dp
        rename_files(self.f_names, self.dp)

    def stop_music(self):
        pygame.mixer.music.stop()


if __name__ == "__main__":
    import sys

    search_string_file = 'search_query.yaml'

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    reactions = Reactions(ui)
    reactions.ui_reactions()

    pygame.mixer.init()
    pygame.mixer.music.load('song.mp3')
    pygame.mixer.music.play()

    MainWindow.show()

    sys.exit(app.exec())
