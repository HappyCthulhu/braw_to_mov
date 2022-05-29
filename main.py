import sys
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog
from ui_imagedialog import Ui_ImageDialog

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_ImageDialog()
ui.setupUi(window)
ui.test()

window.show()
sys.exit(app.exec())
