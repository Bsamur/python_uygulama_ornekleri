
import sqlite3
class Kutuphane():


    db = sqlite3.connect(r"C:\Users\LENOVO\Desktop\python_kurs\grup0041\bahadir\kütüphane2.db")
    cur=db.cursor()



    def sorgulama():
        sorgu = "SELECT Id,adi,yazar FROM kitaplar;"
        Kutuphane.cur.execute(sorgu)
        sonuc=Kutuphane.cur.fetchall()


        for i in sonuc:


            print(i)

    def kayit():

        print("kaydetmek istediğiniz kişinin bilgilerini adi,soyadi,tel no olacak şekilde giriniz")
        a=input('adi:')
        s = input('soyadi:')
        t = input('tel no:')

        sorgu = """INSERT INTO ogrenciler(adi,soyadi,tel)
        VALUES
        ('{}', '{}','{}');""".format(a,s,t)
        sorgu2 = "SELECT Id,adi,soyadi,tel FROM ogrenciler;"
        Kutuphane.cur.execute(sorgu2)
        sonuc = Kutuphane.cur.fetchall()
        for i in sonuc:
            print(i)

        Kutuphane.cur.execute(sorgu)
        Kutuphane.db.commit()
        Kutuphane.cur.close()
        Kutuphane.db.close()

        print("veriler başarıyla kayıt edildi")


Kutuphane.sorgulama()
Kutuphane.kayit()