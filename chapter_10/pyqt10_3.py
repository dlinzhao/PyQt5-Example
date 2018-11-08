"""
PyQt5 tutorial
This example draws three rectangles in three #different colours.
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush


# 颜色是一个对象代表红、绿、蓝(RGB)强度值。
# 有效的RGB值的范围从0到255。
# 我们可以用不同的方法定义了一个颜色。
# 最常见的是RGB十进制或十六进制值的值。
# 我们也可以使用一个RGBA值代表红色,绿色,蓝色,透明度。
# 我们添加一些额外的信息透明度。
# 透明度值255定义了完全不透明,0是完全透明的,例如颜色是无形的。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Simple drag & drop')
        self.show()

    # 绘制工作在paintEvent的方法内部完成。
    # QPainter类负责所有的初级绘制。
    # 之间的所有绘画方法去start()和end()方法。
    # 实际的绘画被委托给drawText()方法。
    def paintEvent(self, event):
        ap = QPainter()
        ap.begin(self)
        self.drawRectangles(ap)
        ap.end()

    # 绘制一些Cylliric文本。文本垂直和水平对齐
    def drawRectangles(self, ap):
        # 实例中我们绘制了3个不同颜色的矩形
        col = QColor(0, 0, 0)
        # 在这里,我们定义一个使用十六进制符号颜色。
        col.setNamedColor('#d4d4d4')
        ap.setPen(col)
        # 我们为QPainter设置了一个笔刷(Bursh)对象并用它绘制了一个矩形。
        # 笔刷是用于绘制形状背景的基本图形对象。
        # drawRect()方法接受四个参数，前两个是起点的x,y坐标，
        # 后两个是矩形的宽和高。这个方法使用当前的画笔与笔刷对象进行绘制。
        ap.setBrush(QColor(200, 0, 0))
        ap.drawRect(10, 15, 90, 60)

        ap.setBrush(QColor(255, 80, 0, 160))
        ap.drawRect(130, 15, 90, 60)

        ap.setBrush(QColor(25, 0, 90, 200))
        ap.drawRect(250, 15, 90, 60)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
