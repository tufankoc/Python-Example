#ürünler

Ürünler=["Telefon","Bilgisayar","Kamera","Klavye","Mouse","Televizyon"]

#ürünleri Listele
print(Ürünler)

#Kaç Adet Ürün Var?
print(len(Ürünler))

#İlk 2 Ürünü Listele
print(Ürünler[0:3])

#Son 2 Ürünü Listele
print(Ürünler[-2:])

#Son ürünü Listele
print(Ürünler[-1])

#Bilgisayar Ürünü yerine Tablet Ürünü ile Değiştir
Ürünler[1]="Tablet"
print(Ürünler)

#Çamaşır Makinası Ürünü ekle
Ürünler.append("Çamaşır Makinası")
print(Ürünler)

#Telefon Ürününü çıkar
Ürünler.pop(0)
print(Ürünler)

#Ürünleri Tersten Listele
print(Ürünler[::-1])
