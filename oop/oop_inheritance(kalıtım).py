
'''
class Personel:
    pass

per_1 = Personel()
per_2 = Personel()

print(Personel)
print(per_1)
print(per_2)

print("__" * 50)

per_1.isim = "ahmet"
per_1.soyisim = "tekin"
per_1.eposta = "ahmet.tekin@firma.com"

per_2.isim = "mehmet"
per_2.soyisim = "çetin"
per_2.eposta = "mehmet.çetin@firma.com"

print(per_1.eposta)
print()
print(per_2.eposta)

'''

'''
class Personel:
    def __init__(self, isim, soyisim, maas, boy, kilo, meslek):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f"{isim.lower()}.{soyisim.lower()}@firma.com"
        self.boy = boy
        self.kilo = kilo
        self.meslek = meslek
        

    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"
    
    def ücret(self):
        return f"{self.isim} {self.soyisim} adlı personelin maaşı {self.maas} tl dir."
    
    def fiziksel_özellikler(self):
        return f"{self.isim} {self.soyisim} adlı personelin boyu = {self.boy} kilosu = {self.kilo}"
    
    def meslegi(self):
        return f"{self.isim} {self.soyisim} adlı personelin mesleği = {self.meslek}"
    

per_1 = Personel("ahmet", "tekin", 45000, 187, 80, "avukat")
per_2 = Personel("mehmet", "can", 55000, 192, 85, "doktor")
per_3 = Personel("kemal", "doğan", 62500, 182, 76, "öğretmen")

print(per_1.tam_isim())
print()
print(per_2.tam_isim())
print()
print(per_3.tam_isim())
print('__'*30)
print(Personel.tam_isim(per_1))
print()
print(Personel.tam_isim(per_2))
print()
print(Personel.tam_isim(per_3))
print()
print('__'*20)
print(per_1.ücret())
print('__'*20)
print(per_3.fiziksel_özellikler())
print('__'*20)
print(per_2.fiziksel_özellikler())
print('__'*20)
print(Personel.fiziksel_özellikler(per_1))
print('__'*20)
print(Personel.ücret(per_3))
print('__'*20)
print(per_1.meslegi())
print('__'*20)
print(Personel.meslegi(per_3))


#print(f"{per_1.isim} {per_1.soyisim} adlı personelin maaşı = {per_1.maas} tl dir.")
#print()
#print(f"{per_2.isim} {per_2.soyisim} adlı personelin maaşı = {per_2.maas} tl dir.")
#print()
#print(per_1.eposta)
#print()
#print(per_2.eposta)
#print()
#print(f"{per_3.isim} {per_3.soyisim} adlı personelin maaşı = {per_3.maas} tl dir.")
#print()
#print(per_3.eposta)

'''

#from pprint import pprint
#
#class Personel:
#    
#    zam_orani = 1.2
#    personel_sayisi = 0
#
#    
#    def __init__(self, isim, soyisim, maas):
#        self.isim = isim
#        self.soyisim = soyisim
#        self.maas = maas
#        self.eposta = f"{isim}.{soyisim}@firma.com"
#        
#        Personel.personel_sayisi += 1
#
#    def tam_isim(self):
#        return f"{self.isim} {self.soyisim}"
#    
#    def zam_uygula(self):
#        self.maas = self.maas * self.zam_orani
#        return self.maas
#
#print(f"personel sayısı = {Personel.personel_sayisi}")
#per_1 = Personel("ahmet", "can", 40000)
#per_2 = Personel("metin", "yiğit", 50000)
#print(f"personel sayısı = {Personel.personel_sayisi}")
#per_3 = Personel("ali", "caner", 70000)
#print(f"personel sayısı = {Personel.personel_sayisi}")

#print(per_1.zam_uygula())
#print(per_2.zam_uygula())
#print("__"*50)

#print(per_1.maas)
#per_1.zam_uygula()
#print(per_1.maas)

#print(Personel.zam_orani)
#print(per_1.zam_orani)
#print(per_2.zam_orani)

#pprint(per_1.__dict__)
#print("________________________")
#pprint(Personel.__dict__) 

#Personel.zam_orani = 1.4
#
#print(Personel.zam_orani)
#print(per_1.zam_orani)
#print(per_2.zam_orani)
#print("__"*50)
#
#per_1.zam_orani = 1.7
#
#print(Personel.zam_orani)
#print(per_1.zam_orani)
#print(per_2.zam_orani)

#pprint(per_1.__dict__)
#per_1.zam_orani = 1.8
#pprint("_______değiştikten sonra________")
#pprint(per_1.__dict__)

#per_1.zam_orani = 1.8

#per_1.zam_uygula()
#print(per_1.maas)
#print("_____________________________")

#per_2.zam_uygula()
#print(per_2.maas)
#print("_____________________________")

#per_2.zam_orani = 1.6

#per_2.zam_uygula()
#print(per_2.maas)

'''
from pprint import pprint

class Takım:
    
    oyuncu_sayisi = 0
    zam_orani = 1.5
    prim_miktarı = 10000
    ceza_miktarı = 5000
    transfer_ücreti = 1 
    
    def __init__(self, isim, soyisim, maas, boy, kilo, yas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.boy = boy
        self.kilo = kilo
        self.yas = yas
        
        Takım.oyuncu_sayisi += 1

    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"
    
    def zam_uygula(self):
        self.maas = self.maas * self.zam_orani
        return self.maas
    
    def fiziksel_özellikler(self):
        return f"{self.isim} {self.soyisim} adlı oyuncunun boyu = {self.boy} kilosu = {self.kilo}"
    
    def maas_göster(self):
        return f"{self.isim} {self.soyisim} adlı oyuncunun maaşı = {self.maas} liradır."
    
    def yas_göster(self):
        return f"{self.isim} {self.soyisim} adlı oyuncunun yaşı = {self.yas}"
    
    def primle_birlikte_maas_göster(self):
        self.maas = self.maas + self.prim_miktarı
        return f"prim aldıktan sonraki maaş {self.maas}"
    
    def ceza_uygula(self):
        self.maas = self.maas - self.ceza_miktarı
        return f"ceza yedikten sonraki maaş {self.maas}"
    
    def transfer_bedeli(self):
        if 50000 <= self.maas <= 70000:
            self.transfer_ücreti = self.maas * 5
        
        if 80000 <= self.maas <= 99000:
            self.transfer_ücreti = self.maas * 7
        
        if self.maas >= 100000:
            self.transfer_ücreti = self.maas * 9
            
        return f"{self.isim} {self.soyisim} adlı oyuncunun transfer bedeli = {self.transfer_ücreti} liradır."
        
        


print(f"takımdaki oyuncu sayısı = {Takım.oyuncu_sayisi}")
oyuncu1 = Takım("ali", "demir", 60000, 182, 75, 32)
oyuncu2 = Takım("veli", "yılmaz", 70000, 180, 77, 28)
oyuncu3 = Takım("ahmet", "yıldırım", 80000, 178, 73, 25)
oyuncu4 = Takım("mehmet", "yaşar", 90000, 185, 82, 30)
print(f"takımdaki oyuncu sayısı = {Takım.oyuncu_sayisi}")

print(oyuncu1.fiziksel_özellikler())
print(oyuncu2.maas_göster())
print(oyuncu3.yas_göster())
print(oyuncu4.tam_isim())
print("__"* 200)

oyuncu1.zam_uygula()
print(oyuncu1.maas_göster())
print("__" * 30)

oyuncu2.zam_uygula()
print(oyuncu2.maas_göster())
print("__" * 30)

oyuncu3.zam_orani = 1.2
oyuncu3.zam_uygula()
print(oyuncu3.maas_göster())
print("__" * 30)

oyuncu4.zam_orani = 1.3
oyuncu4.zam_uygula()
print(oyuncu4.maas_göster())

print("__" * 200)

print(oyuncu1.maas_göster())
print()
print(oyuncu1.primle_birlikte_maas_göster())
print("__" * 30)

print(oyuncu2.maas_göster())
print()
oyuncu2.prim_miktarı = 25000
print(oyuncu2.primle_birlikte_maas_göster())

print("__" * 30)

print(oyuncu3.maas_göster())
print()
oyuncu3.prim_miktarı = 15000
print(oyuncu3.primle_birlikte_maas_göster())

print("__" * 30)

print(oyuncu4.maas_göster())
print()
print(oyuncu4.primle_birlikte_maas_göster())

print("__" * 200)

oyuncu5 = Takım("selim", "ay", 100000, 175, 70, 22)

print(oyuncu5.fiziksel_özellikler())
print("__" * 20)
print(oyuncu5.tam_isim())
print("__" * 20)
print(oyuncu5.yas_göster())
print("__" * 20)
print(oyuncu5.maas_göster())
print("__" * 20)
oyuncu5.zam_orani = 1.80
oyuncu5.zam_uygula()
print(oyuncu5.maas_göster())
print("__" * 20)
oyuncu5.prim_miktarı = 50000
print(oyuncu5.primle_birlikte_maas_göster())
print("__" * 20)
print(f"takımdaki oyuncu sayısı = {Takım.oyuncu_sayisi}")

print("__" * 200)

print(oyuncu1.maas_göster())
oyuncu1.ceza_miktarı = 50000
print(oyuncu1.ceza_uygula())
print(oyuncu1.maas_göster())

print("__" * 200)

print(oyuncu2.maas_göster())
print(oyuncu2.ceza_uygula())
print(oyuncu2.maas_göster())

print("__" * 200)

print(oyuncu4.maas_göster())
oyuncu4.ceza_miktarı = 60000
print(oyuncu4.ceza_uygula())
print(oyuncu4.maas_göster())

print(oyuncu1.transfer_bedeli())
print("__" * 30)
print(oyuncu2.transfer_bedeli())
print("__" * 30)
print(oyuncu3.transfer_bedeli())
print("__" * 30)
print(oyuncu4.transfer_bedeli())

'''

'''
class Personel:
    
    zam_orani = 1.2
    personel_sayisi = 0

    
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.eposta = f"{isim}.{soyisim}@firma.com"
        
        Personel.personel_sayisi += 1

    
    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"
    
    
    def zam_uygula(self):
        self.maas = self.maas * self.zam_orani
        return self.maas
    
    
    @classmethod
    def zam_oranini_belirle(cls, oran):
        eski_oran = cls.zam_orani
        cls.zam_orani = oran
        print(f"eski zam orani {eski_oran} güncellendi. yeni oran : {cls.zam_orani}")
    
    @classmethod
    def from_string(cls, per_str):
        isim, soyisim, maas = per_str.split("-")
        return cls(isim, soyisim, maas)
    
    @staticmethod
    def mesai_gunu(gun):
        if gun.weekday() == 5 or gun.weekday() == 6:
            return "hafta sonu"
        else:
            return "hafta içi"



per_1 = Personel("hakan", "ayan", 15000)
per_2 = Personel("erkan", "demir", 20000)

Personel.zam_oranini_belirle(1.4)
print(Personel.zam_orani)
print(per_1.zam_orani)
print(per_2.zam_orani)
print("__"*50)

per_3_str = "ali-çelik-35000"
per_4_str = "nedim-göl-40000"
per_5_str = "yusuf-ince-50000"

yeni_per1 = Personel.from_string(per_3_str)
print(yeni_per1.eposta)
print(yeni_per1.maas)
print("__"*50)

yeni_per2 = Personel.from_string(per_4_str)
print(yeni_per2.eposta)
print(yeni_per2.maas)
print("__"*50)

yeni_per3 = Personel.from_string(per_5_str)
print(yeni_per3.eposta)
print(yeni_per3.maas)
print("__"*50)

import datetime 
tarih = datetime.date(2000,1,29)
print(tarih.day)
print(Personel.mesai_gunu(tarih))

'''

'''
from datetime import date

class Kisi:
    zam_orani = 1.1
    kisi_sayisi = 0
    def __init__(self, isim, yas, maas, meslek):
        self.isim = isim
        self.yas = yas
        self.maas = maas
        self.meslek = meslek
        self.eposta = f"{isim}.{yas}@gmail.com"
        Kisi.kisi_sayisi += 1
    
    def bilgilerini_goster(self):
        return f"adı : {self.isim} yaşı : {self.yas} maaşı : {self.maas} mesleği : {self.meslek}"
    
    @classmethod
    def kisi_sayisi_goster(cls):
        return cls.kisi_sayisi
    
    @classmethod
    def string_ile_olustur(cls, string):
        isim, yas, maas, meslek = string.split("-")
        return cls(isim, yas, maas, meslek)
    
    @classmethod
    def dogum_yili_ile_göster(cls, isim, dogum_yili):
        return cls(isim, date.today().year - dogum_yili)
    
    @classmethod
    def zam_orani_degistir(cls,yeni_oran):
        eski_oran = cls.zam_orani
        cls.zam_orani = yeni_oran
        return f"personelin eski zam oranı {eski_oran} iken yeni zam oranı {cls.zam_orani} olmuştur."
    
    @staticmethod
    def maas_arttir(kisi, eski_maas):
        zam_miktarı = 10000
        yeni_maas = int(eski_maas) + zam_miktarı
        return f"{kisi} adlı kişinin eski maaşı = {eski_maas} iken yeni maaşı = {yeni_maas} olmuştur."
    
    @classmethod
    def selamla(cls):
        return "hello"
    
    @staticmethod
    def ugurla():
        return "goodbye"
    


kisi1 = Kisi("ali", 35, 38000, "avukat")
kisi2 = Kisi("veli", 40, 34000, "öğretmen")

print(kisi1.bilgilerini_goster())
print(kisi2.bilgilerini_goster())
print(Kisi.bilgilerini_goster(kisi1))
print(Kisi.bilgilerini_goster(kisi2))
print(Kisi.kisi_sayisi_goster())


kisi3 = Kisi.string_ile_olustur("cemal-24-51000-mühendis")
print(kisi3.bilgilerini_goster())
print(kisi3.eposta)

print(Kisi.kisi_sayisi_goster())

#kisi4 = Kisi.dogum_yili_ile_göster("naci", 1951)
#print(Kisi.kisi_sayisi_goster())

#print(kisi4.isim, kisi4.yas)
#print()

print(kisi1.zam_orani)
print(kisi1.zam_orani_degistir(1.6))
print()

kisi5 = Kisi.string_ile_olustur("caner-47-53000-doktor")
print(kisi5.bilgilerini_goster())

print(Kisi.maas_arttir(kisi5.isim, kisi5.maas))

print(Kisi.selamla())

print(Kisi.ugurla())


#print(Kisi.kisi_sayisi)
#kisi1 = Kisi("ali", 32)
#kisi2 = Kisi("veli", 38)
#print(kisi1.isim)
#print(kisi1.yas)
#print(kisi2.isim)
#print(kisi2.yas)
#print(Kisi.zam_orani)
#print(Kisi.kisi_sayisi)

'''

'''
data = [
    {
        "name" : "a1",
        "page" : 100
    },
     {
        "name" : "a2",
        "page" : 150
    },
     {
        "name" : "a3",
        "page" : 200
    }
]

class Book:
    def __init__(self, name, page):
        self.name = name
        self.page = page
    
    @classmethod
    def from_list(cls, veri):
        books = []
        for i in veri:
            books.append(cls(name = i["name"], page = i["page"]))
        return books
            

kitaplar = Book.from_list(data)
print(kitaplar)
print(kitaplar[0].name)
print(kitaplar[0].page)

'''

'''
data = [
    {
        "isim" : "john",
        "soyisim" : "medley",
        "yas" : 56
    },
    {
        "isim" : "thomas",
        "soyisim" : "bradley",
        "yas" : 62
    },

]

class Kisi:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    @classmethod
    def liste(cls, veri):
        kisiler = []
        for i in veri:
            kisiler.append(cls(name = i["isim"], surname = i["soyisim"], age = i["yas"]))
        return kisiler

people = Kisi.liste(data)
print(people[0].name)
print(people[0].surname)
print(people[0].age)

'''

'''
class Calisan:
    zam_orani = 1.1
    personel_sayisi = 0

    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = f"{ad}.{soyad}@gmail.com"
        Calisan.personel_sayisi += 1
    
    def tam_isim(self):
        return f"adı = {self.ad} soyadı = {self.soyad}"
    
    def maas_arttir(self):
        self.maas = self.maas * self.zam_orani
    
    @classmethod
    def zam_orani_degistir(cls, yeni_oran):
        cls.zam_orani = yeni_oran
    
    @classmethod
    def string_personel(cls, personel_bilgisi):
        name, surname, salary = personel_bilgisi.split("-")
        return cls(name, surname, salary)

    @staticmethod
    def tel_no(telefon):
        phone_number =  telefon.split("-")
        return " ".join(phone_number)
    
    @staticmethod
    def adres(address):
        adr = address.split(".")
        return " ".join(adr)

        
per_1 = Calisan("selim", "emir", 30000)
per_2 = Calisan("vedat", "akyüz", 40000)

metinsel_personel_3 = "umutcan-aydın-33000"

yeni_personel_3 = Calisan.string_personel(metinsel_personel_3)
print(yeni_personel_3.eposta)
#print(Calisan.personel_sayisi)

phone = "0834-111-11-11"
print(Calisan.tel_no(phone))

adresi = "türkiye.ankara.çankaya.mahallesi.ulus.sokak.sincan.caddesi"
print(Calisan.adres(adresi))


Calisan.zam_orani_degistir(1.2)

#per_1.maas_arttir()
#print(per_1.maas)
#print()
#per_2.maas_arttir()
#print(per_2.maas)

#print(Calisan.personel_sayisi)
#per_1.maas_arttir()
#print(per_1.maas)
#per_2.maas_arttir()
#print(per_2.maas)

'''

'''
class Ucus:
    havayolu = "THY"

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu
    
    def anons_yap(self):
        return f"{self.kod} sefer sayılı {self.kalkis}-{self.varis} uçuşumuz {self.sure} dakika sürecektir."

#ucus1 = Ucus()
#print(ucus1.havayolu)

ucus2 = Ucus("TK-153", "izmir", "antalya", 40, 300, 50)

print(f"uçuş-2 bilgileri kod = {ucus2.kod} kalkış yeri = {ucus2.kalkis} varış yeri = {ucus2.varis} süresi = {ucus2.sure} kapasitesi = {ucus2.kapasite} yolcu sayısı = {ucus2.yolcu}")
print()

print(ucus2.havayolu)
print("__" * 200)

ucus3 = Ucus("TK-247", "ankara", "adana", 35, 250, 250)
print(ucus3.havayolu)
print(ucus3.kod)
print(ucus3.kalkis)
print(ucus3.varis)
print(ucus3.sure)
print(ucus3.kapasite)
print(ucus3.yolcu)

print("__" * 200)

print(ucus3.anons_yap())
print()
print(ucus3.__dict__)

'''

'''
class Ucus:
    havayolu = "THY"

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu
    
    
    def anons_yap(self):
        return f"{self.kod} sefer sayılı {self.kalkis}-{self.varis} uçuşumuz {self.sure} dakika sürecektir."

    
    def koltuk_sayisi_guncelle(self):
        return f"uçaktaki boş koltuk sayısı = {self.kapasite - self.yolcu} adettir."
    
    
    def bilet_satis(self, bilet_adedi):
        
        if self.yolcu + bilet_adedi <= self.kapasite:
            self.yolcu += bilet_adedi
            return f"{bilet_adedi} adet bilet satılmıştır. {self.koltuk_sayisi_guncelle()}"
        else:
            return f"işlem gerçekleştirilemedi."
    

    def bilet_iptal(self, bilet_adedi):
        if self.yolcu >= bilet_adedi:
            self.yolcu -= bilet_adedi
            return f"{bilet_adedi} adet bilet iptal edilmiştir. {self.koltuk_sayisi_guncelle()}"
        else:
            return f"işlem gerçekleştirilemedi."




ucus1 = Ucus("TK-182", "istanbul", "mersin", 50, 300, 200)

print(ucus1.koltuk_sayisi_guncelle())
print()
print(ucus1.bilet_satis(10))
print()
print(ucus1.bilet_satis(20))
print()
print(ucus1.bilet_satis(75))
print()
print(ucus1.bilet_iptal(25))
print()
print(ucus1.bilet_iptal(35))
print()
print(ucus1.bilet_iptal(170))

'''

'''
class Seyahat:
    def __init__(self, kalkis, varis):
        self.kalkis = kalkis
        self.varis = varis
    
    def anons(self):
        return f"{self.kalkis} {self.varis} seyahatine hoşgeldiniz."
    

class Otobus(Seyahat):
    def __init__(self, kalkis, varis, mola_duraklari):
        Seyahat.__init__(self, kalkis, varis)
        self.mola_duraklari = mola_duraklari


class Gemi(Seyahat):
    def __init__(self, kalkis, varis, yapim_yili, hiz):
        Seyahat.__init__(self, kalkis, varis)
        self.yapim_yili = yapim_yili
        self.hiz = hiz

seyahat1 = Seyahat("istanbul", "erzurum")
print(seyahat1.anons())
print(seyahat1.kalkis)
print(seyahat1.varis)
print("__"*50)

oto1 = Otobus(["ankara", "adana", "kayseri"], "istanbul", "erzurum")
print(oto1.anons())
print(oto1.kalkis)
print(oto1.varis)
print(oto1.mola_duraklari)
print("__"*50)

gemi1 = Gemi("türkiye", "hollanda", 1945, 20)
print(gemi1.anons())
print(gemi1.hiz)
print(gemi1.yapim_yili)
print(gemi1.kalkis)
print(gemi1.varis)
print("__"*50)

print(isinstance(oto1, Gemi))
print(isinstance(oto1, Otobus))
print(isinstance(oto1, Seyahat))
print(isinstance(gemi1, Seyahat))
print(isinstance(gemi1, Gemi))
print(isinstance(gemi1, Otobus))
print(issubclass(Otobus, Seyahat))
print(issubclass(Gemi, Seyahat))
print(issubclass(Gemi, Otobus))
print(issubclass(Otobus, Gemi))

'''

'''
class Calisan:
    zam_orani = 1.2

    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.eposta = isim + soyisim + "@firma.com"
    
    def bilgileri_goster(self):
        return f"ad = {self.isim} soyad = {self.soyisim} maaş = {self.maas} email = {self.eposta}"

calisan1 = Calisan("kerem", "demir", 23000)
calisan2 = Calisan("kazım", "çelik", 25000)

#print(calisan1.eposta)
#print(calisan2.eposta)

class Yazilimci(Calisan):
    zam_orani = 1.3
    
    def __init__(self, isim, soyisim, maas, bildigi_diller = None):
        super().__init__(isim, soyisim, maas)
        if bildigi_diller == None:
            self.bildigi_diller = []
        else:
            self.bildigi_diller = bildigi_diller

    
    def bilgileri_goster(self):
         return f"ad = {self.isim} soyad = {self.soyisim} maaş = {self.maas} email = {self.eposta} dil = {self.bildigi_diller}"

    
    def bildigi_dili_söyle(self):
        return f"{self.isim} {self.soyisim} adlı yazılımcının bildiği diller = {self.bildigi_diller}"
    
    
    def zam_yap(self):
        eski_maas = self.maas
        yeni_maas = eski_maas * self.zam_orani
        return f"{self.isim} {self.soyisim} adlı yazılımcının eski maaşı = {self.maas} olup yeni maaşı = {yeni_maas}"
    
    
    def yeni_dil_ekle(self, yeni_dil):
        if yeni_dil not in self.bildigi_diller:
           self.bildigi_diller.append(yeni_dil)
           return yeni_dil
    

    def dil_sil(self, dil_ismi):
        for i in self.bildigi_diller:
            if dil_ismi == i:
                self.bildigi_diller.remove(dil_ismi)
        return f"silinen dil = {dil_ismi}"
        


yazilimci1 = Yazilimci("serkan", "ateş", 45000, ["python"])
yazilimci2 = Yazilimci("erkan", "alev", 48000, "java")
yazilimci3 = Yazilimci("ayhan", "şen", 47000)
yazilimci4 = Yazilimci("fikret", "demir", 50000, ["php","javascript"])


class Yonetici(Calisan):
    zam_orani = 1.5

    def __init__(self, isim, soyisim, maas, calisanlar = None):
        super().__init__(isim, soyisim, maas)
        if calisanlar == None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar
    
    
    def bilgileri_goster(self):
        return f"ad = {self.isim} soyad = {self.soyisim} maaş = {self.maas} email = {self.eposta}"
    
    
    def calisan_ekle(self, calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)
    
    
    def calisan_sil(self, calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)
    
    
    def calisanlari_goster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgileri_goster())
    

    def zam_yap(self):
        eski_maas = self.maas
        yeni_maas = eski_maas * self.zam_orani
        return f"{self.isim} {self.soyisim} adlı yöneticinin eski maaşı = {self.maas} olup yeni maaşı = {yeni_maas}"
    
    

yonetici1 = Yonetici("alper", "bayraktar", 85000, [yazilimci1, yazilimci2, yazilimci3, yazilimci4])
yonetici1.calisanlari_goster()
print("__" * 50)

yonetici2 = Yonetici("şevki", "ertuğ", 88000)
yonetici2.calisan_ekle(calisan1)
yonetici2.calisan_ekle(calisan2)
yonetici2.calisanlari_goster()
print("__" * 50)

'''


#yonetici1 = Yonetici("haydar", "kaan", 78000)
#yonetici1.calisan_ekle(calisan1)
#yonetici1.calisan_ekle(yazilimci1)
#
#yonetici1.calisanlari_goster()
#print("__" * 20)
#
#yonetici1.calisan_sil(calisan1)
#yonetici1.calisanlari_goster()
#print("__"* 100)
#
#yonetici2 = Yonetici("harun", "albayrak", 82000, [yazilimci1, yazilimci2, calisan2])
#yonetici2.calisanlari_goster()
#print(yonetici2.bilgileri_goster())
#print()
#
#yonetici2.calisan_ekle(calisan1)
#yonetici2.calisanlari_goster()
#print("__"*20)
#
#yonetici2.calisan_sil(yazilimci1)
#yonetici2.calisanlari_goster()
#print("__"*20)
#
#yonetici2.calisan_sil(yazilimci2)
#yonetici2.calisanlari_goster()
#print("__"*20)
#
#yonetici2.calisan_sil(calisan1)
#yonetici2.calisanlari_goster()
#print("__"*20)
#
#yonetici2.calisan_sil(calisan2)
#yonetici2.calisanlari_goster()
#print()
#
#print(yonetici1.zam_orani)
#print("__"*100)
#
#print(yazilimci1.zam_yap())
#print()
#print(yazilimci2.zam_yap())
#print("__"*100)
#
#print(yonetici1.zam_yap())
#print()
#print(yonetici2.zam_yap())
#print("__"*100)
#
#print(yazilimci3.bildigi_dili_söyle())
#print()
#print(yazilimci4.bildigi_dili_söyle())
#print("__"*50)
#
#print(yazilimci3.yeni_dil_ekle(["c#", "c++", "c", "java", "php"]))
#print(yazilimci3.bildigi_dili_söyle())
#print("__"*50)
#
#print(yazilimci1.yeni_dil_ekle("ruby"))
#print(yazilimci1.bildigi_dili_söyle())
#print("__"*50)
#
#print(yazilimci1.yeni_dil_ekle("python"))
#print(yazilimci1.bildigi_dili_söyle())
#
#print("__"*50)
#
#print(yazilimci1.yeni_dil_ekle("javascript"))
#print(yazilimci1.bildigi_dili_söyle())
#
#print("__"*50)
#
#print(yazilimci1.dil_sil("python"))
#print(yazilimci1.bildigi_dili_söyle())
#
#print("__"*50)
#
#print(yazilimci4.bildigi_dili_söyle())
#print(yazilimci4.bildigi_diller)
#print(yazilimci4.dil_sil("javascript"))
#print(yazilimci4.bildigi_dili_söyle())
#print(yazilimci4.bildigi_diller)
#
#print("__"*50)

'''
class Personel:

    zam_orani = 1.1

    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.eposta = f"{isim}.{soyisim}@sirket.com"
    
    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"
    
    def zam_uygula(self):
        self.maas = self.maas * self.zam_orani

class Yazilimci(Personel):
    zam_orani = 1.2

    def __init__(self, isim, soyisim, maas, programlama_dili):
        super().__init__(isim, soyisim, maas)
        self.programlama_dili = programlama_dili


yaz_1 = Yazilimci("murat", "saka", 46000, "php")
yaz_2 = Yazilimci("burak", "gelebe", 48000, "c++")
yaz_3 = Yazilimci("selim", "şen", 51000, "python")
yaz_4 = Yazilimci("ayten", "uğurlu", 52000, "ruby")
yaz_5 = Yazilimci("meltem", "gören", 55000, "java")
yaz_6 = Yazilimci("ayşe", "demirci", 57000, "c#")


class Mudur(Personel):
    def __init__(self, isim, soyisim, maas, personeller = None):
        super().__init__(isim, soyisim, maas)
        if personeller == None:
            self.personeller = []
        else:
            self.personeller = personeller
    

    def personel_ekle(self, per):
        if per not in self.personeller:
            self.personeller.append(per)
    
    
    def personel_cikar(self, per):
        if per in self.personeller:
            self.personeller.remove(per)
    

    def personeller_listele(self):
        for per in self.personeller:
            print(per.tam_isim())
    



mdr1 = Mudur("oğuz", "taner", 85000, [yaz_1, yaz_2, yaz_3])
mdr2 = Mudur("ekrem", "balcı", 88000)

print(mdr2.eposta)
print("__"*20)
print(mdr2.tam_isim())
print("__"*20)
mdr2.personeller_listele()
print("__"*20)
mdr2.personel_ekle(yaz_4)
print("__"*20)
mdr2.personeller_listele()
mdr2.personel_ekle(yaz_5)
print("__"*20)
mdr2.personeller_listele()
mdr2.personel_ekle(yaz_6)
print("__"*20)
mdr2.personeller_listele()




#print(mdr1.tam_isim())
#print("__"*20)
#mdr1.personeller_listele()
#print("__"*20)
#mdr1.personel_ekle(yaz_4)
#print("__"*20)
#mdr1.personeller_listele()
#print("__"*20)
#mdr1.personel_cikar(yaz_1)
#print("__"*20)
#mdr1.personeller_listele()

#print(mdr1.eposta)
#print(mdr2.eposta)

#print(yaz_1.programlama_dili)
#print(yaz_2.programlama_dili)
#print(yaz_1.eposta)
#print(yaz_2.eposta)

#print(yaz_1.eposta)
#print(yaz_2.eposta)
#print(yaz_1.tam_isim())
#print(yaz_2.tam_isim())
#yaz_1.zam_uygula()
#print(yaz_1.maas)
#yaz_2.zam_uygula()
#print(yaz_2.maas)

#print(yazilimci1.eposta)
#print(yazilimci2.eposta)

#print(calisan1.zam_orani)
#print(yazilimci1.zam_orani)

#print(calisan1.bilgileri_goster())
#print(calisan2.bilgileri_goster())
#print(calisan1.zam_orani)
#print(calisan2.zam_orani)
#print()
#print(yazilimci1.bilgileri_goster())
#print(yazilimci2.bilgileri_goster())
#print(yazilimci1.zam_orani)
#print(yazilimci2.zam_orani)
#print()
#print(yazilimci1.bildigi_dili_söyle())
#print(yazilimci2.bildigi_dili_söyle())

'''

'''
class Person:
    def __init__(self, name, lastname):
        self.isim = name
        self.soyisim = lastname

    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"
    
    def eposta(self):
        return f"{self.isim}.{self.soyisim}@gmail.com"

class Student(Person):
    def __init__(self, name, lastname):
        super().__init__(name, lastname)
       

p1 = Person("kaan", "şener")
s1 = Student("tamer", "ayas")

#print(f"{p1.isim} {p1.soyisim}")
#print("__"*10)
#print(f"{s1.isim} {s1.soyisim}")
#print("__"*10)

print(p1.tam_isim())
print("__"*10)
print(s1.tam_isim())
print("__"* 100)
print(p1.eposta())
print("__"*10)
print(s1.eposta())

'''



'''
class Ogretmen:
    zam_orani = 1.5
    maas = 50000
    ogrenci_sayisi = 0
    devamsizlik_günü = ""
    maas_kesinti = ""
    harclik_verilen_miktar = ""
    prim_miktari = ""
    
    
    def __init__(self, adi, soyadi, bölümü, yas, ogrenciler = None):
        self.adi = adi
        self.soyadi = soyadi
        self.bölümü = bölümü
        self.yas = yas
        if ogrenciler == None:
            self.ogrenciler = []
        else:
            self.ogrenciler = ogrenciler
        
       
        
    def tam_isim(self):
        return f"{self.adi} {self.soyadi}"
    
    
    def eposta(self):
        return f"{self.adi}_{self.soyadi}.okulum@hotmail.com"
    
    
    def bilgileri_goster(self):
        return f"{self.adi} {self.soyadi} isimli öğretmenin bölümü = {self.bölümü} yaşı = {self.yas}"
    
    
    def maas_zam(self):
        eski_maas = self.maas
        yeni_maas = eski_maas * self.zam_orani
        return f"{self.adi} {self.soyadi} isimli öğretmenin eski maaşı {self.maas} tl olup zamlı maaşı {yeni_maas} tl dir."
    
    
    @classmethod
    def maas_kesintisi(cls, kesinti, gün):
        cls.maas_kesinti = kesinti
        cls.devamsizlik_günü = gün
        if cls.maas >= (kesinti * gün):
            kesintili_maas = cls.maas - (kesinti * gün)
            return f"öğretmenin kesintili maaşı = {kesintili_maas} tl"
        else:
            return "kesintili maaş öğretmenin maaşından az olamaz!"
    
    
    @classmethod
    def harclik_ver(cls, harclik_miktari):
        cls.harclik_verilen_miktar = harclik_miktari
        if cls.maas >= harclik_miktari:
            harclik_verdikten_sonra_kalan_maas = cls.maas - harclik_miktari
            return f"öğretmenin harçlık verdikten sonra kalan maaşı = {harclik_verdikten_sonra_kalan_maas} tl"
        else:
            return f"harçlık verilmek istenen miktar öğretmenin maaşından fazla olamaz!"
    
    
    @classmethod
    def prim_göster(cls, prim):
        cls.prim_miktari = prim
        if prim <= cls.maas * 0.20:
            prim_aldıktan_sonraki_maas = cls.maas + prim
            return f"öğretmenin aldığı prim = {prim} tl olup prim aldıktan sonraki maaşı = {prim_aldıktan_sonraki_maas} tl"
        else:
            return f"prim miktarı öğretmenin maaşının yüzde 20 sinden fazla olamaz!"
    
    
    def ogrenci_ekle(self, ogrenci):
        if ogrenci not in self.ogrenciler:
            self.ogrenciler.append(ogrenci)
            Ogretmen.ogrenci_sayisi += 1
    
    
    def ogrenci_sil(self, ogrenci):
        if ogrenci in self.ogrenciler:
            self.ogrenciler.remove(ogrenci)
            Ogretmen.ogrenci_sayisi -= 1
        
    
    
    def ogrencileri_goster(self):
        for ogrenci in self.ogrenciler:
            print(f"mevcut öğrencinin ismi = {ogrenci.tam_isim()}")
    

    
    def ogrenci_sayisini_goster(self):
        return f"öğrenci sayısı = {len(self.ogrenciler)}"
    



class Ogrenci(Ogretmen):
    harclik = ""
    vize_notu = ""
    final_notu = ""
    not_ortalamasi = ""
    devamsizlik_günü = ""
    
    
    def __init__(self, adi, soyadi, bölümü, yas, hobiler = None):
        super().__init__(adi, soyadi, bölümü, yas)
        if hobiler == None:
            self.hobiler = []
        else:
            self.hobiler = hobiler
        
        
    def bilgileri_goster(self):
        return f"{self.adi} {self.soyadi} isimli öğrencinin bölümü = {self.bölümü} yaşı = {self.yas}"
    
    
    def not_ortalamasi_hesapla(self, vize, final):
        self.vize_notu = vize
        self.final_notu = final
        self.not_ortalamasi = (vize * 0.40) + (final * 0.60)
        if  0 <= self.not_ortalamasi < 50:
            return f"{self.tam_isim()} adlı öğrencinin not ortalaması = {self.not_ortalamasi} olup öğrenci sınıfta kalmıştır."
        if 50 <= self.not_ortalamasi <= 100:
            return f"{self.tam_isim()} adlı öğrencinin not ortalaması = {self.not_ortalamasi} olup öğrenci sınıfı geçmiştir."
    
    
    def harclik_al(self, alinan_harclik):
        if alinan_harclik <= self.maas:
            self.harclik_ver(alinan_harclik)
            self.harclik = alinan_harclik
            return f"{self.tam_isim()} adlı öğrencinin mevcut durumdaki harçlığı {self.harclik} tl dir. {self.harclik_ver(alinan_harclik)} dir."
    
    
    def hobi_ekle(self, hobi):
        if hobi not in self.hobiler:
            self.hobiler.append(hobi)
    
    def hobileri_listele(self):
        return f"{self.tam_isim()} adlı öğrencinin hobileri = {self.hobiler}"
    
    def devamsizlik_durumu(self, devamsizlik):
        self.devamsizlik_günü = devamsizlik
        if devamsizlik >= 20:
            return f"{self.tam_isim()} adlı öğrencinin devamsızlık gün sayısı {self.devamsizlik_günü} gündür. devamsızlık günü 20 ye eşit yada 20 den fazla olduğu için sınıf tekrarı yapacaktır."
        if 0 <= devamsizlik < 20:
            return f"{self.tam_isim()} adlı öğrencinin devamsızlık gün sayısı {self.devamsizlik_günü} gündür. kalan gün sayısı {20 - self.devamsizlik_günü} gündür."
            

        
ogrenci1 = Ogrenci("necdet", "yaman", "türkçe", 19, ["kitap okuma", "müzik", "bilgisayar oyunu"])
ogrenci2 = Ogrenci("halil", "doğan", "fizik", 18)
ogrenci3 = Ogrenci("salim", "eroğlu", "kimya", 21)
ogrenci4 = Ogrenci("mehmet", "alptekin", "edebiyat", 17, ["film izlemek", "resim yapmak", "fotoğraf çekmek"])
ogrenci5 = Ogrenci("ali", "sevim", "biyoloji", 20)
ogrenci6 = Ogrenci("burak", "aydın", "coğrafya", 22, ["tenis", "doğa yürüyüşü", "kamp yapmak", "dil öğrenmek"])
ogrenci7 = Ogrenci("samet", "çerkez", "felsefe", 23)

print(ogrenci1.bilgileri_goster())

print("__"*100)

ogretmen1 = Ogretmen("ayhan", "şeker", "matematik", 45)

print(ogretmen1.maas_zam())
print(ogretmen1.maas_kesintisi(3000, 10))
print(ogretmen1.harclik_ver(4000))
print(ogretmen1.prim_göster(10000))
ogretmen1.ogrenci_ekle(ogrenci1)
ogretmen1.ogrenci_ekle(ogrenci2)
ogretmen1.ogrenci_ekle(ogrenci3)
ogretmen1.ogrenci_ekle(ogrenci4)
ogretmen1.ogrencileri_goster()
print(ogretmen1.ogrenci_sayisini_goster())
print("__"*20)
ogretmen1.ogrenci_sil(ogrenci2)
ogretmen1.ogrencileri_goster()
print(ogretmen1.ogrenci_sayisini_goster())
print("__"*20)
ogretmen1.ogrenci_sil(ogrenci4)
ogretmen1.ogrencileri_goster()
print(ogretmen1.ogrenci_sayisini_goster())
print("__"*100)

ogretmen2 = Ogretmen("ogün", "eryaman", "geometri", 51)

print(ogretmen2.tam_isim())
print(ogretmen2.eposta())
print(ogretmen2.bilgileri_goster())
print(ogretmen2.maas_zam())
print(ogretmen2.maas_kesintisi(2000, 8))
print(ogretmen2.harclik_ver(13000))
print(ogretmen2.prim_göster(8000))
print("__"*20)
ogretmen2.ogrenci_ekle(ogrenci5)
ogretmen2.ogrenci_ekle(ogrenci6)
ogretmen2.ogrenci_ekle(ogrenci7)
ogretmen2.ogrencileri_goster()
print()
print(ogretmen2.ogrenci_sayisini_goster())
print(ogretmen1.ogrenci_sayisini_goster())
print("__"*30)
ogretmen1.ogrenci_ekle(ogrenci5)
ogretmen1.ogrenci_ekle(ogrenci6)
ogretmen1.ogrenci_ekle(ogrenci7)
ogretmen1.ogrencileri_goster()
print(ogretmen1.ogrenci_sayisini_goster())
print("__"*30)
ogretmen2.ogrencileri_goster()
print(ogretmen2.ogrenci_sayisini_goster())
print("__"*30)
ogretmen1.ogrenci_sil(ogrenci1)
ogretmen1.ogrenci_sil(ogrenci3)
ogretmen1.ogrenci_sil(ogrenci5)
ogretmen1.ogrenci_sil(ogrenci6)
ogretmen1.ogrenci_sil(ogrenci7)
ogretmen1.ogrencileri_goster()
print(ogretmen1.ogrenci_sayisini_goster())
print("__"*30)
ogretmen2.ogrencileri_goster()
print(ogretmen2.ogrenci_sayisini_goster())
print("__"*30)
ogretmen2.ogrenci_sil(ogrenci5)
ogretmen2.ogrenci_sil(ogrenci6)
ogretmen2.ogrenci_sil(ogrenci7)
ogretmen2.ogrencileri_goster()
print(ogretmen2.ogrenci_sayisini_goster())
print("__"*100)
ogretmen1.ogrencileri_goster()
print(ogretmen1.ogrenci_sayisini_goster())
print()
ogretmen2.ogrencileri_goster()
print(ogretmen2.ogrenci_sayisini_goster())
print("__"*50)

ogretmen1.ogrenci_ekle(ogrenci1)
ogretmen1.ogrenci_ekle(ogrenci2)
ogretmen1.ogrenci_ekle(ogrenci3)
ogretmen1.ogrencileri_goster()
print(ogretmen1.ogrenci_sayisini_goster())
print("__"*10)
ogretmen2.ogrenci_ekle(ogrenci4)
ogretmen2.ogrenci_ekle(ogrenci5)
ogretmen2.ogrenci_ekle(ogrenci6)
ogretmen2.ogrenci_ekle(ogrenci7)
ogretmen2.ogrencileri_goster()
print(ogretmen2.ogrenci_sayisini_goster())
print("__"*100)

ogretmen1.ogrenci_ekle(ogrenci1)
ogretmen1.ogrenci_ekle(ogrenci2)
ogretmen1.ogrenci_ekle(ogrenci3)
ogretmen1.ogrenci_ekle(ogrenci4)
ogretmen1.ogrenci_ekle(ogrenci5)
ogretmen1.ogrenci_ekle(ogrenci6)
ogretmen1.ogrenci_ekle(ogrenci7)
ogretmen1.ogrencileri_goster()
print(ogretmen1.ogrenci_sayisini_goster())
print("__"*10)
ogretmen2.ogrenci_ekle(ogrenci1)
ogretmen2.ogrenci_ekle(ogrenci2)
ogretmen2.ogrenci_ekle(ogrenci3)
ogretmen2.ogrenci_ekle(ogrenci4)
ogretmen2.ogrenci_ekle(ogrenci5)
ogretmen2.ogrenci_ekle(ogrenci6)
ogretmen2.ogrenci_ekle(ogrenci7)
ogretmen2.ogrencileri_goster()
print(ogretmen2.ogrenci_sayisini_goster())
print("__"*100)

ogretmen1.ogrenci_sil(ogrenci1)
ogretmen1.ogrenci_sil(ogrenci2)
ogretmen1.ogrenci_sil(ogrenci3)
ogretmen1.ogrenci_sil(ogrenci4)
ogretmen1.ogrencileri_goster()
print(ogretmen1.ogrenci_sayisini_goster())
print("__"*10)
ogretmen2.ogrenci_sil(ogrenci3)
ogretmen2.ogrenci_sil(ogrenci4)
ogretmen2.ogrenci_sil(ogrenci5)
ogretmen2.ogrenci_sil(ogrenci6)
ogretmen2.ogrenci_sil(ogrenci7)
ogretmen2.ogrencileri_goster()
print(ogretmen2.ogrenci_sayisini_goster())
print("__"*100)

print(ogrenci1.not_ortalamasi_hesapla(60, 80))
print(ogrenci2.not_ortalamasi_hesapla(20, 50))
print(ogrenci3.not_ortalamasi_hesapla(100, 100))
print(ogrenci4.not_ortalamasi_hesapla(0, 0))
print(ogrenci5.not_ortalamasi_hesapla(50, 50))
print(ogrenci6.not_ortalamasi_hesapla(79, 30))
print("__"*100)

print(ogrenci1.harclik_al(12000))
print(ogrenci2.harclik_al(13000))
print("__"*10)

print(ogrenci1.hobiler)
print()
ogrenci2.hobi_ekle(["bisiklet binme", "seyahat", "kitap okuma"])
print(ogrenci2.hobileri_listele())
print()
ogrenci3.hobi_ekle(["futbol", "basketbol", "voleybol"])
print(ogrenci3.hobileri_listele())
print()

print(ogrenci4.hobileri_listele())
ogrenci4.hobi_ekle("enstrüman çalmak")
print(ogrenci4.hobileri_listele())
print()

print(ogrenci5.hobileri_listele())
ogrenci5.hobi_ekle(["yemek yapmak", "dans etmek", "yüzme", "koşu yapmak"])
print(ogrenci5.hobileri_listele())
print(ogrenci5.hobiler)
print()

print(ogrenci6.hobileri_listele())
ogrenci6.hobi_ekle("tiyatro")
ogrenci6.hobi_ekle("kayak yapmak")
ogrenci6.hobi_ekle("dövüş sanatları")
print(ogrenci6.hobileri_listele())
print("__"*100)

print(ogrenci1.devamsizlik_durumu(12))
print(ogrenci2.devamsizlik_durumu(16))
print(ogrenci3.devamsizlik_durumu(22))
print(ogrenci4.devamsizlik_durumu(20))
print(ogrenci5.devamsizlik_durumu(28))
print(ogrenci6.devamsizlik_durumu(5))

'''

'''
class Kare:
    def __init__(self):
        print("kare işlemleri")

class Kare_Alan(Kare):
    def __init__(self):
        super().__init__()
        print("karenin alanı")
    
    def kare_alan_hesapla(self, kenar):
        return kenar * kenar

kare_alan1 = Kare_Alan()
print(kare_alan1.kare_alan_hesapla(8))

class Kare_Cevre(Kare):
    def __init__(self):
        super().__init__()
        print("karenin çevresi")
    
    def kare_cevre_hesapla(self, kenar):
        return kenar * 4

kare_cevre1 = Kare_Cevre()
print(kare_cevre1.kare_cevre_hesapla(9))

class Daire:
    def __init__(self):
        print("daire işlemleri")

class Daire_Alan(Daire):
    def __init__(self):
        super().__init__()
        print("dairenin alanı")
    
    def daire_alan_hesapla(self, pi, r):
        return pi * r * r

daire_alan = Daire_Alan()

print(daire_alan.daire_alan_hesapla(3.14, 12))

class Daire_Cevre(Daire):
    def __init__(self):
        super().__init__()
        print("dairenin çevresi")
    
    def daire_cevre_hesapla(self, pi, r):
        return 2 * pi * r

daire_cevre = Daire_Cevre()

print(daire_cevre.daire_cevre_hesapla(3.14, 15))

class Dört_islem:
    
    def __init__(self):
        print("dört işlem başlıyor..")

class Toplama(Dört_islem):
    def __init__(self):
        super().__init__()
        print("toplama işlemi")
    
    def toplama_yap(self, sayi1, sayi2):
        return sayi1 + sayi2

topla1 = Toplama()

print(topla1.toplama_yap(12, 14))

class Cikarma(Dört_islem):
    def __init__(self):
        super().__init__()
        print("çıkarma işlemi")
    
    def cikarma_yap(self, sayi1, sayi2):
        return sayi1 - sayi2

cikar1 = Cikarma()

print(cikar1.cikarma_yap(24, 28))

class Carpma(Dört_islem):
    def __init__(self):
        super().__init__()
        print("çarpma işlemi")
    
    def carpma_yap(self, sayi1, sayi2):
        return sayi1 * sayi2

carp1 = Carpma()

print(carp1.carpma_yap(12, 20))

class Bolme(Dört_islem):
    def __init__(self):
        super().__init__()
        print("bölme işlemi")
    
    def bolme_yap(self, sayi1, sayi2):
        return sayi1 / sayi2

böl1 = Bolme()

print(böl1.bolme_yap(60, 5))

'''

class Sporcu:
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim
        

class Futbolcu(Sporcu):
    boy = ""
    kilo = ""
    gol_sayisi = ""
    asist_sayisi = ""
    maas = ""
    transfer_ücreti = ""
    zam_orani = ""
    kosma_hizi = ""
    sut_cekme_hizi = ""
    yeni_takimi = ""
    tüm_bilgileri_göster = []
    futbolcular_listesi = []


    def __init__(self, isim, soyisim, kulübü):
        super().__init__(isim, soyisim)
        self.kulübü = kulübü
    
    
    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"
    
    
    def vücut_kitle_endeksi_hesapla(self, kilosu, boyu):
        result = kilosu / (boyu ** 2)
        self.tüm_bilgileri_göster.append(f"futbolcunun vücut kitle endeksi = {result}")
        return f"{self.tam_isim()} adlı futbolcunun vücut kitle indeksi = {result}"
    

    
    def piyasa_degeri(self, maasi, gol, asisti):
        self.maas = maasi
        self.gol_sayisi = gol
        self.asist_sayisi = asisti
        piyasa_degeri = maasi * (gol + asisti)
        self.tüm_bilgileri_göster.append(f"futbolcunun piyasa değeri = {piyasa_degeri}")
        return f"{self.tam_isim()} adlı futbolcunun piyasa değeri = {piyasa_degeri} dolardır."
    

    
    def mac_basina_gol_ortalamasi(self, oynadiği_mac, gol_sayi):
        if oynadiği_mac > 0:
            self.gol_sayisi = gol_sayi
            gol_ortalama = self.gol_sayisi / oynadiği_mac
            self.tüm_bilgileri_göster.append(f"futbolcunun maç başına gol ortalaması = {gol_ortalama}")
            return f"{self.tam_isim()} adlı futbolcunun maç başına gol ortalaması {gol_ortalama}"
        else:
            return f"oynadığı maç sayısı 0 yada 0 dan küçük olamaz!"
    

    
    def mac_basina_asist_ortalamasi(self, oynadiği_mac, asist_sayi):
        if oynadiği_mac > 0:
            self.asist_sayisi = asist_sayi
            asist_ortalama = self.asist_sayisi / oynadiği_mac
            self.tüm_bilgileri_göster.append(f"futbolcunun maç başına asist ortalaması = {asist_ortalama}")
            return f"{self.tam_isim()} adlı futbolcunun maç başına asist ortalaması {asist_ortalama}"
        else:
            return f"oynadığı maç sayısı 0 yada 0 dan küçük olamaz!"
        
            
    
    def transfer_ücreti_göster(self, maasi, gol, asisti, pazarlik_payi):
        piyasa_degeri = maasi * (gol + asisti)
        if pazarlik_payi <= piyasa_degeri / 20:
            gecici_ücret = piyasa_degeri - pazarlik_payi
            self.transfer_ücreti = gecici_ücret
            self.tüm_bilgileri_göster.append(f"futbolcunun transfer ücreti = {self.transfer_ücreti} dolardır.")
            return f"{self.tam_isim()} adlı futbolcunun transfer ücreti = {self.transfer_ücreti} dolardır."
        else:
            return "pazarlık payı piyasa değerinin yirmide birinden fazla olamaz!"
    
    
    
    def maasina_zam_yap(self, maasi, zammi):
        self.maas = maasi
        self.zam_orani = zammi
        zamli_maasi = maasi * zammi
        self.tüm_bilgileri_göster.append(f"futbolcunun zamlı maaşı = {zamli_maasi}")
        return f"{self.tam_isim()} adlı futbolcunun zamlı maaşı {zamli_maasi} dolardır."
    
    
    
    def hizini_arttir(self, hiz, hiz_artis_yüzdesi):
        self.kosma_hizi = hiz
        yeni_kosma_hizi = hiz * hiz_artis_yüzdesi
        self.tüm_bilgileri_göster.append(f"futbolcunun yeni koşma hızı = {yeni_kosma_hizi}")
        return f"{self.tam_isim()} adlı futbolcunun eski koşma hızı {self.kosma_hizi} km/s olup yeni koşma hızı {yeni_kosma_hizi} km/s olmuştur."
    
    
    
    def sut_cekme_hizini_arttir(self, sut_hizi, sut_hizi_artis_yüzdesi):
        self.sut_cekme_hizi = sut_hizi
        yeni_sut_hizi = sut_hizi * sut_hizi_artis_yüzdesi
        self.tüm_bilgileri_göster.append(f"futbolcunun yeni_sut_hizi = {yeni_sut_hizi}")
        return f"{self.tam_isim()} adlı futbolcunun eski şut çekme hızı {self.sut_cekme_hizi} km/s olup yeni şut çekme hızı {yeni_sut_hizi} km/s olmuştur."

    
    
    def transfer_et(self, futbolcu_adi, futbolcu_soyadi, eski_takim, yeni_takim):
        if self.isim == futbolcu_adi and self.soyisim == futbolcu_soyadi and self.kulübü == eski_takim:
            self.kulübü = yeni_takim
            self.tüm_bilgileri_göster.append(f"futbolcunun transfer olduğu takım = {self.kulübü}")
            return f"{self.tam_isim()} adlı futbolcu {self.kulübü} takımına transfer olmuştur."
    
    
    
    def bilgileri_göster(self):
        return self.tüm_bilgileri_göster
    
    
    
    def futbolculari_ekle(self, futbolcunun_adi, futbolcunun_soyadi, futbolcunun_kulübü):
        if self.isim == futbolcunun_adi and self.soyisim == futbolcunun_soyadi and self.kulübü == futbolcunun_kulübü:
            self.futbolcular_listesi.append(f"adı = {self.isim} soyadı = {self.soyisim} kulübü = {self.kulübü}")
    
    
    
    def futbolculari_göster(self):
        return self.futbolcular_listesi
        
    
    


'''
fut1 = Futbolcu("jude", "bellingham", "real madrid")

print(fut1.tam_isim())
print()
print(fut1.kulübü)


kilosunu_gir = int(input("kilo giriniz : "))
boyunu_gir = int(input("boy giriniz : "))
print(fut1.vücut_kitle_endeksi_hesapla(kilosunu_gir, boyunu_gir))
print(fut1.bilgileri_göster())
print()


maasini_gir = int(input("maaş giriniz : "))
gol_sayisini_gir = int(input("gol sayısı giriniz : "))
asist_sayisini_gir = int(input("asist sayısını giriniz : "))
print(fut1.piyasa_degeri(maasini_gir, gol_sayisini_gir, asist_sayisini_gir))
print(fut1.bilgileri_göster())
print()


oynadiği_mac_sayisini_gir = int(input("futbolcunun oynadığı maç sayısını giriniz : "))
gol_sayisini_gir = int(input("gol sayısını giriniz : "))
print(fut1.mac_basina_gol_ortalamasi(oynadiği_mac_sayisini_gir, gol_sayisini_gir))
print(fut1.bilgileri_göster())
print()


oynadiği_mac_sayisini_gir = int(input("futbolcunun oynadığı maç sayısını giriniz : "))
asist_sayisini_gir = int(input("asist sayısını giriniz : "))
print(fut1.mac_basina_asist_ortalamasi(oynadiği_mac_sayisini_gir, asist_sayisini_gir))
print(fut1.bilgileri_göster())
print()


maaş = int(input("maaş giriniz : "))
gol_sayisini_gir = int(input("futbolcunun gol sayısını giriniz : "))
asist_sayisini_gir = int(input("futbolcunun asist sayısını giriniz : "))
pazarlik_payi_miktari = int(input("pazarlık payı miktarını giriniz : "))
print(fut1.transfer_ücreti_göster(maaş, gol_sayisini_gir, asist_sayisini_gir, pazarlik_payi_miktari))
print(fut1.bilgileri_göster())
print()


maasini_gir = int(input("maaş giriniz : "))
zam_oranini_gir = float(input("zam oranını giriniz : "))
print(fut1.maasina_zam_yap(maasini_gir, zam_oranini_gir))
print(fut1.bilgileri_göster())
print()


hizini_gir = int(input("hızını giriniz : "))
hiz_artis_yüzdesini_gir = float(input("hız artış yüzdesini giriniz : "))
print(fut1.hizini_arttir(hizini_gir, hiz_artis_yüzdesini_gir))
print(fut1.bilgileri_göster())
print()


sut_hizini_gir = int(input("şut çekme hızını giriniz : "))
hiz_artis_yüzdesini_gir = float(input("şut çekme hız artış yüzdesini giriniz : "))
print(fut1.sut_cekme_hizini_arttir(sut_hizini_gir, hiz_artis_yüzdesini_gir))
print(fut1.bilgileri_göster())
print()


futbolcu_adini_gir = input("futbolcunun adını giriniz : ").lower()
futbolcu_soyadini_gir = input("futbolcunun soyadını giriniz : ").lower()
eski_takimini_gir = input("futbolcunun eski takımını giriniz : ").lower()
yeni_takimini_gir = input("futbolcunun yeni takımını giriniz : ").lower()
print(fut1.transfer_et(futbolcu_adini_gir, futbolcu_soyadini_gir, eski_takimini_gir, yeni_takimini_gir))
print(fut1.kulübü)
print(fut1.bilgileri_göster())
print()


futbolcu_name = input("futbolcu adını giriniz : ")
futbolcu_lastname = input("futbolcu soyadını giriniz : ")
futbolcu_club = input("futbolcu kulübünü giriniz : ")
fut1.futbolculari_ekle(futbolcu_name, futbolcu_lastname, futbolcu_club)
print()
print(fut1.futbolculari_göster())
print()
print(fut1.bilgileri_göster())


print("__"*200)


fut2 = Futbolcu("thomas", "muller", "bayern munih")

print(fut2.tam_isim())
print()
print(fut2.kulübü)


kilosunu_gir = int(input("kilo giriniz : "))
boyunu_gir = int(input("boy giriniz : "))
print(fut2.vücut_kitle_endeksi_hesapla(kilosunu_gir, boyunu_gir))
print(fut2.bilgileri_göster())
print()


maasini_gir = int(input("maaş giriniz : "))
gol_sayisini_gir = int(input("gol sayısı giriniz : "))
asist_sayisini_gir = int(input("asist sayısını giriniz : "))
print(fut2.piyasa_degeri(maasini_gir, gol_sayisini_gir, asist_sayisini_gir))
print(fut2.bilgileri_göster())
print()


oynadiği_mac_sayisini_gir = int(input("futbolcunun oynadığı maç sayısını giriniz : "))
gol_sayisini_gir = int(input("gol sayısını giriniz : "))
print(fut2.mac_basina_gol_ortalamasi(oynadiği_mac_sayisini_gir, gol_sayisini_gir))
print(fut2.bilgileri_göster())
print()


oynadiği_mac_sayisini_gir = int(input("futbolcunun oynadığı maç sayısını giriniz : "))
asist_sayisini_gir = int(input("asist sayısını giriniz : "))
print(fut2.mac_basina_asist_ortalamasi(oynadiği_mac_sayisini_gir, asist_sayisini_gir))
print(fut2.bilgileri_göster())
print()


maaş = int(input("maaş giriniz : "))
gol_sayisini_gir = int(input("futbolcunun gol sayısını giriniz : "))
asist_sayisini_gir = int(input("futbolcunun asist sayısını giriniz : "))
pazarlik_payi_miktari = int(input("pazarlık payı miktarını giriniz : "))
print(fut2.transfer_ücreti_göster(maaş, gol_sayisini_gir, asist_sayisini_gir, pazarlik_payi_miktari))
print(fut2.bilgileri_göster())
print()


maasini_gir = int(input("maaş giriniz : "))
zam_oranini_gir = float(input("zam oranını giriniz : "))
print(fut2.maasina_zam_yap(maasini_gir, zam_oranini_gir))
print(fut2.bilgileri_göster())
print()


hizini_gir = int(input("hızını giriniz : "))
hiz_artis_yüzdesini_gir = float(input("hız artış yüzdesini giriniz : "))
print(fut2.hizini_arttir(hizini_gir, hiz_artis_yüzdesini_gir))
print(fut2.bilgileri_göster())
print()


sut_hizini_gir = int(input("şut çekme hızını giriniz : "))
hiz_artis_yüzdesini_gir = float(input("şut çekme hız artış yüzdesini giriniz : "))
print(fut2.sut_cekme_hizini_arttir(sut_hizini_gir, hiz_artis_yüzdesini_gir))
print(fut2.bilgileri_göster())
print()


futbolcu_adini_gir = input("futbolcunun adını giriniz : ").lower()
futbolcu_soyadini_gir = input("futbolcunun soyadını giriniz : ").lower()
eski_takimini_gir = input("futbolcunun eski takımını giriniz : ").lower()
yeni_takimini_gir = input("futbolcunun yeni takımını giriniz : ").lower()
print(fut2.transfer_et(futbolcu_adini_gir, futbolcu_soyadini_gir, eski_takimini_gir, yeni_takimini_gir))
print(fut2.kulübü)
print(fut2.bilgileri_göster())
print()


futbolcu_name = input("futbolcu adını giriniz : ")
futbolcu_lastname = input("futbolcu soyadını giriniz : ")
futbolcu_club = input("futbolcu kulübünü giriniz : ")
fut2.futbolculari_ekle(futbolcu_name, futbolcu_lastname, futbolcu_club)
print()
print(fut2.futbolculari_göster())
print()
print(fut2.bilgileri_göster())
'''







class Basketbolcu(Sporcu):
    boy = ""
    kilo = ""
    üclük_sayisi = ""
    ikilik_sayisi = ""
    asist_sayisi = ""
    serbest_atis_sayisi = ""
    maas = ""
    transfer_ücreti = ""
    zam_orani = ""
    kosma_hizi = ""
    yeni_takimi = ""
    ceza_miktari = ""
    tüm_bilgileri_göster = []
    basketbolcular_listesi = []


    def __init__(self, isim, soyisim, kulübü):
        super().__init__(isim, soyisim)
        self.kulübü = kulübü
    
    
    
    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"
    
    
    
    def vücut_kitle_endeksi_hesapla(self, kilosu, boyu):
        result = kilosu / (boyu ** 2)
        self.tüm_bilgileri_göster.append(f"vücut kitle endeksi = {result}")
        return f"{self.tam_isim()} adlı basketçinin vücut kitle indeksi = {result}"
    
    
    
    def piyasa_degeri(self, maasi, üclük, ikilik, asisti, serbest_atis):
        self.maas = maasi
        self.üclük_sayisi = üclük
        self.ikilik_sayisi = ikilik
        self.asist_sayisi = asisti
        self.serbest_atis_sayisi = serbest_atis
        piyasa_degeri = maasi * (üclük + ikilik + asisti + serbest_atis)
        self.tüm_bilgileri_göster.append(f"piyasa değeri = {piyasa_degeri}")
        return f"{self.tam_isim()} adlı basketçinin piyasa değeri = {piyasa_degeri} dolardır."
    
    
    
    def maasina_zam_yap(self, maasi, zammi):
        self.maas = maasi
        self.zam_orani = zammi
        zamli_maasi = maasi * zammi
        self.tüm_bilgileri_göster.append(f"zamlı maaşı = {zamli_maasi}")
        return f"{self.tam_isim()} adlı basketçinin zamlı maaşı {zamli_maasi} dolardır."
    
    
    
    def hizini_arttir(self, hiz, hiz_artis_yüzdesi):
        self.kosma_hizi = hiz
        yeni_kosma_hizi = hiz * hiz_artis_yüzdesi
        self.tüm_bilgileri_göster.append(f"yeni koşma hızı = {yeni_kosma_hizi}")
        return f"{self.tam_isim()} adlı basketçinin eski hızı {self.kosma_hizi} km/s olup yeni hızı {yeni_kosma_hizi} km/s olmuştur."
    
    
    
    def üclük_atis_yüzdesi(self, toplam_üclük_atis_sayisi, isabetli_üclük):
        self.üclük_sayisi = toplam_üclük_atis_sayisi
        if isabetli_üclük <= self.üclük_sayisi:
            üclük_atis_yüzde = isabetli_üclük / self.üclük_sayisi
            self.tüm_bilgileri_göster.append(f"üçlük atış yüzdesi = {üclük_atis_yüzde}")
            return f"{self.tam_isim()} adlı basketçinin üçlük atış yüzdesi {üclük_atis_yüzde}"
        else:
            return f"isabetli üçlük sayısı toplam üçlük atış sayısından fazla olamaz."
    
    
    
    def ikilik_atis_yüzdesi(self, toplam_ikilik_atis_sayisi, isabetli_ikilik):
        self.ikilik_sayisi = toplam_ikilik_atis_sayisi
        if isabetli_ikilik <= self.ikilik_sayisi:
            ikilik_atis_yüzde = isabetli_ikilik / self.ikilik_sayisi
            self.tüm_bilgileri_göster.append(f"ikilik atış yüzdesi = {ikilik_atis_yüzde}")
            return f"{self.tam_isim()} adlı basketçinin ikilik atış yüzdesi {ikilik_atis_yüzde}"
        else:
            return f"isabetli ikilik sayısı toplam ikilik atış sayısından fazla olamaz."
    
    
    
    def serbest_atis_yüzdesi(self, toplam_serbest_atis_sayisi, isabetli_serbest_atis):
        self.serbest_atis_sayisi = toplam_serbest_atis_sayisi
        if isabetli_serbest_atis <= toplam_serbest_atis_sayisi:
            serbest_atis_yüzde = isabetli_serbest_atis / self.serbest_atis_sayisi
            self.tüm_bilgileri_göster.append(f"serbest atış yüzdesi = {serbest_atis_yüzde}")
            return f"{self.tam_isim()} adlı basketçinin serbest atış yüzdesi {serbest_atis_yüzde}"
        else:
            return f"isabetli serbest atış sayısı toplam serbest atış sayısından fazla olamaz."
    
    
    
    def transfer_ücreti_göster(self, maasi, üclük, ikilik, asisti, serbest_atis, pazarlik_payi):
        piyasa_degeri = maasi * (üclük + ikilik + asisti + serbest_atis)
        if pazarlik_payi <= piyasa_degeri / 20:
            gecici_ücret = piyasa_degeri - pazarlik_payi
            self.transfer_ücreti = gecici_ücret
            self.tüm_bilgileri_göster.append(f"transfer ücreti = {self.transfer_ücreti} dolardır.")
            return f"{self.tam_isim()} adlı basketçinin transfer ücreti = {self.transfer_ücreti} dolardır."
        else:
            return "pazarlık payı piyasa değerinin yirmide birinden fazla olamaz!"


    
    def transfer_et(self, basketci_adi, basketci_soyadi, eski_takim, yeni_takim):
        if self.isim == basketci_adi and self.soyisim == basketci_soyadi and self.kulübü == eski_takim:
            self.kulübü = yeni_takim
            self.tüm_bilgileri_göster.append(f"basketçinin transfer olduğu takım = {self.kulübü}")
            return f"{self.tam_isim()} adlı basketçi {self.kulübü} takımına transfer olmuştur."
    

    
    def ceza_miktari_ve_prim_miktari_göster(self, basketci_adi, basketci_soyadi, maas, üclük, ikilik, asisti, serbest_atis, kriter):
        self.maas = maas
        
        if self.isim == basketci_adi and self.soyisim == basketci_soyadi:
            
            toplam_sayi = üclük + ikilik + asisti + serbest_atis
            if toplam_sayi < kriter:
                self.maas = self.maas - (self.maas / 4)
                self.tüm_bilgileri_göster.append(f"basketçinin ceza sonrası maaşı = {self.maas}")
                return f"{self.tam_isim()} adlı basketçi istenen kriterden daha az sayı ürettiği için maaşının 4 te biri kadar ceza almıştır. ceza sonrası maaşı {self.maas} dolardır."
            
            if toplam_sayi >= kriter:
                self.maas = self.maas + (self.maas / 4)
                self.tüm_bilgileri_göster.append(f"basketçinin prim sonrası maaşı = {self.maas}")
                return f"{self.tam_isim()} adlı basketçi istenen kriterden daha fazla sayı ürettiği için maaşının 4 te biri kadar prim almıştır. prim sonrası maaşı {self.maas} dolardır."
        
        else:
            return f"bu isimde bir basketçi bulunamadı!"

    
    
    def bilgileri_göster(self):
        return self.tüm_bilgileri_göster
    
    
    
    def basketcileri_ekle(self, basketcinin_adi, basketcinin_soyadi, basketcinin_kulübü):
        if self.isim == basketcinin_adi and self.soyisim == basketcinin_soyadi and self.kulübü == basketcinin_kulübü:
            self.basketbolcular_listesi.append(f"adı = {self.isim} soyadı = {self.soyisim} kulübü = {self.kulübü}")
    
    
    
    def basketbolculari_göster(self):
        return self.basketbolcular_listesi





bas1 = Basketbolcu("michael", "jordan", "chicago bulls")

print(bas1.tam_isim())
print()
print(bas1.kulübü)
print()

kilosunu_gir = int(input("kilo giriniz : "))
boyunu_gir = int(input("boy giriniz : "))
print(bas1.vücut_kitle_endeksi_hesapla(kilosunu_gir, boyunu_gir))
print(bas1.bilgileri_göster())
print()

maasini_gir = int(input("maaş giriniz : "))
zam_oranini_gir = float(input("zam oranını giriniz : "))
print(bas1.maasina_zam_yap(maasini_gir, zam_oranini_gir))
print(bas1.bilgileri_göster())
print()

maasini_gir = int(input("maaş giriniz : "))
üclük_sayisini_gir = int(input("üçlük sayısı giriniz : "))
ikilik_sayisini_gir = int(input("ikilik sayısı giriniz : "))
asist_sayisini_gir = int(input("asist sayısını giriniz : "))
serbest_atis_sayisini_gir = int(input("serbest atış sayısını giriniz : "))
print(bas1.piyasa_degeri(maasini_gir, üclük_sayisini_gir, ikilik_sayisini_gir, asist_sayisini_gir, serbest_atis_sayisini_gir))
print(bas1.bilgileri_göster())
print()


hizini_gir = int(input("hızını giriniz : "))
hiz_artis_yüzdesini_gir = float(input("hız artış yüzdesini giriniz : "))
print(bas1.hizini_arttir(hizini_gir, hiz_artis_yüzdesini_gir))
print(bas1.bilgileri_göster())
print()


üclük_sayisini_gir = int(input("toplam üçlük sayısını giriniz : "))
isabetli_üclük_sayisini_gir = int(input("isabetli üçlük sayısını giriniz : "))
print(bas1.üclük_atis_yüzdesi(üclük_sayisini_gir, isabetli_üclük_sayisini_gir))
print(bas1.bilgileri_göster())
print()


ikilik_sayisini_gir = int(input("toplam ikilik sayısını giriniz : "))
isabetli_ikilik_sayisini_gir = int(input("isabetli ikilik sayısını giriniz : "))
print(bas1.ikilik_atis_yüzdesi(ikilik_sayisini_gir, isabetli_ikilik_sayisini_gir))
print(bas1.bilgileri_göster())
print()


serbest_atis_sayisini_gir = int(input("toplam serbest atış sayısını giriniz : "))
isabetli_serbest_atis_sayisini_gir = int(input("isabetli serbest atış sayısını giriniz : "))
print(bas1.serbest_atis_yüzdesi(serbest_atis_sayisini_gir, isabetli_serbest_atis_sayisini_gir))
print(bas1.bilgileri_göster())
print()


basketci_adi_gir = input("basketçi adını giriniz : ").lower()
basketci_soyadini_gir = input("basketçi soyadını giriniz : ").lower()
maasini_gir = int(input("maaş giriniz : "))
üclük_sayisini_gir = int(input("üçlük sayısı giriniz : "))
ikilik_sayisini_gir = int(input("ikilik sayısı giriniz : "))
asist_sayisini_gir = int(input("asist sayısını giriniz : "))
serbest_atis_sayisini_gir = int(input("serbest atış sayısını giriniz : "))
kriter_gir = int(input("ceza yada prim için bir kriter giriniz : "))
print(bas1.ceza_miktari_ve_prim_miktari_göster(basketci_adi_gir, basketci_soyadini_gir, maasini_gir, üclük_sayisini_gir, ikilik_sayisini_gir, asist_sayisini_gir, serbest_atis_sayisini_gir, kriter_gir))
print(bas1.bilgileri_göster())
print()


maaş = int(input("maaş giriniz : "))
üclük_say = int(input("üçlük sayısını giriniz : "))
ikilik_say = int(input("ikilik sayısını giriniz : "))
asist_say = int(input("asist sayısını giriniz : "))
serbest_atis_say = int(input("serbest atış sayısını giriniz : "))
pazarlik_payi_miktari = int(input("pazarlık payı miktarını giriniz : "))
print(bas1.transfer_ücreti_göster(maaş, üclük_say, ikilik_say, asist_say, serbest_atis_say, pazarlik_payi_miktari))
print(bas1.bilgileri_göster())
print()


basketci_adi_gir = input("basketçi adını giriniz : ").lower()
basketci_soyadini_gir = input("basketçi soyadını giriniz : ").lower()
eski_takimini_gir = input("basketçinin eski takımını giriniz : ").lower()
yeni_takimini_gir = input("basketçinin yeni takımını giriniz : ").lower()
print(bas1.transfer_et(basketci_adi_gir, basketci_soyadini_gir, eski_takimini_gir, yeni_takimini_gir))
print(bas1.kulübü)
print(bas1.bilgileri_göster())
print()



basketbolcu_name = input("basketbolcu adını giriniz : ")
basketbolcu_lastname = input("basketbolcu soyadını giriniz : ")
basketbolcu_club = input("basketbolcu kulübünü giriniz : ")
bas1.basketcileri_ekle(basketbolcu_name, basketbolcu_lastname, basketbolcu_club)
print()
print(bas1.basketbolculari_göster())
print()
print(bas1.bilgileri_göster())




bas2 = Basketbolcu("magic", "johnson", "los angeles lakers")

print(bas2.tam_isim())
print()
print(bas2.kulübü)
print()

kilosunu_gir = int(input("kilo giriniz : "))
boyunu_gir = int(input("boy giriniz : "))
print(bas2.vücut_kitle_endeksi_hesapla(kilosunu_gir, boyunu_gir))
print(bas2.bilgileri_göster())
print()

maasini_gir = int(input("maaş giriniz : "))
zam_oranini_gir = float(input("zam oranını giriniz : "))
print(bas2.maasina_zam_yap(maasini_gir, zam_oranini_gir))
print(bas2.bilgileri_göster())
print()

maasini_gir = int(input("maaş giriniz : "))
üclük_sayisini_gir = int(input("üçlük sayısı giriniz : "))
ikilik_sayisini_gir = int(input("ikilik sayısı giriniz : "))
asist_sayisini_gir = int(input("asist sayısını giriniz : "))
serbest_atis_sayisini_gir = int(input("serbest atış sayısını giriniz : "))
print(bas2.piyasa_degeri(maasini_gir, üclük_sayisini_gir, ikilik_sayisini_gir, asist_sayisini_gir, serbest_atis_sayisini_gir))
print(bas2.bilgileri_göster())
print()


hizini_gir = int(input("hızını giriniz : "))
hiz_artis_yüzdesini_gir = float(input("hız artış yüzdesini giriniz : "))
print(bas2.hizini_arttir(hizini_gir, hiz_artis_yüzdesini_gir))
print(bas2.bilgileri_göster())
print()


üclük_sayisini_gir = int(input("toplam üçlük sayısını giriniz : "))
isabetli_üclük_sayisini_gir = int(input("isabetli üçlük sayısını giriniz : "))
print(bas2.üclük_atis_yüzdesi(üclük_sayisini_gir, isabetli_üclük_sayisini_gir))
print(bas2.bilgileri_göster())
print()


ikilik_sayisini_gir = int(input("toplam ikilik sayısını giriniz : "))
isabetli_ikilik_sayisini_gir = int(input("isabetli ikilik sayısını giriniz : "))
print(bas2.ikilik_atis_yüzdesi(ikilik_sayisini_gir, isabetli_ikilik_sayisini_gir))
print(bas2.bilgileri_göster())
print()


serbest_atis_sayisini_gir = int(input("toplam serbest atış sayısını giriniz : "))
isabetli_serbest_atis_sayisini_gir = int(input("isabetli serbest atış sayısını giriniz : "))
print(bas2.serbest_atis_yüzdesi(serbest_atis_sayisini_gir, isabetli_serbest_atis_sayisini_gir))
print(bas2.bilgileri_göster())
print()


basketci_adi_gir = input("basketçi adını giriniz : ").lower()
basketci_soyadini_gir = input("basketçi soyadını giriniz : ").lower()
maasini_gir = int(input("maaş giriniz : "))
üclük_sayisini_gir = int(input("üçlük sayısı giriniz : "))
ikilik_sayisini_gir = int(input("ikilik sayısı giriniz : "))
asist_sayisini_gir = int(input("asist sayısını giriniz : "))
serbest_atis_sayisini_gir = int(input("serbest atış sayısını giriniz : "))
kriter_gir = int(input("ceza yada prim için bir kriter giriniz : "))
print(bas2.ceza_miktari_ve_prim_miktari_göster(basketci_adi_gir, basketci_soyadini_gir, maasini_gir, üclük_sayisini_gir, ikilik_sayisini_gir, asist_sayisini_gir, serbest_atis_sayisini_gir, kriter_gir))
print(bas2.bilgileri_göster())
print()


maaş = int(input("maaş giriniz : "))
üclük_say = int(input("üçlük sayısını giriniz : "))
ikilik_say = int(input("ikilik sayısını giriniz : "))
asist_say = int(input("asist sayısını giriniz : "))
serbest_atis_say = int(input("serbest atış sayısını giriniz : "))
pazarlik_payi_miktari = int(input("pazarlık payı miktarını giriniz : "))
print(bas2.transfer_ücreti_göster(maaş, üclük_say, ikilik_say, asist_say, serbest_atis_say, pazarlik_payi_miktari))
print(bas2.bilgileri_göster())
print()


basketci_adi_gir = input("basketçi adını giriniz : ").lower()
basketci_soyadini_gir = input("basketçi soyadını giriniz : ").lower()
eski_takimini_gir = input("basketçinin eski takımını giriniz : ").lower()
yeni_takimini_gir = input("basketçinin yeni takımını giriniz : ").lower()
print(bas2.transfer_et(basketci_adi_gir, basketci_soyadini_gir, eski_takimini_gir, yeni_takimini_gir))
print(bas2.kulübü)
print(bas2.bilgileri_göster())
print()


basketbolcu_name = input("basketbolcu adını giriniz : ")
basketbolcu_lastname = input("basketbolcu soyadını giriniz : ")
basketbolcu_club = input("basketbolcu kulübünü giriniz : ")
bas2.basketcileri_ekle(basketbolcu_name, basketbolcu_lastname, basketbolcu_club)
print()
print(bas2.basketbolculari_göster())
print()
print(bas2.bilgileri_göster())





    







        


        


        

    
    




















    
        




























    


















    


























