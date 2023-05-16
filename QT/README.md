如果你使用的是PyQt5 而不是 PySide2，加载UI文件的代码如下

from PyQt5 import uic

class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi("main.ui")