info = {
    'name': 'John',
    'surname': 'Doe',
    'age': 30,
    'city': 'New York',
    'born': 'Los Angles',
    'is_married': False,
    'children': [ 'Jane', 'Mark' ],
    'cars': [ 'BMW', 'Audi' ]
}

print(info.keys()) # dictionary'in keylerini liste şeklinde verir.
print(info.values()) # dictionary'in değerlerini liste şeklinde verir.
print(info.items()) # dictionary'in key-value parçalarını liste şeklinde verir.
print(info.get('name')) # dictionary'in key'i verilen değerin değerini verir.
print(info.get('name', 'Not found')) # dictionary'in key'i verilen değerin değerini verir. Eğer key'i verilen değer yoksa Not found değerini verir.
info2 = info.copy() # dictionary'in kopyasını verir.
info.update({'name': 'John ', 'surname':'Simith'}) # dictionary'in key'i verilen değerin değerini verir.
print(info)
print(info2)
print(info.pop('name')) # dictionary'in key'i verilen değerin değerini siler.
print(info.__len__()) # dictionary'in keylerinin sayısını verir.
print(info.__contains__('name')) # dictionary'in key'i verilen değerin varlığını verir.