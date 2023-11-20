import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog

class FileProcessor:
    def __init__(self, ui):
        self.input_filename = None
        self.output_filename = None

        self.ui = ui
        self.setup_connections()

    def setup_connections(self):
        self.ui.pushButton.clicked.connect(self.get_input_file)
        self.ui.pushButton_2.clicked.connect(self.get_output_file)
        self.ui.pushButton_3.clicked.connect(self.process_files)

    def get_input_file(self):
        self.input_filename, _ = QFileDialog.getOpenFileName(None, 'Select Input File')
        if self.input_filename:
            self.ui.label.setText(f'Input File: {self.input_filename}')

    def get_output_file(self):
        self.output_filename, _ = QFileDialog.getSaveFileName(None, 'Select Output File')
        if self.output_filename:
            self.ui.label.setText(f'Output File: {self.output_filename}')

    def process_files(self):
        if not self.input_filename or not self.output_filename:
            return

        try:
            with open(self.input_filename, 'r') as file:
                numbers = [int(line) for line in file.readlines()]
                chunk_size = 5
                with open(self.output_filename, 'w') as output_file:
                    while numbers:
                        chunk = sorted(numbers[:chunk_size], reverse=True)
                        for num in chunk:
                            output_file.write(str(num) + '\n')
                        numbers = numbers[chunk_size:]
        except FileNotFoundError:
            self.ui.label.setText('File not found. Please select valid files.')
            return

        self.ui.label.setText('Files processed successfully.')

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(463, 300)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(20, 70, 361, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 150, 360, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 190, 360, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 230, 360, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Task 1"))
        self.label.setText(_translate("Form", "Choose input and output files: "))
        self.pushButton.setText(_translate("Form", "Select Input File"))
        self.pushButton_2.setText(_translate("Form", "Select Output File"))
        self.pushButton_3.setText(_translate("Form", "Process Files"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    processor = FileProcessor(ui)
    sys.exit(app.exec())
