"""
PyQt5 tutorial
This is a simple drag and drop example.
"""

import sys
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QApplication


# 在第一个示例中,我们有一个QLineEdit QPushButton。
# 我们拖着纯文本的行编辑窗口小部件,然后放到按钮部件。按钮的标签会改变。
class Button(QPushButton):
    # 重新实现某些方法才能使QPushButton接受拖放操作。
    # 因此我们创建了继承自QPushButton的Button类。
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)
        self.setAcceptDrops(True)

    # 使该控件接受drop(放下)事件。
    # 重新实现了dragEnterEvent()方法，
    # 并设置可接受的数据类型(在这里是普通文本)。
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    # 重新实现dropEvent()方法，
    # 我们定义了在drop事件发生时的行为。
    # 这里我们改变了按钮的文字。
    def dropEvent(self, event):
        self.setText(event.mimeData().text())


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # QLineEdit内置了对drag(拖动)操作的支持。
        # 我们只需要调用setDragEnabled()方法就可以了。
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button('Button', self)
        button.move(190, 65)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple drag & drop')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
