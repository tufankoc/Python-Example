# integer variable with a value of 10 and a type of integer (int) 
from distutils.log import info
from unicodedata import name


x=2
print(type(x))

# float (decimal) number 
y=2.0
print(type(y))

# complex number (real and imaginary part) 
z=2+3j
print(type(z))
print(z.real) # real part
print(z.imag) # imaginary part

# string  'abc'
s="Hello World. I am a string." 
print(type(s)) # string
print(s[0]) # 0. karekteri getiriyor
print(s[2:7]) # 2 ile 7 arasındaki karakterleri getiriyor
print(s[0:26:2]) # 0 ile 26 arasındaki karakterleri 2 şerli ile getiriyor
print(len(s)) # stringin uzunluğunu getiriyor
print(s.index("e")) # e harfinin index'ini getiriyor
y="Hello Space."
print(s+" "+y) # stringleri birleştiriyor
print(y*3) # 3 defa print() yazıyor
print(s+"\n"+y)

# boolean (true/false) (0/1) 
b=True
print(type(b))
print(10<5)
print(10>5)

# list (array) - array'lerin özellikleri: index, append, pop, insert, remove, reverse, sort
l=[1,2,3]
print(type(l))
print(l[0])
info1=["ahmet",30,"istanbul",True]
print(info1)
info1[0]="mehmet"
print(info1)
info2=["fatma",25,"izmir",False]
info3=[info1,info2]
print(info3)

# tuple  - çoklu elemanlı bir veri tipidir. Örneğin, bir liste'de çok sayıda aynı elemanın var olmasını istiyorsak, tuple tipi kullanılır. Tuple'ların değiştirilemezliklerini sağlar.
t=(1,2,3)
print(type(t))

# set (küme) - çoklu elemanlı bir veri tipidir. Örneğin, bir liste'de çok sayıda aynı elemanın var olmasını istiyorsak, set tipi kullanılır. 
s={1,2,3,2}
print(type(s))
print(s) 

# dictionary (sözlük) - anahtar-değer yapısıdır. Örneğin, bir çok sayıda aynı anahtarın var olmasını istiyorsak, dictionary tipi kullanılır. 
d={'name':'John','age':30,} # key:value
print(type(d))
print(d)
print(d['name'])
d['name']='Smith'
print(d)
d['born']='Los Angles'
print(d) 

# None - bir değerin yok olmasıdır. Örneğin, bir değerin değeri belirlenmediyse, None olarak belirtilir.
n=None
print(type(n))



#Exercise 
x = input("Enter 1. number: ")
y = input("Enter 2. number: ")
z = float(x)+float(y)
print("Answer: ", z)





# class - sınıf 
class MyClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def my_method(self):
        print("Hello")
obj=MyClass("John",30)
obj.my_method()


# function - fonksiyon 
def my_function():
    print("Hello")
my_function()
