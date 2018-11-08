"""
PyQt5 tutorial
This example shows a QCalendarWidget widget.
"""

import sys
from PyQt5.QtWidgets import QWidget,QCalendarWidget, QLabel, QApplication
from PyQt5.QtCore import QDate


# QCalendarWidget提供了一个基于月份的日历控件。
# 它使用户以一种简单直观的方式来选择日期。
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # 创建了一个日历控件和一个标签控件。
        # 选择的日期会显示在标签控件中
        cal = QCalendarWidget(self)
        # 从部件选择一个日期,点击[QDate]发出信号。
        # 我们将这个信号连接到用户定义的showDate()方法。
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        data = cal.selectedDate()
        self.lbl.setText(data.toString())
        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Toggle dialog')
        self.show()

    # 检索所选日期通过调用selectedDate()方法。
    # 然后我们将date对象转换为字符串,并将其设置为小部件的标签。
    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
