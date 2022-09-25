print("""
1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
5. Üs alma
6. Çıkış

""")
choose = int(input("Seçiminiz: "))
if choose == 1:
    x = int(input("1. Sayı: "))
    y = int(input("2. Sayı: "))
    print("{} + {} = {}".format(x, y, x+y))
elif choose == 2:
    x = int(input("1. Sayı: "))
    y = int(input("2. Sayı: "))
    print("{} - {} = {}".format(x, y, x-y))
elif choose == 3:
    x = int(input("1. Sayı: "))
    y = int(input("2. Sayı: "))
    print("{} * {} = {}".format(x, y, x*y))
elif choose == 4:
    x = int(input("1. Sayı: "))
    y = int(input("2. Sayı: "))
    print("{} / {} = {}".format(x, y, x/y))
elif choose == 5:
    x = int(input("1. Sayı: "))
    y = int(input("2. Sayı: "))
    print("{} ** {} = {}".format(x, y, x**y))
elif choose == 6:
    print("Programdan çıkılıyor...")
    exit()
else:
    print("Geçersiz seçim")
    exit()
print("Programdan çıkılıyor...")
exit()

