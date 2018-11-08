"""
PyQt5 tutorial
This example shows how to use QSplitter widget.
"""

import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QSplitter,\
    QStyleFactory, QApplication
from PyQt5.QtCore import Qt


# 通过QSplitter，用户可以拖动子控件边界来调整子控件的尺寸。
# 在下面的示例中，我们展示了三个由两个QSplitter组织的QFrame控件。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        # 创建了三个QFrame与两个QSplitter。
        # 注意在某些主题中这些QSplitter可能会不可见。
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        # 使用一个风格框架为了看到QFrame小部件之间的界限。
        topritght = QFrame(self)
        topritght.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topritght)
        # 创建一个QSplitter小部件和添加两个帧。
        # 也可以将QSplitter添加到另一个QSplitter控件中。
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()

    # 将QLabel控件的文本设置为输入的内容。
    # 通过调用adjustSize()方法将QLabel控件的尺寸调整为文本的长度。
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
