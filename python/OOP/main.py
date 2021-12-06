from Item import Item
from Phone import Phone

item1 = Item('myItem', 750)
print(item1.name)

item1.name = "OtherItemmmmm"
print(item1.name)

item1.apply_increment(0.2)
print(item1)
item1.apply_discount()
print(item1)