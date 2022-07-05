# Form implementation generated from reading ui file 'braw_to_mov.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(413, 383)
        MainWindow.setMouseTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(5, 8, 45);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.speaker_layout = QtWidgets.QHBoxLayout()
        self.speaker_layout.setContentsMargins(-1, 0, 10, 10)
        self.speaker_layout.setObjectName("speaker_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.speaker_layout.addItem(spacerItem)
        self.speaker_button = QtWidgets.QPushButton(self.centralwidget)
        self.speaker_button.setMaximumSize(QtCore.QSize(24, 24))
        self.speaker_button.setStyleSheet("background-image: url(:/icons/speaker.png);")
        self.speaker_button.setText("")
        self.speaker_button.setObjectName("speaker_button")
        self.speaker_layout.addWidget(self.speaker_button)
        self.gridLayout.addLayout(self.speaker_layout, 4, 0, 2, 1)
        self.main_layout = QtWidgets.QGridLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setVerticalSpacing(10)
        self.main_layout.setObjectName("main_layout")
        self.default_label = QtWidgets.QLabel(self.centralwidget)
        self.default_label.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.default_label.setFont(font)
        self.default_label.setStyleSheet("color: rgb(244, 244, 244);\n"
"font-weight:bold;")
        self.default_label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.default_label.setScaledContents(True)
        self.default_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.default_label.setWordWrap(False)
        self.default_label.setObjectName("default_label")
        self.main_layout.addWidget(self.default_label, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.main_layout.addItem(spacerItem1, 0, 0, 1, 1)
        self.buttons_layout = QtWidgets.QGridLayout()
        self.buttons_layout.setContentsMargins(-1, 20, -1, -1)
        self.buttons_layout.setVerticalSpacing(10)
        self.buttons_layout.setObjectName("buttons_layout")
        self.select_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_button.setMinimumSize(QtCore.QSize(150, 40))
        self.select_button.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.select_button.setFont(font)
        self.select_button.setStyleSheet("background-color: rgb(41, 104, 199);\n"
"color: rgb(244, 244, 244);\n"
"font-weight: bold;")
        self.select_button.setObjectName("select_button")
        self.buttons_layout.addWidget(self.select_button, 1, 0, 1, 1)
        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.convert_button.sizePolicy().hasHeightForWidth())
        self.convert_button.setSizePolicy(sizePolicy)
        self.convert_button.setMinimumSize(QtCore.QSize(150, 40))
        self.convert_button.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.convert_button.setFont(font)
        self.convert_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.convert_button.setAutoFillBackground(False)
        self.convert_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(41, 104, 199);\n"
"    color: rgb(244, 244, 244);\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: rgb(159, 159, 159);\n"
"    color: rgb(244, 244, 244);\n"
"    font-weight: bold;\n"
"}")
        self.convert_button.setObjectName("convert_button")
        self.buttons_layout.addWidget(self.convert_button, 2, 0, 1, 1)
        self.main_layout.addLayout(self.buttons_layout, 4, 0, 1, 1)
        self.files_label = QtWidgets.QLabel(self.centralwidget)
        self.files_label.setMaximumSize(QtCore.QSize(16777215, 400))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.files_label.setFont(font)
        self.files_label.setStyleSheet("color: rgb(244, 244, 244);\n"
"font-weight:normal;")
        self.files_label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.files_label.setScaledContents(True)
        self.files_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.files_label.setWordWrap(True)
        self.files_label.setObjectName("files_label")
        self.main_layout.addWidget(self.files_label, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.main_layout.addItem(spacerItem2, 8, 0, 1, 1)
        self.slider_layout = QtWidgets.QHBoxLayout()
        self.slider_layout.setContentsMargins(-1, 20, -1, -1)
        self.slider_layout.setObjectName("slider_layout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.slider_layout.addItem(spacerItem3)
        self.braw_to_mov_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.braw_to_mov_label.sizePolicy().hasHeightForWidth())
        self.braw_to_mov_label.setSizePolicy(sizePolicy)
        self.braw_to_mov_label.setMinimumSize(QtCore.QSize(90, 0))
        self.braw_to_mov_label.setStyleSheet("color: rgb(244, 244, 244);\n"
"font-weight: normal;")
        self.braw_to_mov_label.setObjectName("braw_to_mov_label")
        self.slider_layout.addWidget(self.braw_to_mov_label)
        self.format_slider = QtWidgets.QSlider(self.centralwidget)
        self.format_slider.setMaximumSize(QtCore.QSize(30, 16777215))
        self.format_slider.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.format_slider.setMaximum(1)
        self.format_slider.setPageStep(1)
        self.format_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.format_slider.setObjectName("format_slider")
        self.slider_layout.addWidget(self.format_slider)
        self.mov_to_braw_label = QtWidgets.QLabel(self.centralwidget)
        self.mov_to_braw_label.setMinimumSize(QtCore.QSize(90, 0))
        self.mov_to_braw_label.setStyleSheet("color: rgb(244, 244, 244);\n"
"font-weight: normal;")
        self.mov_to_braw_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.mov_to_braw_label.setObjectName("mov_to_braw_label")
        self.slider_layout.addWidget(self.mov_to_braw_label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.slider_layout.addItem(spacerItem4)
        self.main_layout.addLayout(self.slider_layout, 3, 0, 1, 1)
        self.gridLayout.addLayout(self.main_layout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.default_label.setText(_translate("MainWindow", "The names of selected files will appear here:"))
        self.select_button.setText(_translate("MainWindow", "Select Files"))
        self.convert_button.setText(_translate("MainWindow", "Convert Files"))
        self.files_label.setText(_translate("MainWindow", "No files is selected yet"))
        self.braw_to_mov_label.setText(_translate("MainWindow", ".braw->.mov"))
        self.mov_to_braw_label.setText(_translate("MainWindow", ".mov->.braw"))
