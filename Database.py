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
            "CREATE TABLE IF NOT EXISTS workers (id INTEGER PRIMARY KEY, fio TEXT, cabinets TEXT, cur_place TEXT)") # '1 3 4 5' - массив цифр
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
        self.cur.execute("UPDATE workers SET fio=?, cabinets=?, cur_place=? WHERE id=?", (fio, cabinets, cur_place, id,))
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
#passwords.insert('a', 'a')
workers = WorkersDB()
#workers.insert('Смирнова Майя Ильинична', '1 3 5', '2')
#workers.insert('Лебедева Полина Петровна', '1 2 6', '1')
#workers.insert('Царев Макар Ильич', '6 7 8 9', '6')
#workers.insert('Семенов Кирилл Алексеевич', '5 6 7 8', '5')