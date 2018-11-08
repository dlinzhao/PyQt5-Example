"""
PyQt5 tutorial
This program creates a status bar.
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


# QMainWindow 类提供了一个主要的应用程序窗口。
# 你用它可以让应用程序添加状态栏,工具栏和菜单栏。
class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # 状态栏用于显示状态信息, 用QMainWindow创建状态栏的小窗口。
        # QMainWindow类第一次调用statusBar()方法创建一个状态栏。
        # 后续调用返回的状态栏对象。showMessage()
        # 状态栏上显示一条消息
        self.statusBar().showMessage('ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
