import PySimpleGUI  as sg
import time as t
layout = [

        [sg.Text("请输入您的身份信息以实名认证：")],
        [sg.Text("姓名："),sg.InputText("请输入姓名")],
        [sg.Text("身份证号:"),sg.InputText("请输入身份证号")],
        [sg.Text("（！实名认证一经认证不得修改，请谨慎填写信息！）")],
        [sg.Button("确定"),sg.Button("退出")]
            ]

window = sg.Window("Python GUI",layout)

while True:
    event,values = window.read()

    if event == None:
        break

    if event == "确定":
        sg.Popup("恭喜你，认证通过！")
        t.sleep(1)
        break

    if event == "退出":
        sg.Popup("确认取消吗？")
        t.sleep(1)
        break



window.close()
    