"""
PyQt5 tutorial
In this example we draw 6 lines using different pen styles.
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


# QPen是一个基本的图形对象。
# 用于绘制线条、曲线和轮廓的矩形、椭圆、多边形或其他形状。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Simple drag & drop')
        self.show()

    # 绘制工作在paintEvent的方法内部完成。
    # QPainter类负责所有的初级绘制。
    # 之间的所有绘画方法去start()和end()方法。
    # 实际的绘画被委托给drawText()方法。
    def paintEvent(self, event):
        ap = QPainter()
        ap.begin(self)
        self.drawLines(ap)
        ap.end()

    # 绘制一些Cylliric文本。文本垂直和水平对齐
    def drawLines(self, ap):
        # 我们创建一个QPen对象。颜色是黑色的。
        # 宽度设置为2像素,这样我们可以看到笔风格之间的差异。
        # Qt.SolidLine是预定义的钢笔样式。
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        # 线条勾勒出了六个不同的笔风格。
        # 有五个预定义的钢笔样式。
        # 我们也可以创建自定义的钢笔样式。
        # 最后一行使用一个定制的钢笔绘制风格。
        ap.setPen(pen)
        ap.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        ap.setPen(pen)
        ap.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotDotLine)
        ap.setPen(pen)
        ap.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        ap.setPen(pen)
        ap.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        ap.setPen(pen)
        ap.drawLine(20, 200, 250, 200)
        # 定义了一个画笔风格。
        # 我们设置了Qt.CustomDashLine并调用了setDashPattern()方法，
        # 它的参数(一个数字列表)定义了一种风格，
        # 必须有偶数个数字；其中奇数表示绘制实线，偶数表示留空。
        # 数值越大，直线或空白就越大。
        # 这里我们定义了1像素的实线，4像素的空白，5像素实线，4像素空白
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        ap.setPen(pen)
        ap.drawLine(20, 240, 250, 240)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
