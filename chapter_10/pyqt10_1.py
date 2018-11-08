"""
PyQt5 tutorial
In this example, we draw text in Russian azbuka.
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


# 绘图要在paintEvent()方法中实现。
# 在QPainter对象的begin()与end()方法间编写绘图代码。
# 它会在控件或其他图形设备上进行低级的图形绘制。
# 先以窗体内Unicode文本的绘制为例。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
        \u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
        \u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

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
        self.drawText(event, ap)
        ap.end()

    # 绘制一些Cylliric文本。文本垂直和水平对齐
    def drawText(self, event, ap):
        # 定义一个画笔和一个字体用于绘制文本。
        ap.setPen(QColor(168, 34, 3))
        ap.setFont(QFont('Decorative', 10))
        # drawText()方法将文本绘制在窗体，显示在中心
        ap.drawText(event.rect(), Qt.AlignCenter, self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
