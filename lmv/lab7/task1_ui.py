import random
import sys

from PyQt6 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(642, 357)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(11, 61, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(10, 270, 551, 61))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(11, 100, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(11, 150, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 143, 171, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.remove_elements)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 551, 61))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Task1"))
        self.label.setText(_translate("Form", "Enter parameters N and K: "))
        self.pushButton.setText(_translate("Form", "Remove Elements"))

    def remove_elements(self):
        try:
            N = int(self.lineEdit.text())
            K = int(self.lineEdit_2.text())

            if N >= K:
                self.label_2.setText("N must be less than K")
                return

            random_list = [random.randint(1, 100) for _ in range(20)]
            self.label_3.setText("Random List: " + ', '.join(map(str, random_list)))

            if K > len(random_list):
                K = len(random_list)

            del random_list[N - 1:K]

            self.label_2.setText("Updated List: " + ', '.join(map(str, random_list)))

        except ValueError:
            self.label_2.setText("Please enter valid integers for N and K")

app = QtWidgets.QApplication(sys.argv)
task3_dialog = QtWidgets.QDialog()
ui = Ui_Form()
ui.setupUi(task3_dialog)
task3_dialog.show()
sys.exit(app.exec())