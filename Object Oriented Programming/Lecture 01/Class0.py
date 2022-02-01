class Item: # It is always a good practice to start the class name with capital letter
    pass

item1 = Item() # this is equivalent to random "random_str = str()"

item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))
print('\n')
random_str ="aaa"
print(random_str.upper())

# output:
#     <class '__main__.Item'>
#     <class 'str'>
#     <class 'int'>
#     <class 'int'>
#     AAA