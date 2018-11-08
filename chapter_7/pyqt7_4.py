"""
PyQt5 tutorial
This example shows a QProgressBar widget
"""

import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer


# 一个进度条是一个显示任务进展的控件。
# QProgressBar控件提供了一个水平或垂直PyQt5工具包的进度条。
# 程序员可以设置进度条的最小和最大值。默认值是0到99。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # 显示一个水平的进度条和一个按钮，
        # 用户通过点击按钮开始和停止进度条
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle dialog')
        self.show()

    # 每个QObject及其子类都有一个timerEvent()事件处理器。
    # 我们要重新实现这个事件处理器来响应定时器事件。
    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText("Finished")
            return
        self.step += 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText("start")
        else:
            # 使用定时器timer来激活QProgressBar
            # 调用start()方法启动一个计时器。
            # 这个方法有两个参数:超时和对象将接收的事件。
            self.timer.start(100, self)
            self.btn.setText("Stop")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
