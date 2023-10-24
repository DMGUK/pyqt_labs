from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(439, 337)
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(181, 61, 211, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(parent=Form)
        self.textEdit.setGeometry(QtCore.QRect(60, 40, 61, 171))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(181, 98, 132, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(181, 128, 110, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(319, 98, 75, 24))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "Output the number of elements"))
        self.comboBox.setItemText(1, _translate("Form", "Insert element at the end of vector"))
        self.comboBox.setItemText(2, _translate("Form", "Remove an element from the vector"))
        self.label.setText(_translate("Form", "Input Field"))
        self.pushButton.setText(_translate("Form", "Enter"))

    def add_logic(self, vec):
        self.vec = vec

        for i in range(10):
            self.vec.append(10 + i * 2)
            self.textEdit.append(str(self.vec[i]))

        self.textEdit.setReadOnly(True)

    def on_pushButton_clicked(self):
        action = self.comboBox.currentIndex()

        if action == 0:
            size = len(self.vec)
            self.lineEdit.setText(f'Vector size: {size}')
        elif action == 1:
            try:
                num = int(self.lineEdit.text())
                self.vec.append(num)
            except ValueError:
                QtWidgets.QMessageBox.critical(None, "Error", "Please enter a valid integer.")
        elif action == 2:
            try:
                pos = int(self.lineEdit.text())
                if 0 <= pos < len(self.vec):
                    del self.vec[pos]
                else:
                    QtWidgets.QMessageBox.critical(None, "Error", "Index out of range.")
            except ValueError:
                QtWidgets.QMessageBox.critical(None, "Error", "Please enter a valid integer.")

        self.textEdit.clear()
        for val in self.vec:
            self.textEdit.append(str(val))

    def on_comboBox_currentIndexChanged(self):
        index = self.comboBox.currentIndex()
        if index in [1, 2]:
            self.label.setText("Enter element value:")
            self.lineEdit.setReadOnly(False)
        else:
            self.label.setText("Input Field")
            self.lineEdit.setReadOnly(True)


class MainApplication:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.form)
        self.vec = []
        self.ui.add_logic(self.vec)

        self.ui.pushButton.clicked.connect(self.ui.on_pushButton_clicked)
        self.ui.comboBox.currentIndexChanged.connect(self.ui.on_comboBox_currentIndexChanged)

    def run(self):
        self.form.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    app = MainApplication()
    app.run()