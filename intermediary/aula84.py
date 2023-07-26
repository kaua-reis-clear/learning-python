my_list = []

for number in range(10):
    my_list.append(number)
    
# print(my_list)

my_list = [
    number * 2
    for number in range(10)
]

print(list(range(10)))
print(my_list)

# Mapping data in list comprehension
products = [
    {'name': 'p1', 'price': 20,},
    {'name': 'p2', 'price': 10,},
    {'name': 'p3', 'price': 30,},
]

new_products = [
  {**product, 'price': product['price'] * 1.05}
  if product['price'] > 20 else {**product}
  for product in products
]

print(new_products)
print(*new_products, sep='\n')