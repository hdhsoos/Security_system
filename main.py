import PySimpleGUI as sg
from Database import *


def wrong_update(login, password):
    text_elem = window['-result-'] # получаем доступ к текстовому элементу
    search = passwords.search(login)
    if search == []:
        text_elem.update("Логин не найден.")
    elif search[0][2] != password:
        text_elem.update("Пароль не верный.")
    elif search[0][2] == password:
        open_main_wind()

def open_main_wind():
    global layout, window

    window.close()
    layout = [[sg.Text('Добро пожаловать', pad=((0, 0), (200, 8)))]]
    window = sg.Window('Security program', layout, location=(300, 0), finalize=True, element_justification="center",
                       size=(600, 550))

# All the stuff inside your window.
layout = [[sg.Text('Введи логин и пароль', pad=((0, 0), (200, 8)))],
          [sg.Text('Логин:   '), sg.InputText()],
          [sg.Text('Пароль: '), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')],
          [sg.Text('', key='-result-')]]

# Create the Window
window = sg.Window('Введите логин', layout, location=(300, 0), finalize=True, element_justification="center",
                   size=(600, 550))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    wrong_update(values[0], values[1])

window.close()
