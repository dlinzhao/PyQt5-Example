"""
PyQt5 tutorial
This example shows how to use a QComboBox widget.
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox,QApplication


# QComboBox是允许用户从下拉列表中进行选择的控件。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel("Ubuntu", self)
        # 展示了一个QComboBox与一个QLabel，
        # QComboBox控件中有5个选项(Linux系统的几个发行版名称)。
        # QLabel控件会显示QComboBox中选中的某个选项。
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.lbl.move(50, 150)
        # 当选中某个条目时会调用onActivated()方法。
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()

    # 将QLabel控件的文本设置为输入的内容。
    # 通过调用adjustSize()方法将QLabel控件的尺寸调整为文本的长度。
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
