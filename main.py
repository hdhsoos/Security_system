import PySimpleGUI as sg
from Database import *


def wrong_update(login, password):
    text_elem = window['-result-']  # получаем доступ к текстовому элементу
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
    layout = [[sg.Text('Карта', pad=((133, 0), (8, 8)))],
              [sg.Button('Кабинет 1', size=(10, 5), pad=((5, 10), (0, 0))),
               sg.Button('Кабинет 2', size=(10, 5), pad=((5, 10), (0, 0))), sg.Button('Кабинет 3', size=(10, 5)), sg.Button('Сотрудники', size=(15, 2), pad=((27, 0), (0, 0)))],
              [sg.Button('Кабинет 4', size=(10, 5), pad=((5, 10), (0, 0))),
              sg.Button('Кабинет 5', size=(10, 5), pad=((5, 10), (0, 0))), sg.Button('Кабинет 6', size=(10, 5)), sg.Button('Открыть журнал', size=(15, 2), pad=((27, 0), (0, 0)))],
              [sg.Button('Кабинет 7', size=(10, 5), pad=((5, 10), (0, 0))), sg.Button('Кабинет 8', size=(10, 5),
                                                                                      pad=((5, 10), (0, 0))), sg.Button(
                  'Кабинет 9', size=(10, 5)), sg.Button('Добавить нового охранника', size=(15, 2), pad=((27, 0), (0, 0)))], [sg.Button('Cancel', pad=((205, 0), (30, 0)))]]
    window = sg.Window('Security program', layout, location=(300, 0), finalize=True,
                       size=(480, 400))#, sg.Button('Добавить нового сотрудника', size=(15, 2), pad=((160, 0), (6, 0)))]


# All the stuff inside your window.
layout = [[sg.Text('Введи логин и пароль', pad=((0, 0), (200, 8)))],
          [sg.Text('Логин:   '), sg.InputText(size=(16, 1))],
          [sg.Text('Пароль: '), sg.InputText(size=(16, 1))],
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
    if event == 'Ok':
        wrong_update(values[0], values[1])

window.close()
