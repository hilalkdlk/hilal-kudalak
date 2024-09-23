# Aşağıdaki işlemleri indexing ve slicing kullanarak liste üzerinde uygulayın.

liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

# "3" değerine ulaşmak için indexleme yapın.
# "Hi-Kod" değerine ulaşmak için indexleme yapın.
# 4.7 değerine ulaşmak için indexleme yapın.
# 9,"3",8.4,"Hi-Kod" değerlerine ulaşmak için slicing yapın.
# 8.4,"Hi-Kod","False",4.7 değerlerine ulaşmak için slicing yapın.
print(len(liste))
print(liste[3])
print(liste[5])
print(liste[-1])
print(liste[2:6])
print(liste[4:8])







# Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.
liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
yeni_liste = []

for eleman in liste:
    if isinstance(eleman, str):
        yeni_liste.append(eleman)
print(yeni_liste)





# Enumerate methodunu araştırın ve aşağıdaki örneği enumerate methodu ile yapın.

# for index in range(len(meyveler)):
#     print("{}. indexte bulunan meyve: {}".format(index,meyveler[index])
meyveler = ['armut', 'elma']
for index, meyve in enumerate(meyveler):
    print(index, meyve)