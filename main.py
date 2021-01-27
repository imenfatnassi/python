import sqlite3

try:
    connexion = sqlite3.connect('festival.db')
    connexion.execute("PRAGMA foreign_keys =1")
    create_table = '''CREATE TABLE if not Exists spectacle (
                                   code INTEGER PRIMARY KEY,
                                   name TEXT NOT NULL,
                                   type TEXT NOT NULL);'''
    create_table1 = '''CREATE TABLE if not Exists salle (
                                   num INTEGER PRIMARY KEY,
                                   capa INTEGER);'''
    create_table2 = '''CREATE TABLE if not Exists representation (
                                   numrep INTEGER PRIMARY KEY,
                                   date DATE,
                                   heure TIME,
                                   num_r INTEGER,
                                   coderep INTEGER,
                                   FOREIGN KEY (num_r) REFERENCES salle (num),
                                   FOREIGN KEY (coderep) REFERENCES spectacle (code));'''
    create_table3 = '''CREATE TABLE if not Exists tarif (
                                       id INTEGER PRIMARY KEY,
                                       type TEXT NOT NULL,
                                       prix INTEGER);'''
    create_table4 = '''CREATE TABLE if not Exists billet (
                                       num_b INTEGER PRIMARY KEY,
                                       lieu TEXT NOT NULL,
                                       cat TEXT,
                                       cd INTEGER,
                                       FOREIGN KEY (cd) REFERENCES spectacle (code),
                                       FOREIGN KEY (cat) REFERENCES tarif (type));'''
    create_table5 = '''CREATE TABLE if not Exists spectateur (
                                       id INTEGER PRIMARY KEY,
                                       nom TEXT NOT NULL,
                                       age INTEGER);'''
    cursor = connexion.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(create_table)
    cursor.execute(create_table1)
    cursor.execute(create_table2)
    cursor.execute(create_table3)
    cursor.execute(create_table4)
    cursor.execute(create_table5)
    connexion.commit()
    print("SQLite table created")
    cursor.close()
except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (connexion):
        connexion.close()
        print("sqlite connection is closed")