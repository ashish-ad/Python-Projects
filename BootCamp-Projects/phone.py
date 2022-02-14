from Item import Item

class phone(Item):
     
     def __init__(self, name: str, price: float, quantity=0,broken_phone=0 ):
          # Run validation to received arguments
          assert broken_phone >=0 , f"Broken Phones {broken_phone} is not greater or equal to zero"
          super().__init__(
               name, price, quantity
          )
          # Assign to self object
          self.broken_phone = broken_phone
          
   


Item_phone = phone("Redmi Note 10", 20_000, 5, 4)
Item_phone1 = phone("Samsung S22", 1_00_000, 10)

