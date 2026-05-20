

from abc import ABC, abstractmethod  
from typing import Optional, List    


class Kaynak(ABC):
   
    def __init__(self, baslik: str, kayit_no: str):
        
        self._baslik = baslik
        self._kayit_no = kayit_no

   
    @property
    def baslik(self) -> str:
        
        return self._baslik

    @baslik.setter
    def baslik(self, deger: str):
        
        if not deger.strip():
            raise ValueError("Başlık boş olamaz!")
        self._baslik = deger.strip()


    @property
    def kayit_no(self) -> str:
       
        return self._kayit_no

    @kayit_no.setter
    def kayit_no(self, deger: str):
   
        if not deger.strip():
            raise ValueError("Kayıt numarası boş olamaz!")
        self._kayit_no = deger.strip()



class Kitap(Kaynak):
    

    def __init__(self, baslik: str, kayit_no: str,
                 yazar: str, sayfa_sayisi: int):
       
        super().__init__(baslik, kayit_no)
        self._yazar = yazar
        self._sayfa_sayisi = sayfa_sayisi

    
    @property
    def yazar(self) -> str:
        return self._yazar

    @yazar.setter
    def yazar(self, deger: str):
        if not deger.strip():
            raise ValueError("Yazar adı boş olamaz!")
        self._yazar = deger.strip()

   
    @property
    def sayfa_sayisi(self) -> int:
        return self._sayfa_sayisi

    @sayfa_sayisi.setter
    def sayfa_sayisi(self, deger: int):
        if deger <= 0:
            raise ValueError("Sayfa sayısı pozitif olmalıdır!")
        self._sayfa_sayisi = deger

    def __str__(self) -> str:
        return (f"[KİTAP] Kayıt No: {self._kayit_no} | "
                f"Başlık: {self._baslik} | "
                f"Yazar: {self._yazar} | "
                f"Sayfa: {self._sayfa_sayisi}")



class Dergi(Kaynak):
   

    def __init__(self, baslik: str, kayit_no: str,
                 yayin_donemi: str, sayi_no: int):
        super().__init__(baslik, kayit_no)
        self._yayin_donemi = yayin_donemi
        self._sayi_no = sayi_no

   
    @property
    def yayin_donemi(self) -> str:
        return self._yayin_donemi

    @yayin_donemi.setter
    def yayin_donemi(self, deger: str):
        gecerli = ["aylık", "haftalık", "yıllık", "üç aylık"]
        if deger.lower().strip() not in gecerli:
            raise ValueError(f"Yayın dönemi şunlardan biri olmalı: {gecerli}")
        self._yayin_donemi = deger.strip()

    @property
    def sayi_no(self) -> int:
        return self._sayi_no

    @sayi_no.setter
    def sayi_no(self, deger: int):
        if deger <= 0:
            raise ValueError("Sayı numarası pozitif olmalıdır!")
        self._sayi_no = deger

 
    def __str__(self) -> str:
        return (f"[DERGİ]  Kayıt No: {self._kayit_no} | "
                f"Başlık: {self._baslik} | "
                f"Dönem: {self._yayin_donemi} | "
                f"Sayı No: {self._sayi_no}")



class Islem(ABC):
   
    @abstractmethod
    def ekle(self):
        pass

    @abstractmethod
    def sil(self):
        pass

    @abstractmethod
    def guncelle(self):
        pass

    @abstractmethod
    def listele(self):
        pass



class KitapIslem(Islem):


    def __init__(self):
    
        self._kitaplar: List[Kitap] = []

   
    def _kayit_no_bul(self, kayit_no: str) -> Optional[Kitap]:
        for kitap in self._kitaplar:
            if kitap.kayit_no == kayit_no:
                return kitap
        return None

   
    def kitap_sayisi(self) -> int:
        return len(self._kitaplar)

   
    def ekle(self):
        print("\n── Kitap Ekle ──────────────────────────────")
        baslik    = input("Başlık        : ").strip()
        kayit_no  = input("Kayıt No      : ").strip()

       
        if self._kayit_no_bul(kayit_no):
            print(f" '{kayit_no}' kayıt numarası zaten mevcut!")
            return

        yazar     = input("Yazar         : ").strip()
        try:
            sayfa = int(input("Sayfa Sayısı  : "))
        except ValueError:
            print("  Sayfa sayısı tam sayı olmalıdır!")
            return

        try:
            kitap = Kitap(baslik, kayit_no, yazar, sayfa)
            self._kitaplar.append(kitap)
            print(f"\nKitap başarıyla eklendi.")
            print(f"    Toplam Kitap Sayısı: {self.kitap_sayisi()}")
        except ValueError as e:
            print(f" Hata: {e}")

  
    def sil(self):
        print("\n── Kitap Sil ───────────────────────────────")
        kayit_no = input("Silinecek Kayıt No: ").strip()
        kitap = self._kayit_no_bul(kayit_no)
        if kitap:
            self._kitaplar.remove(kitap)
            print(f"'{kitap.baslik}' kitabı silindi.")
            print(f"    Toplam Kitap Sayısı: {self.kitap_sayisi()}")
        else:
            print(f"'{kayit_no}' kayıt numaralı kitap bulunamadı.")

  
    def guncelle(self):
        print("\n── Kitap Güncelle ──────────────────────────")
        kayit_no = input("Güncellenecek Kayıt No: ").strip()
        kitap = self._kayit_no_bul(kayit_no)
        if not kitap:
            print(f" '{kayit_no}' kayıt numaralı kitap bulunamadı.")
            return

        print(f"Mevcut: {kitap}")
        print("(Değiştirmek istemediğiniz alanı boş bırakın)\n")

        yeni_baslik = input(f"Yeni Başlık [{kitap.baslik}]     : ").strip()
        yeni_yazar  = input(f"Yeni Yazar  [{kitap.yazar}]      : ").strip()
        yeni_sayfa  = input(f"Yeni Sayfa  [{kitap.sayfa_sayisi}]: ").strip()

        try:
            if yeni_baslik:
                kitap.baslik = yeni_baslik
            if yeni_yazar:
                kitap.yazar = yeni_yazar
            if yeni_sayfa:
                kitap.sayfa_sayisi = int(yeni_sayfa)
            print(" Kitap başarıyla güncellendi.")
            print(f"    Güncel: {kitap}")
        except ValueError as e:
            print(f" Hata: {e}")

   
    def listele(self):
        print("\n── Kitap Listesi ───────────────────────────")
        
        if not self._kitaplar:
            print("  Kayıt bulunamadı. Henüz kitap eklenmemiş.")
            return
        for i, kitap in enumerate(self._kitaplar, start=1):
            print(f"  {i:2}. {kitap}")
        print(f"\n  Toplam: {self.kitap_sayisi()} kitap")



class DergiIslem(Islem):
    

    def __init__(self):
        self._dergiler: List[Dergi] = []

    def _kayit_no_bul(self, kayit_no: str) -> Optional[Dergi]:
        for dergi in self._dergiler:
            if dergi.kayit_no == kayit_no:
                return dergi
        return None

    def dergi_sayisi(self) -> int:
        return len(self._dergiler)

    def ekle(self):
        print("\n── Dergi Ekle ──────────────────────────────")
        baslik   = input("Başlık            : ").strip()
        kayit_no = input("Kayıt No          : ").strip()

        if self._kayit_no_bul(kayit_no):
            print(f" '{kayit_no}' kayıt numarası zaten mevcut!")
            return

        print("Yayın Dönemi Seçenekleri: aylık / haftalık / yıllık / üç aylık")
        yayin_donemi = input("Yayın Dönemi      : ").strip()

        try:
            sayi_no = int(input("Sayı No           : "))
        except ValueError:
            print(" Sayı numarası tam sayı olmalıdır!")
            return

        try:
            dergi = Dergi(baslik, kayit_no, yayin_donemi, sayi_no)
            self._dergiler.append(dergi)
            print(f"\n  Dergi başarıyla eklendi.")
            print(f"    Toplam Dergi Sayısı: {self.dergi_sayisi()}")
        except ValueError as e:
            print(f"  Hata: {e}")

    def sil(self):
        print("\n── Dergi Sil ───────────────────────────────")
        kayit_no = input("Silinecek Kayıt No: ").strip()
        dergi = self._kayit_no_bul(kayit_no)
        if dergi:
            self._dergiler.remove(dergi)
            print(f" '{dergi.baslik}' dergisi silindi.")
            print(f"    Toplam Dergi Sayısı: {self.dergi_sayisi()}")
        else:
            print(f" '{kayit_no}' kayıt numaralı dergi bulunamadı.")

    def guncelle(self):
        print("\n── Dergi Güncelle ──────────────────────────")
        kayit_no = input("Güncellenecek Kayıt No: ").strip()
        dergi = self._kayit_no_bul(kayit_no)
        if not dergi:
            print(f" '{kayit_no}' kayıt numaralı dergi bulunamadı.")
            return

        print(f"Mevcut: {dergi}")
        print("(Değiştirmek istemediğiniz alanı boş bırakın)\n")

        yeni_baslik  = input(f"Yeni Başlık  [{dergi.baslik}]          : ").strip()
        yeni_donem   = input(f"Yeni Dönem   [{dergi.yayin_donemi}]    : ").strip()
        yeni_sayi    = input(f"Yeni Sayı No [{dergi.sayi_no}]         : ").strip()

        try:
            if yeni_baslik:
                dergi.baslik = yeni_baslik
            if yeni_donem:
                dergi.yayin_donemi = yeni_donem
            if yeni_sayi:
                dergi.sayi_no = int(yeni_sayi)
            print(" Dergi başarıyla güncellendi.")
            print(f"    Güncel: {dergi}")
        except ValueError as e:
            print(f" Hata: {e}")

    def listele(self):
        print("\n── Dergi Listesi ───────────────────────────")
        if not self._dergiler:
            print("  Kayıt bulunamadı. Henüz dergi eklenmemiş.")
            return
        for i, dergi in enumerate(self._dergiler, start=1):
            print(f"  {i:2}. {dergi}")
        print(f"\n  Toplam: {self.dergi_sayisi()} dergi")




class Menu:
    @staticmethod
    def goster():
        
        print("KÜTÜPHANE")
        print("═" * 20)
        print("  KİTAP İŞLEMLERİ")
        print("  1. Kitap Ekle")
        print("  2. Kitap Sil")
        print("  3. Kitap Güncelle")
        print("  4. Kitapları Listele")
        print("─" * 20)
        print("  DERGİ İŞLEMLERİ")
        print("  5. Dergi Ekle")
        print("  6. Dergi Sil")
        print("  7. Dergi Güncelle")
        print("  8. Dergileri Listele")
        print("─" * 20)
        print("  9. Çıkış")
        print("═" * 20)

def main():
    menu         = Menu()
    kitap_islem  = KitapIslem()
    dergi_islem  = DergiIslem()


    islemler = {
        "1": kitap_islem.ekle,
        "2": kitap_islem.sil,
        "3": kitap_islem.guncelle,
        "4": kitap_islem.listele,
        "5": dergi_islem.ekle,
        "6": dergi_islem.sil,
        "7": dergi_islem.guncelle,
        "8": dergi_islem.listele,
    }

    while True:
        menu.goster()
        secim = input("Yapmak istediğiniz işlemi seçin (1-9): ").strip()

        if secim == "9":
            print("\n Sistemden çıkılıyor. İyi günler!")
            break
        elif secim in islemler:
            islemler[secim]()  
        else:
            print("  Geçersiz seçim! Lütfen 1-9 arasında bir değer girin.")

        input("\n[Devam etmek için Enter'a basın...]")


if __name__ == "__main__":
    main()