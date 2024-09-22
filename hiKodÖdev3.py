#Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.
pi = float(input('pi sayısını giriniz: '))
yaricap = float(input('yarıçağı giriniz: '))

daireAlani = pi*(yaricap**2)
print(f'dairenin alanı {daireAlani}')




# Faktöriyel adında fonksiyon oluşturulur. Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır. 
# Format metodunu kullanılarak ekrana yazdırılır.

sayi = int(input('sayi giriniz: '))
def faktöriyel(sayi):
    if sayi<0:
        return 'Negatif sayıların faktöriyeli alınamaz.'
    
    sonuç = 1
    for i in range(1, sayi+1):
        sonuç *= i
    
    return "Faktöriyel({}) = {}".format(sayi, sonuç)

print(faktöriyel(sayi))




# Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir fonksiyon oluşturun. 

dgYili = int(input('Doğum yılınızı giriniz: '))
mevcutyil = int(input('Mevcut yılı giriniz: '))

def yasHesap(dgYili):
    yas = mevcutyil - dgYili
    return 'Yaşınız {}'.format(yas)

print(yasHesap(dgYili))






# Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.
# (Kişi 65 yaşında ise emekli olur.) Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın.
# (Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :)) Kişi 65 yaşında ya da daha fazlaysa "Emekli oldunuz" yanıtını, 
# 65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak "(isim) emekliliğine (yıl) kaldı." yanıtını versin.



def emeklilikHesabi(dgYili, mevcutyil):
    def yasHesabi(dgYili):
        return mevcutyil - dgYili
    yas = yasHesabi(dgYili)
    
    if yas >= 65:
        return 'Emekli oldunuz.'
    else: 
        kalan = 65-yas
        return 'Emekliliğinize {} kadar yıl kaldı.'.format(kalan)
    

isim = input('isim giriniz: ')
dgYili = int(input('Doğum yılınızı giriniz: '))
mevcutyil = int(input('Mevcut yılı giriniz: '))

print(emeklilikHesabi(dgYili, mevcutyil))