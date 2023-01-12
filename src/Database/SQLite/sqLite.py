import sqlite3

con = sqlite3.connect("dersler.db")

cursor = con.cursor()


def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT, soyad TEXT, numara INT, ogrencinotu INT)")
    con.commit()
    con.close()


def insertRecord():
    cursor.execute("INSERT INTO ogrenciler VALUES ('kerem', 'kok',9090,2342)")
    # cursor.execute("INSERT INTO ogrenciler (ad,soyad,numara,ogrencinotu) VALUES (?,?,?,?)",(ad,soyad,numara,
    # ogrencinotu))
    con.commit()
    con.close()


def showRecord():
    # cursor.execute("SELECT ad FROM ogrenciler WHERE soyad='Kok' AND numara=1234")
    cursor.execute("SELECT * FROM ogrenciler")
    data = cursor.fetchall()
    for i in data:
        print(i)


def updateRecord():
    print("Ilk Değerler -------------------------")
    showRecord()

    cursor.execute("UPDATE ogrenciler SET ad='ugur' WHERE numara=1234")

    print("Güncel Değerler ----------------------")
    showRecord()


def deleteRecord():
    print("Ilk Değerler -------------------------")
    showRecord()
    cursor.execute("DELETE FROM ogrenciler WHERE ogrencinotu=6789")
    print("Son Durum -------------------------")
    showRecord()


if __name__ == "__main__":
    deleteRecord()
