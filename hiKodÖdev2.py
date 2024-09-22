# Ödev-1: Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır. Kullanıcının geliri;
#  10000 ve altındaysa maaşından %5 kesinti olur. 
#  25000 ve altındaysa maaşından %10 kesinti olur. 
#  45000 ve altındaysa maaşından %25 kesinti olur. 
#  Diğer koşullarda %30 kesinti olur. 
# Bu durumlara göre kullanıcının yeni maaşı yazdırılır.

maas = float(input('maaş: '))
if maas<=10000:
    vergiKesintisi = (maas*0.05)
elif maas<=25000:
    vergiKesintisi = (maas*0.1)
elif maas<=45000:
    vergiKesintisi = (maas*0.25)
else: 
    vergiKesintisi = (maas*0.3)

yeniMaas = (maas - vergiKesintisi)

print(f'yeni maaş {yeniMaas}')





# Ödev-2: Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir. Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır, 
# altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. (Sadece koşul kullanılması yeterli.)

kullaniciAdi = input('Kullanıcı adi: ')
sifre = input('Şifre: ')
if len(sifre) == 6:
    print('Hesabınız oluşturuldu.')
else:
    print('Altı haneli bir şifre oluşturunuz.')





# Ödev-3: Bir önceki örnek geliştirilir.

#  Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda. Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır. 
#  Koşulu sağlamıyorsa "Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır. 
#  Bunu oluştururken kullanıcı istediğimiz şartlarda şifre oluşturana kadar sormaya devam eder 

kullaniciAdi = input('Kullanıcı adi: ')
sifre = input('Şifre: ')
while True:
    if 5<=len(sifre)<=10 :
        print('Hesabınız oluşturuldu.')
    else:
        print('Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!')
    break




# Ödev-4: Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.

#  Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar. 
#  Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter. 
#  Tercihe göre kalan hak bilgisi verilir. 
dogruSifre = '1485'
hak = 3


while hak>0:
    girilenSifre = input('şifre: ')
    if girilenSifre == dogruSifre:
        print('Giriş Yapıldı.')
    else: 
        print('Yanlış şifre girildi!')
        hak -= 1
        if hak>0:
            print(f"Kalan hak: {hak}")
        else:
            print("Deneme hakkınız dolmuştur.")
    



