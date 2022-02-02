#QUESTION1
print("QUESTION 1")
a=str(input("ENTER ANY STRING: "))
list=a.split() #To split all the elements of string in a list
dict={} #initializing an empty dictionary
if list.__len__()==1:   #if statement will be implemented when a single word is entered
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   #else statement eill be implemented when more than one word is entered in a string
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")


#QUESTION2
print("QUESTION 2")
while(True):                 #while loop is used so that if any wrong value is entered  then values will be entered again
    day=int(input("ENTER THE DAY: "))
    if(1<=day<=31):
        break
    else:
        print("Please Enter a valid day")
while(True):                  #while loop is used so that if any wrong value is entered  then values will be entered again
    month=int(input("ENTER THE MONTH OF THE YEAR: "))
    if(1<=month<=12):
        break
    else:
        print("Please Enter a valid month")
while(True):                #while loop is used so that if any wrong value is entered  then values will be entered again
    year=int(input("ENTER THE YEAR: "))
    if(1800<=year<=2025):
        break
    else:
        print("Please Enter year from 1800 to 2025 only")
if(month==(1 or 3 or 5 or 7 or 8 or 10) ):    
    if(day==31):
        day=1
        month=month+1
        print(day,"/",month,"/",year)
    elif(day<31):
        day+=1
        print(day,"/",month,"/",year)
    else:
        print("PLEASE ENTER CORRECT DATE")

elif(month== (4 or 6 or 9 or 11) ):
    if(day==30):
        day=1
        month=month+1  
        print(day,"/",month,"/",year)   
    elif(day<30):
        day+=1
        print(day,"/",month,"/",year)
    else:
        print("PLEASE ENTER CORRECT DATE")       
elif(month== 2):
    if((year % 400 == 0) or  
    (year % 100 != 0) and  
    (year % 4 == 0)):   
        if(day==29):
            day=1
            month=month+1
            print(day,"/",month,"/",year)
        elif(day<29):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("PLEASE ENTER CORRECT DATE")
    else:
        if(day==28):
            day=1
            month+=1
            print(day,"/",month,"/",year)
        elif(day<28):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("PLEASE ENTER CORRECT DATE")
elif(month==12):
    if(day==31):
        day=1
        month=1
        year+=1  
        print(day,"/",month,"/",year)
    elif(day<31):
        day+=1;
        print(day,"/",month,"/",year)
    else:
        print("PLEASE ENTER CORRECT DATE")
    
else:
    print("PLEASE ENTER A CORRECT DATE")
print("\n")


#QUESTION3
print("QUESTION 3")
list = [3, 9, 10]
print("LIST IS ")
print(list)
print("The resultant list of tuple is :")
result = [(val, pow(val, 2)) for val in list]
print(result)
print("\n")


#QUESTION4
print("QUESTION 4")
grade=int(input("ENTER YOUR GRADE BETWEEN 4 TO 10: "))
if(grade>10 or grade<4):
    print("PLEASE ENTER CORRECT GRADE")
elif(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")
print("\n")


#QUESTION5
print("QUESTION 5")
x = 6
for i in range(x):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(x-i)-1):
        print(chr(65 + j), end='')  #ASCII VALUE OF A=65,B=66,C=67,D=68,E=69,F=70,G=71,H=72,I=73,J=74,K=75
    print()
print("\n")

#QUESTION6
print("QUESTION 6")
dic={}#initializing an empty dictionary 
while True:
   name=str(input("ENTER YOUR NAME OR PRESS N TO STOP ")) #If a user wants to break the loop he can enter N or n
   if(name=='N'or name=='n'):
       break
   SID=int(input("ENTER YOUR SID OR PRESS N TO STOP "))  #If a user wants to break the loop he can enter N or n
   if(SID=='N'or SID=='n'):
       break
   dic[SID]=name            #Keys are SID and Values are name
print("<A>: ",dic)#printing the dictionary
sort_by_name={k:v for k,v in sorted(dic.items(),key=lambda v:v[1])} #sorting dictionary by values i.e by name as per the question
print("<B>",sort_by_name)
sort_by_sid={k:v for k,v in sorted(dic.items())}#sorting dictionary by keys i.e by SID as per the question
print("<B>",sort_by_name)
print("<C>",sort_by_sid)
print("<D>",dic[21103107])#Searching a student whose SID is 21103107
print("\n")

#QUESTION7
print("QUESTION 7")
#  Function to display the Fibonacci sequence
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
no_of_terms=int(input("ENTER THE NUMBER OF TERMS IN THE SERIES: "))
if no_of_terms <= 0:     # Check if the number of terms is valid
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(no_of_terms):
       print(recur_fibo(i))
       sum=sum+recur_fibo(i)
avg=float(sum/no_of_terms)
print("AVERAGE OF RESULTANT FIBONACCI SERIES IS",avg)


#QUESTION8
print("QUESTION 8")
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# part a
Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Part_A_Set = Set_Union - Set_Intersection
print("<a>", Part_A_Set)

# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("<b>", Part_B_Set)

# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("<c>",Part_C_Set)
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("<d>", Part_D_Set)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("<e>", Part_E_Set)
