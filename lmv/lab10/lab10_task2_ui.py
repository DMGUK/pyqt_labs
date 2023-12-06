from PyQt6 import QtCore, QtGui, QtWidgets
from collections import deque
import random

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 388)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(51, 330, 231, 51))
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 14, 600, 301))
        self.lineEdit.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 330, 231, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.generate_queue)
        self.pushButton_2.clicked.connect(self.manipulate_queue)

        self.queue = None

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Task 2"))
        self.pushButton.setText(_translate("Form", "Generate Queue"))
        self.pushButton_2.setText(_translate("Form", "Manipulate Queue"))

    def generate_queue(self):
        queue = deque(random.sample(range(1, 100), 10))
        self.lineEdit.clear()
        self.lineEdit.setText(f"Original Queue: {list(queue)}")
        self.queue = queue

    def manipulate_queue(self):
        if self.queue:
            max_element = max(self.queue)
            self.queue = deque([num + max_element for num in self.queue])
            self.lineEdit.clear()
            self.lineEdit.setText(f"Manipulated Queue: {list(self.queue)}")
        else:
            self.lineEdit.clear()
            self.lineEdit.append("Please generate the queue first.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
