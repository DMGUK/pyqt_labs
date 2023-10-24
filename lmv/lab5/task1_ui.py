from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(438, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 401, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.perform_operation)
        self.resultLabel = QtWidgets.QLabel(Form)
        self.resultLabel.setGeometry(QtCore.QRect(20, 100, 401, 16))
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Task 1"))
        self.label.setText(_translate("Form", "Enter array (comma separated):"))
        self.pushButton.setText(_translate("Form", "Transform"))

    def perform_operation(self):
        input_array = [int(x) for x in self.lineEdit.text().split(',')]

        if len(input_array) < 3:
            self.resultLabel.setText("Array must have at least 3 elements.")
            return

        first_element = input_array[0]
        transformed_array = [first_element]

        for i in range(1, len(input_array) - 1):
            if input_array[i] % 2 == 0:
                transformed_array.append(input_array[i] + first_element)
            else:
                transformed_array.append(input_array[i])

        transformed_array.append(input_array[-1])

        self.resultLabel.setText("Transformed array: " + ', '.join(map(str, transformed_array)))


app = QtWidgets.QApplication(sys.argv)
task1_dialog = QtWidgets.QDialog()
ui = Ui_Form()
ui.setupUi(task1_dialog)
task1_dialog.show()
sys.exit(app.exec())
