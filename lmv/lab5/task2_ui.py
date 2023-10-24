from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(436, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 401, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 100, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.display_elements)
        self.resultLabel = QtWidgets.QLabel(Form)
        self.resultLabel.setGeometry(QtCore.QRect(20, 100, 401, 50))
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Array Elements Divider"))
        self.label.setText(_translate("Form", "Enter array (comma separated):"))
        self.pushButton.setText(_translate("Form", "Display Elements"))

    def display_elements(self):
        input_array = [int(x) for x in self.lineEdit.text().split(',')]

        even_elements = [str(x) for x in input_array if x % 2 == 0]
        odd_elements = [str(x) for x in input_array if x % 2 != 0]

        result_text = "Even elements: " + ', '.join(even_elements) + "\n" + "Odd elements: " + ', '.join(odd_elements)

        self.resultLabel.setText(result_text)


app = QtWidgets.QApplication(sys.argv)
task2_dialog = QtWidgets.QDialog()
ui = Ui_Form()
ui.setupUi(task2_dialog)
task2_dialog.show()
sys.exit(app.exec())
