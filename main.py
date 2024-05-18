import PySimpleGUI as sg

def wrong_update(login, password):
    # получаем доступ к текстовому элементу
    text_elem = window['-result-']
    # выводим в него новый текст
    text_elem.update("Логин и пароль введены.")

# All the stuff inside your window.
layout = [  [sg.Text('Введи логин и пароль', pad=((0, 0), (200, 8)))],
            [sg.Text('Логин:   '), sg.InputText()],
            [sg.Text('Пароль: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Text('', key='-result-')]]

# Create the Window
window = sg.Window('Window Title', layout, location=(300, 0),finalize=True, element_justification="center", size=(600,550))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    wrong_update(values[0], values[1])

window.close()