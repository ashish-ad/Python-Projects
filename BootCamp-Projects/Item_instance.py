from Item import Item
from phone  import phone

item1 =  Item("Phone", 100,1)
item2 = Item("Laptop",1000,3)
itme3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


Item_phone = phone("Redmi Note 10", 20_000, 5, 4)
Item_phone1 = phone("Samsung S22", 1_00_000, 10)



print(phone.all)
print(Item.all)

# phone_all = phone.all
# for j in phone_all:
#     print(j)
#     print("Ashish")

# item_all = Item.all
# for i in item_all:
#     print(i)
#     print("Pradhan")