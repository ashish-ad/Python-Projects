class Item(object):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price *self.quantity
        




# The double underscore mehtod that is called as special function and is used when ever we create a instance of the class the __init__(): method is used to instantiate into the object like if we define variable inside then while instantiating the object from class we will have to pass all the attributes whatever variable is defined inside __init function.



# Now here variables are being passed by name, price and quantity while creating a object 
# This way of creating object and instantiating object by __init__special function is called as constructor.

# We can set some default values while initiating attributes int __int__ function like:
#                 class Item:
#                       def __init__(self, name, price, quantity = 0):
#                           self.name = name
#                           self.price = price
#                           self.quantity = quantity
#
#
# AS we can see that the value of quantity passed in __init__ function is called as default value of the attritbute that is passed to it.



item1 = Item("Phone",100,5)
item2 = Item("Laptop",1000,3)
print(item1.name,'\n',item1.price,'\n',item1.quantity,'\n',item2.name,'\n',item2.price,'\n',item2.quantity)