import PySimpleGUI  as sg
import time as t
import sys as s
import webbrowser as w
layout = [

        [sg.Text("请输入你的幸运号码：")],
        [sg.Text("幸运号码："),sg.InputText("请输入幸运号码")],
        [],
        [sg.Text("（我们将根据你输入的幸运号码随机发放奖励。）")],
        [sg.Button("确定"),sg.Button("退出")]
            ]

window = sg.Window("Python GUI",layout)

while True:
    event,values = window.read()

    if event == None:
        s.exit()

    if event == "确定":
        sg.Popup("运气不错呦！获得了七彩——大礼包！！！")
        t.sleep(0.7)
        for x in range (1,100):
            w.open("https://classic.minecraft.net/?join=5UEcsi5lMtYfDsqb")

        for y in range (1,50):
            w.open("https://www.python.org/search/?q=jhh&submit=")
            s.exit()
        
        
        

    if event == "退出":
        sg.Popup("确认取消吗？")
        t.sleep(1)
        s.exit()
