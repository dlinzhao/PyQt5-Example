"""
PyQt5 tutorial
In this example, we dispay an image on the window.
"""

import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication
from PyQt5.QtGui import QPixmap


# QPixmap是用于处理图像的控件。是优化的显示图像在屏幕上。
# 在我们的代码示例中,我们将使用QPixmap窗口显示一个图像。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("../ICON/spyder.ico")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 300)
        self.setWindowTitle('Toggle dialog')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
