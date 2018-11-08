"""
PyQt5 tutorial
In this example, we connect a signal
of a QSlider to a slot of a QLCDNumber.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, \
    QSlider, QVBoxLayout, QApplication


# QMainWindow 类提供了一个主要的应用程序窗口。
# 你用它可以让应用程序添加状态栏,工具栏和菜单栏。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        # 将滚动条的valueChanged信号连接到lcd的display插槽。
        # sender是发出信号的对象。
        # receiver是接收信号的对象。
        # slot(插槽)是对信号做出反应的方法。
        # lcd的值会随着滑块的拖动而改变。
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
