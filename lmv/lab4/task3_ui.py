from PyQt6 import QtCore, QtGui, QtWidgets
import sys

from PyQt6.QtWidgets import QApplication, QWidget
from user_data import user_username, user_password


class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):

        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(51, 41, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(51, 90, 121, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(220, 41, 132, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 90, 132, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 180, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login window (Task 3)"))
        self.label.setText(_translate("Dialog", "Enter your login: "))
        self.label_2.setText(_translate("Dialog", "Enter your password: "))
        self.pushButton.setText(_translate("Dialog", "Sign in"))

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        msg = QtWidgets.QMessageBox()

        if username == user_username and password == user_password:
            msg.information(self, 'Sign-in success', 'You have successfully logged in')
            msg.setFixedHeight(200)
            msg.setFixedWidth(300)
        else:
            msg.warning(self, 'Sign-in failure', 'You have failed to log in')
            msg.setFixedHeight(200)
            msg.setFixedWidth(300)

app = QApplication(sys.argv)
dialog = QtWidgets.QDialog()
ex = Ui_Dialog()
ex.setupUi(dialog)
dialog.show()
sys.exit(app.exec())