"""
PyQt5 tutorial
This is a simple game.
"""

import sys
import random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor

# 游戏的一些思想:
# 我们使用QtCore.QBasicTimer()来创建一个游戏循环。
# 俄罗斯方块是绘制的。
# 图形是一个方块一个方块移动的（不是像素）
# 图形其实是一个简单的数字列表。
# 代码包括四类:Tetris, Board, Tetrominoe 和Shape。

# 在比赛开始后立即启动。我们可以通过按p键暂停游戏。
# 空格键将立即把俄罗斯方块块底部。游戏是在恒定速度,实现没有加速度。
# 分数是我们已经删除的行数。


# Tetris 类用来存放游戏。
class Tetris(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        # Board创建一个面板类的实例，并设置应用程序的核心部件。
        self.tboard = Board()
        self.setCentralWidget(self.tboard)
        # 创建一个状态栏将显示消息。
        # 我们将显示三种可能的消息:已删除的行数,停顿了一下消息,或游戏结束的消息。
        # msg2Statusbar是一个自定义的信号,在Board 中实现类。
        # showMessage()是一个内置的方法,在状态栏显示一条消息。
        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        # 启动游戏
        self.tboard.start()

        self.resize(180, 300)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2,
                  (screen.height() - size.height()) // 2)


# Board是编写游戏逻辑的地方。
class Board(QFrame):
    # 创建一个自定义的信号。当我们想写一个信息或状态栏的分数的时候，msg2Statusbar发出一个信号
    msg2Statusbar = pyqtSignal(str)
    # Board的类变量。BoardWidth和BoardHeight定义的块的大小。
    # Speed定义了游戏的速度。每个300 ms将开始一个新游戏循环。
    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self):
        super(Board, self).__init__()
        self.initBoard()

    # 在initBoard()方法初始化一些重要的变量。
    # board变量是一个从0到7的数字列表。
    # 它代表了面板上各种形状和位置。
    def initBoard(self):
        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()

    # shapeAt()方法确定在给定形状块的类型
    def shapeAt(self, x, y):
        return self.board[(y * Board.BoardWidth) + x]

    def setShapeAt(self, x, y, shape):
        self.board[(y * Board.BoardWidth) + x] = shape

    # Board可以动态地调整大小。因此,块的大小可能会有所改变。
    # squareWidth()计算单一方块像素的宽度并返回它。
    # Board.BoardWidth方块板的大小。
    def squareWidth(self):
        return self.contentsRect().width() // Board.BoardWidth

    def squareHeight(self):
        return self.contentsRect().height() // Board.BoardHeight

    def start(self):
        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.newPiece()
        self.timer.start(Board.Speed, self)

    def pause(self):
        if not self.isStarted:
            return

        self.isPaused = not self.isPaused

        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("paused")
        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.contentsRect()

        boarTop = rect.bottom() - Board.BoardHeight * self.squareHeight()
        # 游戏的绘制分为两个步骤，
        # 第一步，绘制所有方块，
        # 这些方块都要保存在底部列表中。
        # 列表通过shapeAt() 方法来添加方块。
        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)
                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,
                                    rect.left() + j * self.squareWidth(),
                                    boarTop + i * self.squareHeight(), shape)
        # 第二步绘制下降中的方块
        if self.curPiece.shape() != Tetrominoe.NoShape:
            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter,
                                rect.left() + x * self.squareWidth(),
                                boarTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                                self.curPiece.shape())

    def keyPressEvent(self, event):
        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return
        key = event.key()

        if key == Qt.Key_P:
            self.pause()
            return
        # keyPressEvent()方法检查按下键。
        # 当按右箭头键,我们试图向右移动一块。
        # 我们使用tyrMove,因为可能无法移动。
        if self.isPaused:
            return
        elif key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)
        elif key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)
        elif key == Qt.Key_Down:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
        elif key == Qt.Key_Up:
            # 向上箭头键将旋转方块。
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
        elif key == Qt.Key_Space:
            # 空格键立即下降到底部
            self.dropDown()
        elif key == Qt.Key_D:
            # 按下D键，可以加速下降。
            self.oneLineDown()
        else:
            super(Board, self).keyPressEvent(event)

    # 计时器事件,当我们前一个方块降到底部后，创建一个新的方块。
    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()
        else:
            super(Board, self).timerEvent(event)

    # clearBoard()方法通过设置Tetrominoe.NoShape清除面板
    def clearBoard(self):
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)

    def dropDown(self):
        newY = self.curY
        while newY > 0:
            if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
                break

            newY -= 1

        self.pieceDropped()

    def oneLineDown(self):
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()

    def pieceDropped(self):
        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()

    # 如果到达底部,会调用removeFullLines()方法。
    # 我们会检查所有完整的线条然后删除它们。
    # 然后移动所有行高于当前删除整行一行。
    # 请注意,我们反的顺序行被删除。否则,就会出错。
    def removeFullLines(self):
        numFullLines = 0
        rowsToRemove = []

        for i in range(Board.BoardHeight):
            n = 0
            for j in range(Board.BoardWidth):
                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1

            if n == 10:
                rowsToRemove.append(i)

        rowsToRemove.reverse()

        for m in rowsToRemove:
            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                    self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:
            self.numLinesRemoved = self.numLinesRemoved + numFullLines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.update()

    # 通过newPiece()方法创建一个新的方块，如果不能进入它的初始位置,游戏就结束了。
    def newPiece(self):
        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

        if not self.tryMove(self.curPiece, self.curX, self.curY):
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")

    # 使用tryMove()方法尝试移动方块。
    # 如果方块的边缘已经接触到面板边缘或者不能移动,我们返回False。
    # 否则我们当前块下降到一个新的位置
    def tryMove(self, newPiece, newX, newY):
        for i in range(4):
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False

            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()

        return True

    def drawSquare(self, painter, x, y, shape):
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                         self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
                         x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
                         y + self.squareHeight() - 1, x + self.squareWidth() - 1, y +1)


# Tetrominoe类包含所有俄罗斯方块的名称，
class Tetrominoe(object):
    # NoShape空形状。
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7


# Shape类包含一个俄罗斯方块的代码。
class Shape(object):
    # coordsTable 元组包含所有可能的俄罗斯方块的坐标值。
    # 这是一个模板的所有块坐标值。
    coordsTable = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1))
    )

    def __init__(self):
        # 创建一个空的列表保存俄罗斯方块的坐标
        self.coords = [[0, 0] for i in range(4)]
        self.pieceShape = Tetrominoe.NoShape
        self.setShape(Tetrominoe.NoShape)

    def shape(self):
        return self.pieceShape

    def setShape(self, shape):
        table = Shape.coordsTable[shape]

        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.pieceShape = shape

    def setRandomShape(self):
        self.setShape(random.randint(1, 7))

    def x(self, index):
        return self.coords[index][0]

    def y(self, index):
        return self.coords[index][1]

    def setX(self, index, x):
        self.coords[index][0] = x

    def setY(self, index, y):
        self.coords[index][1] = y

    def minX(self):
        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m

    def maxX(self):
        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m

    def minY(self):
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m

    def maxY(self):
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m

    # rotateLeft() 向左旋转方块。
    # 如果方块本身不能被旋转，我们就返回当前对象的应用。
    # 否则就创建一个新的块及其坐标设置为的旋转。
    def rotateLeft(self):
        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result

    def rotateRight(self):
        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result


if __name__ == '__main__':
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())
