# **Lecture 01**

#### when on def keyword is used in python main frame then is a function.

#### when def keyword is used inside and defined a function then it is called as method.



#### **If define method in class like wise** 
``` 
class Item:
    def calculate_total_price():
        pass
```

#### **_Then error will be:_**
```
Traceback (most recent call last):
   File "c:\Users\ashis\OneDrive\Documents\GitHub\Python-Projects\Object Oriented Programming\Lecture 01\Class1.py", line 19, in <module>        
    item1.calculate_total_price()
TypeError: Item.calculate_total_price() takes 0 positional arguments but 1 was given
```

#### **Meaning of error:**

This means the error is when we define a object in python by instantiating then the object itself is passed as the argument to the methods that will be called using "." function. 

#### _Thus we need to define self in the method while define_


### Correct way of defining a method in class:

```
class Item:
    def calculate_total_price(self):
        pass
```