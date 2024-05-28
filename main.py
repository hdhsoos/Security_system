import PySimpleGUI as sg
# from Database import *
import time
import sqlite3


# создаём класс для работы с базой данных
class LoginsDB:
    # конструктор класса
    def __init__(self):
        # соединяемся с файлом базы данных
        self.conn = sqlite3.connect("Security.db")
        # создаём курсор для виртуального управления базой данных
        self.cur = self.conn.cursor()
        # если нужной нам таблицы в базе нет — создаём её
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, login TEXT, password TEXT)")
        # сохраняем сделанные изменения в базе
        self.conn.commit()

        # деструктор класса

    def __del__(self):
        # отключаемся от базы при завершении работы
        self.conn.close()

        # просмотр всех записей

    def view(self):
        # выбираем все записи о покупках
        self.cur.execute("SELECT * FROM users")
        # собираем все найденные записи в колонку со строками
        rows = self.cur.fetchall()
        # возвращаем сроки с записями расходов
        return rows

    # добавляем новую запись
    def insert(self, login, password):
        # формируем запрос с добавлением новой записи в БД
        self.cur.execute("INSERT INTO users VALUES (NULL,?,?)", (login, password,))
        # сохраняем изменения
        self.conn.commit()

    # обновляем информацию о покупке
    def update(self, id, login, password):
        # формируем запрос на обновление записи в БД
        self.cur.execute("UPDATE users SET login=?, password=? WHERE id=?", (login, password, id,))
        # сохраняем изменения
        self.conn.commit()

    # удаляем запись
    def delete(self, id):
        # формируем запрос на удаление выделенной записи по внутреннему порядковому номеру
        self.cur.execute("DELETE FROM users WHERE id=?", (id,))
        # сохраняем изменения
        self.conn.commit()

    # ищем запись по названию покупки
    def search(self, login=""):
        # формируем запрос на поиск по точному совпадению
        self.cur.execute("SELECT * FROM users WHERE login=?", (login,))
        # формируем полученные строки и возвращаем их как ответ
        rows = self.cur.fetchall()
        return rows


class WorkersDB:
    # конструктор класса
    def __init__(self):
        # соединяемся с файлом базы данных
        self.conn = sqlite3.connect("Security.db")
        # создаём курсор для виртуального управления базой данных
        self.cur = self.conn.cursor()
        # если нужной нам таблицы в базе нет — создаём её
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS workers (id INTEGER PRIMARY KEY, fio TEXT, cabinets TEXT, cur_place TEXT)")  # '1 3 4 5' - массив цифр
        # сохраняем сделанные изменения в базе
        self.conn.commit()

        # деструктор класса

    def __del__(self):
        # отключаемся от базы при завершении работы
        self.conn.close()

        # просмотр всех записей

    def view(self):
        # выбираем все записи о покупках
        self.cur.execute("SELECT * FROM workers")
        # собираем все найденные записи в колонку со строками
        rows = self.cur.fetchall()
        # возвращаем сроки с записями расходов
        return rows

    # добавляем новую запись
    def insert(self, fio, cabinets, cur_place):
        # формируем запрос с добавлением новой записи в БД
        self.cur.execute("INSERT INTO workers VALUES (NULL,?,?,?)", (fio, cabinets, cur_place,))
        # сохраняем изменения
        self.conn.commit()

    # обновляем информацию о покупке
    def update(self, id, fio, cabinets, cur_place):
        # формируем запрос на обновление записи в БД
        self.cur.execute("UPDATE workers SET fio=?, cabinets=?, cur_place=? WHERE id=?",
                         (fio, cabinets, cur_place, id,))
        # сохраняем изменения
        self.conn.commit()

    # удаляем запись
    def delete(self, id):
        # формируем запрос на удаление выделенной записи по внутреннему порядковому номеру
        self.cur.execute("DELETE FROM workers WHERE id=?", (id,))
        # сохраняем изменения
        self.conn.commit()

    # ищем запись по названию покупки
    def search(self, login=""):
        # формируем запрос на поиск по точному совпадению
        self.cur.execute("SELECT * FROM workers WHERE fio=?", (login,))
        # формируем полученные строки и возвращаем их как ответ
        rows = self.cur.fetchall()
        return rows

    def search_id(self, id=""):
        # формируем запрос на поиск по точному совпадению
        self.cur.execute("SELECT * FROM workers WHERE id=?", (id,))
        # формируем полученные строки и возвращаем их как ответ
        rows = self.cur.fetchall()
        return rows

    def search_second(self, cur_place=""):
        # формируем запрос на поиск по точному совпадению
        self.cur.execute("SELECT * FROM workers WHERE cur_place=?", (cur_place,))
        # формируем полученные строки и возвращаем их как ответ
        rows = self.cur.fetchall()
        return rows


# создаём новый экземпляр базы данных на основе класса
passwords = LoginsDB()
if passwords.search('a') == []:
    passwords.insert('a', 'a')
workers = WorkersDB()
if workers.search('Смирнова Майя Ильинична') == []:
    workers.insert('Смирнова Майя Ильинична', '1 3 5', '2')
if workers.search('Лебедева Полина Петровна') == []:
    workers.insert('Лебедева Полина Петровна', '1 2 6', '1')
if workers.search('Царев Макар Ильич') == []:
    workers.insert('Царев Макар Ильич', '6 7 8 9', '6')
if workers.search('Семенов Кирилл Алексеевич') == []:
    workers.insert('Семенов Кирилл Алексеевич', '5 6 7 8', '5')


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


def delete_worker(id):
    search = workers.search_id(id)
    text_elem = window['-delresult-']
    if search == []:
        text_elem.update("id не существует.")
    else:
        try:
            workers.delete(id)
            text_elem.update("Сотрудник удалён.")
        except:
            text_elem.update("Произошла ошибка.")


def del_worker_menu():
    global window

    window.close()
    layout = [[sg.Text('Введите id сотрудника', pad=((0, 0), (0, 0)))],
              [sg.Text('id: '), sg.InputText(size=(16, 1))],
              [sg.Button('Delete', pad=((118, 0), (0, 0))), sg.Button('Back ')],
              [sg.Text('', key='-delresult-')]]
    window = sg.Window('Удалить сотрудника', layout, location=(300, 0), finalize=True,
                       size=(325, 150))


def add_new_worker(login, password):
    search = workers.search(login)
    text_elem = window['-workresult-']
    if search != []:
        text_elem.update("ФИО уже существует.")
    else:
        try:
            workers.insert(login, password, '0')
            text_elem.update("Сотрудник добавлен.")
        except:
            text_elem.update("Произошла ошибка.")


def open_workers_list():
    global window

    window.close()
    A = []
    for el in workers.view():
        x = ''
        for e in el: x += str(e) + ' - '
        x = x[:-3]
        A.append(x)
    column1 = [[sg.Listbox(A, size=(40, 20), pad=((2, 0), (10, 10)), key='listbox')],
               [sg.Button('Back', pad=((215, 0), (10, 0)))]]
    column2 = [[sg.Button('Показать все', size=(17, 2), pad=((23, 0), (20, 18)))],
               [sg.Button('Найти сотрудника', size=(17, 2), pad=((23, 0), (20, 20)))],
               [sg.Button('Добавить сотрудника', size=(17, 2), pad=((23, 0), (20, 20)))],
               [sg.Button('Изменить информацию', size=(17, 2), pad=((23, 0), (20, 20)))],
               [sg.Button('Удалить сотрудника', size=(17, 2), pad=((23, 0), (20, 20)))]]
    layout = [[sg.Column(column1), sg.Column(column2)]]
    window = sg.Window('Список сотрудников', layout, location=(310, 0), size=(500, 420))


def open_log():
    global window
    A = []
    try:
        f = open('log.txt', 'r')
    except:
        f = open('log.txt', 'w')
        f.close()
        f = open('log.txt', 'r')
    for el in f:
        A.append(el)
    window.close()
    layout = [[sg.Listbox(A, size=(75, 20), pad=((2, 0), (10, 10)))], [sg.Button('Back', pad=((250, 0), (15, 0)))]]
    window = sg.Window('Журнал', layout, location=(300, 0), finalize=True,
                       size=(580, 420))


def find_worker(fio):
    global window

    window.close()
    A = []
    for el in workers.search(fio):
        x = ''
        for e in el: x += str(e) + ' - '
        x = x[:-3]
        A.append(x)
    column1 = [[sg.Listbox(A, size=(40, 20), pad=((2, 0), (10, 10)), key='listbox')],
               [sg.Button('Back', pad=((215, 0), (10, 0)))]]
    column2 = [[sg.Button('Показать все', size=(17, 2), pad=((23, 0), (20, 30)))],
               [sg.Button('Найти сотрудника', size=(17, 2), pad=((23, 0), (20, 30)))],
               [sg.Button('Добавить сотрудника', size=(17, 2), pad=((23, 0), (20, 30)))],
               [sg.Button('Обновить информацию', size=(17, 2), pad=((23, 0), (20, 30)))],
               [sg.Button('Удалить сотрудника', size=(17, 2), pad=((23, 0), (20, 30)))], ]
    layout = [[sg.Column(column1), sg.Column(column2)]]
    window = sg.Window('Список сотрудников', layout, location=(300, 0), size=(500, 420))


def find_worker_menu():
    global window

    window.close()
    layout = [[sg.Text('Введите фио сотрудника', pad=((0, 0), (0, 0)))],
              [sg.Text('ФИО: '), sg.InputText(size=(16, 1))],
              [sg.Button('Find', pad=((118, 0), (0, 0))), sg.Button('Back ')],
              [sg.Text('', key='-findworkresult-')]]
    window = sg.Window('Найти сотрудника', layout, location=(300, 0), finalize=True,
                       size=(325, 150))


def update_worker(id, fio, kabinets, cur_place):
    search = workers.search_id(id)
    text_elem = window['-updatebutton-']
    if search == []:
        text_elem.update("id не существует.")
    else:
        if len(cur_place) > 1:
            text_elem.update("Введите одну цифру для текущего кабинета.")
        else:
            try:
                if fio == '':
                    fio = search[0][1]
                if kabinets == '':
                    kabinets = search[0][2]
                if cur_place == '':
                    cur_place = search[0][3]
                    workers.update(id, fio, kabinets, cur_place)
                    text_elem.update("Сотрудник обновлён.")
                else:
                    if cur_place not in search[0][2] and cur_place != '0':
                        text_elem.update("У сотрудника нет доступа в этот кабинет.")
                        f = open('log.txt', 'a')
                        x = time.ctime(time.time())
                        f.write('{} Сотрудник {} покинул кабинет {}.\n'.format(x, fio, search[0][3]))
                        f.write('{} Сотрудник {} пытался попасть \nв кабинет {}.\n'.format(x, fio, cur_place))
                        f.write('{} Сотрудник {} зашёл в кабинет {}.\n'.format(x, fio, search[0][3]))
                    else:
                        workers.update(id, fio, kabinets, cur_place)
                        x = time.ctime(time.time())
                        f = open('log.txt', 'a')
                        if search[0][3] == '0':
                            f.write('{} Сотрудник {} зашёл в офис.\n'.format(x, fio))
                        else:
                            f.write('{} Сотрудник {} покинул кабинет {}.\n'.format(x, fio, search[0][3]))
                        if cur_place == '0':
                            f.write('{} Сотрудник {} покинул офис.\n'.format(x, fio))
                        else:
                            f.write('{} Сотрудник {} зашёл в кабинет {}.\n'.format(x, fio, cur_place))
                        f.close()
                        text_elem.update("Сотрудник обновлён.")

            except:
                text_elem.update("Произошла ошибка.")


def update_worker_menu():
    global window

    window.close()
    layout = [[sg.Text('Введите id, фио, доступные и текущий\nкабинеты для обновления.', pad=((0, 0), (0, 0)))],
              [sg.Text('id: (обязательно)'), sg.InputText(size=(16, 1))],
              [sg.Text('ФИО: (необязательно)           '), sg.InputText(size=(16, 1))],
              [sg.Text('Номера через пробел: (необязательно)'), sg.InputText(size=(16, 1))],
              [sg.Text('Текущее местоположение: (необязательно)'), sg.InputText(size=(16, 1))],
              [sg.Button('Update', pad=((118, 0), (0, 0))), sg.Button('Back ')],
              [sg.Text('', key='-updatebutton-')]]
    window = sg.Window('Обновить информацию', layout, location=(300, 0), finalize=True,
                       size=(375, 215))


def adding_worker_menu():
    global window

    window.close()
    layout = [[sg.Text('Введите фио и кабинеты для нового сотрудника', pad=((0, 0), (0, 0)))],
              [sg.Text('ФИО:                          '), sg.InputText(size=(16, 1))],
              [sg.Text('Номера через пробел: '), sg.InputText(size=(16, 1))],
              [sg.Button('Add ', pad=((118, 0), (0, 0))), sg.Button('Back ')],
              [sg.Text('', key='-workresult-')]]
    window = sg.Window('Добавить сотрудника', layout, location=(300, 0), finalize=True,
                       size=(325, 150))


def open_sec_list():
    global window

    window.close()
    layout = [[sg.Text('Введите логин и пароль для нового охранника', pad=((0, 0), (0, 0)))],
              [sg.Text('Логин:   '), sg.InputText(size=(16, 1))],
              [sg.Text('Пароль: '), sg.InputText(size=(16, 1))],
              [sg.Button('Add', pad=((40, 0), (0, 0))), sg.Button('Back')],
              [sg.Text('', key='-secresult-')]]
    window = sg.Window('Добавить охранника', layout, location=(300, 0), finalize=True,
                       size=(325, 130))


def rooms(number):
    global window

    window.close()
    A = []
    for el in workers.search_second(number):
        x = ''
        for e in el: x += str(e) + ' - '
        x = x[:-3]
        A.append(x)
    column1 = [[sg.Text('id    fio    доступные кабинеты    текущее место')],
               [sg.Listbox(A, size=(40, 20), pad=((2, 0), (10, 10)))], [sg.Button('Back', pad=((128, 0), (8, 0)))]]
    layout = [[sg.Column(column1)]]
    window = sg.Window('Комната {}'.format(number), layout, location=(300, 0), size=(340, 440))


def open_main_wind():
    global window

    window.close()
    column1 = [[sg.Text('Карта', pad=((133, 0), (8, 8)))],
               [sg.Button('Кабинет 1', size=(10, 5), pad=((5, 10), (0, 0))),
                sg.Button('Кабинет 2', size=(10, 5), pad=((5, 10), (0, 0))), sg.Button('Кабинет 3', size=(10, 5))
                ],
               [sg.Button('Кабинет 4', size=(10, 5), pad=((5, 10), (0, 0))),
                sg.Button('Кабинет 5', size=(10, 5), pad=((5, 10), (0, 0))), sg.Button('Кабинет 6', size=(10, 5))
                ],
               [sg.Button('Кабинет 7', size=(10, 5), pad=((5, 10), (0, 0))), sg.Button('Кабинет 8', size=(10, 5),
                                                                                       pad=((5, 10), (0, 0))),
                sg.Button(
                    'Кабинет 9', size=(10, 5))], [sg.Button('Cancel', pad=((200, 0), (30, 0)))]]
    column2 = [[sg.Button('Сотрудники', size=(17, 2), pad=((23, 0), (20, 0)))],
               [sg.Button('Открыть журнал', size=(17, 2), pad=((23, 0), (20, 0)))],
               [sg.Button('Добавить нового охранника', size=(17, 2), pad=((23, 0), (20, 0)))]]
    layout = [[sg.Column(column1), sg.Column(column2)]]
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
                   size=(300, 160))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    global A
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break  # if user closes window or clicks cancel
    elif event == 'Ok':
        wrong_update(values[0], values[1])
    elif event == 'Add':
        add_new_sec(values[0], values[1])
    elif event == 'Find':
        find_worker(values[0])
    elif event == 'Add ':
        add_new_worker(values[0], values[1])
    elif event == 'Сотрудники':
        open_workers_list()
    elif event == 'Back':
        open_main_wind()
    elif event == 'Back ':
        open_workers_list()
    elif event == 'Открыть журнал':
        open_log()
    elif event == 'Добавить нового охранника':
        open_sec_list()
    elif event == 'Найти сотрудника':
        find_worker_menu()
    elif event == 'Добавить сотрудника':
        adding_worker_menu()
    elif event == 'Показать все':
        A = []
        for el in workers.view():
            x = ''
            for e in el: x += str(e) + ' - '
            x = x[:-3]
            A.append(x)
        window['listbox'].update(A)
    elif event == 'Кабинет 1':
        rooms('1')
    elif event == 'Кабинет 2':
        rooms('2')
    elif event == 'Кабинет 3':
        rooms('3')
    elif event == 'Кабинет 4':
        rooms('4')
    elif event == 'Кабинет 5':
        rooms('5')
    elif event == 'Кабинет 6':
        rooms('6')
    elif event == 'Кабинет 7':
        rooms('7')
    elif event == 'Кабинет 8':
        rooms('8')
    elif event == 'Кабинет 9':
        rooms('9')
    elif event == 'Удалить сотрудника':
        del_worker_menu()
    elif event == 'Delete':
        delete_worker(values[0])
    elif event == 'Изменить информацию':
        update_worker_menu()
    elif event == 'Update':
        update_worker(values[0], values[1], values[2], values[3])

window.close()
