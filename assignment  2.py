print ("que 1")
print ("part a")
string="Python is a case sensitive language"
print("lenght of string is",(len(string)))
print ("part b")
print("Reverse of string is","'"+string[-1: :-1]+"'")

print  ("part c")
print (string[10:26])
print ("part d")
new_string=string.replace("a case sensitive","object oriented")
print (new_string)
print ("part e")
print("index of substring 'a' is",string.index('a') )
print("part f")
print(string.replace(" ",""))



print("que 2")

name =input("enter your name:")
sid= int(input ("enter your SID:"))
department=input("enter your department name:")
cgpa=float(input("enter your CGPA:"))
line1=('Hey',name,'Here!  '
       ' My sid is  ',sid ,
       '  I am from ', department,' and my CGPA is ',cgpa  )
print(line1,)

print("que3")
a=56
b=10
print("a$b =",a&b)
print("a|b+=",a|b)
print("a**b=",a**b)
print("left sift a by 2bits=",a<<2 ,"left sift b by 2 bits =",b>>2)
print("right sift a by 2 bits=",a>>2)
print("right sift b by 4 bits=",b>>4)


print("que 4" )
a = float(input("enter the first number:"))

b= float(input("enter the second number:"))

c = float(input ("enter the third number:"))
if a>b and a>c:
    print ("largest number is ",a)

    
if b>c and b>a:
    print ("largest numbr is ",b)

    
if c>a and c>a :
    print=("largest number is ",c)

print ("ques 5")
anything=input("Enter the string: ")
if 'name' in anything:
    print("yes,word name is present")

else:
    print("no,word name is not present")

print ("ques 6")
side1= float (input("length of the one side= "))
side2=float(input("length of second side ="))
side3 =float(input("length of the third side ="))
if side1+side2 >side3 and side1+side3>side2 and side2 +side3>side1 :
    print("yes, triangle can be formes")
else :     
    print("no, triangle cant be formed") 

