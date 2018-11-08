"""
PyQt5 tutorial
This example draws 9 rectangles in different brush styles.
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt


# QBrush是一个基本的图形对象。
# 它用于油漆的背景图形形状,如矩形、椭圆形或多边形。
# 三种不同类型的刷可以:一个预定义的刷,一个梯度,或纹理模式。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Simple drag & drop')
        self.show()

    # 绘制工作在paintEvent的方法内部完成。
    # QPainter类负责所有的初级绘制。
    # 之间的所有绘画方法去start()和end()方法。
    # 实际的绘画被委托给drawText()方法。
    def paintEvent(self, event):
        ap = QPainter()
        ap.begin(self)
        self.drawBrushes(ap)
        ap.end()

    # 绘制一些Cylliric文本。文本垂直和水平对齐
    def drawBrushes(self, ap):
        # 绘制九个不同的矩形
        # 定义了一个笔刷对象，然后将它设置给QPainter对象，
        # 并调用painter的drawRect()方法绘制矩形。
        brush = QBrush(Qt.SolidPattern)
        ap.setBrush(brush)
        ap.drawRect(10, 15, 90, 60)

        brush.setStyle(Qt.Dense1Pattern)
        ap.setBrush(brush)
        ap.drawRect(130, 15, 90, 60)

        brush.setStyle(Qt.Dense2Pattern)
        ap.setBrush(brush)
        ap.drawRect(250, 15, 90, 60)

        brush.setStyle(Qt.DiagCrossPattern)
        ap.setBrush(brush)
        ap.drawRect(10, 105, 90, 60)

        brush.setStyle(Qt.Dense5Pattern)
        ap.setBrush(brush)
        ap.drawRect(130, 105, 90, 60)

        brush.setStyle(Qt.Dense6Pattern)
        ap.setBrush(brush)
        ap.drawRect(250, 105, 90, 60)

        brush.setStyle(Qt.HorPattern)
        ap.setBrush(brush)
        ap.drawRect(10, 195, 90, 60)

        brush.setStyle(Qt.VerPattern)
        ap.setBrush(brush)
        ap.drawRect(130, 195, 90, 60)

        brush.setStyle(Qt.BDiagPattern)
        ap.setBrush(brush)
        ap.drawRect(250, 195, 90, 60)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
