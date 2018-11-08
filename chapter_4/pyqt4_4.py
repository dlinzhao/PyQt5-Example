"""
PyQt5 tutorial
This program creates a skeleton of
a classic GUI application with a menubar,
toolbar, statusbar, and a central widget.
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QTextEdit, QApplication
from PyQt5.QtGui import QIcon


# QMainWindow 类提供了一个主要的应用程序窗口。
# 你用它可以让应用程序添加状态栏,工具栏和菜单栏。
class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # 创建了一个QTextEdit,并把他设置为窗口的布局
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('../ICON/exit.png'), '&Exit', self)
        # 快捷方式
        exitAction.setShortcut('Ctrl+Q')
        # 鼠标指针悬停在该菜单项上时的提示。
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()
        # 创建一个菜单栏
        menubar = self.menuBar()
        # 添加菜单
        fileMenu = menubar.addMenu('&File')
        # 添加事件
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
