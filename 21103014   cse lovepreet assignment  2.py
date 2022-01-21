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

name=input("Please enter your name: ")
sid=int(input("Enter SID: "))
dep=input("Enter department name: ")
cgpa=float(input("Enter CGPA: "))
print('''
''')
print('''Hey, %s Here!
     My SID is %s
     I am from %s department and my CGPA is %s'''%(name,sid,dep,cgpa))

       

print("que3")
a=56
b=10
print("a&b =",a&b)
print("a|b+=",a|b)
print("a**b=",a**b)
print("left sift a by 2bits=",a<<2 ,"left sift b by 2 bits =",b>>2)
print("right sift a by 2 bits=",a>>2)
print("right sift b by 4 bits=",b>>4)


print("que 4" )
l=[]
for i in range(3):
    num=float(input("Enter number %s: "%(i+1)))
    l.append(num)

l.sort(reverse=True)
print("The greatest value is:",l[0])


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
if float(side1+side2) >float(side3) and float(side1+side3)>float(side2) and float(side2 +side3)>float(side1 ):
    print("yes, triangle can be formes")
else :     
    print("no, triangle cant be formed") 

