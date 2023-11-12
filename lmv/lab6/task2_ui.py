from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Task 2")
        Form.resize(542, 345)
        self.matrix_input = QtWidgets.QTextEdit(parent=Form)
        self.matrix_input.setGeometry(QtCore.QRect(9, 9, 256, 192))
        self.matrix_input.setObjectName("textEdit")
        self.transform_button = QtWidgets.QPushButton(parent=Form)
        self.transform_button.setGeometry(QtCore.QRect(9, 220, 250, 50))
        self.transform_button.setObjectName("pushButton")
        self.result_label = QtWidgets.QLabel(parent=Form)
        self.result_label.setGeometry(QtCore.QRect(9, 280, 250, 60))
        self.result_label.setText("")
        self.result_label.setObjectName("label")

        self.transform_button.clicked.connect(self.transform)  # Connect button click to transform function

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Task 2"))
        self.matrix_input.setPlaceholderText(_translate("Form", "Enter the values in the following way : \n(\ne.g.\n1, 2, 3; \n4, 5, 6\n)"))
        self.transform_button.setText(_translate("Form", "Transform the matrix"))

    def transform(self):
        try:
            matrix_str = self.matrix_input.toPlainText()
            matrix = [[int(num) for num in row.split(',')] for row in matrix_str.split(';')]

            if len(matrix) < 1 or any(len(row) != len(matrix[0]) for row in matrix):
                self.result_label.setText("Invalid matrix format.")
                return

            transformed_matrix = self.transform_matrix(matrix)
            self.result_label.setText("Transformed Matrix:")
            for row in transformed_matrix:
                self.result_label.setText(self.result_label.text() + f"\n{', '.join(map(str, row))}")

        except Exception as e:
            self.result_label.setText(f"Error: {e}")

    def swap_min_max(self, row):
        min_val = min(row)
        max_val = max(row)
        min_idx = row.index(min_val)
        max_idx = row.index(max_val)
        row[min_idx], row[max_idx] = max_val, min_val
        return row

    def transform_matrix(self, matrix):
        transformed_matrix = []
        for row in matrix:
            transformed_row = self.swap_min_max(row)
            transformed_matrix.append(transformed_row)
        return transformed_matrix


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    task2_dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(task2_dialog)
    task2_dialog.show()
    sys.exit(app.exec())