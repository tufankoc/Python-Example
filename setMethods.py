cluster = {
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
}
print(cluster) 
cluster.add("A") # add() methodu kümeye eleman ekler. 
print(cluster)
cluster.remove("a") # remove() methodu kümeden eleman siler.
print(cluster)
cluster.discard("A") # discard() methodu kümeden eleman siler.
print(cluster)
cluster.pop() # pop() methodu kümeden eleman siler.
print(cluster)
cluster.clear() # clear() methodu kümeden tüm elemanları siler.
print(cluster)
cluster.update(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]) # update() methodu kümeye eleman ekler.
print(cluster)
print(cluster.__contains__("A")) # __contains__() methodu kümede eleman var mı diye bakar.


