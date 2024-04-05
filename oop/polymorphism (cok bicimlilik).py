
'''
class Audi:
    def renk(self):
        print("beyaz")
    
    def fiyat(self):
        print("6 milyon")

class Mercedes:
    def renk(self):
        print("mavi")
    
    def fiyat(self):
        print("5 milyon")

class Bmw:
    def renk(self):
        print("kırmızı")
    
    def fiyat(self):
        print("4 milyon")

class Volvo:
    def renk(self):
        print("siyah")
    
    def fiyat(self):
        print("3 milyon")

def araba_renk(arac):
    arac.renk()

def araba_fiyat(arac):
    arac.fiyat()

a = Audi()
m = Mercedes()
b = Bmw()
v = Volvo()

araba_renk(a)
araba_renk(m)
araba_renk(b)
araba_renk(v)

araba_fiyat(a)
araba_fiyat(m)
araba_fiyat(b)
araba_fiyat(v)

'''

'''
class Calisan:
    maas = 30000
    
    
    def zam_orani_göster(self):
        oran = 1.2
        return oran
    
    def prim_göster(self):
        primi = 5000
        return primi
    
    def yillik_izinli_oldugu_gün_sayisi(self, calisdigi_yil):
        if 1 <= calisdigi_yil <=5:
            yillik_izin_gün_sayisi = 14
        elif 6 <= calisdigi_yil <= 14:
            yillik_izin_gün_sayisi = 20
        elif calisdigi_yil >= 15:
            yillik_izin_gün_sayisi = 26
        return yillik_izin_gün_sayisi
    
    def aylik_yemek_ücreti(self):
        aylik_ise_geldigi_gün_sayisi = 20
        günlük_yemek_ücreti = 200
        return aylik_ise_geldigi_gün_sayisi * günlük_yemek_ücreti
    
    def aylik_ise_gelmedigi_gün_sayisi(self):
        gelmedigi_gün_sayisi = 10
        return gelmedigi_gün_sayisi
    
    def aylik_maas_kesintisi(self):
        günlük_ücret = self.maas / 30
        gelmedigi_gün_sayisi = 10
        return günlük_ücret * gelmedigi_gün_sayisi
    
    
    def aylik_alacagi_mesai_ücreti(self):
        saatlik_ücret = (self.maas / 30) / 24
        aylik_calisdigi_mesai_saati = 50
        return saatlik_ücret * aylik_calisdigi_mesai_saati
    
    def aylik_alacagi_toplam_ücret(self):
        zam_orani = self.zam_orani_göster()
        mesai_ücreti = self.aylik_alacagi_mesai_ücreti()
        kesinti = self.aylik_maas_kesintisi()
        yemek_ücreti = self.aylik_yemek_ücreti()
        prim = self.prim_göster()
        toplam = ((self.maas * zam_orani) + mesai_ücreti + prim + yemek_ücreti) - kesinti
        return toplam


        
    

class Muhasebeci(Calisan):

    def zam_orani_göster(self):
        oran = 1.3
        return oran
     
    def prim_göster(self):
        primi = 8000
        return primi
     
    def yillik_izinli_oldugu_gün_sayisi(self, calisdigi_yil):
        if 1 <= calisdigi_yil <=5:
            yillik_izin_gün_sayisi = 14
        elif 6 <= calisdigi_yil <= 14:
            yillik_izin_gün_sayisi = 20
        elif calisdigi_yil >= 15:
            yillik_izin_gün_sayisi = 26
        return yillik_izin_gün_sayisi
     
    def aylik_yemek_ücreti(self):
        aylik_ise_geldigi_gün_sayisi = 18
        günlük_yemek_ücreti = 200
        return aylik_ise_geldigi_gün_sayisi * günlük_yemek_ücreti
    
    def aylik_ise_gelmedigi_gün_sayisi(self):
        gelmedigi_gün_sayisi = 12
        return gelmedigi_gün_sayisi
    
    def aylik_maas_kesintisi(self):
        günlük_ücret = self.maas / 30
        gelmedigi_gün_sayisi = 12
        return günlük_ücret * gelmedigi_gün_sayisi
    
    def aylik_alacagi_mesai_ücreti(self):
        saatlik_ücret = (self.maas / 30) / 24
        aylik_calisdigi_mesai_saati = 40
        return saatlik_ücret * aylik_calisdigi_mesai_saati
    
    def aylik_alacagi_toplam_ücret(self):
        zam_orani = self.zam_orani_göster()
        mesai_ücreti = self.aylik_alacagi_mesai_ücreti()
        kesinti = self.aylik_maas_kesintisi()
        yemek_ücreti = self.aylik_yemek_ücreti()
        prim = self.prim_göster()
        toplam = ((self.maas * zam_orani) + mesai_ücreti + prim + yemek_ücreti) - kesinti
        return toplam
    
    
        
     
     


class Yazilimci(Calisan):

    def zam_orani_göster(self):
        oran = 1.4
        return oran
     
    def prim_göster(self):
        primi = 10000
        return primi
     
    def yillik_izinli_oldugu_gün_sayisi(self, calisdigi_yil):
        if 1 <= calisdigi_yil <=5:
            yillik_izin_gün_sayisi = 14
        elif 6 <= calisdigi_yil <= 14:
            yillik_izin_gün_sayisi = 20
        elif calisdigi_yil >= 15:
            yillik_izin_gün_sayisi = 26
        return yillik_izin_gün_sayisi
     
    def aylik_yemek_ücreti(self):
        aylik_ise_geldigi_gün_sayisi = 23
        günlük_yemek_ücreti = 200
        return aylik_ise_geldigi_gün_sayisi * günlük_yemek_ücreti
    
    def aylik_ise_gelmedigi_gün_sayisi(self):
        gelmedigi_gün_sayisi = 7
        return gelmedigi_gün_sayisi
    
    def aylik_maas_kesintisi(self):
        günlük_ücret = self.maas / 30
        gelmedigi_gün_sayisi = 7
        return günlük_ücret * gelmedigi_gün_sayisi
    
    def aylik_alacagi_mesai_ücreti(self):
        saatlik_ücret = (self.maas / 30) / 24
        aylik_calisdigi_mesai_saati = 80
        return saatlik_ücret * aylik_calisdigi_mesai_saati
    
    def aylik_alacagi_toplam_ücret(self):
        zam_orani = self.zam_orani_göster()
        mesai_ücreti = self.aylik_alacagi_mesai_ücreti()
        kesinti = self.aylik_maas_kesintisi()
        yemek_ücreti = self.aylik_yemek_ücreti()
        prim = self.prim_göster()
        toplam = ((self.maas * zam_orani) + mesai_ücreti + prim + yemek_ücreti) - kesinti
        return toplam
     
    



class Grafiker(Calisan):

    def zam_orani_göster(self):
        oran = 1.5
        return oran
    
    def prim_göster(self):
        primi = 12000
        return primi
    
    def yillik_izinli_oldugu_gün_sayisi(self, calisdigi_yil):
        if 1 <= calisdigi_yil <=5:
            yillik_izin_gün_sayisi = 14
        elif 6 <= calisdigi_yil <= 14:
            yillik_izin_gün_sayisi = 20
        elif calisdigi_yil >= 15:
            yillik_izin_gün_sayisi = 26
        return yillik_izin_gün_sayisi
    
    def aylik_yemek_ücreti(self):
        aylik_ise_geldigi_gün_sayisi = 15
        günlük_yemek_ücreti = 200
        return aylik_ise_geldigi_gün_sayisi * günlük_yemek_ücreti
    
    def aylik_ise_gelmedigi_gün_sayisi(self):
        gelmedigi_gün_sayisi = 15
        return gelmedigi_gün_sayisi
    
    def aylik_maas_kesintisi(self):
        günlük_ücret = self.maas / 30
        gelmedigi_gün_sayisi = 15
        return günlük_ücret * gelmedigi_gün_sayisi
    
    def aylik_alacagi_mesai_ücreti(self):
        saatlik_ücret = (self.maas / 30) / 24
        aylik_calisdigi_mesai_saati = 20
        return saatlik_ücret * aylik_calisdigi_mesai_saati
    
    def aylik_alacagi_toplam_ücret(self):
        zam_orani = self.zam_orani_göster()
        mesai_ücreti = self.aylik_alacagi_mesai_ücreti()
        kesinti = self.aylik_maas_kesintisi()
        yemek_ücreti = self.aylik_yemek_ücreti()
        prim = self.prim_göster()
        toplam = ((self.maas * zam_orani) + mesai_ücreti + prim + yemek_ücreti) - kesinti
        return toplam

    
    

cal = Calisan()
print(f"çalışanın normal maaşı = {cal.maas}")
print(f"çalışanın zam oranı = {cal.zam_orani_göster()}")
print(f"çalışanın primi = {cal.prim_göster()}")
print(f"çalışanın yıllık izinli olduğu gün sayısı = {cal.yillik_izinli_oldugu_gün_sayisi(5)}")
print(f"çalışanın aylık yemek ücreti = {cal.aylik_yemek_ücreti()}")
print(f"çalışanın aylık işe gelmediği gün sayısı = {cal.aylik_ise_gelmedigi_gün_sayisi()}")
print(f"çalışanın aylık ücret kesintisi = {cal.aylik_maas_kesintisi()}")
print(f"çalışanın aylık alacağı mesai ücreti = {int(cal.aylik_alacagi_mesai_ücreti())}")
print(f"çalışanın aylık alacağı toplam maaş = {int(cal.aylik_alacagi_toplam_ücret())}")

print("_"*50)

muh = Muhasebeci()
print(f"muhasebecinin normal maaşı = {muh.maas}")
print(f"muhasebecinin zam oranı = {muh.zam_orani_göster()}")
print(f"muhasebecinin primi = {muh.prim_göster()}")
print(f"muhasebecinin yıllık izinli olduğu gün sayısı = {muh.yillik_izinli_oldugu_gün_sayisi(6)}")
print(f"muhasebecinin aylık yemek ücreti = {muh.aylik_yemek_ücreti()}")
print(f"muhasebecinin aylık işe gelmediği gün sayısı = {muh.aylik_ise_gelmedigi_gün_sayisi()}")
print(f"muhasebecinin aylık ücret kesintisi = {muh.aylik_maas_kesintisi()}")
print(f"muhasebecinin aylık alacağı mesai ücreti = {int(muh.aylik_alacagi_mesai_ücreti())}")
print(f"muhasebecinin aylık alacağı toplam maaş = {int(muh.aylik_alacagi_toplam_ücret())}")

print("_"*50)

yaz = Yazilimci()
print(f"yazılımcının normal maaşı = {yaz.maas}")
print(f"yazılımcının zam oranı = {yaz.zam_orani_göster()}")
print(f"yazılımcının primi = {yaz.prim_göster()}")
print(f"yazılımcının yıllık izinli olduğu gün sayısı = {yaz.yillik_izinli_oldugu_gün_sayisi(15)}")
print(f"yazılımcının aylık yemek ücreti = {yaz.aylik_yemek_ücreti()}")
print(f"yazılımcının aylık işe gelmediği gün sayısı = {yaz.aylik_ise_gelmedigi_gün_sayisi()}")
print(f"yazılımcının aylık ücret kesintisi = {yaz.aylik_maas_kesintisi()}")
print(f"yazılımcının aylık alacağı mesai ücreti = {int(yaz.aylik_alacagi_mesai_ücreti())}")
print(f"yazılımcının aylık alacağı toplam maaş = {int(yaz.aylik_alacagi_toplam_ücret())}")

print("_"*50)

gra = Grafiker()
print(f"grafikerin normal maaşı = {gra.maas}")
print(f"grafikerin zam oranı = {gra.zam_orani_göster()}")
print(f"grafikerin primi = {gra.prim_göster()}")
print(f"grafikerin yıllık izinli olduğu gün sayısı = {gra.yillik_izinli_oldugu_gün_sayisi(18)}")
print(f"grafikerin aylık yemek ücreti = {gra.aylik_yemek_ücreti()}")
print(f"grafikerin aylık işe gelmediği gün sayısı = {gra.aylik_ise_gelmedigi_gün_sayisi()}")
print(f"grafikerin aylık ücret kesintisi = {gra.aylik_maas_kesintisi()}")
print(f"grafikerin aylık alacağı mesai ücreti = {int(gra.aylik_alacagi_mesai_ücreti())}")
print(f"grafikerin aylık alacağı toplam maaş = {int(gra.aylik_alacagi_toplam_ücret())}")

'''

'''
class Circle:
    
    def alan_hesapla(self):
        pi = 3.14
        r = 5
        return pi * r * r
    
    def cevre_hesapla(self):
        pi = 3.14
        r = 6
        return 2 * pi * r
    
circle = Circle()
print(f"dairenin alanı = {circle.alan_hesapla()}")
print(f"dairenin çevresi = {circle.cevre_hesapla()}")

class Square(Circle):

    def alan_hesapla(self):
        kenar = 8
        return kenar * kenar
    
    def cevre_hesapla(self):
        kenar = 10
        return kenar * 4

square = Square()
print(f"karenin alanı = {square.alan_hesapla()}")
print(f"karenin çevresi = {square.cevre_hesapla()}")

class Rectangle(Circle):
    
    def alan_hesapla(self):
        kisa_kenar = 12
        uzun_kenar = 20
        return kisa_kenar * uzun_kenar
    
    def cevre_hesapla(self):
        kisa_kenar = 30
        uzun_kenar = 40
        return 2 * (kisa_kenar + uzun_kenar)

rectangle = Rectangle()
print(f"dikdörtgenin alanı = {rectangle.alan_hesapla()}")
print(f"dikdörtgenin çevresi = {rectangle.cevre_hesapla()}")


def alani(a):
    return a.alan_hesapla()

def cevresi(c):
    return c.cevre_hesapla()

print(alani(circle))
print(alani(square))
print(alani(rectangle))

print(cevresi(circle))
print(cevresi(square))
print(cevresi(rectangle))
    
'''

'''
class Albay:
    
    def isim_soyisim(self):
        print("hakan çelik")
    

    def maas(self):
        print("80000 tl")
    
    def yas(self):
        print("53")


class Yarbay(Albay):

    def isim_soyisim(self):
        print("hasan demir")
    

    def maas(self):
        print("70000 tl")
    
    def yas(self):
        print("48")

    

class Binbasi(Yarbay):

    def isim_soyisim(self):
        print("harun gümüş")
    

    def maas(self):
        print("60000 tl")
    
    def yas(self):
        print("45")


class Yüzbasi(Binbasi):

    def isim_soyisim(self):
        print("halil bakır")
    

    def maas(self):
        print("50000 tl")
    
    
    def yas(self):
        print("38")

    

alb = Albay()
alb.isim_soyisim()
alb.maas()
alb.yas()

yar = Yarbay()
yar.isim_soyisim()
yar.maas()
yar.yas()

bin = Binbasi()
bin.isim_soyisim()
bin.maas()
bin.yas()

yüz = Yüzbasi()
yüz.isim_soyisim()
yüz.maas()
yüz.yas()

print("__"*100)


def tüm_bilgileri_göster(rütbe):
    rütbe.isim_soyisim() 
    rütbe.maas()
    rütbe.yas()

tüm_bilgileri_göster(alb)
print()
tüm_bilgileri_göster(yar)
print()
tüm_bilgileri_göster(bin)
print()
tüm_bilgileri_göster(yüz)

'''

'''
class PepGuardiola:

    def raisee(self):

        raise_rate = 0.1
        result = 1000000 + 1000000 * raise_rate
        print('Pep Guardiola: ', result)


class LionelMessi(PepGuardiola):
      
    def raisee(self):
           
        raise_rate = 0.2
        result = 1000000 + 1000000 * raise_rate
        print('Lionel Messi: ', result)

      
class KylianMbappe(PepGuardiola):
     
    def raisee(self):
          
        raise_rate = 0.3
        result = 1000000 + 1000000 * raise_rate
        print('Kylian Mbappe: ', result)


class CristianoRonaldo(PepGuardiola):

    def raisee(self):

        raise_rate = 0.4
        result = 1000000 + 1000000 * raise_rate
        print('Cristiano Ronaldo: ', result)


class  KevinDeBruyne(PepGuardiola):

    def raisee(self):
        
        raise_rate = 0.5
        result = 1000000 + 1000000 * raise_rate
        print('Kevin De Bruyne: ', result)


class JudeBellingham(PepGuardiola):

    def raisee(self):

        raise_rate = 0.6
        result = 1000000 + 1000000 * raise_rate
        print('Jude Bellingham: ', result)

class Ronaldinho(PepGuardiola):

    def raisee(self):

        raise_rate = 0.7
        result = 1000000 + 1000000 * raise_rate
        print('Ronaldinho: ', result)


pep = PepGuardiola()
lio = LionelMessi()
kyl = KylianMbappe()
cri = CristianoRonaldo()
kev = KevinDeBruyne()
jud = JudeBellingham()
ron = Ronaldinho()

Team_list = [pep, lio, kyl, cri, kev, jud, ron]

for i in Team_list:
    i.raisee()

'''










