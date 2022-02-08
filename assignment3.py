print ("que 1")
def word_count(str): #define a new  user  function for counting the words
    counts=dict() # defined the counts as dictnary for beter understanding and split it 
    words=str.split()

    for word in words: #just a simple for statement
        if word in counts:
            counts[word]+=1 #  count for  repetition 
        else:
            counts[word]=1
    return counts
print(word_count('my name is is  lovepreet. Currently i am doing btech in cse from pec chandigarh'))



print()



print ("que2")
year = int(input("Input a year: "))

if (year % 4 == 0):
    # first inputed the year and chech it wheather it is leap year or non leap year
    leap_year = True
elif (year % 4 == 0):
    #checked leap year by checking remainder when diveded by 4
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False
#leap year condition checked
month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    #inputed the month and filled the imformation of days in each month
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
        #applied the condition of feb in leap year and non leap year
else:
    month_length = 30
     # added for remaining months in a year 


day = int(input("Input a day [1-31]: ")) #inputed a day in a str

if day < month_length:
    day += 1
    #applied the condition for date change that if days are less than mounth lenght than just add the it by 1
else:
    day = 1
    if month == 12:#aplied the condition for month change and year change respectively
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [dd-mm-yyyy] %d-%d-%d." % (day,month,year))


print()

print("que3")
my_list = [3, 9, 10,]  #list is defined
print("The list is") 
print(my_list) 
print('The resultant tuple is :')
my_result = [(val, pow(val, 2)) for val in my_list] #satisfing the condition for ques  and printing the result 
print(my_result)

print()

print("que4")
grades=float(input("Enter your grade point(from 4.0 to 10.0):"))#input the float value of grade point
if grades<=10.0 and grades>=9.1:
    print("your grade is A+ and outstanding performance")#using if ,elif, else statement for different grade point given  
elif grades<9.1 and grades>=8.1:                         
    print ("your grade is A and excelent performance ") #then printed the suitable text and grade accordin to grade given    
elif grades< 8.1 and grades>=7.1:
    print("your grade is B+ and very good performance ")
elif grades<7.1 and grades>=6.1:
    print ("your grade is B and good performace")     
elif grades <6.1 and grades >=5.1:
    print ("your grade s C+ and average performance") 
elif grades<5.1 and grades>=4.1:
    print ("your grade is C and below average performance ")
elif grades==4.0 :
    print("your grade is D and poor performance ")
else :
    print ("error message (wroung input)")

print()

print("que5")
    
for i in range(11, 0, -2):#doing  this for use 11 character and del 2 character every time in the range 
    for j in range(65, 65+i):#just define the range starting for nun 65 i.e is for the alphabets 
        a = chr(j) #difined a to character of j
        print(a, end="") #then printed the a
    print()
print()

print("que6")

dic={}#initializing an empty dictionary 
while True:
   name=str(input("ENTER YOUR NAME OR PRESS N TO STOP ")) #if a user wants to break the loop he can enter N or n
   if(name=='N'or name=='n'):
       break
   SID=int(input("ENTER YOUR SID OR PRESS N TO STOP "))  #if a user wants to break the loop he can enter N or n
   if(SID=='N'or SID=='n'):
       break
   dic[SID]=name            #Keys are SID and Values are name
print("part a: ",dic)#printing the dictionary
sort_by_name={k:v for k,v in sorted(dic.items(),key=lambda v:v[1])} #sorting dictionary by values i.e by name as per the question
print("part b:",sort_by_name)
sort_by_sid={k:v for k,v in sorted(dic.items())}#sorting dictionary by keys i.e by SID as per the question
print("part c:",sort_by_sid)
print("part d:",dic[ 21103014])#Searching a student whose sid 
print("\n")


print()

print("que 7")
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

  
print()


print("que 8")
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
print("set 1=",Set1)
print("set2 =",Set2)
print("set3 =",Set3)
# part a
Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Part_A_Set = Set_Union - Set_Intersection
print("part a )set of all the element present in both set 1 and set 2 but not in both are =", Part_A_Set)

# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("part b)set of all elements that are not in only one of three sets= ", Part_B_Set)

# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("part c)set of elements that are in exactly in two of the sets=",Part_C_Set)
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("part d)set of all integers in the range of 1 to 10 that are not in set 1=", Part_D_Set)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("part e)set of all integers in the range 1 to 10 that are not in set1, set2, set3+", Part_E_Set)






