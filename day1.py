#basically comment  start with # and python ignore them during execution....
a=10
b=20
print(a+b)
#line four print sum of a and b but if i comment it python ignore this 
# print(a+b)  i comment this 
print ('this is comment that wrriten in line 1,5 and 6')

#------------------------------------------------------------------------------
#variabels 
#variables thats use to store dataor values on behalf of user  it can be string, number,list,dictionary etc
a=10
b=20
print(a)
print(b)
#note 
# 1-variable name can not be start from number  like 123a 
# 2-variable can start with underscore ex _123a
# 3-variable can not be start with special characer like @,#,$,%,&,. etc
# variable never have space between letter and words like a b=10,abc abc=20,a b c=10
#can use _ at the place of blank space.... abc_abc=10

#important  note 
#variable stored in python or make memory in system on the..
#basis of value stored in variable not depend of variable name 

a=10
b=10
print(id(a)) #140715070448712
print(id(a)) #140715070448712


#here variable name different ,value are same and the address are appear same when print it .
a=20
b=30
print(id(a))   #140715070449032
print(id(b))   #140715070449352

#here variable name different ,value are differen and the address are appear also different when print it .

#we can declared multiple variable in one line 

a,b,c=10,20,"hello"
print("a value is",a)
print("b value is ",b)
print("c value is ",c)

#how to take input from user in console and perform some action 

a=int(input("enter value of a "))  #input always provide string so convert it into int
b=int(input("enter the value of b ")) #input always provide string so convert it into int
c=a+b
print(f"addition of {a} and {b} is ",c)

#print your name on console take input from console 

my_name=input("Enter Your Name ")
print(my_name)

#if i not convert input in int it consider string and cancatinate it,if dont want to perform 
#cancatinatin convert both input in string
a=input("enter first number ")   #10
b=input("enter second  number ")  #20
c=a+b
print(c) #1020(cancatination perform)

#math operator +,-,/,*,//,% 
a=10
b=20
c=a+b #30
c=a*b #200
c=a/b  #0.5
c=a//b   #0 it print only full part not print after decimal
c=a%b
print(c) 

#calculator app 
food_charge=100
tippercentage=20/100
tip=food_charge*tippercentage
totalspend=food_charge+tip
print(totalspend)
#convert this app and take input from  user 

food_charge=int(input('Enter total food charge in dolar '))
gstpercentage=food_charge*(30/100)
tip_percentage=input('Enter tip percentage ')
tip=food_charge*(int(tip_percentage)/100)
totalspend=food_charge+tip+gstpercentage
# print("my total spended over the food is ",totalspend)
# string formatting print totalspend usinf string formatting 
print(f'my total spend on food is ${totalspend}')

#boolean data type ......
#True and False  only can be the value of the boolean data type...
a=True  
if(a):
    print("true")
else:
    print("false")

#weather emoji app
weather=input('how is the weather ? ')
if (weather=='rain'):
    print("☔")
elif (weather=='cloudy'):
    print("👕")
elif (weather=='winter'):
    print("🔥")
else:
    print("🌞")

#  write  code in pythonic way
score=int(input("Enter your Number"))
if score>60 and score<=100:
      print("passed with 'A' grade")
elif score>40 and score<=60:
    print("passed with 'B' grade")
elif score>=30 and score<=40:
 print("passed with 'c' grade")
else:
    print("Failed ! good luck for next time. ")



 




