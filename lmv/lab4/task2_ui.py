from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Task 2")
        Dialog.resize(500, 210)
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 10, 132, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 37, 132, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 64, 131, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 37, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 64, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(8, 120, 450, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 160, 171, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_2, self.lineEdit)
        Dialog.setTabOrder(self.lineEdit, self.lineEdit_3)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Number order checker (Task 2)"))
        self.label.setText(_translate("Dialog", "Enter the first number: "))
        self.label_2.setText(_translate("Dialog", "Enter the second number: "))
        self.label_3.setText(_translate("Dialog", "Enter the third number:"))
        self.label_4.setText(_translate("Dialog", "The result is: "))
        self.pushButton.setText(_translate("Dialog", "Check the results"))
        self.pushButton.clicked.connect(self.performOperation)

    def performOperation(self):
        try:
            x = int(self.lineEdit.text())
            y = int(self.lineEdit_2.text())
            z = int(self.lineEdit_3.text())

            if x < y < z or x > y > z:
                x *= 2
                y *= 2
                z *= 2
            else:
                x = -x
                y = -y
                z = -z

            result = f'First number: {x}, Second number: {y}, Third number: {z}'
            self.label_4.setText(f'Result: {result}')
        except ValueError:
            self.label_4.setText('Please enter valid numbers.')


app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(dialog)
dialog.show()
sys.exit(app.exec())

