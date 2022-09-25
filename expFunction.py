#sınırsız argümanlar
def my_func(*args): #args is a tuple of arguments
    print(args) 
    for i in args: 
        print(i) 

my_func(1,2,3,4,5,6,7,8,9,10) 

def id(**args): #args is a dictionary of arguments
    for i in args.keys(): 
        print(i)

id(a=1,b=2,c=3) 

#ortalama alma
def average(*args): #args is a tuple of arguments
    return sum(args)/len(args)

print(average(10,20))

#2 ortalama alma
def average2(*x): #args is a dictionary of arguments
    result = 0
    for i in x:
        result += i
        result1 = result/len(x)
    return round(result1,3)

print(average2(5,10,14))
