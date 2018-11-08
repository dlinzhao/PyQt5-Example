"""
PyQt5 tutorial
In this example, we create three toggle buttons.
They will control the background color of a QFrame.
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QApplication
from PyQt5.QtGui import QColor


# ToggleButton是QPushButton的一种特殊模式。
# 它是一个有两种状态的按钮：按下与未按下。
# 通过点击在这两种状态间来回切换。这种功能在某些场景会很实用。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # 创建了三个ToggleButton与一个QWidget。
        # 我们将QWidget的背景色设为黑色。
        # ToggleButton会切换颜色值中的红色、绿色与蓝色部分。
        # QWidget的背景颜色依赖于按下的按钮。
        self.col = QColor(0, 0, 0)
        # 创建一个QPushButton并通过其setCheckable()方法来得到一个ToggleButton。
        redb = QPushButton('red', self)
        redb.setCheckable(True)
        redb.move(10, 10)
        # 将clicked信号连接到用户自定义的方法。
        # 我们通过clicked信号操作一个布尔值。
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle dialog')
        self.show()

    def setColor(self, pressed):
        source = self.sender()
        if pressed:
            val = 255
        else:
            val = 0
        if source.text() == 'red':
            self.col.setRed(val)
        elif source.text() == 'blue':
            self.col.setBlue(val)
        else:
            self.col.setGreen(val)
        # 更新颜色中的红包部分。
        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
