""""
Google Scraper  Gerekli Modüller: BS4 - google - googlesearch-python
"""
from googlesearch import search

# '+' dan sonra gelen yere yazılan anahtar kelime veya kelimeler kullanıcı tarafından görülmez.
# kullanıcının yaptığı sorgu ile kendisini harmanlar. bunun için anahtar kelime veya kelimeler özenle seçilmeli
# yanına birkaç tane daha artı koyarak tek tek anahtar kelime yaratılabilir
# örnek + " Atatürk" + " Timur" + " Savaş" vesaire.
ip = input("Aramak istediğiniz sorguyu yazınız: ") + " Atatürk"

# num_results fonksiyonuna bir rakam girilmezse sonsuz arama yapar.
# rakam çok fazla olursa google IP bloke edebilir.
for url in search(ip, num_results=100):
    print(url)

# .EXE uzantısında CMD'nin direkt kapanmaması için basit çözüm.
print(" Linkleri bir yere kopyalayınız. Tekrar arama yapmak için programı kapatıp tekrar açınız. " "\n Programı kapatmak için ENTER tuşuna basınız")

input("...")
