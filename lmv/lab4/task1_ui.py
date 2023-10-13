from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class Ui_Task1(object):
    def setupUi(self, Task1):
        Task1.setObjectName("Task 1")
        Task1.resize(497, 249)
        self.pushButton = QtWidgets.QPushButton(parent=Task1)
        self.pushButton.setGeometry(QtCore.QRect(170, 170, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=Task1)
        self.label.setGeometry(QtCore.QRect(60, 70, 151, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Task1)
        self.lineEdit.setGeometry(QtCore.QRect(220, 70, 241, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=Task1)
        self.label_2.setGeometry(QtCore.QRect(98, 130, 301, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Task1)
        self.pushButton.clicked.connect(self.findDescription)
        QtCore.QMetaObject.connectSlotsByName(Task1)

    def retranslateUi(self, Task1):
        _translate = QtCore.QCoreApplication.translate
        Task1.setWindowTitle(_translate("Task1", "Number type checker (Task 1)"))
        self.pushButton.setText(_translate("Task1", "Check the result"))
        self.label.setText(_translate("Task1", "Enter the nuber to check : "))
        self.label_2.setText(_translate("Task1", "The result is: "))

    def findDescription(self):
        try:
            number = int(self.lineEdit.text())

            if number < 0:
                sign = 'negative'
            elif number > 0:
                sign = 'positive'
            else:
                sign = 'zero'

            if -9 <= number <= 9:
                magnitude = 'single-digit'
            elif 10 <= abs(number) <= 99:
                magnitude = 'double-digit'
            else:
                magnitude = 'three-digit or more'

            result = f'{sign} {magnitude} number'
            self.label_2.setText(f'Result: {result}')
        except ValueError:
            self.label_2.setText('Please enter a valid number.')


app = QtWidgets.QApplication(sys.argv)
task1_dialog = QtWidgets.QDialog()
ui = Ui_Task1()
ui.setupUi(task1_dialog)
task1_dialog.show()
ui.findDescription()
sys.exit(app.exec())