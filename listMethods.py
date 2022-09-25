list = [1,2,5,"ahmet",True,None,2.5]
list.append("fatma") # ekleme yapar append
list.insert(2,"mehmet") # istediğin sıraya ekleme yapar insert
list.remove("mehmet") # silme yapar remove
list.pop() # silme yapar pop
list.pop(5) # istediğin sıradaki silme yapar pop
list.index("ahmet") # istediğin elemanın sırasını verir index
list.count("ahmet") # istediğin elemanın kaç tane olduğunu verir count
list.extend(["fatma","mehmet"]) # listeyi birbirine ekler extend
print(list)


list2 = [1,2,5,6,7,8,9,10]
list2.sort() # listeyi sıralar sort
list2.reverse() # listeyi tersine çevirir reverse
print(list2)

list.extend(list2) # listeyi birbirine ekler extend
print(list)
print(list.__contains__("ahmet")) # liste içerisinde istediğin eleman var mı yok mu kontrolü yapar __contains__
print(list.__len__()) # liste uzunluğunu verir __len__
print(list.__getitem__(2)) # liste içerisinde istediğin sırada elemanı verir __getitem__
print(list.__setitem__(2,"mehmet")) # liste içerisinde istediğin sırada elemanı değiştirir __setitem__
print(list.__delitem__(2)) # liste içerisinde istediğin sırada elemanı siler __delitem__
print(list.__iter__()) # liste içerisinde elemanları tek tek döndürür __iter__
print(list.__next__()) # liste içerisinde elemanları tek tek döndürür __next__
print(list.__reversed__()) # liste içerisinde elemanları tersine çevirir __reversed__
print(list.__str__()) # liste içerisinde elemanları string olarak döndürür __str__
print(list.__repr__()) # liste içerisinde elemanları string olarak döndürür __repr__
print(list.__eq__(list2)) # liste içerisinde elemanları eşit mi kontrol eder __eq__
print(list.__lt__(list2)) # liste içerisinde elemanları küçük mi kontrol eder __lt__
print(list.__gt__(list2)) # liste içerisinde elemanları büyük mi kontrol eder __gt__
print(list.__le__(list2)) # liste içerisinde elemanları küçük veya eşit mi kontrol eder __le__
print(list.__ge__(list2)) # liste içerisinde elemanları büyük veya eşit mi kontrol eder __ge__
print(list.__ne__(list2)) # liste içerisinde elemanları eşit mi kontrol eder __ne__
print(list.__add__(list2)) # liste içerisinde elemanları birleştirir __add__
print(list.__mul__(list2)) # liste içerisinde elemanları çarpır __mul__
print(list.__truediv__(list2)) # liste içerisinde elemanları bölümüne göre bölüyor __truediv__
print(list.__floordiv__(list2)) # liste içerisinde elemanları bölümüne göre bölüyor __floordiv__
print(list.__mod__(list2)) # liste içerisinde elemanları mod alıyor __mod__
print(list.__divmod__(list2)) # liste içerisinde elemanları bölümüne göre bölüyor __divmod__
print(list.__pow__(list2)) # liste içerisinde elemanları üs alıyor __pow__
print(list.__lshift__(list2)) # liste içerisinde elemanları sola kaydırıyor __lshift__
print(list.__rshift__(list2)) # liste içerisinde elemanları sağa kaydırıyor __rshift__
print(list.__and__(list2)) # liste içerisinde elemanları ve işlemi yapıyor __and__
print(list.__xor__(list2)) # liste içerisinde elemanları çift ve işlemi yapıyor __xor__
print(list.__or__(list2)) # liste içerisinde elemanları veya işlemi yapıyor __or__
print(list.__radd__(list2)) # liste içerisinde elemanları birleştirir __radd__
print(list.__rmul__(list2)) # liste içerisinde elemanları çarpıyor __rmul__
print(list.__rtruediv__(list2)) # liste içerisinde elemanları bölüyor __rtruediv__
print(list.__rfloordiv__(list2)) # liste içerisinde elemanları bölüyor __rfloordiv__
print(list.__rmod__(list2)) # liste içerisinde elemanları mod alıyor __rmod__
print(list.__rdivmod__(list2)) # liste içerisinde elemanları bölüyor __rdivmod__
print(list.__rpow__(list2)) # liste içerisinde elemanları üs alıyor __rpow__
print(list.__rlshift__(list2)) # liste içerisinde elemanları sola kaydırıyor __rlshift__
print(list.__rrshift__(list2)) # liste içerisinde elemanları sağa kaydırıyor __rrshift__
print(list.__rand__(list2)) # liste içerisinde elemanları ve işlemi yapıyor __rand__
print(list.__rxor__(list2)) # liste içerisinde elemanları çift ve işlemi yapıyor __rxor__
print(list.__ror__(list2)) # liste içerisinde elemanları veya işlemi yapıyor __ror__
print(list.__iadd__(list2)) # liste içerisinde elemanları birleştirir __iadd__
print(list.__imul__(list2)) # liste içerisinde elemanları çarpıyor __imul__
print(list.__itruediv__(list2)) # liste içerisinde elemanları bölüyor __itruediv__
print(list.__ifloordiv__(list2)) # liste içerisinde elemanları bölüyor __ifloordiv__
print(list.__imod__(list2)) # liste içerisinde elemanları mod alıyor __imod__
print(list.__ipow__(list2)) # liste içerisinde elemanları üs alıyor __ipow__
print(list.__ilshift__(list2)) # liste içerisinde elemanları sola kaydırıyor __ilshift__
print(list.__irshift__(list2)) # liste içerisinde elemanları sağa kaydırıyor __irshift__
print(list.__iand__(list2)) # liste içerisinde elemanları ve işlemi yapıyor __iand__
print(list.__ixor__(list2)) # liste içerisinde elemanları çift ve işlemi yapıyor __ixor__
print(list.__ior__(list2)) # liste içerisinde elemanları veya işlemi yapıyor __ior__
print(list.__contains__(list2)) # liste içerisinde elemanları içeriyor __contains__
print(list.__iter__(list2)) # liste içerisinde elemanları iter eder __iter__
print(list.__next__(list2)) # liste içerisinde elemanları iter eder __next__
print(list.__reversed__(list2)) # liste içerisinde elemanları tersine çevirir __reversed__


list.clear() # listi temizler clear