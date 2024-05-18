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

def add_new_sec(login, password):
    search = passwords.search(login)
    text_elem = window['-secresult-']
    if search != []:
        text_elem.update("Логин уже существует.")
    else:
        try:
            passwords.insert(login, password)
            text_elem.update("Охранник добавлен.")
        except:
            text_elem.update("Произошла ошибка.")
def open_workers_list():
    global layout, window

    window.close()
    layout = [[sg.Text('Здесь будет список работников, добавление, удаление')],
              [sg.Button('Back', pad=((205, 0), (30, 0)))]]
    window = sg.Window('Список сотрудников', layout, location=(300, 0), finalize=True,
                       size=(480, 400))


def open_log():
    global layout, window

    window.close()
    layout = [[sg.Text('Здесь будет журнал')], [sg.Button('Back', pad=((205, 0), (30, 0)))]]
    window = sg.Window('Журнал', layout, location=(300, 0), finalize=True,
                       size=(480, 400))

def open_sec_list():
    global layout, window

    window.close()
    layout = [[sg.Text('Введите логин и пароль для нового охранника', pad=((0, 0), (0, 0)))],
              [sg.Text('Логин:   '), sg.InputText(size=(16, 1))],
              [sg.Text('Пароль: '), sg.InputText(size=(16, 1))],
              [sg.Button('Add', pad=((40, 0), (0, 0))), sg.Button('Back')],
              [sg.Text('', key='-secresult-')]]
    window = sg.Window('Добавить охранника', layout, location=(300, 0), finalize=True,
                       size=(325, 130))

def open_main_wind():
    global layout, window

    window.close()
    layout = [[sg.Text('Карта', pad=((133, 0), (8, 8)))],
              [sg.Button('Кабинет 1', size=(10, 5), pad=((5, 10), (0, 0))),
               sg.Button('Кабинет 2', size=(10, 5), pad=((5, 10), (0, 0))), sg.Button('Кабинет 3', size=(10, 5)),
               sg.Button('Сотрудники', size=(15, 2), pad=((27, 0), (0, 0)))],
              [sg.Button('Кабинет 4', size=(10, 5), pad=((5, 10), (0, 0))),
               sg.Button('Кабинет 5', size=(10, 5), pad=((5, 10), (0, 0))), sg.Button('Кабинет 6', size=(10, 5)),
               sg.Button('Открыть журнал', size=(15, 2), pad=((27, 0), (0, 0)))],
              [sg.Button('Кабинет 7', size=(10, 5), pad=((5, 10), (0, 0))), sg.Button('Кабинет 8', size=(10, 5),
                                                                                      pad=((5, 10), (0, 0))), sg.Button(
                  'Кабинет 9', size=(10, 5)),
               sg.Button('Добавить нового охранника', size=(15, 2), pad=((27, 0), (0, 0)))],
              [sg.Button('Cancel', pad=((205, 0), (30, 0)))]]
    window = sg.Window('Security program', layout, location=(300, 0), finalize=True,
                       size=(480, 400))
    # , sg.Button('Добавить нового сотрудника', size=(15, 2), pad=((160, 0), (6, 0)))]


# All the stuff inside your window.
layout = [[sg.Text('Введите логин и пароль', pad=((0, 0), (4, 4)))],
          [sg.Text('Логин:   '), sg.InputText(size=(16, 1))],
          [sg.Text('Пароль: '), sg.InputText(size=(16, 1))],
          [sg.Button('Ok'), sg.Button('Cancel')],
          [sg.Text('', key='-result-')]]

# Create the Window
window = sg.Window('Введите логин', layout, location=(300, 0), finalize=True, element_justification="center",
                   size=(300, 130))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': break  # if user closes window or clicks cancel
    if event == 'Ok': wrong_update(values[0], values[1])
    if event == 'Add': add_new_sec(values[0], values[1])
    if event == 'Сотрудники': open_workers_list()
    if event == 'Back': open_main_wind()
    if event == 'Открыть журнал': open_log()
    if event == 'Добавить нового охранника': open_sec_list()

window.close()
