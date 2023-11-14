import random

from PyQt6 import QtCore, QtWidgets

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def count(self, value):
        count = 0
        current = self.head
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return count

    def reverse(self, start_idx, end_idx, callback=None):
        if start_idx < 0 or end_idx < 0 or start_idx >= end_idx:
            return

        current = self.head
        count = 0

        while count < start_idx:
            current = current.next
            count += 1

        start_node = current

        while count < end_idx:
            current = current.next
            count += 1

        end_node = current

        while start_node != end_node and end_node.next != start_node:
            start_node.data, end_node.data = end_node.data, start_node.data
            start_node = start_node.next
            end_node = end_node.prev

            if callback:
                callback()
                QtCore.QCoreApplication.processEvents()

    def iter_swap(self, first, last, callback=None):
        first.data, last.data = last.data, first.data

        if callback:
            callback()
            QtCore.QCoreApplication.processEvents()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(688, 509)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(21, 63, 251, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(21, 198, 251, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(21, 225, 251, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(21, 352, 251, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(21, 379, 251, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(71, 90, 161, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 260, 161, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 410, 161, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtWidgets.QTextEdit(parent=Form)
        self.textEdit.setGeometry(QtCore.QRect(301, 61, 341, 101))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=Form)
        self.textEdit_2.setGeometry(QtCore.QRect(301, 190, 346, 100))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=Form)
        self.textEdit_3.setGeometry(QtCore.QRect(301, 330, 348, 100))
        self.textEdit_3.setObjectName("textEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.linked_list = DoublyLinkedList()

        values = [random.randint(1, 100) for _ in range(10)]
        for value in values:
            self.linked_list.append(value)

        self.pushButton_3.clicked.connect(self.count_elements)
        self.pushButton_4.clicked.connect(self.reverse_elements)
        self.pushButton_5.clicked.connect(self.iter_swap_elements)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Task 3"))
        self.pushButton_3.setText(_translate("Form", "Count the occurrence"))
        self.pushButton_4.setText(_translate("Form", "Reverse a list"))
        self.pushButton_5.setText(_translate("Form", "Iter swap a list"))

    def count_elements(self):
        value_to_count = int(self.lineEdit.text())
        count = self.linked_list.count(value_to_count)
        self.textEdit.clear()
        self.textEdit.append(f"The value {value_to_count} appears {count} times in the linked list.")

    def reverse_elements(self):
        start_idx = int(self.lineEdit_2.text())
        end_idx = int(self.lineEdit_3.text())

        def callback():
            self.textEdit_2.clear()
            self.textEdit_2.append(f"Elements reversed in the specified range (indices {start_idx}-{end_idx}) in the linked list.")
            self.display_linked_list(self.textEdit_2)

        self.linked_list.reverse(start_idx, end_idx, callback)

    def iter_swap_elements(self):
        index_1 = int(self.lineEdit_4.text())
        index_2 = int(self.lineEdit_5.text())

        def callback():
            self.textEdit_3.clear()
            self.textEdit_3.append(f"Elements at indices {index_1} and {index_2} swapped in the linked list.")
            self.display_linked_list(self.textEdit_3)

        self.linked_list.iter_swap(self.linked_list.head, self.linked_list.tail, callback)

    def display_linked_list(self, output_field):
        current = self.linked_list.head
        elements = []

        while current:
            elements.append(current.data)
            current = current.next

        output_field.append("Resulting Linked List: " + ", ".join(map(str, elements)))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
