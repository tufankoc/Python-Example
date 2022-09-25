# for döngüsü
for i in range(1,10):
    print(i)
    if i == 5:
        continue
    elif i == 7:
        continue
    print("i = {}".format(i))

# Example 1
x = [0,1,2,3,4,5,6,7,8,9,10]
for i in x:
    print(i)

# Example 2
number = range(1,10) # 1,2,3,4,5,6,7,8,9 değerlerini verir
for i in number:
    print("{}. Tufan Koç".format(i))

# Example 3
number = range(1,1010000)
for i in number:
    if i%2 == 0:
        print("{} çifttir".format(i))
    else:
        print("{} tektir".format(i))

# while döngüsü
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    elif i == 7:
        continue
    print("i = {}".format(i))
    i += 1

