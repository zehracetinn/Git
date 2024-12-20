"""
#print("merhabaaa")
print("Merhaba, Dünya!")
print(5 + 3)
ad = "zehra"
yas = 19
print(ad)
print(yas)
sayi1 = 10     # int veri tipinde
sayi2 = 33.3   # float  veri tğipinde

print(sayi1)
print(sayi2)
mesaj = "Python"
harf = 'A'#char

print(mesaj)
print(harf)
dogruMu = True
yanlisMi = False

print(dogruMu)
print(yanlisMi)
print(5 > 3)  # Bu ifade True döner
print(2 > 7)  # Bu ifade False döner
# List örneği
meyveler = ["Elma", "Armut", "Muz", "Çilek"]
meyveler.append("Karpuz")  # Listeye yeni bir eleman ekleme
print(meyveler)

# Set örneği
sayilar = {1, 2, 3, 4, 2}  # Set'te aynı eleman tekrar etmez
sayilar.add(5)
print(sayilar)
# Tuple kullanımı basit bir örnek
renkler = ("Kırmızı", "Mavi", "Yeşil")
print(renkler)  # bütün tuple'ı ekrana yaz
print(renkler[0])  # ilk elemanı alıp yazdır

# tuple elemanları değiştirilemez. Aşağıdaki satırı açarsan hata verir:
# renkler[0] = "Sarı"



# Sözlük kullanımı
ogrenci = {
    "ad": "Ali",
    "yas": 21,
    "ders": "Python"
}

# Bilgileri yazdırmak
print(ogrenci["ad"])  # Ali'nin adı
print(ogrenci.get("yas"))  # Ali'nin yaşı

# Yeni bilgi ekle
ogrenci["not"] = 95  # not ekliyoruz
print(ogrenci)  # güncel hali yazdır


# Hava durumu kontrolü
hava_durumu = "gunesli"  # hava durumu gunesli

if hava_durumu == 'yagisli':
    print("Şemsiyeni al!")  # yağmur varsa şemsiye al
else:
    print("Hava gayet iyi.")  # yağmur yoksa sıkıntı yok

# biraz daha detaylı kontrol yapalım
hava_durumu = "karli"

if hava_durumu == 'yagisli':
    print("Şemsiyeni al!")  # yine şemsiye öner
elif hava_durumu == 'karli':
    print("Atkını unutma!")  # kar yağarsa atkı lazım
else:
    print("Gayet güzel, bir şey alman gerekmez.")



# Yorum bırakanlar ve moderatör kontrolü
yorum_birakanlar = ["Ismail Aydemir", "Uygar Aydin", "Naz Yagcioglu",
                    "Ferhat Ibrik", "Ulas Acil", "Bilal Kurucay"]

moderator = "Uygar Aydin"  # moderatör kim

# Herkesi kontrol et
for yorumcu in yorum_birakanlar:
    if yorumcu == moderator:
        print(f"{yorumcu} moderatör arkadaşımız.")
    else:
        print(f"{yorumcu} normal bir kullanıcı.")

moderator = "Ferhat Ibrik"

# Listeyi sıra numarası ile döner (1'den başlar)
for i, kullanici in enumerate(yorum_birakanlar, 1):
    ad, soyad = kullanici.split()  # İsim ve soyadı ayır
    if kullanici == moderator:  # Eğer kullanıcı moderatöre eşitse
        print(f"{i}. Moderatorun Adi {ad} ve Soyadi {soyad}")  # Moderatör bilgisi yazdır
    else:  # Moderatör değilse
        print(f"{i}. Kullanicinin Adi {ad} ve Soyadi {soyad}")  # Kullanıcı bilgisi yazdır
# Sözlük tanımlama
kullanici1 = {'ad': 'Naz', 'soyad': 'Yagcioglu'}

# Tüm anahtar-değer çiftlerini yazdır
for k, v in kullanici1.items():
    print("Key: {}\tValue: {}".format(k, v))  # Anahtar ve değeri yazdırır

# Sadece anahtarları yazdır
for k in kullanici1.keys():
    print("Key: {}".format(k))  # Anahtarları yazdırır
'''items() → Anahtar ve değeri döner.
keys() → Sadece anahtarları döner.
format() → String içinde değişkenleri yazdırır.
'''
print(17)
ulkeler =['TR' ,  'İNG','DANİMARKA']#lise
siralamalar =range (1,4)# bu sayılarv arasından sayı seçiyor
for ulke in zip(ulkeler,siralamalar)
    print(ulke)# dönüyor listdekdei ülkleleri ve yanına listeedği sayıları yazıyor
''''
break = anında döngüyü sonlandırmakmiçin kullanılır
continue = döngüde bir aşamda varsa o olanı sadece sonalndırır devamını devam eder
pass=bir blkota hiçbir işlem yapılması istenmediği zaman pass kullanılır 
def my_function():
    pass  # Henüz fonksiyonu doldurmadık



'''

def mesaj_ver(isim="Misafir"): #def diyince fonksiyon açıyor
    print(f"Merhaba, {isim}!")

# Fonksiyonu farklı argümanlarla çağırma kodı budur
mesaj_ver("Ali")
mesaj_ver()  # Default değer kullanırlar

# Global ve yerel değişkenler
x = 10  # Global değişkendir

def carp():
    y = 2  # Yerel değişkendirr
    return x * y  # Global 'x' kullanılır

print("Çarpım:", carp())


# map fonksiyonu ile her elemanı 2 ile çarpma bölümü
sayilar = [1, 2, 3, 4, 5]#liste tanımladık
carpim = list(map(lambda x: x * 2, sayilar))#map burda listedeki tüm elemnlara aynı işlemi uygular
print("Map ile çarpım:", carpim)

# filter fonksiyonu ile çift sayıları seçme
cift_sayilar = list(filter(lambda x: x % 2 == 0, sayilar))# filterde koşulu sağlayan elemları döndürmeyi sağlar #liseteye çeviririz
print("Filter ile cifft sayılar:", cift_sayilar)

# Kullanıcıdan bölme işlemini yapma kodu hatalarla
try:
    sayi1 = int(input("Birinci sayıyı girin: "))#input kullanıcıdan sayı girmeyi sağlar
    sayi2 = int(input("İkinci sayıyı girin: "))


    sonuc = sayi1 / sayi2  # Bölme işlemidir
    print(f"Bölüm: {sonuc}")#bölme işleminin sonuuucudur

except ZeroDivisionError:
    # Sıfıra bölme hatası için özel mesaj
    print("Hata: Bir sayı sıfıra bölünemez!")

except ValueError:
    # Geçersiz veri tipi hatası
    print("Hata: Lütfen geçerli bir sayı girin!")

except Exception as e:
    # Diğer tüm hatalar
    print(f"Beklenmeyen bir hata oluştu: {e}")


    class Ucak:#uçak adında bir sınıf tanımlıyoruz
        def __init__(self, kapasite):

class Ucak:
    def __init__(self, kapasite):
        """
        uçak nesnesi olusturuyoruz
        kapasiteyi giriyoruz ve yolcu sayısını başta 0 yapıyoruz
        """
        self.kapasite = kapasite  # uçağın toplam kapasitesi
        self.yolcu = 0  # yolcu sayısı sıfırla başlıyo

    def bos_koltuk_sayisi(self):
        """
        boş koltukları sayan bi fonk
        """
        return self.kapasite - self.yolcu  # boş koltuk sayısı hesaplanıyo

    def bilet_satis(self, bilet_adedi=1):
        """
        bilet satışı yapıyo. eğer kapasite dolarsa hata veriyo
        """
        if self.yolcu + bilet_adedi <= self.kapasite:
            self.yolcu += bilet_adedi  # yolcu sayısını arttırıyoruz
            print(f"{bilet_adedi} bilet satıldı. "
                  f"kalan koltuk: {self.bos_koltuk_sayisi()}.")
        else:
            print("kapasite doldu, satış olmadı!!!")

    def bilet_iptal(self, bilet_adedi=1):
        """
        bilet iptali yapılıyo ama eğer yolcu sayısından fazla iptal istenirse yapmıyo
        """
        if self.yolcu >= bilet_adedi:
            self.yolcu -= bilet_adedi  # yolcu sayısını düşürüyo
            print(f"{bilet_adedi} bilet iptal edildi. "
                  f"kalan koltuk: {self.bos_koltuk_sayisi()}.")
        else:
            print("iptal edilecek yolcu yok!!!")

    def ucus_bilgisi(self):
        """
        uçağın genel bilgilerini yazdırır
        """
        print(f"kapasite: {self.kapasite}")
        print(f"mevcut yolcu: {self.yolcu}")
        print(f"boş koltuk: {self.bos_koltuk_sayisi()}")


# uçak nesnesi oluşturuyoz kapasitesini de 150 yaptık
ucak = Ucak(kapasite=150)

# burda bir sürü işlem yapıyoruz
ucak.ucus_bilgisi()  # bilgileri yazdır
ucak.bilet_satis(30)  # 30 tane bilet sattık
ucak.bilet_satis(100)  # 100 bilet daha sattık
ucak.bilet_iptal(20)  # 20 bilet iptal ettik
ucak.bilet_satis(50)  # kapasite dolduğu için satamıyo
ucak.bilet_iptal(200)  # elimizde bu kadar yolcu yok, iptal etmiyo
ucak.ucus_bilgisi()  # son bilgileri yazdırıyoruz

import os  # dosya işlemleri için modül

# şuanki çalışma dizinini öğreniyoruz
print("şuanki dizin:", os.getcwd())

# yeni bir klasör açıyoruz
os.mkdir("Yeni_Klasor")  # 'Yeni_Klasor' diye bir klasör açıldı
print("'Yeni_Klasor' oluşturuldu.")

# mevcut dizindeki dosya ve klasörleri yazdırıyoruz
print("dosya/klasör listesi:", os.listdir())

# klasörün ismini değiştiriyoruz
os.rename("Yeni_Klasor", "Degistirilen_Klasor")  # klasör adı değişti
print("'Yeni_Klasor' -> 'Degistirilen_Klasor' olarak değiştirildi.")

# klasörü siliyoruz
os.rmdir("Degistirilen_Klasor")  # klasör usiliyoruz değiştiriyoruz d
print("'Degistirilen_Klasor' silindi.")

import re  # regex işlemleri için gerekli modül

# metin içinde eşleşme buluyoruz
metin = "Python programlama çok güzel bi şey!"
eslesme = re.search(r"Python", metin)  # 'Python' kelimesini bulmaya çalışıyoruz
if eslesme:
    print("eşleşme bulundu:", eslesme.group())

# metindeki tüm sayıları buluyoruz
metin = "123 ABC 456 DEF 789 GHI"
eslesmeler = re.findall(r"\d+", metin)  # sadece sayıları arıyoruz
print("bulunan sayılar:", eslesmeler)

# metindeki sayıları başka bişeyle değiştiriyoruz
duzenlenmis_metin = re.sub(r"\d+", "[SAYI]", metin)  # sayıları [SAYI] yapıyoruz
print("düzenlenmiş metin:", duzenlenmis_metin)

# telefon numarasını doğruluyoruz
metin = "Telefon numarası: 123-456-7890"
eslesme = re.search(r"\d{3}-\d{3}-\d{4}", metin)  # telefon formatını buluyoruz
if eslesme:
    print("telefon numarası bulundu:", eslesme.group())
else:
    print("telefon numarası yok!")

# Eğer bir eşleşme bulunursa, telefon numarasını ekrana yazdırır.
if eslesme:
    print("Geçerli bir telefon numarası bulundu:", eslesme.group())
    # `eslesme.group()` eşleşen metni döner, yani "123-456-7890"

# 2. E-posta doğrulama
email = "ornek@mail.com"

# `re.match` ile e-posta adresinin doğruluğunu kontrol ediyoruz.
# Regex deseni: [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
# - `[a-zA-Z0-9._%+-]+`: E-posta kullanıcı adı kısmı; harfler, sayılar ve bazı özel karakterler içerebilir.
# - `@`: E-posta adresinde "@" sembolü.
# - `[a-zA-Z0-9.-]+`: Alan adı kısmı; harfler, sayılar, nokta ve tire içerebilir.
# - `\.`: Nokta sembolü.
# - `[a-zA-Z]{2,}`: Alan adının son kısmı; en az 2 harf içermeli (örneğin, "com", "org").
email_dogrulama = re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email)

# Eğer bir eşleşme bulunursa, e-posta adresini ekrana yazdırır.
if email_dogrulama:
    print("Geçerli bir e-posta adresi bulundu:", email_dogrulama.group())
    # `email_dogrulama.group()` eşleşen metni döner, yani "ornek@mail.com"


import random  # Rastgele sayı seçmek için kullandık bu modülü.
import math  # Matematik işlemleri falan yapıcaz, o yüzden lazım.

# Rastgele bi sayı alıyoruz 1 ile 100 arasında, baya basit aslında.
sayi = random.randint(1, 100)
print("Şansa seçilen sayı:", sayi)  # Seçtiğimiz sayıyı ekrana yazıyoruz.

# Karekökyü hesaplıyoruz, tabii önce sayıyı yukarda seçmiştik, onun için.
karekok = math.sqrt(sayi)  # Matematik modülüyle karekök hesaplama.
print(f"{sayi} sayısının karekökü:", karekok)

# Pi'yi de yazdırıyoruz bi yandanii
print("Pi sayısı:", math.pi)

# Şimdi de Pi'yi yuvarlayalım, böyle milimetrik haliyle kafa karıştırıyor.
yuvarlama = round(math.pi, 2)
print("Yuvarlanmış Pi sayısı:", yuvarlama)

from collections import Counter  # Bu modül sayıları falan saymak için baya kullanışlı.

# Bi tane liste yaptık, içinde bi şarkı sözü var, bi de "kiraz" falan koyduk iki kere.
data = ['Yine yine sev beni, deli deli sev beni', 'kiraz', 'kiraz']

# Counter, bu listedeki elemanları sayıyor, kimin eli kimin cebinde gibi.
counter = Counter(data)
print(counter)  # Her elemanın kaç kere geçtiğini gösterir.

# En çok tekr
print(counter.most_common(2))

import datetime  # Tarih ve zaman işleri için kullandık.
import time  # Saatle alakalı şeyler yapmak için lazım.

# Şu anki zamanı alıyoruz, ne kadar saat kaldı falan der gibi.
now = datetime.datetime.now()
print(now)

# Özel bi tarih ve zaman da oluşturabiliyoruz, mesela bi doğum günü tarihi diyelim.
custom_date = datetime.datetime(2023, 5, 17, 15, 30)
print(custom_date)

# Zaman ölçümü yapıyoruz, baya basit aslında. Önce başlıyoruz, sonra bitiyoruz.
start_time = time.time()  # Başlangıç zamanı.
time.sleep(2)  # 2 saniye uyutuyor programı, bekliyoruz yani.
end_time = time.time()  # Sonra bitiş zamanı alınıyor.

# Geçen süreyi hesaplıyoruz, 2 saniye uyuduk ama  bunu matematikle gösteriyoruz.
print(f"Geçen süre: {end_time - start_time:.2f} saniye")

#ı.

def my_decorator(func):  # Bu decorator'un kendisi, baya havalı bi şey.
    def wrapper():  # İçine başka bi fonksiyonu sarıyoruz, adı 'wrapper' ama kafana göre değiştir.
        print("Fonksiyon çalışmadan önce.")  # Fonksiyondan önce yapılacak şey.
        func()  # Burada sarılmış fonksiyonu çalıştırıyoruz.
        print("Fonksiyon çalıştıktan sonra.")  # Ve sonrasında yapılacak şey.
    return wrapper  # Dışarıya bu süslenmiş hali dönüyor.

@my_decorator  # Burada decorator'u çağırdık, 'hello' fonksiyonuna taktık.
def hello():
    print("Merhaba!")  # Normalde bu fonksiyon sadece bunu yazacaktı ama ekstra çıktı geldi.

hello()  # Fonksiyonu çalıştırıyoruz.
# Çıktı:
# Fonksiyon çalışmadan önce.
# Merhaba!
# Fonksiyon çalıştıktan sonra.

import requests  # İnternetten veri çekmek

# A

# 1. İstek gönderilecek URL tanımlanır
url = "https://api.github.com"
# Bu, GitHub'ın API'sinin ana sayfasına yapılan bir HTTP isteğidir.
# Genelde API ile etkileşim kurmak için bu tür URL'ler kullanılır.

# 2. Basit bir GET isteği gönderme
response = requests.get(url)
# 'requests.get()' fonksiyonu, belirtilen URL'ye bir HTTP GET isteği gönderir.
# Dönen sonuç, bir 'Response' nesnesidir ve bu nesne isteğe ilişkin detayları içerir.

# 3. Yanıt durumu (status_code) ve içeriği (content/json)
print(response.status_code)
# 'response.status_code' ile isteğin durum kodu alınır.
# Örnek:
# - 200: Başarılı bir istek
# - 404: Sayfa bulunamadı
# - 500: Sunucu hatası

print(response.json())
# 'response.json()' ile yanıtın JSON formatındaki içeriği alınır.
# JSON, genelde API'lerin gönderdiği veri formatıdır.
# Bu içerik bir Python sözlüğüne (dictionary) dönüştürülür ve yazdırılır.
import requests  # HTTP isteklerini göndermek için 'requests' modülünü içe aktarır.

# 1. POST isteği gönderilecek URL tanımlanır
url = "https://jsonplaceholder.typicode.com/posts"
# 'jsonplaceholder.typicode.com' test amaçlı kullanılabilen sahte bir API'dir.
# Bu URL, yeni bir "post" (gönderi) oluşturmak için kullanılır.

# 2. Gönderilecek veri tanımlanır (JSON formatında)
data = {
    "title": "Yeni Gönderi",               # Gönderinin başlığı
    "body": "Bu bir test gönderisidir.",   # Gönderinin içeriği
    "userId": 1                            # Gönderiyi oluşturan kullanıcının kimliği
}

# 3. POST isteği gönderme
response = requests.post(url, json=data)
# 'requests.post()' fonksiyonu belirtilen URL'ye POST isteği gönderir ve 'data' parametresi ile veriyi iletir.
# 'json=data' ifadesi, veriyi JSON formatında gönderir.

# 4. Yanıt durumu kodunu yazdırma
print(response.status_code)
# 'response.status_code' ile isteğin durum kodu alınır.
# Örnek: 201 (Oluşturuldu), 400 (Hatalı İstek)

# 5. Yanıtın JSON formatındaki içeriğini yazdırma
print(response.json())
# 'response.json()' ile sunucudan dönen yanıtın JSON formatındaki içeriği alınır ve ekrana yazdırılır.
# Yeni oluşturulan gönderinin detaylarını içerir.
import tkinter as tk  # tkinter modülünü 'tk' kısaltması ile içe aktarır.

import tkinter as tk  # tkinter modülünü alıp kısaltıyoruz, yoksa çok uzun oluyor.

# 1. Seçim yapılan şeyi gösteren fonsksiyon (yanlış yazım olsun biraz doğal dursun :P)
def secilen_elemani_yazdir():
    secili = listbox.curselection()  # Listbox'tan hangi eleman seçilmiş onu alıyoruz.
    if secili:  # Eğer bişey seçilmişse çalışır bu
        print(f"Seçilen: {listbox.get(secili[0])}")  # Seçilen neyse konsola yazıyor.

# 2. Pencere yapıyoruz (ana pencere, bi çeşit container gibi)
root = tk.Tk()
root.title("Tkinter Listbox")  # Başlığı ayarlıyoruz ama aslında adı ne olursa olsun farketmez :D
root.geometry("300x200")  # Pencerenin boyutunu ayarladık ki çok küçük veya büyük olmasın.

# 3. Liste kutusunu yapıyoruz
listbox = tk.Listbox(root)
# Bu bir widget ve içine eleman koyabiliyoruz, mesela meyveler falan.
listbox.pack(pady=20)
# 'pack' ile listeyi pencereye ekliyoruz, biraz aralıklı durması için de boşluk koyuyoruz.

# 4. Listeye eleman koyuyoruz (Elma, Armut falan filan)
for eleman in ["Elma", "Armut", "Kiraz", "Muz"]:
    listbox.insert(tk.END, eleman)  # Her birini sırayla listeye koyduk, ama END ne dersen, hep sonuna ekliyor.

# 5. Bir buton yapıyoruz ki kullanıcı seçimini göstersin
buton = tk.Button(root, text="Seçimi Yazdır", command=secilen_elemani_yazdir)
# 'text' dediğimiz şey butonun üzerinde yazan yazı, 'command' ise butona tıklayınca ne yapacak, onu belirtiyoruz.
buton.pack(pady=10)  # Yine boşluk koyduk biraz, yoksa üst üste biner.

# 6. Pencereyi çalıştırıyoruz (mainloop ana döngü gibi, olmadan pencere açılmaz)
root.mainloop()
# Bu döngü, pencere açık kaldıkça çalışır, kullanıcı etkileşimlerini yakalar.


button = tk.Button(root, text="Seçimi Göster", command=secilen_elemani_yazdir)
# 'Button' widget'ı ile bir buton oluşturulur ve üzerine "Seçimi Göster" yazılır.
# Butona tıklanıldığında 'secilen_elemani_yazdir()' fonksiyonu çalışacak.
button.pack(pady=10)
# 'pack()' metodu ile buton pencereye eklenir ve 'pady=10' ile butonun üst ve alt kısmına 10 piksel boşluk eklenir.

root.mainloop()
# 'mainloop()' metodu, pencereyi etkileşimli hale getirir ve kullanıcı etkileşimlerini dinler.
# Bu döngü, pencereyi sürekli açık tutar.


import ssl  # Güvenli bağlantılar için ssl modülünü içe aktarır.
import smtplib  # E-posta gönderimi için smtplib modülünü içe aktarır.

sifre = '<kullanici_sifresi>'  # Gönderici e-posta şifresini belirtimek için ekledik.


alici = kullanici  # Alıcı adresini belirler. Bu örnekte alıcı kendi e-posta adresi.


baslik = 'Python Gönderisi'  # E-posta başlığını belirtir.
mesaj = """\
Subject: {}

Merhaba, bu mesaj Python ile gönderildi.
""".format(baslik)  # E-postanın içeriğini oluşturur. 'format' fonksiyonu başlığı eklerbu yüzden fomrt kullandık

# 4. SSL bağlamı oluşturmaya yarayan bir kod satırıdır bu
context = ssl.create_default_context()  # SSL güvenli bağlantısı için bağlam (context) oluşturur.

# 5. SMTP sunucusu ve bağlantı bilgileri
port = 465  # SSL bağlantısı için kullanılan port numarası.
host = "smtp.gmail.com"  # Gmail'in SMTP sunucu adresi.

try:
    # 6. Sunucuya bağlanma ve giriş yapma
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as eposta_sunucu:
        eposta_sunucu.login(kullanici, sifre)  # Sunucuya kullanıcı adı ve şifre ile giriş yapar.

        # 7. E-postayı gönderme
        eposta_sunucu.sendmail(kullanici, alici, mesaj)  # E-posta gönderme işlemi yapılır.

        print("E-posta başarıyla gönderildi!")  # E-posta başarıyla gönderildiğinde bu mesaj yazdırılır.
except Exception as e:
    print(f"E-posta gönderiminde bir hata oluştu: {e}")  # Hata durumunda hata mesajı yazdırılır.
# Gerekli kütüphanelerin import edilmesi
# imap_tools, IMAP protokolü ile e-posta işlemleri yapmak için kullanılan bir kütüphane
from imap_tools import MailBox, AND
import datetime

# E-posta bağlantısı kurmak için MailBox nesnesi oluşturuyoruz
# Gmail IMAP sunucusunu kullanıyoruz
posta_kutusu = MailBox('imap.gmail.com')

# Kullanıcı bilgileri ile giriş yapıyoruz
# "kullanici" ve "sifre" değişkenlerinin ilgili e-posta ve şifre bilgisi ile doldurulması gerekiyor
posta_kutusu.login(kullanici="kullanici@gmail.com", sifre="sifre", initial_folder="INBOX")

# E-posta kriterlerini tanımlıyoruz
# Bu örnekte, 1 Ocak 2021'den itibaren gönderilmiş olan e-postaları ve belirli bir kullanıcıdan gelenleri seçiyoruz
kriter = AND(date_gte=datetime.date(2021, 1, 1), from_="ornek@kullanici.com")

# Kriterlere uygun e-postaları getirip metin içeriklerini yazdırıyoruz
for msg in posta_kutusu.fetch(kriter):
    print(msg.text)  # E-postanın metin içeriğini konsola yazdırıyoruz

# Daha karmaşık bir işlem için bir fonksiyon tanımlıyoruz
# Bu fonksiyon belirli bir dosya adına göre e-posta armak iin yaptıkg
def dosya_isiminden_mail_bul(eposta_kutusu_param, dosya_ismi_param, kriter_param):

    for mesaj in eposta_kutusu_param.fetch(kriter_param):#for kullandık bu dönm eye yarıyor
        # Mesajın eklerini kontrol ediyoruz
        if mesaj.attachments:
            for ek in mesaj.attachments:
                # Eğer ekin dosya adı aranan dosya adına eşitse mi onu kotnrol ediyrouz
                if dosya_ismi_param == ek.filename:
                    return '{} isimli dosya, {} tarihli ve {} başlıklı e-postadadır.'.format(
                        dosya_ismi_param,
                        mesaj.date_str,
                        mesaj.subject
                    )
    return "Aranan dosya bulunamadı." # bu kelimyei döndüüryoruz

"""
"""a_ismi = 'e-posta.ipynb'  # Aranacak dosyanın adını giriyoruz
sonuc = dosya_isiminden_mail_bul(posta_kutusu, dosya_ismi, kriter)
print(sonuc)

# İşlem tamamlandıktan sonra posta kutusunu kapatıyoruz log la 
posta_kutusu.logout()

"""