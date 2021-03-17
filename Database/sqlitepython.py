import sqlite3

con = sqlite3.connect("dersler.db")

cursor = con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT, soyad TEXT, numara INT, ogrencinotu INT)")
    con.commit()
    con.close()

def degerekle():
    cursor.execute("INSERT INTO ogrenciler VALUES ('kerem', 'kok',9090,2342)")
   # cursor.execute("INSERT INTO ogrenciler (ad,soyad,numara,ogrencinotu) VALUES (?,?,?,?)",(ad,soyad,numara,ogrencinotu))
    con.commit()
    con.close()

def degergoster():
    #cursor.execute("SELECT ad FROM ogrenciler WHERE soyad='Kok' AND numara=1234")
    cursor.execute("SELECT * FROM ogrenciler")
    data = cursor.fetchall()
    for i in data:
        print(i)

def degerguncelle():
    print("Ilk Değerler -------------------------")
    degergoster()

    cursor.execute("UPDATE ogrenciler SET ad='ugur' WHERE numara=1234")

    print("Güncel Değerler ----------------------")
    degergoster()

def degersil():
    print("Ilk Değerler -------------------------")
    degergoster()
    cursor.execute("DELETE FROM ogrenciler WHERE ogrencinotu=6789")
    print("Son Durum -------------------------")
    degergoster()

degersil()