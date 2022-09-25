from concurrent.futures import process
import datetime


print("""\t *** Merhaba XBank'a hoşgeldiniz. *** 
\t\t Bekleyiniz...""")

data = {
    "Tufan" : {
        "isim" : "Tufan",
        "soyisim" : "Koç",
        "kartNo" : "12",
        "sifre" : "1233",
        "bakiye" : 1000,
        "limit" : 1000,
        "islem" : 0,
        "islemTarihi" : "0"
    },
    "Ahmet" : {
        "isim" : "Ahmet",
        "soyisim" : "Kaya",
        "kartNo" : "1234",
        "sifre" : "1223",
        "bakiye" : 1000,
        "limit" : 1000,
        "islem" : 0,
        "islemTarihi" : "0"
    }
} 
for i in range(0,1000):
    inputCrediCard = input("\n\nKartınızı No'nu Giriniz : ")
    if inputCrediCard == data["Tufan"]["kartNo"]:
        i = 0
        for i in range(0,3):
            inputPassword = input("\n\nLütfen Şifrenizi Giriniz : ")
            if inputPassword == data["Tufan"]["sifre"] :
                if data["Tufan"]["islem"] == 3:
                    print("\n\nKartınızın islem limitini asıldı.")
                    exit()
                else:
                    data["Tufan"]["islem"] = 0
                    print ("\n\n Hoşgeldiniz {}{} Lütfen İşlem Seçiniz.".format(data["Tufan"]["isim"],data["Tufan"]["soyisim"]))   
                    selectProcess = input(""" 
                    1-Para Yatır
                    2-Para Çek
                    3-Bakiye Sorgula
                    4-Hesap Bilgileri
                    Q-Çıkış\n""")
                    if selectProcess == "1":
                        inputAmount = input("\n\nLütfen Yatırılacak Tutarı Giriniz : ")
                        if inputAmount.isdigit(): # inputAmount.isnumeric(): sayı mı kontrol eder
                                data["Tufan"]["bakiye"] += int(inputAmount)
                                data["Tufan"]["islem"] += 1
                                data["Tufan"]["islemTarihi"] = str(datetime.datetime.now())
                                print("\n\n{} TL Yatırıldı.".format(inputAmount))
                        else:
                            print("\n\nLütfen Sayı Giriniz.")
                    elif selectProcess == "2":
                        inputAmount = input("\n\nLütfen Çekilecek Tutarı Giriniz : ")
                        if inputAmount.isdigit():
                            if int(inputAmount) <= data["Tufan"]["bakiye"]:
                                data["Tufan"]["bakiye"] -= int(inputAmount)
                                data["Tufan"]["islem"] += 1
                                data["Tufan"]["islemTarihi"] = str(datetime.datetime.now())
                                print("\n\n{} TL Çekildi.".format(inputAmount))
                            else:
                                print("\n\nYetersiz Bakiye.")
                    elif selectProcess == "3":
                        print("\n\nBakiyeniz : {} TL".format(data["Tufan"]["bakiye"]))
                    elif selectProcess == "4":
                        print("\n\nHesap Bilgileri : ")
                        print("\n\nHesap No : {}".format(data["Tufan"]["kartNo"]))
                        print("\n\nHesap Sahibi : {} {}".format(data["Tufan"]["isim"],data["Tufan"]["soyisim"]))
                        print("\n\nBakiye : {} TL".format(data["Tufan"]["bakiye"]))
                        print("\n\nLimit : {} TL".format(data["Tufan"]["limit"]))
                        print("\n\n{}".format(data["Tufan"]["islemTarihi"]))
                        break
                    elif selectProcess == "Q":
                        print("\n\nÇıkış Yapılıyor...")
                        exit()

            else:
                data["Tufan"]["islem"] = data["Tufan"]["islem"] + 1
                data["Tufan"]["islemTarihi"] = str(datetime.datetime.now())
                if data["Tufan"]["islem"] == 3:
                    print("Kartınız Kilitlendi. Lütfen Şubeyi Arayın.")
                print ("Şifreniz Yanlış. Lütfen Tekrar Deneyin.")
    else: 
        ...
    if inputCrediCard == data["Ahmet"]["kartNo"]:
            i = 0
            for i in range(0,3):
                inputPassword = input("\n\nLütfen Şifrenizi Giriniz : ")
                if inputPassword == data["Ahmet"]["sifre"] :
                    if data["Ahmet"]["islem"] == 3:
                        print("\n\nKartınızın islem limitini asıldı.")
                        exit()
                    else:
                        data["Ahmet"]["islem"] = 0
                        print ("\n\n Hoşgeldiniz {}{} Lütfen İşlem Seçiniz.".format(data["Ahmet"]["isim"],data["Ahmet"]["soyisim"]))   
                        selectProcess = input(""" 
                        1-Para Yatır
                        2-Para Çek
                        3-Bakiye Sorgula
                        4-Hesap Bilgileri
                        Q-Çıkış\n""")
                        if selectProcess == "1":
                            inputAmount = input("\n\nLütfen Yatırılacak Tutarı Giriniz : ")
                            if inputAmount.isdigit(): # inputAmount.isnumeric(): sayı mı kontrol eder
                                    data["Ahmet"]["bakiye"] += int(inputAmount)
                                    data["Ahmet"]["islem"] += 1
                                    data["Ahmet"]["islemTarihi"] = str(datetime.datetime.now())
                                    print("\n\n{} TL Yatırıldı.".format(inputAmount))
                            else:
                                print("\n\nLütfen Sayı Giriniz.")
                        elif selectProcess == "2":
                            inputAmount = input("\n\nLütfen Çekilecek Tutarı Giriniz : ")
                            if inputAmount.isdigit():
                                if int(inputAmount) <= data["Ahmet"]["bakiye"]:
                                    data["Ahmet"]["bakiye"] -= int(inputAmount)
                                    data["Ahmet"]["islem"] += 1
                                    data["Ahmet"]["islemTarihi"] = str(datetime.datetime.now())
                                    print("\n\n{} TL Çekildi.".format(inputAmount))
                                else:
                                    print("\n\nYetersiz Bakiye.")
                        elif selectProcess == "3":
                            print("\n\nBakiyeniz : {} TL".format(data["Ahmet"]["bakiye"]))
                        elif selectProcess == "4":
                            print("\n\nHesap Bilgileri : ")
                            print("\n\nHesap No : {}".format(data["Ahmet"]["kartNo"]))
                            print("\n\nHesap Sahibi : {} {}".format(data["Ahmet"]["isim"],data["Ahmet"]["soyisim"]))
                            print("\n\nBakiye : {} TL".format(data["Ahmet"]["bakiye"]))
                            print("\n\nLimit : {} TL".format(data["Ahmet"]["limit"]))
                            print("\n\n{}".format(data["Ahmet"]["islemTarihi"]))
                        elif selectProcess == "Q":
                            print("\n\nÇıkış Yapılıyor...")
                            exit()

                else:
                    data["Ahmet"]["islem"] = data["Ahmet"]["islem"] + 1
                    data["Ahmet"]["islemTarihi"] = str(datetime.datetime.now())
                    if data["Ahmet"]["islem"] == 3:
                        print("Kartınız Kilitlendi. Lütfen Şubeyi Arayın.")
                    print ("Şifreniz Yanlış. Lütfen Tekrar Deneyin.")
    else: 
        ...


