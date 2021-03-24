class Calisan():
    def __init__(self,isim,maas,departman):
        print("Çalışan Sınıfının Yapıcı Fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgilerigoster(self):
        print("Çalışan sınıfının bilgileri gösteriliyor.....")
        print("İsim: ", self.isim, " Maas: ", self.maas, " Departman: ", self.departman)

    def maasazamnyap(self,zam_miktari):
        print("Maasa zam yapıldı...")
        self.maas += zam_miktari

    def departmandegistir(self, yeni_departman):
        print("Departman değiştiriliyor....")
        self.departman = yeni_departman

'''
calisan = Calisan("Ugur",2000,"Computer")
calisan.bilgilerigoster()
'''

class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisi_sayisi):
        #overriding
        print("Yönetici sınıfının yapıcı fonksiyonu")
        super().__init__(isim,maas,departman)
        self.kisi_sayisi = kisi_sayisi #ek özellik olarak bunu ekledik

    def bilgilerigoster(self):
        #overriding
        print("Yönetici sınıfının bilgileri gösteriliyor...")
        print("İsim: ", self.isim, " Maas: ", self.maas, " Departman: ", self.departman, "Kisi sayısı: ", self.kisi_sayisi)


yonetici = Yonetici("ugur",5000,"Computer",20)
yonetici.bilgilerigoster()