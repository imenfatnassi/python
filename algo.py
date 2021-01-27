# changement de dossier
import os
import csv
#
# importation des données
import pandas
import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("connection succeed")
    except Exception as e:
        print(e)
    return conn

def get_count(conn,table,name):

    cur = conn.cursor()
    cur.execute("select count(name) FROM " +table+" where name=?",(name,))
    row = cur.fetchone()
    return [row[0],name]

def get_column(conn,table,column):

    cur = conn.cursor()
    cur.execute("select DISTINCT("+column+") FROM "+table)
    rows = cur.fetchall()
    return rows

def select_all(conn,table):

    cur = conn.cursor()
    cur.execute("SELECT * FROM "+table)

    rows = cur.fetchall()

    for row in rows:
        print(row)

def write(names,file_out):
    wtr = csv.writer(open(file_out, 'w'), delimiter=',', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
    for name in names:
        row = get_count(conn, "spectacle", name[0])
        print(row[0])
        wtr.writerow([str(row[0]),str(row[1])])



conn= create_connection("festival.db")

names=get_column(conn,"spectacle","name")
write(names, "result.txt")


os.chdir("E:\MP2L2\DATA")
D = pandas.read_table("data_spectacle.txt.txt", sep="\t", header=0, index_col=0)
print(D.head)
print(D.shape)
