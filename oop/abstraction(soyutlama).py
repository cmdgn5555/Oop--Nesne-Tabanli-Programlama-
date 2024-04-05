
'''
from abc import ABC, abstractmethod

class Human(ABC):

    @abstractmethod
    def walk(self):
        pass
    
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Person(Human):
    def __init__(self):
        super().__init__()
    
    def walk(self):
        print("ı am walking...")
    
    def run(self):
        print("ı am running...")
    
    def eat(self):
        print("ı am eating...")
    
    def sleep(self):
        print("ı am sleeping...")

p = Person()
p.run()
p.eat()
p.sleep()
p.walk()


class Sportsman(Human):
    def __init__(self):
        super().__init__()
    
    def walk(self):
        print("sportsman is walking...")
    
    def run(self):
        print("sportsman is running...")
    
    def eat(self):
        print("sportsman is eating...")
    
    def sleep(self):
        print("sportsman is sleeping...")
    

s = Sportsman()
s.walk()
s.eat()
s.sleep()
s.run()

'''

'''
from abc import ABC, abstractmethod

class İslemler(ABC):
    
    @abstractmethod
    def topla(self):
        pass
    
    @abstractmethod
    def cikar(self):
        pass
    
    @abstractmethod
    def carp(self):
        pass
    
    @abstractmethod
    def böl(self):
        pass


class Toplama(İslemler):
    def __init__(self):
        super().__init__()
    
    def topla(self):
        a = 10
        b = 20
        return f"toplama işleminin sonucu = {a + b}"
    
    def cikar(self):
        pass
    
    def carp(self):
        pass
    
    def böl(self):
        pass


top = Toplama()
print(top.topla())


class Cikarma(İslemler):
    def __init__(self):
        super().__init__()
    
    def topla(self):
        pass
    
    def cikar(self):
        a = 50
        b = 40
        return f"çıkarma işleminin sonucu = {a - b}"
    
    def carp(self):
        pass
    
    def böl(self):
        pass

cik = Cikarma()
print(cik.cikar())


class Carpma(İslemler):
    def __init__(self):
        super().__init__()
    
    def topla(self):
        pass
    
    def cikar(self):
        pass
    
    def carp(self):
        a = 15
        b = 12
        return f"çarpma işleminin sonucu = {a * b}"
        
    def böl(self):
        pass

car = Carpma()
print(car.carp())


class Bölme(İslemler):
    def __init__(self):
        super().__init__()
    
    def topla(self):
        pass
    
    def cikar(self):
        pass
    
    def carp(self):
        pass
        
    def böl(self):
        a = 100
        b = 4
        return f"bölme işleminin sonucu = {a / b}"

bol = Bölme()
print(bol.böl())

'''
from abc import ABC, abstractmethod

class Okul(ABC):
    
    @abstractmethod
    def tam_isim_göster(self):
        pass

    
    @abstractmethod
    def diger_bilgiler(self):
        pass

    def zam_uygula(self):
        pass


         
class Müdür(Okul):
    
    maas = 35000
    zam_orani = 1.4
    
    def __init__(self, isim, soyisim, boy, kilo, yas):
        self.isim = isim
        self.soyisim = soyisim
        self.boy = boy
        self.kilo = kilo
        self.yas = yas

    
    def tam_isim_göster(self):
        return f"isim = {self.isim} soyisim = {self.soyisim}" 
    
    
    def zam_uygula(self):
        return f"maaş = {self.maas} zam oranı = {self.zam_orani} zamlı maaş = { self.maas * self.zam_orani}"
    
    
    def diger_bilgiler(self):
        return f"boy = {self.boy} kilo = {self.kilo} yaş = {self.yas}"

m = Müdür("orhan", "demir", 172, 66, 57)
print(m.tam_isim_göster())
print(m.zam_uygula())
print(m.diger_bilgiler())

print("_"*100)


class Ögretmen(Okul):
    
    maas = 30000
    zam_orani = 1.3

    def __init__(self, isim, soyisim, boy, kilo, yas, bildigi_diller, hobiler):
        self.isim = isim
        self.soyisim = soyisim
        self.boy = boy
        self.kilo = kilo
        self.yas = yas
        self.bildigi_diller = bildigi_diller
        self.hobiler = hobiler
    
    
    def tam_isim_göster(self):
        return f"isim = {self.isim} soyisim = {self.soyisim}"
    
    
    def zam_uygula(self):
        return f"maaş = {self.maas} zam oranı = {self.zam_orani} zamlı maaş = { self.maas * self.zam_orani}"
    
    
    def diger_bilgiler(self):
        return f"boy = {self.boy} kilo = {self.kilo} yaş = {self.yas} bildiği diller = {self.bildigi_diller} hobiler = {self.hobiler}"
    
    
    def bildigi_diller_güncelle(self, dil):
        if dil not in self.bildigi_diller:
            self.bildigi_diller.append(dil)
        return self.bildigi_diller
    
    
    def hobiler_güncelle(self, hobi):
        if hobi not in self.hobiler:
            self.hobiler.append(hobi)
        return self.hobiler
      

ö = Ögretmen("ercan", "samet", 186, 82, 32, ["ingilizce", "almanca"], ["kitap okumak", "dans etmek"])
print(ö.tam_isim_göster())
print(ö.zam_uygula())
print(ö.diger_bilgiler())
print(ö.bildigi_diller_güncelle("italyanca"))
print(ö.hobiler_güncelle("balık tutmak"))
print(ö.diger_bilgiler())

print("_"*100)

class Ögrenci(Okul):
    
    def __init__(self, isim, soyisim, boy, kilo, yas):
        self.isim = isim
        self.soyisim = soyisim
        self.boy = boy
        self.kilo = kilo
        self.yas = yas
        
    
    def tam_isim_göster(self):
        return f"isim = {self.isim} soyisim = {self.soyisim}"
    
    
    def diger_bilgiler(self):
        return f"boy = {self.boy} kilo = {self.kilo} yaş = {self.yas}"
    
    
    def harf_notu_göster(self, vize, final):
        
        if 0 <= vize <= 100 and 0 <= final <= 100:
            not_ortalama = int(vize * 0.3 + final * 0.7)
            print(f"vize notu = {vize} final notu = {final} not ortalaması = {int(vize * 0.3 + final * 0.7)}")
        
            if 0 <= not_ortalama <= 29:
                return f"FF"
            elif 30 <= not_ortalama <= 39:
                return f"FD"
            elif 40 <= not_ortalama <= 44:
                return f"DD"
            elif 45 <= not_ortalama <= 54:
                return f"DC"
            elif 55 <= not_ortalama <= 64:
                return f"CC"
            elif 65 <= not_ortalama <= 75:
                return f"CB"
            elif 76 <= not_ortalama <= 80:
                return f"BB"
            elif 81 <= not_ortalama <= 87:
                return f"BA"
            elif 88 <= not_ortalama <= 100:
                return f"AA"
        else:
            return f"vize notu yada final notu 0 dan küçük 100 den büyük olamaz!"
    
    
    def devamsizlik_göster(self, gelmedigi_gün_sayisi):
        if gelmedigi_gün_sayisi > 20:
            return f"öğrencinin okula gelmediği gün sayısı {gelmedigi_gün_sayisi} gündür. 20 günden fazla olduğu için okulda kalmıştır..."
        if 0 <= gelmedigi_gün_sayisi <= 20:
            return f"öğrencinin okula gelmediği gün sayısı {gelmedigi_gün_sayisi} olup kalan devamsızlık gün sayısı {20 - gelmedigi_gün_sayisi} dir."
        
        
ögr = Ögrenci("mehmet", "tural", 170, 75, 22)
print(ögr.tam_isim_göster())
print(ögr.diger_bilgiler())
print(ögr.harf_notu_göster(50, 80))
print(ögr.devamsizlik_göster(5))











    
    




    




    







    







    







