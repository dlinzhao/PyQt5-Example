"""
PyQt5 tutorial
In this example, we determine the event sender object.
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame,\
    QColorDialog, QApplication
from PyQt5.QtGui import QColor


# QColorDialog显示一个用于选择颜色值的对话框
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # 初始化QFrame的颜色为黑色
        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 22)
        self.btn.clicked.connect(self.showDialog)
        # 程序显示一个按钮和一个QFrame。QFrame的背景为黑色。
        # 通过QColorDialog,我们可以改变它的背景。
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget {background-color: %s}" % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        # 弹出QColorDialog
        col = QColorDialog.getColor()
        # 检查col的值。如果点击的是Cancel按钮，返回的颜色值是无效的。
        # 当颜色值有效时，我们通过样式表(style sheet)来改变背景颜色。
        if col.isValid():
            self.frm.setStyleSheet("QWidget {background-color: %s}" % col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
