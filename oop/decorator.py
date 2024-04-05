'''
def decorator(fonk):
    def wrapper():
        print("fonksiyon çalışmadan önceki işlemler")
        fonk()
        print("fonksiyon çalıştıktan sonraki işlemler")
    return wrapper

@decorator
def fonksiyon():
    print("fonksiyon çalışıyor")

fonksiyon()

'''

'''
import time

def yazdir(fonk):
    def wrapper():
        print("isim yazdırılıyor.")
        time.sleep(10)
        fonk()
        print("isim yazdırılıyor.")
        time.sleep(10)
        fonk()
        print("isim yazdırılıyor.")
        fonk()
        time.sleep(10)
        print("yazdırma bitti")
    return wrapper

@yazdir
def isim():
    print("kemal")

isim()

'''

'''
import time

def zaman_hesapla(fonk):
    def wrapper(*args):
        basla = time.time()
        fonk(*args)
        bitir = time.time()
        print(f"islem {bitir - basla} saniye sürdü.")
    return wrapper


@zaman_hesapla
def kareleri_al(liste):
    for i in liste:
        print(i ** 2)

@zaman_hesapla
def küpleri_al(liste):
    for i in liste:
        print(i ** 3)

@zaman_hesapla
def topla(a, b):
    time.sleep(1)
    print(a + b)

topla(4, 14)

'''

'''
import time

def hesapla(fonk):
    def wrapper(a, b):
        baslangic = time.time()
        print("işlemler yapılıyor")
        time.sleep(3)
        fonk(a, b)
        bitis = time.time()
        print(f"işlem {bitis - baslangic} saniyede bitti!")
    return wrapper


@hesapla
def topla(a, b):
    print(f"toplama işleminin sonucu = {a + b}")

@hesapla
def cikar(a, b):
    print(f"çıkarma işleminin sonucu = {a - b}")

@hesapla
def carp(a, b):
    print(f"çarpma işleminin sonucu = {a * b}")

@hesapla
def böl(a, b):
    print(f"bölme işleminin sonucu = {a / b}")

topla(20, 15)
cikar(30, 15)
carp(12, 15)
böl(60, 15)

'''

'''
import time

def hesapla(fonk):
    def wrapper(a):
        baslangic = time.time()
        time.sleep(2)
        sonuc = fonk(a)
        bitis = time.time()
        print(f"işlem {bitis - baslangic} saniye sürdü..")
        return sonuc
    return wrapper

@hesapla
def faktöriyel(a):
    fakt =1
    for i in range(1, a + 1):
        fakt *= i
    return fakt

print(faktöriyel(10))


@hesapla
def küpleri_al(a):
    küpler_listesi = []
    for i in a:
        küpler_listesi.append(i ** 3)
    return küpler_listesi

print(küpleri_al(range(100)))



@hesapla
def kareleri_al(a):
    kareler_listesi = []
    for i in a:
        kareler_listesi.append(i ** 2)
    return kareler_listesi

print(kareleri_al(range(100)))

'''

'''
def ikiyle_carp(fonk):
    def wrapper(a, b, c):
        sonuc = fonk(a*2, b*2, c*2)
        return sonuc
    return wrapper


@ikiyle_carp
def topla(a, b, c):
    return a + b + c

print(topla(5, 10, 15))


def karesini_al(fonk):
    def wrapper(a, b, c, d, e):
        sonuc = fonk(a**0.5, b**0.5, c**0.5, d**0.5, e**0.5)
        return sonuc
    return wrapper


@karesini_al
def sayilar(a, b, c, d, e):
    return a, b, c, d, e 

print(sayilar(16, 25, 36, 49, 64))


def küpünü_al(fonk):
    def wrapper(a, b, c, d, e):
        sonuc = fonk(a**3, b**3, c**3, d**3, e**3)
        return sonuc
    return wrapper


@küpünü_al
def sayilar(a, b, c, d, e):
    return a, b, c, d, e

print(sayilar(2, 4, 6, 10, 20))

'''

'''
def dene():
    print("xyz")

dene()

f = dene

f()

def deneme():
    print("deneme çalışıyor")

    def test():
        return "test çalışıyor"
    
    print(test())

print(deneme())
print("__"*50)

def decorator(fonk):
    def wrapper():
        print("başla")
        fonk()
        print("bitir")
       
    return wrapper


@decorator
def yaz():
    print("yazılıyor") 

yaz()

'''

'''
import time

def süre(fonk):
    def wrapper(x):
        baslama = time.time()
        sonuc = fonk(x)
        bitis = time.time()
        print(f"işlem {bitis - baslama} saniye sürdü!!")
        return sonuc
    return wrapper


@süre
def faktöriyel(x):
    fakt = 1
    for i in range(1, x + 1):
        fakt *= i
    return fakt

print(faktöriyel(5))


def süre(fonk):
    def wrapper(*args):
        baslama = time.time()
        sonuc = fonk(*args)
        bitis = time.time()
        print(f"işlem {bitis - baslama} saniye sürdü!!")
        time.sleep(5)
        return sonuc
    return wrapper

@süre
def küp_al(liste):
    küp_list = []
    for i in liste:
        küp_list.append(i ** 3)
    return küp_list

print(küp_al(range(100000)))

'''












        




 
    












