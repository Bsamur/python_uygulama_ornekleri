import random
import time


class kumandaprogramı():
    def __init__(self,tv_durum="kapalı",tv_kanal_listesi=["star","trt"],tv_sesi=0,tv_kanal_değiştir="TRT") :
        self.tv_durum=tv_durum
        self.tv_kanal_listesi=tv_kanal_listesi
        self.tv_sesi=tv_sesi
        self.tv_kanal_değiştir=tv_kanal_değiştir
    def __len__(self):
        print("kanal listesi uzunluğu:",len(self.tv_kanal_listesi))
    def tv_aç(self):
        if self.tv_durum=="kapalı":
            print("tv açılıyor")
            self.tv_durum="açık"
        else:
            print("tv açık durumda")
    def tv_kapat(self):
        if self.tv_durum=="açık":
            print("tv kapanıyor")
            self.tv_durum="kapalı"
        else:
            print("tv kapalı durumda")
    def tv_sesi(self):
        while True:
            ses_seviyesi=input("seviyeyi artırmak için '>' basınız\nseviyeyi azaltmak için '<' basınız")
            if ses_seviyesi=='>':
                if self.tv_sesi!=20:
                    self.tv_sesi+=1
                    print("ses seviyesi:",self.tv_sesi)
            elif ses_seviyesi=='<':
                if self.tv_sesi!=0:
                    self.tv_sesi-=1
                    print("ses seviyesi:",self.tv_sesi)
            else:
                print("seviye :",self.tv_sesi)
                break
            
    def kanal_ekleme(self,kanal_ismi):
        self.tv_kanal_listesi.append(kanal_ismi)
       
        
        
        
        