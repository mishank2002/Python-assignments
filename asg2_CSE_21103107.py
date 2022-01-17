# QUESTION 1
string1="Python is a case sensitive language" #string1
print("<A>THE LENGTH OF STRING IS",len(string1)) #function to find LENGTH OF STRING
print("<B>THE REVERSED STRING IS ",string1[-1::-1])
string2=string1[10:26] #STORED a case sensitive IN A NEW STRING
string2="Object Oriented" #REPLACED "a csae sensitive" WITH "object oriented"
print("<E>THE INDEX OF SUBSTRING a is ",string1.find('a'))
print("<F>THE ORIGINAL STRING AFTER REMOVING WHITESPACES IS",string1.replace(" ",""))
print("\n")


#QUESTION 2
NAME=input("ENTER YOUR NAME")
SID=input("ENTER YOUR SID")
DEPARTMENT=input("ENTER YOUR DEPARTMENT")
CGPA=input("ENTER YOUR CGPA")
print("Hey,",NAME,"Here!")
print("My SID is ",SID)
print("I am from ",DEPARTMENT,"and my CGPA is ",CGPA)
print("\n")


#QUESTION 3
a=56
b=10
print("a. ",a&b)
print("b. ",a|b)
print("c. ",a^b)
print("Left shift both a and b with 2 bits respectively are :",a<<2 ,b<<2)
print("Right shift a with 2 bits and b with 4 bits respectively are : ",a>>2,b>>4)
print("\n")


#QUESTION 4
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("THE LARGEST NUMBER IS ",largest)
print("\n")


#QUESTION 5
s=input("ENTER A STRING")
if (s.find('name') != -1):
    print ("Yes")
else:
    print ("No")
print("\n")

#QUESTION 6
a=int(input("ENTER FIRST SIDE OF TRIANGLE"))
b=int(input("ENTER SECOND SIDE OF TRIANGLE"))
c=int(input("ENTER THIRD SIDE OF TRIANGLE"))
if(a>(b+c)):
    print("No")
elif(b>(a+c)):
    print("No")
elif(c>(a+b)):
    print("No")
else:
    print("Yes")
print("\n")

    

