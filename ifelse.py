# if - else durum kontrolü
from unicodedata import name


x = 5

if x == 5:
    print("x değeri 5'e eşit")
elif x == 6:
    print("x değeri 6'e eşit")
elif x == 7:
    print("x değeri 7'e eşit")

# Example 
userName = "admin"
password = "12345"
x = input("Kullanıcı Adı: ")
y = input("Şifre: ")

if userName == x and password == y :
    print("Giriş başarılı")
else:
    print("Giriş başarısız")

# Example 2 

if userName == x and password == y :
    print("Giriş başarılı")
elif userName == x and password != y :
    print("Şifre yanlış")
elif userName != x and password == y :
    print("Kullanıcı adı yanlış")
else:
    print("Giriş başarısız")

# Example 3

if userName == x and password == y :
    print("Giriş başarılı! Hoşgeldiniz {}".format(x))
elif userName == x and password != y :
    print("Şifre yanlış")
elif userName != x and password == y :
    print("Kullanıcı adı yanlış")
else:
    print("Giriş başarısız")
    

name = str(input("İsim: ")) 
surname = str(input("Soyisim: "))
school = str(input("Okul: "))
age = int(input("Yaş: "))
sc = ("İlköğretim", "Lise", "Öğretim", "Lisans", "Yüksek Lisans", "Doktora")

if school not in sc:
    print("Okul seçimi yanlış")
elif (age >= 18) and (school == "Lise" or school == "Lisans" or school == "Yüksek Lisans" or school == "Doktora"):
    print("Ehliyet alabilirsiniz {} {}".format(name, surname))
else :
    print("Ehliyet alamazsınız {} {}".format(name, surname))

number = int(input("Sayı: "))
control = (number > 0) and (number%2 == 1)
if control:
    print("{} Sayısı tek sayıdır".format(number))
else:
    print("{} Sayısı çift sayıdır".format(number))