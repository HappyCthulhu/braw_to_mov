import os
from pathlib import PurePath, Path
import pygame
from PyQt6.QtCore import QResource
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog

from braw_to_mov import Ui_MainWindow
from find_path import find_path


class MainController:
    def __init__(self, ui):
        self.ui = ui
        self.connect_slots()
        self.music_status = False
        self.formatting_direction = 0

    def connect_slots(self):
        self.ui.select_button.clicked.connect(self.select_files)
        self.ui.convert_button.clicked.connect(self.rename_files)
        self.ui.speaker_button.clicked.connect(self.control_music)
        self.ui.format_slider.valueChanged.connect(self.define_format)

    def define_format(self):
        self.formatting_direction = self.ui.format_slider.value()

    def select_files(self):
        if self.ui.format_slider.value() == 0:
            self.format_from = '.braw'
            self.format_to = '.mov'
        else:
            self.format_from = '.mov'
            self.format_to = '.braw'

        f_ps, _ = QFileDialog.getOpenFileNames(caption='Navigation',
                                               filter=f"{self.format_from} files (*{self.format_from});;All Files (*)")

        if self.check_if_input_files_have_correct_format(f_ps, self.format_from) and f_ps:
            f_names = self.display_files(f_ps)
            f_names_with_brackets = ', '.join([f'"{f_name}"' for f_name in f_names])
            self.ui.files_label.setText(f_names_with_brackets)
            self.ui.convert_button.setEnabled(True)
        else:
            self.ui.files_label.setStyleSheet("color: rgb(244, 244, 244);\n"
                                              "font-weight: normal;")
            self.ui.convert_button.setEnabled(False)

    def check_if_input_files_have_correct_format(self, f_ps, format_from):

        not_needed_format = [fp for fp in f_ps if not fp.endswith(format_from)]

        if not_needed_format:
            f_names = self.display_files(not_needed_format)
            f_names_with_brackets = ', '.join([f'"{f_name}"' for f_name in f_names])

            self.ui.files_label.setText(f'❗These files are not {format_from}:\n'
                                        f'{f_names_with_brackets}')
            # TODO: не могу заставить это менять цвет:
            # self.ui.files_label.setStyleSheet("color: rgb(0, 0, 0)")
            return False

        return True

    def display_files(self, f_ps):
        self.f_names = [PurePath(fp).parts[-1] for fp in f_ps]
        self.dp = Path(f_ps[0]).parent.absolute()
        return self.f_names

    def rename_files(self):
        for old_name in self.f_names:
            old_fp = Path(self.dp).joinpath(old_name)
            new_fp = f'{Path(self.dp).joinpath(old_name.split(".")[0])}{self.format_to}'

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
    QResource.registerResource(find_path("resource.rcc"))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    reactions = MainController(ui)

    pygame.mixer.init()
    pygame.mixer.music.load(find_path('song.mp3'))
    MainWindow.show()

    sys.exit(app.exec())
