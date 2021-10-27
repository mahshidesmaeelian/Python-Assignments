import sqlite3

con = sqlite3.connect('todolist.db')

my_cursor = con.cursor()

def add(title1,description):

    my_cursor.execute(f'INSERT INTO Task(Title , Description) VALUES ("{title1}" , "{description}")')
    con.commit()


def get_all():

    my_cursor.execute('SELECT * FROM Task')
    result = my_cursor.fetchall()
    return result

def update_done(a):
    my_cursor.execute(f'UPDATE Task SET Done = 1 WHERE Title = "{a}"')
    con.commit()

def update_not_done(b):
    my_cursor.execute(f'UPDATE Task SET Done = 2 WHERE Title = "{b}" ')
    con.commit()

def remove_function(l):
    my_cursor.execute(f'DELETE FROM Task WHERE Title = "{l}"')
    con.commit()
    