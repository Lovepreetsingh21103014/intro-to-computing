print("que1")
def TowerOfHanoi(n , source, destination, auxiliary):
	if n==1:
		print ("Move disk 1 from source",source,"to destination",destination)
		return
	TowerOfHanoi(n-1, source, auxiliary, destination)
	print ("Move disk",n,"from source",source,"to destination",destination)
	TowerOfHanoi(n-1, auxiliary, destination, source)
		
# Driver code
n = int(input("number of disks for tower of honaoi:"))
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods

print()

print("que2")
# Print Pascal's Triangle in Python
from math import factorial

# input n
row=int (input("enter the number of rows for pascal's triagle:"))
for i in range(row):
	for j in range(row-i+1):

		# for left spacing
		print(end=" ")

	for j in range(i+1):

		# nCr = n!/(n-r)!*r!)
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

	
	print()
print("que3")
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("""quotient of %s and %s is %s """%(num1,num2,num1//num2))
print("""remaider between %s and %s is %s """%(num1,num2,num1&num2))
Quotient=num1//num2
Remainder=num1&num2

print("part a")
print(" Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

print("part b")
if (Quotient == 0):
    print(" The quotient is zero")
if (Remainder == 0):
    print(" The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print(" All the values are non zero")

print("part c")
partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f" Filtered out numbers that are greater than 4 are : {result}")
print("part d")
setresult = set(result)
print(" Set:",setresult)

print("part e")
immutableSet = frozenset(setresult) #frozen Set is used to make the set immutable
print(" Immutable set:",immutableSet)

print("part f")
print(" Hash value of the max value from the above set:", hash(max(immutableSet)))
print()



print("que 4 ")
class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
        print(self.name,self.roll_no)
        
    
    def __del__(self):
        print("object deleted")
        

#creating object
student1 = Student("lovepreet", 21103014)
student2=Student("choota bheem ","18 45 10 07")
#deleting object
del student1
del student2

print()
print("que 5")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print(self.name,self.salary) 
 
#creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

print("part a")# updating salary
employee1.salary = 70000
print(""" The updated salary of %s is %s""" %(employee1.name,employee1.salary))
print("part b")#deleting a record
del employee3
print("Record of viren deleted", end='')
print()

print("que 6")
#inputting a word from the first friend
word =input("Enter the word: ")
word=word.lower()

#inputting a meaningful word with the exact same letters
testword = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
testword=testword.lower()
#defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
#shopkeeper's input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(testword):
        print("The letters aren't exact, friendship is not true")
        return
    ans = input("Does the word makes sense?(y/Y or n/N )")

    if ans == 'y' or ans=='Y':
        print(" Congrats! The friend has passed the friendship test")
    elif ans == 'n' or ans=='N':
        print("The word doesn't have a meaning, friendship is not true")
    else:
        print("Invalid input,try again with y/Y or n/N ")
        userinput()
userinput()
