
'''
class Personel:

    zam_orani = 1.2

    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        
    
    @property
    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"
    
    @tam_isim.setter
    def tam_isim(self, tam_ad):
        isim, soyisim = tam_ad.split(" ")
        self.isim = isim
        self.soyisim = soyisim
    
    @tam_isim.deleter
    def tam_isim(self):
        print("isim soyisim silindi!!!!")
        self.isim = None
        self.soyisim = None
    
    @property
    def eposta(self):
        return f"{self.isim}.{self.soyisim}@gmail.com"
    
    @eposta.deleter
    def eposta(self):
        print("eposta silindi!!!!")
        self.isim = None
        self.soyisim = None

p = Personel("cemil", "serçe", 33000)

p.isim = "kaan"
p.tam_isim = "fatih karaman"
print(p.__dict__)
print(p.eposta)
print(p.tam_isim)

del p.eposta
print(p.eposta)

del p.tam_isim
print(p.tam_isim)

'''

'''
class Müdür:
    def __init__(self, isim, soyisim, yas, boy, kilo, mezuniyet, maas, zam_oran):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.boy = boy
        self.kilo = kilo
        self.mezuniyet = mezuniyet
        self.maas = maas
        self.zam_oran = zam_oran
        self.hobiler = []
        
    @property 
    def tam_ad(self):
        return f"isim = {self.isim} soyisim = {self.soyisim}"
    
    @tam_ad.setter
    def tam_ad(self, full_name):
        isim, soyisim = full_name.split(" ")
        self.isim = isim
        self.soyisim = soyisim
    
    @tam_ad.deleter
    def tam_ad(self):
        print("tam ad silinmiştir..")
        self.isim = None
        self.soyisim = None
    
    @property
    def eposta(self):
        return f"eposta = {self.isim}.{self.soyisim}@hotmail.com"
    
    @eposta.deleter
    def eposta(self):
        print("eposta silinmiştir...")
        self.isim = None
        self.soyisim = None
    
    @property
    def diger_bilgiler(self):
        return f"yaş = {self.yas} boy = {self.boy} kilo = {self.kilo} mezuniyet = {self.mezuniyet}"
    
    @diger_bilgiler.setter
    def diger_bilgiler(self, yeni_bilgiler):
        yas, boy, kilo, mezuniyet = yeni_bilgiler.split(" ")
        self.yas = yas
        self.boy = boy
        self.kilo = kilo
        self.mezuniyet = mezuniyet
    
    @diger_bilgiler.deleter
    def diger_bilgiler(self):
        print("diğer bilgiler silinmiştir..")
        self.yas = None
        self.boy = None
        self.kilo = None
        self.mezuniyet = None

    @property
    def zam_uygula(self):
        return f"normal maaşı = {self.maas} zam oranı = {self.zam_oran} zamlı maaş = {self.maas * self.zam_oran}"
    
    @zam_uygula.setter
    def zam_uygula(self, yeni_oran):
        self.zam_oran = yeni_oran
        return self.zam_oran * self.maas
    
    @zam_uygula.deleter
    def zam_uygula(self):
        print("zam uygula silinmiştir..")
        self.maas = 0
        self.zam_oran = 0
    
    @property
    def hobiler_ekle(self):
        if len(self.hobiler) == 0:
            self.hobiler.append("kitap okumak")
            self.hobiler.append("balık tutmak")
            self.hobiler.append("seyahat etmek")
            return self.hobiler
    
    @hobiler_ekle.deleter
    def hobiler_ekle(self):
        print("hobiler silinmiştir...")
        
     
m = Müdür("can", "bayraktar", 48, 180, 90, "yüksek lisans", 60000, 1.5)
print(m.tam_ad)
m.tam_ad = "kerim canberk"
print(m.tam_ad)
del m.tam_ad
print(m.tam_ad)
print(m.eposta)
del m.eposta
print(m.eposta)
print(m.diger_bilgiler)
m.diger_bilgiler = "68 179 77 lise"
print(m.diger_bilgiler)
del m.diger_bilgiler
print(m.diger_bilgiler)
print(m.zam_uygula)
m.zam_uygula = 2.8
print(m.zam_uygula)
del m.zam_uygula
print(m.zam_uygula)
print(m.hobiler_ekle)
del m.hobiler_ekle
m.hobiler_ekle

print("_"*5000)


class Calisan(Müdür):
    def __init__(self, isim, soyisim, yas, boy, kilo, mezuniyet, maas, zam_oran, günlük_yemek_parasi, calistigi_gün_sayisi):
        super().__init__(isim, soyisim, yas, boy, kilo, mezuniyet, maas, zam_oran)
        self.günlük_yemek_parasi = günlük_yemek_parasi
        self.calistigi_gün_sayisi = calistigi_gün_sayisi
    
    @property
    def tam_ad(self):
        return f"isim = {self.isim} soyisim = {self.soyisim}"
    
    @tam_ad.setter
    def tam_ad(self, full_name):
        isim, soyisim = full_name.split(" ")
        self.isim = isim
        self.soyisim = soyisim
    
    @tam_ad.deleter
    def tam_ad(self):
        print("tam ad silindi!")
        self.isim = None
        self.soyisim = None
    
    @property
    def eposta(self):
        return f"eposta = {self.isim}.{self.soyisim}@hotmail.com"
    
    @eposta.deleter
    def eposta(self):
        print("eposta silindi!")
        self.isim = None
        self.soyisim = None
    
    @property
    def diger_bilgiler(self):
        return f"yaş = {self.yas} boy = {self.boy} kilo = {self.kilo} mezuniyet = {self.mezuniyet}"
    
    @diger_bilgiler.setter
    def diger_bilgiler(self, yeni_bilgiler):
        yas, boy, kilo, mezuniyet = yeni_bilgiler.split(" ")
        self.yas = yas
        self.boy = boy
        self.kilo = kilo
        self.mezuniyet = mezuniyet
    
    @diger_bilgiler.deleter
    def diger_bilgiler(self):
        print("diğer bilgiler silindi!")
        self.yas = None
        self.boy = None
        self.kilo = None
        self.mezuniyet = None
    
    @property
    def zam_uygula(self):
        return f"normal maaşı = {self.maas} zam oranı = {self.zam_oran} zamlı maaş = {self.maas * self.zam_oran}"
    
    @zam_uygula.setter
    def zam_uygula(self, yeni_maas):
        self.maas = yeni_maas
        return self.maas * self.zam_oran
    
    @zam_uygula.deleter
    def zam_uygula(self):
        print("zam uygula silindi!!!")
        self.maas = 0
        self.zam_oran = 0
    
    @property
    def yemek_parasi_hesapla(self):
        return f"çalışanın günlük yemek parası ücreti = {self.günlük_yemek_parasi} çalıştığı gün sayısı = {self.calistigi_gün_sayisi} aylık yemek parası ücreti = {self.günlük_yemek_parasi * self.calistigi_gün_sayisi}"
    
    @yemek_parasi_hesapla.setter
    def yemek_parasi_hesapla(self, yemek_parasi):
        self.günlük_yemek_parasi = yemek_parasi
        return self.günlük_yemek_parasi * self.calistigi_gün_sayisi
    
    @yemek_parasi_hesapla.deleter
    def yemek_parasi_hesapla(self):
        print("yemek parası hesapla silinmiştir...")
        self.günlük_yemek_parasi = 0
        self.calistigi_gün_sayisi = 0



c = Calisan("hasan", "alp", 40, 175, 70, "lise", 25000, 1.2, 150, 22)
print(c.tam_ad)
c.tam_ad = "ulvi yıldırım"
print(c.tam_ad)
print(c.eposta)
del c.eposta
print(c.eposta)
print(c.diger_bilgiler)
print(c.zam_uygula)
c.diger_bilgiler = "65 195 100 ilkokul"
print(c.diger_bilgiler)
c.zam_uygula = 40000
print(c.zam_uygula)
del c.zam_uygula
print(c.zam_uygula)
del c.tam_ad
print(c.tam_ad)
del c.diger_bilgiler
print(c.diger_bilgiler)
print("_" * 50)
print(c.tam_ad)
print(c.eposta)
print(c.diger_bilgiler)
print(c.zam_uygula)
print(c.yemek_parasi_hesapla)
c.yemek_parasi_hesapla = 550
print(c.yemek_parasi_hesapla)
del c.yemek_parasi_hesapla
print(c.yemek_parasi_hesapla)

'''

'''
class User:
    def __init__(self, isim, soyisim, telefon, kullanici_adi, sifre):
        self.isim = isim
        self.soyisim = soyisim
        self.telefon = telefon
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre
    
    @property
    def tam_ad_göster(self):
        return f"kullanıcının adı = {self.isim} soyadı = {self.soyisim}"
    
    @tam_ad_göster.setter
    def tam_ad_göster(self, full_name):
        isim, soyisim = full_name.split(" ")
        self.isim = isim
        self.soyisim = soyisim
    
    
    @property
    def telefon_göster(self):
        return f"kullanıcının telefonu = {self.telefon}"
    
    
    @telefon_göster.setter
    def telefon_göster(self, yeni_telefon_no):
        self.telefon = yeni_telefon_no
    
    @telefon_göster.deleter
    def telefon_göster(self):
        print("telefon göster silinmiştir..")
        self.telefon = None
    
    
    @property
    def kullanici_adi_ve_sifre_göster(self):
        return f"kullanıcının kullanıcı adı = {self.kullanici_adi} sifresi = {self.sifre}"
    
    
    @kullanici_adi_ve_sifre_göster.setter
    def kullanici_adi_ve_sifre_göster(self, yeni):
        yeni_kullanici_adi, yeni_sifre = yeni.split(" ")
        self.kullanici_adi = yeni_kullanici_adi
        self.sifre = yeni_sifre
    

    
    @property
    def giris_yap(self):
        if self.isim == "jack" and self.soyisim == "david" and self.telefon == "9876543210" and self.kullanici_adi == "tiger" and self.sifre == "abcde":
            return f"{self.isim} {self.soyisim} adlı kullanıcı başarıyla giriş yapmıştır..."
        else:
            return f"giriş başarısızdır!"
    
    
    

u = User("john", "parker", "0123456789", "monster", "abc")

print(u.tam_ad_göster)
print(u.telefon_göster)
print(u.kullanici_adi_ve_sifre_göster)
print(u.giris_yap)
print("_"*50)

u.tam_ad_göster = "jack david"
print(u.tam_ad_göster)
print(u.giris_yap)
print("_"*50)

u.telefon_göster = "9876543210"
print(u.telefon_göster)
print(u.giris_yap)
print("_"*50)

u.kullanici_adi_ve_sifre_göster = "tiger abcde"
print(u.kullanici_adi_ve_sifre_göster)
print(u.giris_yap)
print("_"*50)

'''














        