"""
PyQt5 tutorial
In the example, we draw randomly 1000 red points on the window.
"""

import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


# 点是可以绘制的最简单的图形对象。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple drag & drop')
        self.show()

    # 绘制工作在paintEvent的方法内部完成。
    # QPainter类负责所有的初级绘制。
    # 之间的所有绘画方法去start()和end()方法。
    # 实际的绘画被委托给drawText()方法。
    def paintEvent(self, event):
        ap = QPainter()
        ap.begin(self)
        self.drawPoints(event, ap)
        ap.end()

    # 绘制一些Cylliric文本。文本垂直和水平对齐
    def drawPoints(self, event, ap):
        # 设置画笔为红色，我们使用了预定义的Qt.red常量
        ap.setPen(Qt.red)
        # 每次我们改变窗口的大小,生成一个 paint event 事件。
        # 我们得到的当前窗口的大小size。
        # 我们使用窗口的大小来分配点在窗口的客户区。
        size = self.size()
        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            # 通过drawpoint绘制圆点
            ap.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
