#Dictionaries...
#key=>value formate
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered
#When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
  
  
def introducer():
    person={
    'name':'sarvagya',
    'shirt':'black',
    'laptop':'apple',
    'asset':3000,
    'debt':2000,
    'favourite_fruit':['🍎','🥭','🍌','🍊','🍇'],  #we can add list inside a dictionary
    'networth':lambda:person['asset']-person['debt'],
     }
    print(f"my name is {person['name']} , my shirt color is {person['shirt']}  ,i have {person['laptop']} laptop and my networth is {person['networth']()} my faviourite fruit is {person['favourite_fruit']} ")
#  print(person['name'])
#  print(person['shirt'])
#  print(person['laptop'])
    print(person.values()) #to get dict_values and dict_key
    print(person.keys())
    #can convert Dictionaries into list 
    print(list(person.values()))
    
    #getting values from the list 
    for values in list(person.values()):
        print(values)

introducer()
#dictionaries are mutable .. ex below 
student={
    'name':'xyz',
    'shirt_color':'blue',
    'company':'amplus'
}
print(student['company'])
print(student)
student['company']='nagaro'
print(student['company'])
print(student)

#dictionaries are ordered.....
things={
    'fruit':'banana',
    'color':'black',
    'car':'audi'
    }
print(list(things))
print(list(reversed(things)))

#Dictionaries cannot have two items with the same key:means duplicate not allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)  #here it print latest year "year":"2020"

#To determine how many items a dictionary has, use the len() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

print(len(thisdict)) #not accept duplicate value and print only length  3 

#The values in dictionary items can be of any data type:
#here holds String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)

#create dictionaries.........
  # It is also possible to use the dict() constructor to make a dictionary.
# Using the dict() method to make a dictionary:



thisdict = dict(name = "John", age = 36, country = "Norway")
 
print(thisdict)


#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

#Add a color item to the dictionary by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)


#The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)