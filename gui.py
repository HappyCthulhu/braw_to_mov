from PyQt6 import QtCore, QtWidgets


class Ui_ImageDialog(object):
    def setupUi(self, ImageDialog):
        ImageDialog.setObjectName("ImageDialog")
        ImageDialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(ImageDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(ImageDialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(ImageDialog)
        self.radioButton.setGeometry(QtCore.QRect(90, 90, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(ImageDialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(130, 140, 185, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(ImageDialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(250, 20, 104, 71))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.dateEdit = QtWidgets.QDateEdit(ImageDialog)
        self.dateEdit.setGeometry(QtCore.QRect(20, 190, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit = QtWidgets.QLineEdit(ImageDialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 130, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(ImageDialog)
        self.buttonBox.accepted.connect(ImageDialog.accept)
        self.buttonBox.rejected.connect(ImageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ImageDialog)

    def retranslateUi(self, ImageDialog):
        _translate = QtCore.QCoreApplication.translate
        ImageDialog.setWindowTitle(_translate("ImageDialog", "Dialog"))
        self.pushButton.setText(_translate("ImageDialog", "PushButton"))
        self.radioButton.setText(_translate("ImageDialog", "RadioButton"))
        self.commandLinkButton.setText(_translate("ImageDialog", "CommandLinkButton"))
