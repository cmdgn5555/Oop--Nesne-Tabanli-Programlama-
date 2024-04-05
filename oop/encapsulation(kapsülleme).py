
'''
class BankaHesabi:
    __banka_adi = "HSBC"
    __subesi = "Çankaya"
    
    def __init__(self, isim, soyisim, para_miktari, kimlik_no, borcu, hesaptan_cekilen_para_miktari):
        self.isim = isim
        self.soyisim = soyisim
        self.__para_miktari = para_miktari
        self.__kimlik_no = kimlik_no
        self.__borcu = borcu
        self.__hesaptan_cekilen_para_miktari = hesaptan_cekilen_para_miktari
    
    def getMoney(self):
        return self.__para_miktari
    
    def setMoney(self, yeni_miktar):
        self.__para_miktari = yeni_miktar
    
    def depositMoney(self):
        self.__para_miktari = self.__para_miktari + 2000
    
    def sendMoney(self):
        self.__para_miktari = self.__para_miktari - 5000
    
    def getIdNo(self):
        return self.__kimlik_no
    
    def __setIdNo(self, yeni_kimlik_nosu):
        self.__kimlik_no = yeni_kimlik_nosu
    
    def getBankName(self):
        return self.__banka_adi
    
    def getBankBranch(self):
        return self.__subesi
    
    def show_debt(self):
        return self.__borcu
    
    def collect_debt(self):
        self.__para_miktari = self.__para_miktari - self.__borcu
        
    def withdrawMoney(self):
        self.__para_miktari = self.__para_miktari - self.__hesaptan_cekilen_para_miktari
        

    

müsteri1 = BankaHesabi("metin", "aybars", 100000, 123456, 65000, 1000)
müsteri2 = BankaHesabi("şevket", "ozan", 200000, 998877, 80000, 2000)

print(müsteri1.isim)
print(müsteri1.soyisim)
print(müsteri1.getMoney())
print("_"*50)
print(müsteri2.isim)
print(müsteri2.soyisim)

print(müsteri2.getMoney())
müsteri2.setMoney(3850000)
print(müsteri2.getMoney())
print("__"*50)
print(müsteri1.getMoney())
müsteri1.depositMoney()
print(müsteri1.getMoney())
print("_"*100)
print(müsteri1.getMoney())
müsteri1.sendMoney()
print(müsteri1.getMoney())
print("_"*100)
print(müsteri1.getMoney())
müsteri1.sendMoney()
print(müsteri1.getMoney())
print("_"*200)
print(müsteri2.getMoney())
müsteri2.setMoney(3250000)
print(müsteri2.getMoney())
müsteri2.depositMoney()
print(müsteri2.getMoney())
müsteri2.sendMoney()
print(müsteri2.getMoney())
print("_"*100)
print(müsteri1.getIdNo())
print(müsteri2.getIdNo())
print("_"*100)
#print(müsteri1.banka_adi)
#print(müsteri2.banka_adi)
#müsteri1.setIdNo(99999)
#müsteri2.setIdNo(88888)
print(müsteri1.getIdNo())
print(müsteri2.getIdNo())
print("_"*100)
print(müsteri1.getBankName())
print(müsteri2.getBankName())
print()
print(müsteri1.getBankBranch())
print(müsteri2.getBankBranch())
print("_"*100)
#print(müsteri1.borcu)
#print(müsteri2.borcu)
print(müsteri1.show_debt())
print(müsteri2.show_debt())
print("_"*200)
müsteri3 = BankaHesabi("mehmet", "şen", 400000, 10203040, 75000, 25000)
print(müsteri3.getMoney())
print()
print(müsteri3.show_debt())
print()
müsteri3.collect_debt()
print(müsteri3.getMoney())
print()
müsteri3.withdrawMoney()
print(müsteri3.getMoney())

'''

'''
class Personel:
    
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.__zam_orani = 1.2
    
    def zam_yap(self):
        self.maas = self.maas * self.__zam_orani
    
    def __getZamOrani(self):
        return self.__zam_orani
    
    def setZamOrani(self, yeni_zam_orani):
        self.__zam_orani = yeni_zam_orani


p1 = Personel("can", "demir", 25000)
#print(p1.maas)
#print()
#print(p1.getZamOrani())
#print()
#p1.zam_yap()
#print(p1.maas)
#print()
#p1.setZamOrani(1.8)
#print(p1.getZamOrani())
#p1.zam_yap()
#print(p1.maas)
#print()
#p1.__zam_orani = 1.5
#print(p1.getZamOrani())
#p1.zam_yap()
#print(p1.maas)
print(help(p1))
print(p1.getZamOrani())

'''

'''
class Ogrenci:
    def __init__(self, isim, soyisim, vize, final):
        self.isim = isim
        self.soyisim = soyisim
        self.__vize = vize
        self.__final = final
    
    def getVize(self):
        return self.__vize
    
    def getFinal(self):
        return self.__final
    
    def setVize(self, yeni_vize):
        if yeni_vize < 0 or yeni_vize > 100:
            raise ValueError("vize notu 0 dan küçük yada 100 den büyük olamaz!")
        else:
            self.__vize = yeni_vize
        return self.__vize
    
    def setFinal(self, yeni_final):
        if yeni_final < 0 or yeni_final > 100:
            raise ValueError("final notu 0 dan küçük yada 100 den büyük olamaz!")
        else:
            self.__final = yeni_final
        return self.__final
    
    def notHesapla(self):
        return int(self.__vize * 0.3 + self.__final * 0.7)
    
    def kaldi_mi_gecti_mi(self):
        not_ortalaması = self.notHesapla()
        if 0 <= not_ortalaması < 50:
            return f"öğrenci sınıfta kalmıştır! not ortalaması {not_ortalaması}"
        if 50 <= not_ortalaması <= 100:
            return f"öğrenci sınıfı geçmiştir... not ortalaması {not_ortalaması}"


ogr = Ogrenci("hakan", "başeren", 90, 40)
print(ogr.isim)
print(ogr.soyisim)
print(ogr.getVize())
print(ogr.getFinal())
print(ogr.notHesapla())
print("_"*50)

ogr2 = Ogrenci("alper", "ercan", 50, 100)
print(ogr2.notHesapla())
print(ogr2.setVize(49))
print(ogr2.notHesapla())
print()
ogr2.setFinal(50)
print(ogr2.notHesapla())
print(ogr2.kaldi_mi_gecti_mi())
print("_"*30)
print(ogr.getVize())
print(ogr.getFinal())
ogr.setVize(30)
ogr.setFinal(60)
print(ogr.notHesapla())
print(ogr.kaldi_mi_gecti_mi())

'''

'''
class Basketbolcu:
    def __init__(self, isim, soyisim, takimi, üclük, ikilik, serbest_atis):
        self.isim = isim
        self.soyisim = soyisim
        self.takimi = takimi
        self._üclük = üclük
        self._ikilik = ikilik
        self.__serbest_atis = serbest_atis
    
    def bilgileri_göster(self):
        return f"adı = {self.isim} soyadı = {self.soyisim} takımı = {self.takimi}"
    
    def getSerbestAtis(self):
        return self.__serbest_atis
    
    def setSerbestAtis(self, yeni_serbest_atis):
        self.__serbest_atis = yeni_serbest_atis
        return self.__serbest_atis
    
    def __toplam_sayi(self):
        toplam = self._üclük + self._ikilik + self.__serbest_atis
        return toplam
    
    def toplam_sayiyi_göster(self):
        tüm_toplam = self.__toplam_sayi()
        return tüm_toplam

basketci1 = Basketbolcu("michael", "jordan", "chicago bulls", 150, 200, 250)
print(basketci1.bilgileri_göster())
print(f"üçlük sayısı = {basketci1._üclük}")
print(f"ikilik sayısı = {basketci1._ikilik}")
#print(f"serbest atış sayısı = {basketci1.__serbest_atis}")
print(f"serbest atış sayısı = {basketci1.getSerbestAtis()}")
basketci1.setSerbestAtis(500)
print(f"serbest atış sayısı = {basketci1.getSerbestAtis()}")
basketci1._ikilik = 1000
print(f"ikilik sayısı = {basketci1._ikilik}")
#print(f"toplam sayı = {basketci1.__toplam_sayi()}")
print(f"toplam sayıyı göster = {basketci1.toplam_sayiyi_göster()}")

'''

'''
class Araba:
    def __init__(self, marka, model, fiyat, hiz, yakit_deposu):
        self.marka = marka
        self.model = model
        self.__fiyat = fiyat
        self.__hiz = hiz
        self.__yakit_deposu = yakit_deposu
        

    def __getFiyat(self):
        return self.__fiyat
    
    def __getHiz(self):
        return self.__hiz
    
    def hizini_arttir(self, hiz_artis_orani):
        return self.__hiz * hiz_artis_orani
    
    def fiyati_arttir(self, fiyat_artis_orani):
        return self.__fiyat * fiyat_artis_orani
    
    def yakit_deposu_arttir(self, arttirma_orani):
        return self.__yakit_deposu * arttirma_orani
    
    def arac_fiyatini_goster(self):
        fiyat = self.__getFiyat()
        return fiyat
    
    def arac_hizini_goster(self):
        hizi = self.__getHiz()
        return hizi
    
    def yakit_deposu_göster(self):
        return self.__yakit_deposu
    

arac1 = Araba("audi", "a5", 4000000, 380, 60)

print(f"aracın markası = {arac1.marka}")
print(f"aracın modeli = {arac1.model}")
#print(f"aracın fiyatı = {arac1.getFiyat()}")
#print(f"aracın hızı = {arac1.getHiz()}")
print(f"aracın fiyatı = {arac1.arac_fiyatini_goster()}")
print(f"aracın hızı = {arac1.arac_hizini_goster()}")
print(f"aracın hızı arttırıldıktan sonraki hızı = {arac1.hizini_arttir(1.4)}")
print(f"aracın fiyatı arttırıldıktan sonraki fiyatı = {arac1.fiyati_arttir(1.2)}")
print(f"aracın yakıt deposu = {arac1.yakit_deposu_göster()} litredir.")
print(f"aracın yeni yakıt deposu = {arac1.yakit_deposu_arttir(1.2)} litredir.")

'''














        








        





















        