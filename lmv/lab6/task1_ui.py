from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Task 1")
        Form.resize(521, 349)
        self.matrix_input = QtWidgets.QPlainTextEdit(parent=Form)
        self.matrix_input.setGeometry(QtCore.QRect(21, 21, 261, 151))
        self.matrix_input.setObjectName("plainTextEdit")
        self.action_selection = QtWidgets.QComboBox(parent=Form)
        self.action_selection.setGeometry(QtCore.QRect(20, 190, 261, 31))
        self.action_selection.setObjectName("comboBox")
        self.action_selection.addItem("")
        self.action_selection.addItem("")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 240, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.result_label = QtWidgets.QLabel(parent=Form)
        self.result_label.setGeometry(QtCore.QRect(20, 300, 251, 31))
        self.result_label.setText("")
        self.result_label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.calculate)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Task 1"))
        self.matrix_input.setPlaceholderText(_translate("Form", "Enter the values in the following way : \n(\ne.g.\n1, 2, 3; \n4, 5, 6\n)"))
        self.action_selection.setItemText(0, _translate("Form", "Find the sum of even columns in the matrix"))
        self.action_selection.setItemText(1, _translate("Form", "Find the sum of odd columns in the matrix"))
        self.pushButton.setText(_translate("Form", "Calculate the result"))

    def calculate(self):
        try:
            matrix_str = self.matrix_input.toPlainText()
            matrix = [[int(num) for num in row.split(',')] for row in matrix_str.split(';')]

            if len(matrix) < 1 or any(len(row) != len(matrix[0]) for row in matrix):
                self.result_label.setText("Invalid matrix format.")
                return

            if self.action_selection.currentIndex() == 0:
                even_sum = self.calculate_even_columns(matrix)
                self.result_label.setText(f"Sum of even columns: {even_sum}")
            elif self.action_selection.currentIndex() == 1:
                odd_sum = self.calculate_odd_columns(matrix)
                self.result_label.setText(f"Sum of odd columns: {odd_sum}")

        except Exception as e:
            self.result_label.setText(f"Error: {e}")

    def calculate_even_columns(self, matrix):
        even_column_sum = 0
        for j in range(len(matrix[0])):
            if j % 2 == 0:
                for i in range(len(matrix)):
                    even_column_sum += matrix[i][j]
        return even_column_sum

    def calculate_odd_columns(self, matrix):
        odd_column_sum = 0
        for j in range(len(matrix[0])):
            if j % 2 != 0:
                for i in range(len(matrix)):
                    odd_column_sum += matrix[i][j]
        return odd_column_sum


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    task1_dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(task1_dialog)
    task1_dialog.show()
    sys.exit(app.exec())
