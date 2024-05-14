#!/usr/bin/env python
# coding: utf-8

# In[70]:


#Mathematical operator

a,b= 10,3
print(a+b)
print(a-b)
print(a/b)  #Standard division
print(a%b)  #Remainder
print(a//b) #Floor division # divides the number and then rounds down to the nearest whole number
print(a*b)  #Multiplication
print(a**b) #square


# In[ ]:


#Equal to sign
==
#Not equal to sign
get_ipython().system('=')


# In[7]:


# 'username' is not the same as 'userName' #use underscores (_) to separate the words,like this_is_a_variable_name
#x += 2 simply means x = x + 2.

#Integers are numbers with no decimal parts, such as -5, -4, -3, 0, 5, 7 etc. e.g userAge = 30, pin_code = 272154

#Float refers to numbers that have decimal parts, such as 1.234, -0.023,12.01 e.g userHeight=1.82, userWeight=67.2

#To declare a string, you can either use variableName = ‘initialvalue’ (single quotes) 
#or variableName = “initial value” (double quotes) e.g userName = ‘Peter’, userSpouseName = “Janet”, userAge = ‘30’

# NOTE---> , if you wrote userAge = 30 (without quotes),userAge is an integer.

#We can combine multiple substrings by using the concatenate sign (+). For instance, “Peter” + “Lee” is equivalent
#to the string “PeterLee”.

#upper() and lower() method for strings

"RAM".lower() # Converting uppercase character to lowercase. If there are no uppercase characters in the given string, 
#it returns the original string.


# In[8]:


"ram".upper()   #Capitalize all the letters in a string


# In[ ]:


#TYPE CASTING IN PYTHON

#Convert from one data type to another, such as from an integer-----> to a string.

#There are three built-in functions in Python that allow us to do type casting. These are the int(), float(), 
# and str() functions.

#int(5.712)----> 5 ,int("4")----> 4   where 5.712 is float, and "4" is string.
# NOTE---> we cannot type int (“Hello”) or int(“4.22321”). We’ll get an error in both cases

#float(2)----> 2.0, float("2")-----> 2.0   where 2 is integer, and "2" is a string

#string(2)---> "2" , string(2.0)----> "2.0"


# In[ ]:


#LIST

# we use square brackets [ ] when declaring a list. Multiple values are separated by a comma.
# For instance, userAge = [21, 22, 23, 24, 25]

#We can also declare a list without assigning any initial values to it. We simply write listName = []. What we have now is an empty list with
#no items in it. We have to use the append() method mentioned below to add items to the list.

#Individual values in the list are accessible by their indexes, and indexes always start from ZERO, not 1

#Alternatively, you can access the values of a list from the back. The last item in the list has an index of -1, 
#the second last has an index of -2 and so forth.

#List items are ordered, changeable, and allow duplicate values.

#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list.

#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

##List items can be of any data type:
#String, int and boolean data types:


#list1 = ["apple", "banana", "cherry"]
#list2 = [1, 5, 7, 9, 3]
#list3 = [True, False, False]

#A list with strings, integers and boolean values:
#list1 = ["abc", 34, True, 40, "male"]


# In[14]:


list =['veg','cook','place','worker','drinks']

print(list[0])  #  0 INDEX
print(list[1])  #  1 INDEX
print(list[-1]) # -1 INDEX
print(list[-2]) # -2 INDEX


# In[22]:


#It is also possible to use the list() constructor when creating a new list.

fruit = list(("apple","orange","banana","grapes")) ## note the double round-brackets
print(fruit)


# In[18]:


#TUPLE

# we use round brackets ( ) when declaring a tuple. Multiple values are separated by a comma.
# for instance, tuple = ("apple","orange","banana","kiwi","grapes")

#You access the individual values of a tuple using their indexes, just like with a list.

#Tuple items are ordered, unchangeable, and allow duplicate values.

#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#Since tuples are indexed, they can have items with the same value:


# In[12]:


tuple = ("apple","orange","banana","kiwi","grapes")
print(tuple[0])  #  0 INDEX
print(tuple[1])  #  1 INDEX
print(tuple[-1]) # -1 INDEX
print(tuple[-2]) # -2 INDEX
print(len(tuple)) #To determine how many items a list has, use the len() function:


# In[ ]:





# In[ ]:


#.............IMPORTANT NOTE..........#
#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.



# In[ ]:


#DICTIONARY

#we use curly brackets { } when declaring a dictionary. Multiple pairs are separated by a comma.
Dict = {1:"apple",2:"orange",3:"banana"} # 1,2,3 --->key    apple,orange,banana --->value

# you cannot declare a dictionary like this: myDictionary = {“Peter”:38, “John”:51, “Peter”:13}
#This is because “Peter” is used as the dictionary key twice.

#


# In[24]:


#string to list
list('python')


# In[25]:


#Dictionary 

Dict = {1:"apple",2:"orange",3:"banana"} # 1,2,3 --->key    apple,orange,banana --->value
print("Items are =",Dict)
del Dict[1]  #Delete item number 1
print("Items are =",Dict)
del Dict[3]  #Delete item number 3
print("Items are =",Dict)


# In[31]:


# write a program to print all even numbers among 1 to 100
number = list(range(1,101))
     for i in number:
        if i%2 == 0:
            print(i)


# In[16]:


#indexing
'python'[0]  # always starts from zero, end with -1


# In[5]:


#indexing
'python'[1]


# In[6]:


#indexing
'python'[3]


# In[7]:



'I AM PYTHON'[0:6]


# In[8]:


'AAAABBBBCCCCC'[1:10:3]


# In[9]:


'PYTHONCLASSES'[1:10:3]


# In[13]:


#DATA TYPE LIST
listx=[1,3,4, 'abc']


# In[14]:


listx.append('python')


# In[ ]:


listx


# In[ ]:


[1,3,4,'abc','python']


# In[ ]:


listx.extend(['abc','xyz'])


# In[ ]:


listx. #. dot operator get us different methods from data type


# In[ ]:


[1,3,4,'abc','python','abc','xyz']


# In[15]:


['a','a','a'].count('a')


# In[16]:


#Tuple
t1=(1,1,2,3)
print(type(t1))


# In[17]:


t1[0]


# In[ ]:


t1[0]= 'a' tuple cant be changed


# In[19]:


alien_0={'color':'green','points':100}
print(type(alien_0))


# In[20]:


alien_0['color']


# In[ ]:


alien_0['color']='red'


# In[ ]:


alien_0
{'color':'red','points':100}


# In[ ]:





# In[ ]:





# In[ ]:





# In[21]:


#######............set.................######.........Duplicates Not Allowed
#Once a set is created, you cannot change its items, but you can remove items and add new items.
#Sets are used to store multiple items in a single variable.



set('aaabcdeeff')


# In[1]:


thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)


# In[2]:


thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)


# In[ ]:





# In[23]:


list(range(-2,2)) # ()---> Here final value will be excluded


# In[98]:


#Python's enumerate method allows you to iterate over a list, tuple, or dictionary and 
#return a tuple containing the index of each element and the element itself


# In[ ]:





# In[24]:


list(enumerate(['a', 'b', 'c', 'd', 'e', 'f'])) #enumerate will be useful for indexing


# In[25]:


zip([1,2],['a','b'])


# In[28]:


list(zip([1,2],['a','b']))


# In[33]:


input()
list= 'python'


# In[ ]:


print(list)


# In[ ]:


'python',c++,java,julia,split(',')  #string to list


# In[32]:


'python'.upper()


# In[9]:


Restaurant =['veg','cook','place','worker','drinks']

print(Restaurant[-1])


# In[10]:


Restaurant =('veg','cook','place','worker','drinks')
print(Restaurant[-2])


# In[1]:


Restaurant =('veg','cook','place','worker','drinks')
print(Restaurant[1])


# In[15]:


a,b=5,2
print(a**b)
print(a//b)
print(a%b)


# In[18]:


int(5.8) #type casting


# In[25]:


float('49') # type casting


# In[22]:


str(4) # type casting


# In[30]:


int(3.7)  #type casting


# In[28]:


'ramdhari'.upper() ##upper() method for string


# In[29]:


'RAMDHARI'.lower()  ##lower( )method for string


# In[ ]:





# In[50]:


subject = "chemistry" #Formatting Strings using the % Operator
experience=4    #We use the %s and %d formatters as placeholders in the string.
mess="Ram dhari pandey is known for %s from last %d years"%(subject,experience)
print(mess)


# In[73]:


NHPC=1.23416#5.3f where 5 refers total length and 3 refers 3 decimal places. f represents float(number with decimal)
message="I want to buy a stock of price %5.3f"%(NHPC)
print(message)


# In[84]:


#The parameter 'Apple’ has a position of 0 ,1299 has a position of 1 and 1.235235245 has a position of 2 #Positions always start from ZERO.

message = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('apple',1299,1.23456)
print(message)


# In[88]:


number=[20,21,22,23,24] #list #use square brackets [ ] when declaring a list.
print(number[0])  #indexes always start from ZERO,
print(number[1])
print(number[2])
print(number[-1]) #The last item in the list has an index of -1


# In[7]:


number=[20,21,22,23,24]
number[3]=10
number.append(50)  # If you want to add value(50) in the end
print(number[-1])
print(number[2])


# In[ ]:


#plan for class-2
(1)If-Else condition
(2)Loops-for,while-inner Loop(Loop inside Loop)
(3)combination of If-Else and Loops
(4)break,continue, and pass
(5)Iterators #A process that is repeated more than one time by applying the same logic is called an Iteration.
(6)List comprehension-advanced


# In[10]:


#SYNTAX-FORMULA,PSEUDO CODE
#(1)If-Else:
if <condition>:                      # Useful in seperating protein sequences
    <code>
  # induntation  
    
elif(if-else) <condition>
    <code>
    
else:
    <code>


# In[26]:


#write a progarm to get the number from user and check whether it is even or odd
x=int(input("what number is in your mind"))

if x % 2 == 0:
    print("number is even")
    
else:
    print("number is odd")
    

        


# In[32]:


#write a program to get the number from user and check whether number is grater than 100 or not
number=int(input("what is the number in your mind"))

if number > 100:
    print('yes ,it is grater than 100')
    
else:
    print('yes,it is less than 100')
    


# In[91]:


z=int(input("what is the number in your mind?"))
if z % 2 ==0:
    print("number is Even")
if z % 2 !=0:
    print("number is Odd")


# In[71]:


#check the number whether it is +ve,-ve anything!
xx=int(input("what is number in your mind"))

if xx>0:#if "IF" condition passes, it goes out program,#it does not care about elif, else!
        print("+ve")
 
elif xx < 0:
    print("-ve")

else:
    print("It is zero")


# In[79]:


#write a program to check a given number is divisible by 9,18,27 or not?

a = int(input("Please enter a number"))
if a % 9 == 0:
        print("Yes,it is divisble by 9")
        
if a % 18 == 0:
       print("Yes, it is divisble by 18")
        
if a % 27 == 0:
    print("Yes, it is divisible by 27")



# In[75]:


# write a program to get the number from user to check whether a number is divisible by 3,5,6

x=int(input('enter a number'))

if x % 3 == 0:
    print("yes it is divisible by 3")
    
if x % 5 == 0:
    print("yes it is divisible by 5")
    
if x % 6 == 0:

    print("yes it is divisible by 6")


# In[73]:


#(2)Looping
cities= ['torun','warsaw','lodz','bodgoz']




# In[ ]:


3 syntax for 

for<item> in <iterables>
   <item>


# In[80]:


# Iterables is an object which contains stream of data
cities= ['torun','warsaw','lodz','zakopani']
for city in cities:
    print("I have visited cities")


# In[ ]:


I


# In[72]:


#write a list and it should have some numbers, and add 5 to each numbers in the list
n=list(range(1,6))  # same as n=[1,2,3,4,5]
for i in n:  #Iterate through each element in the list
    i=i+5    # Add 5 to the current element
    print(i)
    


# In[78]:


n=list(range(1,5)) # In range, last number is excluded  #Same as n=[1,2,3,4]
b=[]
for i in a:
    i=i-1
    b.append(i)
print(b)
    
    


# In[54]:


a=[1,2,3,4]
b=[]
for i in a:
    i=i+5
    b.append(i)
print(b)


# In[65]:


a=[1,2,3,4]
b=[]
for i in a:
    if i!=2:
        i=i+5
        b.append(i)
print(b)


# In[ ]:





# In[ ]:


# while Loop!
 <initialization>
    
 while<condition>
     <code>
    
    <increment/decrement>


# In[26]:


while True:
    print('yes!')


# In[44]:


a=True

while a:
     comment=input('what is your password?')
        
     if comment == 'end':
        


# In[ ]:





# In[4]:


i=5  # print number from 5 to 0
while i>=0:
    print(i)
    i=i-1


# In[2]:


i=0  # print number from 0 to 5
while i<=5:
    print(i)
    i=i+1


# In[26]:


i=-2  # print number from -2 to 3
while i<=3:
        print(i)
        i=i+1


# In[25]:


number = list(range(-3,4)) ### for loop is used for iterating over a sequence (that is either a list, a tuple, 
for i in number:  # a dictionary, a set, or a string)
    print(i)
    


# In[68]:


number = [*range(-3,3)]
for i in number:
    print(i)


# In[63]:


number = [1,2,3,4,5,6,7,8]
for i in number:
    if i % 2 !=0:
        print(i)
    


# In[65]:


number = list(range(-3,4)) # for loop is used for iterating over a sequence (that is either a list, a tuple,
for i in number:           # a dictionary, a set, or a string)
    if i % 2 !=0:
        if i !=1:
            print(i)


# In[51]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# In[74]:


for x in range(4): # Zero is included
  print(x)


# In[71]:


for x in "Ram": #Even strings are iterable objects, they contain a sequence of characters
  print(x)


# In[66]:


# create a time bomb which should count from 1 to 4 and after 10, it needs to 


# In[41]:


x=1
while x<4:
        print('tick tick', x)
        print('booomm')
        x=x+1


# In[45]:


fruits = ["apple", "banana", "cherry"]    ###########.....break statement....##########
for x in fruits:
  print(x)
  if x == "banana":
    break


# In[44]:


fruits = ["apple", "banana", "cherry"]  #
for x in fruits:
  if x == "banana":
    break
  print(x) 


# In[66]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# In[67]:


x= list(range(1,6))
for i in x:
    if i==4:
        continue
    print(i)
            
               


# In[68]:


x= list(range(1,6))
for i in x:
    print(i)
    if i==4:
        continue
    
            


# In[10]:


a=[1,2,3,4,5]  #Square all the elements from "a" and store it in "b"
b=[]
for i in a:
    i=i**2
    b.append(i)
print(b)    


# In[ ]:





# In[ ]:


#nested  for loop --loop inside loop
#syntax
for <variable1> in <iterable1>:  # outer loop
    <code>
    
  for<variable2> in <iterable2>:  # inner loop
        <code>


# In[ ]:


#nested  while loop
#initialization!
while<


# In[ ]:


#class-3 date 26/03/24
(1)List/generator comprehension
(2)sting formatting
(3)Itertools  
(4)Functions


# In[33]:


#Square all the elements from lista and store it in listb!
lista =[1,2,3,4]
listb=[]

for x in lista:
    listb.append(x**2)
    
print(lista+listb)   


# In[35]:


lista=list(range(1,7)) ##Square even number from lista and store it in listb!

listb=[]

for x in lista:
    if x % 2 == 0:
        listb.append(x**2)
    

print(listb)




# In[16]:


lista=[1,2,3,4]  ##Square odd number from lista and store it in listb!

listb=[]

for x in lista:
    if x % 2 != 0:
        listb.append(x**2)
    

print(listb)


# In[69]:


a = [0, 5, 10, 15, 20] #Iterator
for i in a:
    if i % 2 == 0:
        print(str(i)+' is an Even Number')#The str(i) converts the integer i to a string so it can be 
    else:                                  #concatenated with the rest of the message
        print(str(i)+' is an Odd Number')


# In[ ]:


#list_comp
#syntax
var= [<what_you_want_code> <for_loop>]
var= [<what_you_want_code> <for_loop> <if>]
var= [<what_you_want_code> <if_else> <for_loop>]
var= [<what_you_want_code> <for_loop1> <for_loop2>]


# In[45]:


list1=list(range(1,10))
list2=[]

for x in list1:
    if x%2 !=0: #Not equal to sign(!=)
        list2.append(x)
        
print(list2)        


# In[96]:



# initializing the list 
list = [] 
  
for i in range(11): 
    if i % 2 == 0: 
        list.append(i) 
  
# print elements 
print(list) 


# In[ ]:


#####################.............List_comprehension............##############
#syntax
var1= [<what_you_want_code> <for_loop>]
var2= [<what_you_want_code> <for_loop> <if>]
var3= [<what_you_want_code> <if_else> <for_loop>]
var4= [<what_you_want_code> <for_loop1> <for_loop2>]


# In[ ]:


#Square all the elements from lista and store it in listb using ------> list_comprehension

#var1= [<what_you_want_code> <for_loop>]

lista=[1,2,3,4]
xyz=[a**2 for a in lista]
print(xyz)


# In[88]:


list1=list(range(1,10))    #################......List comprehension.......#################

#var2= [<what_you_want_code> <for_loop> <if>]

odd= [x for x in list1 if x%2 !=0]  #List comprehension offers a shorter syntax when you want to create  a new list based on the values of an existing list
print(odd)


# In[95]:


#var2= [<what_you_want_code> <for_loop> <if>]

list1=list(range(10))
odd= [x**2 for x in list1 if x%2 !=0]  #List comprehension offers a shorter syntax when you want to create  a new list based on the values of an existing list
print(odd)


# In[56]:


#var1= [<what_you_want_code> <for_loop>]

dummy=[[],{},(),'ssss']#dummy is a list containing four elements: an empty list [], an empty dictionary {}, an empty tuple (), and a string 'ssss
data_type=[] 
data_type= [type(x) for x in dummy]#This is a list comprehension that iterates over each element m in the dummy list.
print(data_type)#for each element, it retrieves its type using the type() function and appends it to the data_type list.


# In[91]:


#If-else in list_comp
#var3 = [<what_you_want_code> <if-else> <for-loop>]

numbers= [1,3,2,5,7,4,8,9,10,11,19,17,26]
ans= ['even' if i%2 == 0 else 'odd' for i in numbers]
print(ans)


# In[93]:


#var4 = [<what_you_want_code> <for_loop1> <for_loop2>]
list1 = ['python','java']
list2 = [1997,1990]

nested_loop = [(i,j) for i in list1 for j in list2]
print(nested_loop)


# In[ ]:


# Generator_comp
var= (<what_you_want_code> <for_loops>)
var=(<what_you_want_code> <for_loops> <if>)
var=(<what_you_want_code> <if_else> <for_loops>)
var=(<what_you_want_code> <for_loop1> <for_loop2>)


Advantages


# In[ ]:





# In[ ]:





# In[ ]:





# In[127]:


listaa =[1,2,3,4]


# In[ ]:





# In[128]:


#function


# In[129]:


# BMI (Body Mass Index), weight in kg /(height) **2 in meter
#60 kg ,170 cm


# In[130]:


print(30/1.34)
print(40/1.74)
print(50/1.84)
print(60/1.44)


# In[ ]:


# syntax of function

def <function_name> (<arguments>):
    """doc string"""
    <code>
    


# In[132]:


def BMI (weight,height): #Function name
    """this is doing bmi calculation"""
    print(weight/height**2)
    


# In[133]:


BMI(60,1.6)# FUNCTION CALLING


# In[134]:


# AREA OF TRIANGLE 1/2 * b * h

def tri (b,h):
    print('triangle area is',1/2 * b * h)
tri(20,40)    


# In[135]:


tri(10,89)


# In[73]:


#print vs return

def dummy_1():
    print('HEY I am dummy file')
    print('Bye')
dummy_1()    


# In[83]:


def dummy_2():
    return 'HEY I am dummy file'
    print('Bye')
dummy_2()  


# In[79]:


# position arguments, keywards arguments
def about (Name, Age):
    print(f'Hello,My name is {Name}, and I am {Age} years old') #the 'f-string' allows you to directly insert the values of 'name' and 'age' into the string.
    #proper string formatting
   


# In[80]:


about('Tom',28) #position arguments


# In[138]:


about(Age=28, Name='Tom') # keywards arguments


# In[139]:


# defaults arguments
def registration (name,country='Austria'):  # defaul---->Country is already given
    print(f'My name is {name}, and I am from {country}')


# In[140]:


registration ('Tom','India')


# In[141]:


registration('Tom') # defaul---->The country "Austria" is already given


# In[142]:


#none

def life (Name, department, country=None):
    print(f'My name is {Name}, and I am pursuing Ph.D in {department}, and I am from {country}')
    
life('Tom', 'chemistry')    


# In[169]:


#PIZZA_HUT
def pizza (name,sex, address,pizza_size):
    """Hey I am pizza function"""
    print("*******Hey weicome to our pizza_Hut*******")
    
    name=input("what is your name?")
    if sex == 'M':
        print("Hey we are pleased to have you,Mr",name)
        
    if sex == 'F':
         print("Hey we are pleased to have you,Mrs",name)
            
    if sex == 'O':
         print("Hey we are pleased to have you,Thg",name)
            
    flag=True   

    while flag:
        pizza_size = int(input('what size of pizza do you want in cm?'))
        
    if pizza_size > 851000:
            print("Hey it is big, we do not have that huge size pizza")
            
    else:
        
        flag = flag
        
        print("oh what toppings do you want?")
    
    toppings = []
    for i in range(5):
                item = input()
                
    print('Item',i+1, 'Added')
    toppings.append(item)
            
    suggestion = input('Do you want any sugges?')
    details = {}
    print('*****Your billing*****')
        
    details['name'] = name
    details['sex'] = sex
    details['address'] = address
    details['pizza_size'] = pizza_size
    details['sugges'] = suggestion
    
    print(details)
        
    print()
    print(" thank you so much and your pizza is delivered at Dorm no-2")
    


# In[ ]:


****class-4
(1)*arg,**kwargs
(2)string formatting
(3)print vs return
(4)more functions and properties


# In[ ]:





# In[7]:


#print vs return
def dummy ():
    print('Hey I am dummy file')
    print('Bye')
    
dummy()   


# In[8]:


def dummy ():
    return('Hey I am dummy file')
    print('Bye')
    
dummy()    


# In[ ]:


# write a function to calculate gravity
def gravity ()


# In[ ]:





# In[20]:


#*argss-arbitary arguments ######## Using *args to pass a variable number of non keyword arguments to a function
def pizza(*toppings):
    print('hey you are ordered with the toppings',toppings)
    
pizza('cheese','mayo','garlic')
pizza('Chiken','Egg','Fish','Mutton','Salmon')


# In[ ]:





# In[21]:


def abroad(*trip):  ### Using *args to pass a variable length of non keyword arguments to a function
    print('we are exploring Europe',trip)
    print('Switezerland is very expensive',)
    print(len(trip))
    print(type(trip))
abroad('warsaw','Venice','Amsterdom')    
abroad('paris','zuric','Barcelona','Berlin','Munich')   


# In[18]:


def add(*b):  ##### Using *args to pass a variable number of arguments to a function
    c=0  #In the function, we should use an asterisk * before the parameter name to pass variable length arguments.
    for i in b:
        c=c+i
    print(c)
    
add(4,5,9)
add(9,3,4,6)
add(3,4,5,8,5)
add(1,3,5,7,9,4)
   

    


# In[3]:


def add(a,*b): # 
    c=0
    for i in b:
        c=c+i
        print(c)
        
add(1,2,3,4,5)


# In[ ]:





# In[ ]:


#write a function to take parameters, "name","subjects",you want to make subjects as flexible 
#simply call/print the name and subjects
print(f'hey {name} and I see you are taking these courses{subjects}')


# In[36]:


def about(name,*subjects):
    print(f'hey {name}, I saw, you are taking {subjects}')
    
about('maths','science','arts','geography','python')    


# In[11]:


#kwargs-keywords arguments##Python passes variable length non keyword argument to function using *args but we cannot 
#use this to pass keyword argument. For this problem Python has got a solution called **kwargs it allows us to pass
#the variable length of keyword arguments to the function. In the function, we use the double asterisk ** before
#the parameter name to denote this type of argument.
        
      


# In[40]:


def my_func(**kwargs,):    ###variable length of keyword arguments
    for key, value in kwargs.items():
        print(f'{key}:{value}')
        
my_func(Chiken="Tikka",chai="Tandoori")
my_func(Desi1="Daru",Desi2="katta",Desi3="egg")
        
    


# In[ ]:


#function properties- first class functions
***rule 1** ---->function can be assigned variables


# In[12]:


def simple():
    print('hey i am simple function')
    
simple()
print(type(simple))


# In[13]:


x=simple
print(type(x))


# In[14]:


id(x),id(simple)


# In[ ]:


***rule 2** ---->functions can be passed as arguments in another functions


# In[18]:


def fun_1(a,b):#first function
    ans=a+b
    return ans

def fun_2(fun,c): # second function  # here fun is a variable name you could take anything
    return x+c

fun_2(fun_1(1,2),3)


# In[20]:


***rule 3** ---->functions can be returned from another functions

def fun1(a): #outer function
    
    def fun2(b): #inner functions
        
        return a*b
    
    return fun2

x = fun1(10)
print(x)
print(x(2))


# In[ ]:


***rule 4***--->functions can be stored in the data structures


# In[24]:


def square(x): #fun1
    return x**2

def cubic(x): #fun2
    return x**3

operations = [square,cubic] #list

for op in operations:
    print(op(10))


# In[ ]:


###########.............Lambda function.........############ 
syntax:
    
<var> = lambda <parameters> : <operation/codings>


# In[25]:


#write a function to add two numbers

def add (a,b):
    return a+b

add(1,2)


# In[26]:


add_1 = lambda a,b : a+b
add_1(1,2)


# In[27]:


mul = lambda a,b : a*b
mul(3,4)


# In[ ]:


# Higher order functions ----> functions can be used inside the functions
1) map
2)filter
3)reduce


# In[28]:


numbers= list(range(1,20))
print(numbers)


# In[ ]:


#map(fun, <data_string>)
#map fun takes a fun and a data string
#and it does  operate on it
#return a list


# In[85]:


print(*map(lambda i:i**2,range (10)))
print(*filter(lambda i:i%2 == 0, range(10)))
print(*filter(lambda i:i%2 != 0, range(10)))


# In[92]:


#Define a list of numbers
#numbers = [1, 2, 3, 4, 5]

# Define a simple function
def square(number):
    return number ** 2

# Use the map function
squares = list(map(square, range(6)))

print(squares)


# In[77]:


numbers= list(range(1,9))
list(map(lambda x: x**2, numbers))


# In[30]:


#write a lambda fun for this polynomial, f(x) = 2x**2 + 3*x + 1
#dat_str [1,2,3,4]
num = [1,2,3,4]
list(map(lambda x : 2*x**2 + 3*x + 1, num))


# In[31]:


#map + lambda + if + else
is_even = lambda x: True if x%2 == 0 else False #right
#is_even = lambda x: True if x%2 == 0 True else False# wrong
print(list(map(is_even ,[1,10,5,3])))


# In[81]:


#######################....... ...filter....................############


# In[86]:


number_list = range(-5, 5)
x = list(filter(lambda x: x < 0, number_list))
print(x)


# In[88]:


number_list = range(-5, 5)
x= list(filter(lambda x: -3 < x <  4, number_list))
print(x)


# In[35]:


numbers = [1,2,3,4,5]
print(list(filter(lambda x : x%2 ==0, numbers)))


# In[29]:


from functools import reduce


# In[33]:


num = [1,2,3,4,5]#1+2+3+4+5
ans = reduce(lambda x,y : x+y, num)
print(ans)


# In[42]:



product = reduce((lambda x, y: x * y), [1, 2, 3, 4])


# In[ ]:


#any ,all, key, sorted ---> few of builtians in python!


# In[37]:


elements = ['Aluminium','Zinc','Potassium','Boron']
print(sorted(elements, key =len))


# In[38]:


len('string')


# In[39]:


pairs= [(11,'newsland'),(6,'Netherland'), (1,'Finland')]
print(sorted(pairs, key = lambda x: x[0])) #we defined our function


# In[41]:


pairs= [(11,'newsland'),(6,'Netherland'), (1,'Finland')]
print(sorted(pairs, key = lambda x: len((x[1]))


# In[ ]:


#any all


# In[42]:


listx = [True, True, True]
print(all(listx))


# listy = []
#   

# In[ ]:





# In[ ]:





# In[ ]:





# In[43]:


#any()
listx = [True, True, True]
print(any(listx))


# In[ ]:


# any and all are the exact opposite! and they are having different properties


# In[ ]:





# In[ ]:





# In[ ]:


#Topics to be covered
1) command line arguments
2)Itertools
3) Import/module


# In[ ]:


# command line arguments

rules/steps to be followed:
    AIM: You can run the script from the files in console.
        1) first arguments always be file_name
        2)Input will be considered as string at first
        3)Use "exit" to stop the code
        
        
        
        
        example:
            1)you have file X.py (.py---->python)
            2)you run this file from cmd
            
          syntax:
            python <file>  <arguments>


# In[ ]:


#Itertools


# In[16]:


import itertools


# In[17]:


Permu= itertools.permutations([1,2,3])
print(Permu)


# In[18]:


combos = itertools.combinations([1,2,3],2)


# In[20]:


list(combos)


# In[ ]:


#how to use module import
#I will see you in final class!
#install: pandas,Matplotlib (install it by conda, pip)
#python environment--->conda


# In[ ]:


##When using a function from a module, 
##Use the -------> syntax: module_name.function_name.


# In[6]:


import math   ## Here is 'math' is module_name


# In[31]:


math.sqrt(25) #. dot operator to access different functions, and 'sqrt' is function_name


# In[12]:


from math import sqrt


# In[13]:


sqrt(25)


# In[28]:


#Importing `*` in Python
#All the functions and constants can be imported using *. 

from math import *
print(pi)
print(factorial(6))
print(int(2.5))
 


# In[ ]:





# In[ ]:


#os module
import os


# In[ ]:


3 make directory
os.mkdir('new folder')


# In[ ]:


with open ('newfolder/dummy.txt', 'w') as file:
    file.write('hey i am dummy text')


# In[ ]:


os.rename('newfolder/dummy.txt','newfolder/dummy_new.txt')
#os.rename (<old_name>, <new_name>)


# In[ ]:





# In[15]:


def registration(name,country='poland'):
    print(f'I am {name}), and I am from {country}')
    
registration('ram')    
    


# In[21]:


def addition(a,b):
    z=a+b
    x=a*b
    print(x)
    return z,x
    
    
addition(2,4)    


# In[ ]:


def linear_function(a,b):
    def inner(x):
        return a*x+b
    return inner
print(linear_function(2.,1.)(5.1))

f = linear_function(2.,1.)
print(f)
print(dir(f))
print(dir(f))   #list of attributes
print(f._closure_)


# In[69]:


##......List Comprehension......##
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Example:
#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Without list comprehension, you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# In[70]:


#With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# In[23]:


##############...........Lambda in python..........########################

#syntax
#lambda arguments : expression

x = lambda a, b : a * b
print(x(5,6))


# In[24]:


x = lambda a,b,c : a+b+c
print(x(5,6,2))


# In[42]:


def myfun(n): #The power of lambda is better shown when you use them as an anonymous function inside another function.
    return lambda a : a * n

mydoubler = myfun(5)  #Say you have a function definition that takes one argument, 
print(mydoubler(11))  #and that argument will be multiplied with an unknown number:


# In[43]:


def print_square_numbers():
    for i in range(11):
        square = i * i
        print(f"The square of {i} is: {square}")
        
print_square_numbers()    


# In[27]:


def myfun(n):
    return lambda a : a * n

mydoubler = myfun(2)
mydoubler = myfun(3)

print(mydoubler(11))
print(mydoubler(11))


# In[7]:


#list of square of number from 0 to 10
print(*[i**2 for i in range(10)])   #list comprehension,  *- unpacking
print(*(i**2 for i in range(10)))   #generator expression
print(*map(lambda i:i**2,range (10)))
print(*filter(lambda i:i%2 == 0, range(10)))
print(sorted(range(-5,5)))
print(sorted(range(-5,5),key= abs))


# In[54]:


# A Python program to demonstrate need 
# of packing and unpacking
 
# A sample function that takes 4 arguments
# and prints them.
def fun(a, b, c, d):
    print(a, b, c, d)
 
# Driver Code
my_list = [1, 2, 3, 4]
 
# This doesn't work
fun(my_list)


# In[58]:


# A Python program to demonstrate need 
# of packing and unpacking
 
# A sample function that takes 4 arguments
# and prints them.
def fun(a, b, c, d):
    print(a, b, c, d)
 
# Driver Code
my_list = [1, 2, 3, 4]
 
# This doesn't work ## We need to keep in mind that 
#the no. of arguments must be the same as the length of the list that we are unpacking for the arguments.


fun(*my_list)


# In[ ]:





# In[ ]:





# In[9]:


def restriction(up,lo):
    def decorator(f):
        def inner(*args):
            y = f(*args)
            if y > up:  
                return up
            if y < lo: 
                return lo
            else:
                
                return y
        return inner
    return decorator

import numpy as np
import matplotlib.pyplot as plt

@restriction(.5,-.5)
def f(x):
    return x**2-2

X = np. linspace(-2,2,201)
Y = [f(x) for x in X]
plt.plot(X,Y)
plt.show()


# In[13]:


def restriction(up,lo):
    def decorator(f):
        @wraps(f)
        def inner(*args):
            y = f(*args)
            if y > up:  
                return up
            if y < lo: 
                return lo
            else:
                return y
        #inner._name_ = f._name_
        #inner._doc_ = f._doc_
        return inner
    return decorator

import numpy as np
import matplotlib.pyplot as plt

@restriction(.5,-.5)
def f(x):
    """Our quadratic function"""
    return x**2-2

X = np. linspace(-2,2,201)
Y = [f(x) for x in X]
plt.plot(X,Y)
plt.show()


# In[37]:


def restriction(up,lo):
    def decorator(f):
        def inner(*args):
            y = f(*args)
            if y > up:  
                return up
            if y < lo: 
                return lo
            else:
                return y
        return inner
    return decorator

import numpy as np
import matplotlib.pyplot as plt

@restriction(-.5,.5)
def f(x):
    return x**2-2

X = np. linspace(-2,2,201)
Y = [f(x) for x in X]
plt.plot(X,Y)
plt.show()


# In[5]:


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2-2

x = np. linspace(-2,2,201)
plt.plot(x,f(x))
plt.show()


# In[ ]:





# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

@restriction(-.5,.5)
def f(x):
    return x**2-2

X = np. linspace(-2,2,201)
Y = [f(x) for x in X]
plt.plot(X,Y)
plt.show()


# In[11]:


def derivative(f):
    h= 1e-5
    def inner(x):
        return (f(x+h))- f(x)/h
    #inner._name_ = f._name_
    #inner._doc_ = f._doc_
    return inner

import numpy as np
import matplotlib.pyplot as plt

@derivative
@restriction(-.5,.5)
def f(x):
    return x**2-2

X = np. linspace(-2,2,201)
Y = [f(x) for x in X]
plt.plot(X,Y)
plt.show()


# In[31]:


class L:
    x=0
    def f(*args):
        print(args)
a1=L()           #instance
a2= L()

print(dir(a1))

a1.x = 1
a2.y =2
x=3

print(dir(a1))
print(a1.x, a2.x,x)

L.f('Alice')
a2.f('Alice')
print(type(L.f),type(a2.f))
    
    


# In[37]:


###############################
print('x'+ 'Alice'.strip()+'X') #.strip()--->This is a string method that removes spaces at the beginning and at the end of the string. 
print(*map(lambda i:i**2,range (10)))
print(*map(lambda s:s.strip(),['a','b','c'])) # The correct lambda function should take a parameter (let's call it x here), 
#instance.strip() <=> class.strip(instance)   # and then strip whitespace from x.
print('a'.__class__)
#print(*map(lambda str.strip(),['a','b','c']))
############################


# In[38]:


class L:
    def __init__(self,x,y):   # This method is called the constructor or initializer
        self.x = x
        self.y = y
        
a = L(4,2) 
print(a.x, a.y)
    


# In[2]:


class parent:   #The parent class has two methods: function1() and function2()
    a = 2
    def function1(self): #calculates the square of the attribute a
        return self.a**2 #The return keyword is used to specify a value that a function should return when a function is called. 
        return 4*self.a  #It performs some calculations or operations and then returns the value or a set of values to the calling code.
    def function2(self):
class child(parent):     #child class inherits from parent and overrides the function2() method.
    def function2(self):
        return 5*self.a
c = child()
print(c.function1())     #Tries to print the result of function1()
print(c.function2())     #Tries to print the result of function2()

print(dir(c))            #This prints all attributes and methods of the instance c

print(c.__class__ == child)  # Checks if the class of c is child. This will return True
print(c.__class__ == parent) #Checks if the class of c is parent. This will return False.
print(isinstance(c,child))   #Checks if c is an instance of child class. This will return True.
print(isinstance(c,parent))  # Checks if c is an instance of parent class. This will return True
#because child is a subclass of parent.
 


# In[10]:


class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'[{self.x};{self.y}]'
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __mul__(self,other):
        if isinstance(other,Vector):
            return (self.x*other.x+self.y*other.y)
        else:
            return Vector(self.x*other,self.y*other)
    __rmul__ = __mul__  
    def __truediv__(self,other):
        if isinstance(other,Vector):
            raise TypeError('cannot divide vector by vector')
        else:
            return Vector(self.x/other,self.y/other)
    __call__ = __mul__    
    def __GETITEM__(self,item):
        if item =='x':
            return self.x
        elif item == 'y':
            return self.y
        else:
            raise ValueError
    def __eq__(sel,other):
        return self.x == other.x and self.y == other.y
    def __getattr__(self,name): #handles not defined attributes
        if name == 'r':
            return (self.x**2+self.y**2)**.5
        
v = Vector(-3,4)

print(v+v, v*v, v*2, 2*v, v/2) #v/v ----> vector by vector can not be divided 
print(dir(1))
print(9//4, 9%4, 9/4)
print(callable(v))
print((v))
#print(v['X'])
#print(v == v)
print(7 & 3)


# In[8]:


import numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x*y, x+y, x-y, y-x, x/y, y/x, x//y, x%y,y%x, x&y)
print(dir(x))

def g():    #iterator defined as a value of generator function
    yield 1
    yield 2
print(g())
gen = g()
for i in gen:
    print(i)
    
gen = g() 
print(next(gen),next(gen))
print(dir(gen))


# In[21]:


import numpy as np    #Numerical python----> numpy
x = np.array([1,2,3])#Numpy is python library of high-level mathematical functions, used for working with arrays, 
y = np.array([4,5,6]) #in domain of linar algebra,fourier transform, and matrices
print(x*y, x@y)
print(dir(x))

class our_range:
    def __init__(self,n):
        self.i = 0
        self.n = n
    __iter__ = lambda self:self
    def __next__(self):
        i = self.i
        self.i += 1
        if i < self.n:
            return i
        else:
            raise StopIteration
            
    def our_range(n):
        i = 0
        while i<n:
            yield i
            i = i+1
            
    for i in our_range(5):
        print(i)
                            


# In[34]:


#  print(*map(lambda x:2**x, range(10)))-----> In this expression replace lambda expression with function object.

def function1(x):
     return 2 ** x

print(*map(function1, range(10)))


# In[94]:


#print(*map(lambda x:x**2, range(10)))-----> In this expression replace lambda expression with function object.

def function2(x):
    return x ** 2

print(*map(function2,range(10)))


# In[ ]:





# In[16]:




def our_range(n):
       i = 0
       while i<n:
           yield i
           i = i+1
           
for i in our_range(10):
       print(i)
                           
   


# In[95]:


def print_numbers():
    for i in range(11):
        print(i)
print_numbers()        


# In[2]:



class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'[{self.x};{self.y}]'
    def __getattr__(self,name):  #handles not defined attributes
        if name == 'r':
            return(self.x**2+self.y**2)**.5
        else:
            raise AttributeError
    def __setattr__(self,name,value):
        
        if name == 'r':
            ratio = value/v.r
            self.x *= ratio
            self.y *= ratio
        else:
            super().__setattr__(name,value) #we rever original behaviour of __settattr__
            
v = vector(3,4)
print(hasattr(v,'r'),'r' in dir(v))
print(v.r)
v.r = 10
print(v.x,v.y,v.r)
print(hasattr(v,'r'),'r' in dir(v))
print(v.__dict__)

            
        


# In[ ]:



class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'[{self.x};{self.y}]'
    def __getattr__(self,name):  #handles not defined attributes
        if name == 'r':
            return(self.x**2+self.y**2)**.5
        else:
            raise AttributeError
    def __setattr__(self,name,value):
        
        if name == 'r':
            ratio = value/v.r
            self.x *= ratio
            self.y *= ratio
        else:
            super().__setattr__(name,value) #we rever original behaviour of __settattr__
            
v = vector(3,4)
print(hasattr(v,'r'),'r' in dir(v))
print(v.r)
v.r = 10
print(v.x,v.y,v.r)
print(hasattr(v,'r'),'r' in dir(v))
print(v.__dict__)


# In[4]:



class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'[{self.x};{self.y}]'
    def __getattr__(self,name):  #handles not defined attributes
        if name == 'r':
            return(self.x**2+self.y**2)**.5
        else:
            raise AttributeError
    def __setattr__(self,name,value):
        
        if name == 'r':
            ratio = value/v.r
            self.x *= ratio
            self.y *= ratio
        else:
            super().__setattr__(name,value) #we rever original behaviour of __settattr__
            
class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'[{self.x};{self.y}]'  
    #r = property(lambda self:(self.x**2+self.y**2)**.5)
    @property  #function property return a descriptor
    def r(self):
        return (self.x**2+self.y**2)**.5
    @r.setter
    def r(self,value):
        ratio = value/v.r
        self.x *= ratio
        self.y *= ratio 
            
            
            
            
            
v = vector(3,4)
print(hasattr(v,'r'),'r' in dir(v))
print(v.r)
v.r = 10
print(v.x,v.y,v.r)
print(hasattr(v,'r'),'r' in dir(v))
print(v.__dict__)


# In[1]:


from math import pi, sin ,cos

class vector:
        def __init__(self,x,y):
            self.x = x
            self.y = y 
        @staticmethod
        def norm(x,y):
            return(x**2+y**2)**.5
        @classmethod
        def polar(cls,r,phi):
            return cls(r*cos(phi),r*sin(phi))
        def __str__(self):
            return f'[{self.x};{self.y}]'  
        #r = property(lambda self:(self.x**2+self.y**2)**.5)
        @property  #function property return a descriptor
        def r(self):
            return self.norm(self.x,self.y)
        @r.setter
        def r(self,value):
            ratio = value/v.r
            self.x *= ratio
            self.y *= ratio 
            
class our_vector(vector):
    pass
                
v = vector.polar(5,pi/2)   #here cls = vector
print(v, type(v))
v = our_vector.polar(5,pi/2)   #here cls = our_vector
print(v,type(v))
print(v.r)
print(dir(v))   #our_vector has __slots__ and __dict__
v.a =1          #hence we again can add attributes to instances

###################################
from time import time
import tracemalloc as tm

class k:
    __slots__ = ('a') #Use of  __slots__ ----->(1)Fast access to attributes, (2)Saves memory space

    def __init__(self,a):
        self.a = a
        
tm.start()
t = time()

l = [k(i) for i in range(10**5)]
print('time:{}, actual memory:{},peak memory:{}'.format(time()-t,*tm.get_traced_memory()))

tm.stop()
######### above and below ###########################
class k:
    def __init__(self,a):
        self.a = a
        
tm.start()
t = time()

l = [k(i) for i in range(10**5)]
print('time:{}, actual memory:{},peak memory:{}'.format(time()-t,*tm.get_traced_memory()))

tm.stop()


#k =k()
#print(k.__dict__)
#k.x = 1


# In[ ]:


class k:
    __slots__ = ('a')
    
k =k()
#print(k.__dict__)
k.x = 1
        


# In[11]:


####################................Global and local variables....................###################


a = 10                  #global variables outside of function (at the top)
def something():
    a = 15              # local variables are defined within the function
    b = 12
    print("Inside_a",a) # Note---> you could access or print global variables(here, a =10) from anywhere in the file
                      # means inside as well as outside of function
something()
print("Outside_a",a)    
#print("Outside_b",b)  # b is defined as local variable within function so you cannot print it outside of function


# In[21]:


x = 10
def something():
    global x    # "x" specified as a global variable by using keyword "global". Here,there is no local variables.
    x = 15
    print("Inside_x",x)
    
something()
print("Outside_x",x)


# In[20]:


x = 10
print(id(x))
def something():
    x = 9
    
    y = globals()['x']  # globals() -----> It is used to make changes to a global variable from a local location
    print(id(y))  
        
    print("Inside_x",x)
    globals()['x'] = 15
    
something()
print("Outside_x",x)


# In[22]:


##########################.................Decorator without Parameters.....................##########################

def make_pretty(func):    # make_pretty() is a decorator
#make_pretty() that takes a function as its argument and has a nested function named inner(), and returns the inner function.
    def inner():
        print("I got decorated")
        func()
    return inner
          #Instead of assigning the function call to a variable, Python provides a much more elegant way to achieve 
@make_pretty     #this functionality using the @ symbol.
def ordinary():
    print("I am ordinary")

ordinary()  


# In[23]:


########################................Decorator with Parameters...............#######################

def smart_divide(func):
    def inner(a, b):           # a and b are parameters
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)  #calling the divide() function with the arguments (2,5)

divide(2,0)   #calling the divide() function with the arguments (2,0)


# In[24]:


####################.................Multiple decorators can be chained in Python..............##################
def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")


# In[4]:


#During the 10th classes we discussed:

#1. the numpy package, numpy.array object and function constructing it (linspace, arange, zeros, ones).

#2. the pointwise definition of arythmetic and logical operators, array versions of mathematical functions provided by numpy.

#3. multidimensional matrices and related functions (meshgrid, reshape, flatten)

#4. linear algebra (eig, eigh, diag)

#5. plotting 2d graphs

#6. plotting 3d graphs (contour, contour, imshow, plot_surface)

#7. animating 2d graphs

import numpy as np
import matplotlib.pyplot as plt

A = np.array([1,2,3])
print(A)
A = np.linspace(0,1,11)
print(A)

A = np.arange(0,2,.33)
print(A)

A = np.zeros(5)
print(A)

A = np.ones(5)
print(A)    


# In[8]:


###########point wise operation

A =np.array([1,2,3])
B =np.array([4,5,6])
print(A+B, A*B, A/B)
print(A**.5, 2**A)
print(np.sin(A),np.log2(A))
print(np.logical_and(A>2,A<4))  #logical_and   and logical_or


###########multidimensional arrays
A = np.array([[1,2],[3,4]])
print(A)
print(A.shape)
A= np.zeros((2,2,2))
print(A,A.shape)


Z = X**2 + Y**2
print(Z)



############# slices

#A = np.arange(16).reshape(4,4)
A = np.arange(16,dtype=np.float).reshape(4,4)
#A =A.flatten()
print(A)

print(A[1:3,:])
print(A[:,:2])
A[1:3,1:3] = np.array([.1,.2,.3,.4]).reshape(2,2)
print(A)

A[A>10] = 0
print(A)
#############linear algebra
print(dir(np.linalg))






# In[12]:


from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = plt.axes(projection = '3d', azim = 60, elev = 60)
ax.plot_surface(X,Y,Z, cmap ='jet')
plt.savefig('figure.png')
plt.show


# In[16]:


###################....................Animation........................#######################

from matplotlib.animation import FuncAnimation
fig = plt.figure()

X = np.linspace(-2,2, 201)
Y = X**2
line, = plt.plot(X,Y)  #UNPACKING 1-ELEMENT TUPLE

def anim(p):
    Y = X**2 - p*X**4
    line.set_ydata(Y)
a = FuncAnimation(fig, anim, np.arange(0,1,.01), repeat = False, interval = 50)  
plt.savefig('figure.png')
plt.show


# In[14]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegWriter
get_ipython().run_line_magic('matplotlib', 'qt')
from mpl_toolkits.mplot3d import Axes3D

X = Y = np.linspace(-4,4,1001)
X,Y = np.meshgrid(X,Y)
Z = np.sin(X+Y)

fig = plt.figure()
ax = plt.axes(projection = '3d', azim = 60, elev = 60)
ax.plot_surface(X,Y,Z,cmap = 'jet')

def anim(phi):
    Z = np.exp(-.1*phi)*np.sin(X+Y+phi)
    ax.clear()
    ax.set_zlim(-1,1)
    ax.plot_surface(X,Y,Z,camp ='jet')
    
a = FuncAnimation(fig,anim,np.arange(0,2*np.pi,.1))
#from IPython.display import HTML
#HTML(a.to_html5_video())

plt.show()


# In[23]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#%matplotlib widget
T = np.linspace(0,2*np.pi, 1001)
X = np.sin(2*T)
Y = np.sin(3*T)

def update(phi):
    X = np.sin(2*T+Phi)
    Y = np.sin(3*T+phi)
    l.set_xdata(X)
    l.set_ydata(Y)
    
fig,ax = plt.subplots()
l, = ax.plot(X,Y)
slider = Slider(ax = fig.add_axes([0.07,0.02,0.86,0.02]), label = r'$\phi$', valmin = -np.pi, valmax = np.pi ,valinit =0)

slider.on_changed(update)
plt.show()


# In[13]:


import numpy as np
from scipy.integrate import solve_ivp, odeint
import matplotlib.pyplot as plt
#from matplot.animation import FuncAnimation
G = 1; M =1; m = 1

def vector_field(x,t):    #(t,x) for solve_ivp
    rx, ry, vx, vy = x    #phase space variable
    c = -G*M/(rx**2 + ry**2)**1.5
    return [vx, vy, c*rx, c*rx]  #phase velocity

time_points = np.linspace(0,20,1001)
t_span = [time_points[0],time_points[-1]]
initial_contion = [1,0,0,1]            #2 or 0.5 value to play around
res = solve_ivp(vector_field, t_span, initial_condition, t_eval = time_points, method ='RK23')   #'DOP853'


y = res.y.T
#y = odeint(vector_field, initial_contion,time_points)

#time series
#for i in range(4):
#plt.plot(time_points,y[:,i])

#trajectory
plt.plot(y[:,0],y[:,1])

trajectory, = plot([initial_condition[0]],[initial_condition[1]])
earth, = plot([initial_condition[0]],[initial_condition[1]],'.')

plt.show()


# In[ ]:


import numpy as np
from scipy.integrate import solve_ivp, odeint
import matplotlib.pyplot as plt
#from matplot.animation import FuncAnimation
G = 1; M =1; m = 1

def vector_field(x,t):    #(t,x) for solve_ivp
    rx, ry, vx, vy = x    #phase space variable
    c = -G*M/(rx**2 + ry**2)**1.5
    return [vx, vy, c*rx, c*rx]  #phase velocity

time_points = np.linspace(0,20,1001)
t_span = [time_points[0],time_points[-1]]
initial_contion = [1,0,0,1]            #2 or 0.5 value to play around
res = solve_ivp(vector_field, t_span, initial_condition, t_eval = time_points, method ='RK23')   #'DOP853'


y = res.y.T
#y = odeint(vector_field, initial_contion,time_points)

#time series
#for i in range(4):
#plt.plot(time_points,y[:,i])

#trajectory
plt.plot(y[:,0],y[:,1])

trajectory, = plot([initial_condition[0]],[initial_condition[1]])
earth, = plot([initial_condition[0]],[initial_condition[1]],'.')

def anim(i):
    earth.set_xdata()

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




