"""
PyQt5 tutorial
In this example, we determine the event sender object.
"""

import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton,\
    QSizePolicy, QFontDialog, QLabel, QApplication


# QFontDialog对话框用以选择字体
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        # 创建了一个按钮和一个标签，通过QFontDialog来改变标签的字体
        self.btn = QPushButton('Dialog', self)
        self.btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn.move(20, 22)
        self.btn.clicked.connect(self.showDialog)

        vbox.addWidget(self.btn)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):
        # 弹出字体选择对话框，getFont()方法返回字体名称和ok参数，
        # 如果用户点击了ok他就是True,否则就是false
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
