"""
PyQt5 tutorial
In this example, we determine the event sender object.
"""

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


# 创建了一个名为closeApp的信号。
class Communicate(QObject):
    closeApp = pyqtSignal()


# QMainWindow 类提供了一个主要的应用程序窗口。
# 你用它可以让应用程序添加状态栏,工具栏和菜单栏。
class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        # 连接着QMainWindow的close()插槽。
        # 信号closeApp是Communicate的类属性，它由pyqtSignal()创建。
        self.c.closeApp.connect(self.close)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    # 这个信号会在按下鼠标时触发
    def mousePressEvent(self, event):
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
