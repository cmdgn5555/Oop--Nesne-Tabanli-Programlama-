
'''
class Sporcu:

    def yaz(self):
        print("sporcu")


class Futbolcu(Sporcu):
        pass


class Basketbolcu(Sporcu):

    def yaz(self):
        print("basketbolcu")


class Voleybolcu(Sporcu):

    def yaz(self):
        print("voleybolcu")


class Boksör(Sporcu):
        pass


sporcu1 = Sporcu()
sporcu1.yaz()
print()

futbolcu1 = Futbolcu()
futbolcu1.yaz()
print()

basketbolcu1 = Basketbolcu()
basketbolcu1.yaz()
print()

voleybolcu1 = Voleybolcu()
voleybolcu1.yaz()
print()

boksör1 = Boksör()
boksör1.yaz()
print()
'''

'''
class Toplama:
    def sonuc(self, a, b):
        print(f"toplama sonucu : {a + b}")


class Carpma(Toplama):
    def sonuc(self, a, b):
        print(f"çarpma sonucu : {a * b}")


class Bölme(Toplama):
    def sonuc(self, a, b):
        print(f"bölme sonucu : {a / b}")


class Cikarma(Toplama):
    def sonuc(self, a, b):
        print(f"çıkarma sonucu : {a - b}")



topla1 = Toplama()
topla1.sonuc(5, 8)

carp1 = Carpma()
carp1.sonuc(4, 12)

böl1 = Bölme()
böl1.sonuc(22, 11)

cikar1 = Cikarma()
cikar1.sonuc(50, 35)

'''

'''
class Personel:
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas

    
    def tam_isim(self):
        print(f"personelin adı-soyadı = {self.isim} {self.soyisim}")
    
    
    def email(self):
        print(f"personelin email adresi = {self.isim}.{self.soyisim}_@hotmail.com")
    
    
    def maas_göster(self):
        print(f"personelin maaşı = {self.maas}")
    
    
    def maas_zammi(self, zam_orani):
        print(f"personelin zam oranı {zam_orani} olup zamlı maaşı {self.maas * zam_orani} liradır.")


per1 = Personel("ali", "okan", 23000)
per1.tam_isim()
print()
per1.email()
print()
per1.maas_göster()
print()
per1.maas_zammi(1.5)
print("_"*50)


class Profesör_Doktor(Personel):
    def __init__(self, isim, soyisim, maas):
        super().__init__(isim, soyisim, maas)
    
    
    def tam_isim(self):
        print(f"profesör doktorun adı-soyadı = {self.isim} {self.soyisim}")
    
    
    def email(self):
        print(f"profesör doktorun email adresi = {self.isim}.{self.soyisim}@gmail.com")
    
    
    def maas_göster(self):
        print(f"profesör doktorun maaşı = {self.maas}")
    
    
    def maas_zammi(self, zam_orani):
        print(f"profesör doktorun zam oranı {zam_orani} olup zamlı maaşı {self.maas * zam_orani} liradır.")
    
    
prof1 = Profesör_Doktor("alper", "somun", 150000)
prof1.tam_isim()
print()
prof1.email()
print()
prof1.maas_göster()
print()
prof1.maas_zammi(1.2)
print("_"*50)


class Docent_Doktor(Personel):
    def __init__(self, isim, soyisim, maas):
        super().__init__(isim, soyisim, maas)
    

    def tam_isim(self):
        print(f"doçent doktorun adı-soyadı = {self.isim} {self.soyisim}")
    
    
    
    def email(self):
        print(f"doçent doktorun email adresi = {self.isim}.{self.soyisim}_@yandexmail.com")
    
    
    
    def maas_göster(self):
        print(f"doçent doktorun maaşı = {self.maas}")
    
    
    
    def maas_zammi(self, zam_orani):
        print(f"doçent doktorun zam oranı {zam_orani} olup zamlı maaşı {self.maas * zam_orani} liradır.")


doc1 = Docent_Doktor("ayhan", "aras", 120000)
doc1.tam_isim()
print()
doc1.email()
print()
doc1.maas_göster()
print()
doc1.maas_zammi(1.3)
print("_"*50)


class Hemsire(Profesör_Doktor):
    def __init__(self, isim, soyisim, maas):
        super().__init__(isim, soyisim, maas)
    

    def tam_isim(self):
        print(f"hemşirenin adı-soyadı = {self.isim} {self.soyisim}")
    
    
    
    def email(self):
        print(f"hemşirenin email adresi = {self.isim}.{self.soyisim}_@yahomail.com")
    
    
    
    def maas_göster(self):
        print(f"hemşirenin maaşı = {self.maas}")
    
    
    
    def maas_zammi(self, zam_orani):
        print(f"hemşirenin zam oranı {zam_orani} olup zamlı maaşı {self.maas * zam_orani} liradır.")


hem1 = Hemsire("ayşe", "yıldız", 30000) 
hem1.tam_isim()
print()
hem1.email()
print()
hem1.maas_göster()
print() 
hem1.maas_zammi(1.8)

'''

'''
class Audi:
    zam_orani = 1.2
    fiyat = 5000000
    hizi = 400
    hiz_artis_orani = 1.1
    
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    
    def zamli_fiyat(self):
        print(f"aracın zamlı fiyatı = {self.fiyat * self.zam_orani}")
    
    def hizini_arttir(self):
        print(f"aracın hızı arttırıldıktan sonra yeni hızı = {self.hizi * self.hiz_artis_orani}")

a1 = Audi("audi", "a6")
a1.zamli_fiyat()
a1.hizini_arttir()


class Skoda(Audi):
    zam_orani = 1.3
    fiyat = 1500000
    hizi = 250
    hiz_artis_orani = 1.2
    def __init__(self, marka, model):
        super().__init__(marka, model)
    
s1 = Skoda("skoda", "octavia")
s1.zamli_fiyat()
s1.hizini_arttir()


class Opel(Skoda):
    zam_orani = 1.4
    fiyat = 2000000
    hizi = 300
    hiz_artis_orani = 1.3
    def __init__(self, marka, model):
        super().__init__(marka, model)

o1 = Opel("opel", "astra")
o1.zamli_fiyat()
o1.hizini_arttir()


class Nissan(Opel):
    zam_orani = 1.5
    fiyat = 2500000
    hizi = 200
    hiz_artis_orani = 1.4
    def __init__(self, marka, model):
        super().__init__(marka, model)

n1 = Nissan("nissan", "qashqai")
n1.zamli_fiyat()
n1.hizini_arttir()
'''





        
