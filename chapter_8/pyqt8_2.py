"""
PyQt5 tutorial
This example shows text which is entered in a QLineEdit in a QLabel widget.
"""

import sys
from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QApplication


# QLineEdit是用于输入或编辑单行文本的控件。
# 它还有撤销重做、剪切复制和拖拽功能。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # 示例中展示了一个QLineEdit与一个QLabel。
        # 我们在QLineEdit中输入的文字会实时显示在QLabel控件中。
        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)
        # 文本框的内容发生改变的时候，会调用onChanged方法
        qle.textChanged[str].connect(self.onChanged)

        self.move(300, 300)
        self.setWindowTitle('Toggle dialog')
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
