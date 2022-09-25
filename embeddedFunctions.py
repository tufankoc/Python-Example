#abs fonksiyonu kullanarak sayıların mutlak değerlerini bulur.
print(abs(-5))
print(abs(5)) 
print(abs(0))
print(abs(5.5))

#round fonksiyonu sayıların yuvarlanmasını sağlar.
print(round(5.5))
print(round(5.4))
print(round(5.6))
print(round(5.5220, 1)) #round(5.5220, 1) = 5.5 

#max fonksiyonu sayıların en büyüğünü bulur.
print(max(5, 10))
print(max(5, -10, -20))
print(max([5, 10, -20]))

#min fonksiyonu sayıların en küçüğünü bulur.
print(min(5, 10))
print(min(5, -10, -20))
print(min([5, 10, -20]))

#sum fonksiyonu sayıların toplamını bulur.
print(sum([5, 10, -20]))

#len fonksiyonu listelerin uzunluğunu bulur.
print(len([5, 10, -20]))

#all fonksiyonu listelerin tüm elemanlarının True olup olmadığını kontrol eder.
x = [5<6, 10<20, -20<1]
print(all(x))
#any fonksiyonu 1 tane True olduğunda Turu döndürür.
print(any(x)) 

#bool fonksiyonu True veya False döndürür.
print(bool(0))
#chr fonksiyonu karakter kodunu döndürür.
print(chr(65))

#enumerate fonksiyonu listelerin elemanlarını ve indislerini döndürür.
for i, j in enumerate(["a", "b", "c"]):
    print(i, j)

#zip fonksiyonu listelerin elemanlarını ve indislerini döndürür.
for i, j in zip([1, 2, 3], ["a", "b", "c"]):
    print(i, j)

#map fonksiyonu listelerin elemanlarını ve indislerini döndürür.
print(list(map(lambda x: x*2, [1, 2, 3])))
#id fonksiyonu bir nesnenin adresini döndürür.
print(id(1)) 

#type fonksiyonu bir nesnenin türünü döndürür.
print(type(1))
#dir fonksiyonu bir nesnenin tüm özelliklerini döndürür.
print(dir(1))
#help fonksiyonu bir nesnenin kullanım kılavuzunu döndürür.

#hex fonksiyonu sayıların hexadecimal karşılığını döndürür.
print(hex(10))
#oct fonksiyonu sayıların octal karşılığını döndürür.
print(oct(10)) 
