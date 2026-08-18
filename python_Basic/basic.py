'''print("Hello World")
print(1+2)
print('hello')
'''


# single line and comment
'''
multiple line comment 
multiple line comment 
'''

#variable decalration 
'''a = 20
b= 10.5
c='krish'
d = True
e = False
print(d | e)   # use of AND Operation    or we can used in 2 ways (|/or)
print(d & e)    #use of OR operation  (AND/&)
print(type(b))
print(type(a))
print(type(c))
print(type(d))
'''

#type casting baaki hai 

#CONCATINATION 
'''name = 'adarsh' 
print(name + ' tripathi')
'''


#complex number 
'''j = 1.0-2.3j
print(j)
print(j.real, j.imag)
'''

#Dynamic Typing 
'''z = 10
print(z)
z = 'adarsh11'
print(z)
'''

#strong typing 
'''print(z + "23")
'''


#string formating 
#place holder is there  look like this {}
'''
first_name = 'adarsh'
last_name = 'tripathi'
print ("The first name is {} and the last name is {}".format(first_name, last_name))
print ("The first name is {1} and the last name is {0}".format(last_name,first_name)) 
'''

#input type 
'''
name = input("Enter the name ")
print(name)
'''

#if statement and elif statement  
'''val = input("Enter the number ")    #by default in input it's in string so we need to change the value to what ever we wanted in that data type
value = float(val)
if(value > 100):
    print("the number is greater than 100")
elif(value<50):
    print("The number is smaller than 50")
else:
    print("The number is odd")
print(value)
print(10%2==0) '''

#for loops and while loops 
'''
lst = [1,2,3,4,5,6]
sum1 = 0
for i in lst:
    sum1 =sum1 + i
    
print(sum1)    
'''

#break and continue 
''':- Break means out 
but continue means on given ball is out 
but u continue play from next ball
'''

'''
age = int(input("Enter the age "))
if(age < 18):
        print("You are not eligible to vote")   
else:
        print("You are eligible to vote")
'''      

#equal  to operator
'''
a = 10
b = 10
lst=[1,2,3]
lst1=[1,2,3]
print(id(a))
print(id(b))
print(id(lst))
print(id(lst1))
if(lst is not lst1):
    print("lst is not  lst1")
if(a is b):
    print("a is b")     #a is b is checking for the address of the variable is same or not but in case of equal to operator it is checking for the value of the variable is same or not
    #but in case of == only check for value not for the location of the variable
'''


        