from win32com import client
# str="前面有两个垃圾桶，四辆车"
# engine = client.Dispatch("sapi.spvoice")
# engine.Speak(str)
str="前面有两个垃圾桶，四辆车"
engine = client.Dispatch("sapi.spvoice").Speak(str)
