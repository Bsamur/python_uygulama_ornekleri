import sqlite3 as sql

from debugpy import connect


class kutuphane():
    def __init__(self) :
        self.baglan()
    
    def baglan(self):
        self.db=sql.connect(r"C:\Users\LENOVO\Desktop\python_kurs\grup0041\bahadir\kütüphane4.db")
        self.cur=self.db.cursor()
    def ogrenci_kayit(self,adi,soyadi,sehir_Id):
        self.isim=adi
        self.soyisim=soyadi
        self.sehir=sehir_Id
        
        sorgu=f"""
        INSERT INTO ogrenci(adi,soyadi,sehir_Id)
        VALUES
        ('{self.isim}','{self.soyisim}','{self.sehir}');
        
        """
        self.cur.execute(sorgu)
        self.db.commit()
        self.kapat()
        
    def kitap_kayit(self,adi,yazar):
        self.kitap_adi=adi
        self.yazar=yazar
        sorgu=f"""
        INSERT INTO kitaplar (adi,yazar)
        VALUES ('{self.kitap_adi}','{self.yazar}');
        """
        
        self.cur.execute(sorgu)
        self.db.commit()
        self.kapat()
        print("kitap kaydedildi.....")
    def ogrenci_listele(self):
        sorgu="""SELECT adi,soyadi FROM ogrenci; """
        self.cur.execute(sorgu)
        sonuc=self.cur.fetchall()
        for i in sonuc:
            print(i)
        self.kapat()
    def kitap_listele(self):
        sorgu="""SELECT adi,soyadi FROM kitaplar; """
        self.cur.execute(sorgu)
        sonuc=self.cur.fetchall()
        for i in sonuc:
            print(i)
        self.kapat()
    menu="""
    1-yeni öğrenci kayıt
    2-yeni kitap kayıt
    3-öğrenci listesi
    4-kitap"""
    
        
        
    def kapat(self):
        
        self.cur.close()
        self.db.close()
        print("veriler başarıyla kaydedildi....")
    while True:
        print(menu)
        secim=input("seçiminiz: ")

        if secim=="1":
            adi=input("öğrenci adi: ")
            soyadi=input("öğrenci soyadi: ")
            sehir_Id=input("şehir id: ")
            
            ogrenci_kayit(adi,soyadi,sehir_Id)
        elif secim=="2":
            adi=input("kitap adi: ")
            yazar=input("yazar ismi: ")
            
            kitap_kayit(adi,yazar)
        elif secim=="3":
            ogrenci_listele()
        elif secim=="4":
            kitap_listele()
ogr1=kutuphane()
ogr1.ogrenci_kayit("mehmet","rıza",43)
ogr1.kitap_kayit("Deliliğe Övgü","Desiderius Erasmus")