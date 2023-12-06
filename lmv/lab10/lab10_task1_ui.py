from PyQt6 import QtCore, QtGui, QtWidgets
from collections import deque
import random

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(555, 392)
        self.text_edit = QtWidgets.QTextEdit(parent=Form)
        self.text_edit.setGeometry(QtCore.QRect(10, 10, 531, 301))
        self.text_edit.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_edit.setFont(font)
        self.text_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(21, 326, 231, 51))
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 326, 231, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.generate_stack)
        self.pushButton_2.clicked.connect(self.replace_values)

        self.stack = None

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Task 1"))
        self.pushButton.setText(_translate("Form", "Generate Stack"))
        self.pushButton_2.setText(_translate("Form", "Replace Values"))

    def generate_stack(self):
        stack = deque(random.sample(range(-100, 100), 10))
        self.text_edit.append(f"Original Stack: {list(stack)}")
        self.stack = stack

    def replace_values(self):
        if self.stack:
            modified_stack = deque([1 if num > 0 else -1 for num in self.stack])
            self.text_edit.append(f"Modified Stack: {list(modified_stack)}")
        else:
            self.text_edit.setText("Please generate the stack first.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
