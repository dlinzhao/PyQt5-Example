import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# 从当前文件夹导入
from Qt_Designer.login import Ui_MainWindow


class LoginRun(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LoginRun, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = LoginRun()
    widget.show()
    sys.exit(app.exec_())
