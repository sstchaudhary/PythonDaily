#function in python ..............
def say_my_name():
    print("sarvagya")
say_my_name()

#function with argument.....
def say_my_name_with_arg(name):
    # print("my name is:",name)
    print(f"my name is : {name}")
say_my_name_with_arg("sarvagya")

#function with multiple argument....
def  name_with_greeting(name,greetings):
     print(f"hi,{greetings} {name}")
name_with_greeting("sarvagya","GoodMorning")

#default argument...........
def name_greeting_with_default_arg(name,greeting="good morning"):
    print(f"hi {name} {greeting}")
name_greeting_with_default_arg("sarvagya")

#default argument always come in the end ....
#if trying to write default argument at begning and a 
# normal argument following default the error arise like  
#Non-default argument follows default argument

#named argument....
def name_greet(name,greeting):
    print(f"hii {name} {greeting}")

name_greet(name="sarvaya",greeting="good morring")

#function with returning some values ............

def sum_two_number(a,b):
    c=a+b
    return c
sum=sum_two_number(2,3)
print("sum is ",sum)

# def sum(a,b):
#     c=a+b
#     return c
# sum=sum(int(input("enter first number")),int(input("enter second number")))
# print("sum is ",sum)

#writing code in more pythonic way............

def sum(a:int,b:int)->int:
    return a+b
print(sum(20,30))

#lambda function...
sum2=lambda a,b:a+b
print(sum2(10,5))

#greeting with lambda function 

greet=lambda greet,name:f"{greet} {name}"
print(greet("good morning","sarvagya"))

#assertin testing 
assert sum_two_number(50,40)==90
assert sum_two_number(50,50)==100
assert sum_two_number(-10,10)==0
assert sum_two_number(-10,-20)==-30

print("all assertin tes passed ")
#==========================================================================
                    #LIST
#list=> list in python syntax wise just like array in other language
#  but some language just allow homogenious data storages 
#list allow hetrogenioius data element we can store any kind of data in List

fruits=["apple","orange","mango","banana"]
# how to access list element 
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])

#can access using for in loop ..........
for fruit in fruits:
 print(fruit)

#list is mutable so we can append fruit in fruits .....
fruits.append('grapes')
fruits.append('guvava')
for fruit in fruits:
 print(fruit)

 #slicing in list........
print("======================================slicing=============")
print(fruits[0:2]) #0th index is including but not 2nd 
print(fruits[0:4]) #printing first four 
print("modified list",fruits)
print(fruits[0:len(fruits)-1]) #only exclude last  fruit item from array
print("====================step by step===========")
print(fruits[0:6:1]) #step by one default
print(fruits[0:6:2])  #step by two expecting ['apple', 'mango',  'grapes']

#fruits[a:b:c]
#a=start index
#b=end index
#c=steps by steps 

#reverse list using slicing trick.........
print(fruits[::-1])

#list can hold different types of data types ...........
mylist=['apple',"mango",10,0.5,-10,]
print(len(mylist))

for listitem in mylist:
   print(listitem)

#lots of inbuild methods available in list ...........
#like pop(),clear(),append(),insert(),index(),remove(),count(),pop(),sort(),reverse()
#we can use this 
