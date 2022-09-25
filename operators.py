from re import X


print(243.5+5) # 243.5+5 = 248.5 
print(231/5) # 230/5 = 46.0
print(230*5) # 230*5 = 1050
print(230-5) # 230-5 = 225
print(230%5) # 230%5 = 0
print(230**5) # 230**5 = 23025
print(231//5) # 230//5 = 46

x,y = 10,20 
print(x,y) # x,y değerleri 10,20 olarak ekrana yazdırılır.
x = x + 5 # x değişkeninin değeri 5 eklenir.
print(x) 
x+=10 # X değişkeninin değeri 10 eklenir.
print(x)

print(x<y) # x değişkeninin değeri y değişkeninin değeriden küçük mü?
print(x>y) # x değişkeninin değeri y değişkeninin değeriden büyük mü?
print(x==y) # x değişkeninin değeri y değişkeninin değerine eşit mi?
print(x!=y) # x değişkeninin değeri y değişkeninin değerine eşit değil mi?
print(x<=y) # x değişkeninin değeri y değişkeninin değerine eşit veya küçük mü?
print(x>=y) # x değişkeninin değeri y değişkeninin değerine eşit veya büyük mü?
print(x is y) # x değişkeninin değeri y değişkeninin değerine eşit mi?
print(x is not y) # x değişkeninin değeri y değişkeninin değerine eşit değil mi?
print(x in [1,2,3,4,5]) # x değişkeninin değeri 1,2,3,4,5 listede mi?
print(x not in [1,2,3,4,5]) # x değişkeninin değeri 1,2,3,4,5 listede değil mi?
print(x is None) # x değişkeninin değeri None mi?
print(x is not None) # x değişkeninin değeri None değil mi?
print(x is True) # x değişkeninin değeri True mi?
print(x is not True) # x değişkeninin değeri True değil mi?
print(x is False) # x değişkeninin değeri False mi?
print(x is not False) # x değişkeninin değeri False değil mi?

print(x and y) # x ve y değerlerinin değerleri eşit mi?
print(x or y) # x ve y değerlerinin değerleri eşit mi?
print(not x) # x değerinin değeri False mi?
print(not y) # y değerinin değeri False mi?
print(not x and y) # x ve y değerlerinin değerleri eşit mi?
print(not x or y) # x ve y değerlerinin değerleri eşit mi?
print(not (x and y)) # x ve y değerlerinin değerleri eşit mi?
print(not (x or y)) # x ve y değerlerinin değerleri eşit mi?
