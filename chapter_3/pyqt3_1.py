"""
PyQt5 tutorial
This example shows three labels on a window using absolute positioning.
"""
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Examle(QWidget):
    def __init__(self):
        super(Examle, self).__init__()
        self.initUI()

    def initUI(self):
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('absolute')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Examle()
    sys.exit(app.exec_())
