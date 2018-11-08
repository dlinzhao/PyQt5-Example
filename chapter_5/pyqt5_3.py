"""
PyQt5 tutorial
In this example, we determine the event sender object.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


# QMainWindow 类提供了一个主要的应用程序窗口。
# 你用它可以让应用程序添加状态栏,工具栏和菜单栏。
class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('bnt1', self)
        btn1.move(30, 50)

        btn2 = QPushButton('bnt2', self)
        btn2.move(150, 50)
        # 创建了两个按钮。在buttonClicked()方法中通过调用sender()方法
        # 来判断当前按下的是哪个按钮。
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    # 两个按钮连接到了同一个插槽。
    def buttonClicked(self):
        # 通过调用sender()方法来判断信号源
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
