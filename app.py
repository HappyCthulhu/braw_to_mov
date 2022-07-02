import os
from pathlib import PurePath, Path

import pygame
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog

from braw_to_mov import Ui_MainWindow
from find_path import find_path


class MainController:
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

        if self.check_if_only_braw_files(f_ps) and f_ps:
            self.display_files(f_ps)
            self.ui.convert_button.setEnabled(True)

    def check_if_only_braw_files(self, f_names):
        for f_name in f_names:
            if not f_name.endswith('.braw'):
                self.ui.files_label.setText(f'Only .braw files are allowed! Those files is not .braw:\n'
                                            f'{f_name}')
                return False
        return True

    def display_files(self, f_ps):
        self.f_names = [PurePath(fp).parts[-1] for fp in f_ps]
        self.dp = Path(f_ps[0]).parent.absolute()
        self.ui.files_label.setText(', '.join(self.f_names))

    def rename_files(self):
        for old_name in self.f_names:
            old_fp = Path(self.dp).joinpath(old_name)
            new_fp = f'{Path(self.dp).joinpath(old_name.split(".")[0])}.mov'

            os.rename(old_fp, new_fp)
        self.ui.files_label.setText('Success!')
        self.ui.convert_button.setEnabled(False)

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
    pygame.mixer.music.load(find_path('song.mp3'))
    MainWindow.show()

    sys.exit(app.exec())
