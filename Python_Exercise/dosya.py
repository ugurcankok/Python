import sys


def kayit():
    dosya = open("dosya.txt", "a")
    g = input(
        "Dosya kaydetmek için içerik bilgisi. \n ISBN,yazaradı,kitapadı,kategoriadı (Kayıtları bu şekilde yapınız!) \n")
    dosya.write(g + "\n")
    dosya.close()
    print("Kayıt başarılı...\n")


def arama():
    g = input("Aramak istediğiniz kategoriyi seçiniz (isbn,yazaradi,kitapadi,kategoriadi):\n")
    dosya = open("dosya.txt", "r")
    veri = dosya.readlines()
    hata = ""

    if (g == "isbn"):
        giris = input("Aranacak isbn numarasını giriniz: ")
        for i in veri:
            if (i.split(',')[0] == giris):
                print("\nBulunan kayıt: " + i)
                hata = ""
                break
            else:
                hata = "Aranan kayıt bulunamadı."

    if (g == "yazaradi"):
        giris = input("Aranacak yazar adını giriniz: ")
        for i in veri:
            if (i.split(',')[1] == giris):
                print("\nBulunan kayıt: " + i)
                hata = ""
                break
            else:
                hata = "Aranan kayıt bulunamadı."

    if (g == "kitapadi"):
        giris = input("Aranacak kitap adını giriniz: ")
        for i in veri:
            if (i.split(',')[2] == giris):
                print("\nBulunan kayıt: " + i)
                hata = ""
                break
            else:
                hata = "Aranan kayıt bulunamadı."

    if (g == "kategoriadi"):
        giris = input("Aranacak kitap adını giriniz: ")
        for i in veri:
            if (i.split(',')[3].strip("\n") == giris):
                print("\nBulunan kayıt: " + i)
                hata = ""
                break
            else:
                hata = "Aranan kayıt bulunamadı."

    if (hata != ""):
        print(hata)
        arama()
    dosya.close()


while (True):
    giris = input("İşlem seçiniz \nk: kayıt işlemleri \ns: arama işlemleri\nx: çıkış\n")
    if (giris == "k"):
        kayit()
    if (giris == "s"):
        arama()
    if (giris == "x"):
        sys.exit(0)