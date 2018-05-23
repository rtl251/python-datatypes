# groceries.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}]


#1. Print all products (already done for you!).
print(products)

#2.Print the first product.
print(type(products))

#3.Print the name of the first product.
print(products[0]["name"])

#4. Print the number of products.
print(len(products))

#5.Print the name of each product.
for p in products:
    print(p["name"])

#6. Print in alphabetical order the name of each product.
import operator
products_a2z = products
products_a2z.sort(key=operator.itemgetter('name'))
for p in products_a2z:
    print(p["name"])

#7.Print in alphabetical order the name of each product, and include its price rounded to two decimal places.
import operator
products_a2z = products
products_a2z.sort(key=operator.itemgetter('name'))
for p in products_a2z:
    print(p["name"], round(p["price"],2))

#8.Print the number of unique departments.
mylist = []
for p in products:
    mylist.append(str(p["department"]))
print (len(set(mylist)))

#9.Print the name of each unique department.
mylist = []
for p in products:
    mylist.append(str(p["department"]))
print (set(mylist))

#10.Print in alphabetical order the name of each unique department.
mylist = []
for p in products:
    mylist.append(str(p["department"]))

nodups = []
for p in mylist:
    if p not in nodups:
        nodups.append(p)

nodups=sorted(nodups)
for p in nodups:
    print(p)


#11. Print in alphabetical order the name of each unique department, as well as the number
# of products associated with that department.
#from collections import Counter

from collections import Counter
mylist = []
for p in products:
    mylist.append(str(p["department"]))

mylist=sorted(mylist)
list_count=Counter(mylist)
print(list_count)

#12.Print in alphabetical order the name of each unique department,
# as well as the number of products associated with that department, and properly differentiate
# between "products" plural and "product" singular, depending on how many there are.

#from collections import Counter

#mylist = []
#for p in products:
    #mylist.append(str(p["department"]))


#mylist=sorted(mylist)
#dict_count=Counter(mylist)
#newdict={}

#for p in dict_count:
    #newdict.append(p)

#Can't figure out how to alter values only in dictionary :/
