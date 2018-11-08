# PyQt5中文教程

### 【第一节】 PyQt5简介
    本教程适合初学者和中级程序员。
    看完这个教程，你将能够开发一些简单的pyqt5界面应用程序。
    - QtCore:包含了核心的非GUI功能。此模块用于处理时间、文件和目录、各种数据类型、流、URL、MIME类型、线程或进程。
    - QtGui包含类窗口系统集成、事件处理、二维图形、基本成像、字体和文本。
    - qtwidgets模块包含创造经典桌面风格的用户界面提供了一套UI元素的类。
    - QtMultimedia包含的类来处理多媒体内容和API来访问相机和收音机的功能。
    - Qtbluetooth模块包含类的扫描设备和连接并与他们互动。描述模块包含了网络编程的类。这些类便于TCP和IP和UDP客户端和服务器的编码，使网络编程更容易和更便携。
    - Qtpositioning包含类的利用各种可能的来源，确定位置，包括卫星、Wi-Fi、或一个文本文件。
    - Enginio模块实现了客户端库访问Qt云服务托管的应用程序运行时。
    - Qtwebsockets模块包含实现WebSocket协议类。
    - QtWebKit包含一个基于Webkit2图书馆Web浏览器实现类。
    - Qtwebkitwidgets包含的类的基础webkit1一用于qtwidgets应用Web浏览器的实现。
    - QtXml包含与XML文件的类。这个模块为SAX和DOM API提供了实现。
    - QtSvg模块提供了显示SVG文件内容的类。可伸缩矢量图形（SVG）是一种描述二维图形和图形应用的语言。
    - QtSql模块提供操作数据库的类。
    - QtTest包含的功能，使pyqt5应用程序的单元测试

### 【第二节】PyQt5基本功能
    1. 简单的例子
    2. 应用程序的图标
    3. 显示提示语
    4. 关闭窗口
    5. 消息框
    6. 窗口显示在屏幕的中间

### 【第三节】PyQt5布局管理
    1. 绝对定位
    2. 框布局 Boxlayout
    3. 表格布局 QGridLayout
    4. 表格布局中跨越多个行或列

### 【第四节】PyQt5菜单和工具栏
    1. 主窗口
    2. 状态栏
    3. 菜单栏
    4. 工具栏
    5. 综合

### 【第五节】PyQt5事件和信号
    1. 事件 Event
        所有的GUI程序都是事件驱动的。事件主要由用户触发，但也可能有其他触发方式：例如网络连接、window manager或定时器。
        当我们调用QApplication的exec_()方法时会使程序进入主循环。主循环会获取并分发事件。在事件模型中，有三个参与者：
            + 事件源
            + 事件对象
            + 事件接收者
        事件源是状态发生变化的对象。它会生成事件。事件(对象)封装了事件源中状态的变动。事件接收者是要通知的对象。事件源
        对象将事件处理的工作交给事件接收者。
        PyQt5有一个独特的signal&slot(信号槽)机制来处理事件。信号槽用于对象间的通信。signal在某一特定事件发生时被触发，
        slot可以是任何callable对象。当signal触发时会调用与之相连的slot。
    2. 信号槽 Signals & slots
    3. 重新实现事件处理器
    4. 事件发送者
    5. 发出信号

### 【第六节】PyQt5对话框
    1. QInputDialog
    2. QColorDialog
    3. QFontDialog
    4. QFileDialog

### 【第七节】PyQt5控件
    1. QCheckBox
    2. 开关按钮 Toggle button
    3. 滑动条 QSlider
    4. 进度条QProgressBar
    5. 日历控件 QCalendarWidget

### 【第八节】PyQt5控件(II)
    1. QPixmap
    2. 文本框 QLineEdit
    3. QSplitter
    4. 下拉列表 QComboBox

### 【第九节】PyQt5拖拽
    在计算机图形用户界面中,拖放的操作(或支持的作用)点击虚拟对象和拖动到另一个位置
    或到另一个虚拟对象。一般来说,它可以用于调用多种行动,或创建各种类型的两个抽象对
    象之间的关联。拖放是图形用户界面的一部分。拖拽操作让用户直观地做复杂的事情。通
    常,我们可以拖放两件事:数据或一些图形对象。如果我们把一个图像从一个应用程序到另
    一个地方,我们拖拽二进制数据。如果我们把一个标签在Firefox中并将其移动到另一个地
    方,我们拖拽一个图形组件。
    
    1. 简单拖放
    2. 拖放一个按钮

### 【第十节】PyQt5绘图
    1. 绘制文本
    2. 画点
    3. 颜色
    4. QPen(画笔)
    5. QBrush(笔刷)

### 【第十一节】PyQt5自定义控件
    PyQt5包含种类丰富的控件。但能满足所有需求的控件库是不存在的。
    通常控件库只提供了像按钮、文本控件、滑块等最常用的控件。但如
    果需要某种特殊的控件，我们只能自己动手来实现。 自定义控件需要
    使用工具库提供的绘图工具，可能有两种方式：在已有的控件上进行
    拓展或从头开始创建自定义控件。
    1 Burning widget(烧录控件)

### 【第十二节】PyQt5俄罗斯方块
    俄罗斯方块称为积木拼图游戏。
    在这个游戏中,我们有七种不同形状叫tetrominoes:
        s形
        Z-shape
        t形
        一个l型的空间
        一个线,
        MirroredL-shape
        正方形。
    这些形状的形成有四个方格, 形状是跌倒。
    俄罗斯方块游戏的对象是移动和旋转的形状使他们适合尽可能多。
    如果我们设法形成一个行,该行摧毁我们得分。我们直到我们玩俄罗斯方块游戏。
    1 俄罗斯方块

### 【第十三节】QtDesigner使用
    1. 创建.ui文件
    2. 在.ui文件上右键转换为python文件
    3. 使用下面代码进行调用
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        # widget 类型由UI文件中setupUi()函数参数决定
        widget = QtWidgets.QWidget()
        # UI文件生成的类名
        ui = Ui_form()
        ui.setupUi(widget)
        widget.show()
        sys.exit(app.exec_())