import sqlite3
import random
import datetime

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("connection succeed")
    except Exception as e:
        print(e)

    return conn

def create_spectateur(conn, spectateur):
    sql = ''' INSERT INTO 'spectateur'(id,nom,age)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, spectateur)
    conn.commit()
    return cur.lastrowid

def create_spectacle(conn, spectacle):
    sql = ''' INSERT INTO 'spectacle'(code,name,type)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, spectacle)
    conn.commit()
    return cur.lastrowid

def create_tarif(conn, tarif):
    sql = ''' INSERT INTO 'tarif'(id,type,prix)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, tarif)
    conn.commit()
    return cur.lastrowid

def create_billet(conn, data):

    sql = ''' INSERT INTO 'billet'(num_b,lieu,cat,cd)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

def select_all(conn,table):

    cur = conn.cursor()
    cur.execute("SELECT * FROM "+table)

    rows = cur.fetchall()

    for row in rows:
        print(row)

def create_salle(conn, data):

    sql = ''' INSERT INTO 'salle'(num,capa)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

def create_representation(conn, data):

    sql = ''' INSERT INTO 'representation'(numrep,date,heure,num_r,coderep)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

def truncate_table(conn,table):
    sql = 'DELETE FROM '+table
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def random_spectateur():
    for x in range(1, 50, 1):
        spectateur = (x, random.choice(names), random.randint(7, 80))
        spectateur_id = create_spectateur(conn, spectateur)

def random_tarif():
     for x in range(1, 50, 1):
         tarif = (x, random.choice(tarif_type), random.choice(tarif_prix))
         tarif_id = create_tarif(conn, tarif)

#en cour
def random_billet():
    for x in range(1, 50, 1):
        billet = (x,random.choice(billet_lieu), random.choice(tarif_type), random.choice(code_id))
        billet_id = create_billet(conn, billet)

def random_spectacle():
    for x in range(1, 50, 1):
        spectale = (x, random.choice(spectale_name), random.choice(spectale_type))
        spectale_id = create_spectacle(conn, spectale)


def insert_salle():
    salle = ('1','300')
    salle_id = create_salle(conn, salle)
    salle = ('2','600')
    salle_id = create_salle(conn, salle)

def random_representation():
    date = datetime.datetime(2020,8,1,12,00,00)
    pair = 0
    last_choice=1
    for x in range(1, 50, 1):
        pair=pair+1
        if(pair == 2):
            pair=0
            date += datetime.timedelta(hours=1)
        representation = (x, str(date.date()), str(date.time()), last_choice, random.choice(spectale_id))
        representation_id = create_representation(conn, representation)
        if (last_choice==1):
            last_choice=2
        else:
            last_choice=1



conn=create_connection('festival.db')

#DATA
names=["Maqsood","Nasim","Jamal","Asad","Yasser","Bahiga","Raheem","Yasir"]
spectale_name = ["La Machine de Turing","Et pendant ce temps, Simone veille !","Le Lac des cygnes","La Promesse de l'aube","L'Avare","La Mouette","12 hommes en colère","Tangled","Something Borrowed","Remember Me","Rachel Getting Married","Not Easily Broken","Music and Lyrics","RICHARD","MASSENET","METROPOLE"]
spectale_type = ["théâtre", "cinéma", "musique"]
tarif_type = ["normal", "reduit", "place"]
tarif_prix = ["15.000", "10.000", "80.000"]
billet_lieu = ["guichet de public","bureau de gestion"]

# a supprimer ( code )
code_id=[]
for x in range(1,50,1):
    code_id.append(x)

tarif_id=[]
for x in range(1,50,1):
    tarif_id.append(x)


salle=[1,2]
spectale_id=[]
for x in range(1,50,1):
    spectale_id.append(x)

insert_salle()
random_spectacle()
random_spectateur()
random_representation()
random_tarif()
random_billet()


print("printing spectateur table")
select_all(conn,'spectateur')
print("printing spectacle table")
select_all(conn,'spectacle')
print("printing salle table")
select_all(conn,'salle')
print("printing representation table")
select_all(conn,'representation')
print("printing tarif table")
select_all(conn,'tarif')
print("printing billet table")
select_all(conn,'billet')