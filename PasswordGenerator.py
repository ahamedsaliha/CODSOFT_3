#Importing an random package
import random

#setting string to their appropriate values 
uppercase_letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
lowercase_letters=uppercase_letters.lower() 
digits="0123456789" 
symbols="@#$%^&*!~`/[]:,.;" 

#Initializing the variable to true
upper=True 
lower=True 
nums=True
syms=True

#setting a string to empty
all="" 


# if these contidions are true then the all string will be add the uppercase letters and so on..

if upper: 
    all+=uppercase_letters 

if lower:
    all+=lowercase_letters

if nums:
    all+=digits 

if syms:
    all+=symbols 

#Getting inputs from the user
length=int(input("Enter your password length: ")) 
no_of_password=int(input("Enter your no of passwords you want: "))  

#To generate passwords
for i in range(no_of_password):
    password="".join(random.sample(all,length))
    print(password)