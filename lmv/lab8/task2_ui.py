from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
import shutil

class FileSwapper:
    def __init__(self, ui):
        self.ui = ui
        self.setup_connections()

    def setup_connections(self):
        self.ui.pushButton.clicked.connect(self.select_first_file)
        self.ui.pushButton_2.clicked.connect(self.select_second_file)
        self.ui.pushButton_3.clicked.connect(self.swap_contents)

    def select_first_file(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Select first file", "", "Text Files (*.txt);;All Files (*)")
        self.ui.lineEdit.setText(file_path)

    def select_second_file(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Select second file", "", "Text Files (*.txt);;All Files (*)")
        self.ui.lineEdit_2.setText(file_path)

    def swap_contents(self):
        first_file_path = self.ui.lineEdit.text()
        second_file_path = self.ui.lineEdit_2.text()

        if first_file_path == "" or second_file_path == "":
            self.ui.lineEdit_3.setText("Please select both files.")
            return

        try:
            temp_file_path = "temp.txt"
            shutil.copy(first_file_path, temp_file_path)
            shutil.copy(second_file_path, first_file_path)
            shutil.copy(temp_file_path, second_file_path)
            self.ui.lineEdit_3.setText("Files swapped successfully.")

        except Exception as e:
            self.ui.lineEdit_3.setText(f"Error: {e}")

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 353)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 330, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 70, 200, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 160, 200, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 110, 330, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 200, 200, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 240, 330, 90))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Task 2"))
        self.pushButton.setText(_translate("Form", "Select first file"))
        self.pushButton_2.setText(_translate("Form", "Select second file"))
        self.pushButton_3.setText(_translate("Form", "Swap the contents"))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    file_swapper = FileSwapper(ui)  # Initialize the FileSwapper passing the Ui_Form instance
    app.exec()
