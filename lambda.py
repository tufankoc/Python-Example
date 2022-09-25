#lambda fonksiyonu

from typing import List


sum = lambda x,y: x+y
print(sum(10,20))

square = lambda x: x*x
List = [1,2,3,4,5,6,7,8,9,10]
result = list(map(square,List))
print(result)