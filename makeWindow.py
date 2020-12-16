from tkinter import Widget
import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [ [sg.Text('Enter something : '), sg.InputText()],
           [sg.Button('OK'), sg.Button('CANCLE')]]

window = sg.Window('a small window', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'CANCLE':
        break
    print('You entered ', values[0])

window.close()