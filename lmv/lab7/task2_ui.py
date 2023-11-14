import random
import sys
from collections.abc import Iterable

from PyQt6 import QtCore, QtWidgets

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList(Iterable):
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def sort_descending(self):
        if not self.head or not self.head.next:
            return

        def merge_sort(node):
            if not node or not node.next:
                return node

            middle = get_middle(node)
            next_to_middle = middle.next
            middle.next = None

            left = merge_sort(node)
            right = merge_sort(next_to_middle)

            return merge(left, right)

        def merge(left, right):
            result = None

            if not left:
                return right
            if not right:
                return left

            if left.data >= right.data:
                result = left
                result.next = merge(left.next, right)
            else:
                result = right
                result.next = merge(left, right.next)

            return result

        def get_middle(node):
            if not node:
                return node

            slow = node
            fast = node

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        self.head = merge_sort(self.head)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(713, 571)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(21, 61, 171, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(21, 90, 132, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 130, 151, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sort_linked_list)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(21, 200, 301, 321))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(350, 200, 331, 321))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Task 2"))
        self.label.setText(_translate("Form", "Enter the number of nodes: "))
        self.pushButton.setText(_translate("Form", "Sort the List"))


    def sort_linked_list(self):
        try:
            num_nodes = int(self.lineEdit.text())

            linked_list = LinkedList()
            for _ in range(num_nodes):
                linked_list.append(random.randint(1, 100))

            original_list = "Original List:\n" + ', '.join(
                str(node) + ('\n' if i % 10 == 9 else '') for i, node in enumerate(linked_list))
            linked_list.sort_descending()
            sorted_list = "Sorted List (descending):\n" + ', '.join(
                str(node) + ('\n' if i % 10 == 9 else '') for i, node in enumerate(linked_list))

            self.label_2.setText(original_list)
            self.label_3.setText(sorted_list)

        except ValueError:
            self.label_2.setText("Please enter a valid integer for the number of nodes")
            self.label_3.setText("Please enter a valid integer for the number of nodes")


app = QtWidgets.QApplication(sys.argv)
task2 = QtWidgets.QDialog()
ui = Ui_Form()
ui.setupUi(task2)
task2.show()
sys.exit(app.exec())

