"""
PyQt5 tutorial
This example shows a QSlider widget.
"""

import sys
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


# QSlider是一个带有简单滑块的控件。滑块可以前后拖动。
# 我们可以通过拖动选择一个特定的值。有时使用滑动条比
# 直接输入数字或使用旋转框更加自然。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.lable = QLabel(self)
        self.lable.setPixmap(QPixmap("../ICON/add.png"))
        self.lable.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle dialog')
        self.show()

    # 根据滑动条的值来设置标签的图像。
    def changeValue(self, value):
        if value == 0:
            self.lable.setPixmap(QPixmap("../ICON/back.png"))
        elif 0 < value <= 30:
            self.lable.setPixmap(QPixmap("../ICON/bottom.png"))
        elif 30 < value < 80:
            self.lable.setPixmap(QPixmap("../ICON/call-start.png"))
        else:
            self.lable.setPixmap(QPixmap("../ICON/call-stop.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
