from win32com import client
# pip install pypiwin32
# pywin32模块 快速调用windows API的一个模块库
import time
"""
声音模块
"""
class Voice():
    def __init__(self):
        #初始定义声音引擎
        #创建一个应用
        self.engine = client.Dispatch("sapi.spvoice")
        # self.engine.Visible=True
    def speak(self,str):
        self.engine.Speak(str)


if __name__ == '__main__':
    voice = Voice()
    test="前面有两个垃圾桶，四辆车"
    voice.speak(test)