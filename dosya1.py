import os
dosya=open(r"C:\Users\LENOVO\Desktop\python kurs\grup0041\bahadir\dosya.txt","w")

for i in range(5):

    dosya.write("merhaba dünya"+"\n")

dosya.close()
""" 1-write(w): dosya yoksa oluşturur, varsa tüm içeriği silip yeni bilgiyi ekler
    2-append(a): dosya yoksa oluşturur, varsa yeni bilgiyi değiştirmez girmiş olduğumuz bilgiyi en sona ekler.
    3-read(r): dosyayı okuma modunda açar. bu modda birşey yazılamaz sadece okuma yapılabilir.dosya yoksa hata verir...
"""