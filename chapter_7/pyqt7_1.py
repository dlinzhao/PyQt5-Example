"""
PyQt5 tutorial
In this example, we determine the event sender object.
"""

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt


# QCheckBox复选框控件，它有两个状态:打开和关闭，
# 他是一个带有文本标签（Label）的控件。
# 复选框常用于表示程序中可以启用或禁用的功能。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # 创建一个复选框, 将切换窗口标题。
        cb = QCheckBox('show title', self)
        cb.move(20, 20)
        # 有设置窗口标题,所以我们也必须检查复选框。
        # 默认情况下,没有设置窗口标题和也没有勾选复选框。
        cb.toggle()
        # 将自定义的changeTitle()方法连接到stateChanged信号
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Font dialog')
        self.show()

    def changeTitle(self, state):
        # 复选框的状态经由state参数传入changeTitle()方法。
        # 在勾选复选框时设置窗体标题，
        # 取消勾选时就将标题设为空字符串。
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
