#(que1
#a,b,c are the to enter the respective number
a=input("enter the first number")
b=input("enter the second number")
c=input("enter the third number")
d=(int(a)+int(b)+int(c))/3
#average formula is sum of terms /number of terms
print("the average of three numbers is : ")
print(float(d)) 
#result is printed

#"que2")
standard_deduction=10000
dependent_deducton=3000
gross=input("enter your gross salary=")
no_of_dependent=input("number of dependented on your family=")
taxable_income=int(gross)-int(standard_deduction)-int(dependent_deducton)*int(no_of_dependent)
tax=(float(taxable_income*0.2))
print("your income tax is")
print(float(tax))
#in ithis i just input the values of standard deduction and dependnet dedeution and put it in the the formula given


#("que3")
name=input("enter your name :")
gender=str( input("gender(use M(male),F(female),U(unknown)):"))
if(gender=="M"):
    print("male")
if(gender=="F"):
        print("female")
if(gender=="u"):
        print("unknown")            
SID=input("enter your sid:")
course_name=input("enter your course name:")
cgpa=float(input("enter your cgpa:"))
Student=(SID,name,gender,course_name,cgpa)
print(Student)
#in this just taking the input of name gender sid course cgpa and given the printing camand

#("que4")
marks=[]
for i in range(5):
        marks.append(input("enter the marks of student:"))
marks.sort()
print(marks)        
#in this range has been taken for 5 student and then sorted and given the print cammand

#("que5")
colour=['Red','Green','White','Black','Pink','Yellow']
colour.remove(colour[3])
print("part a of question=",colour)
colour=['Red','Green','White','Black','Pink','Yellow']
colour[3]='Purple';colour[4]='Purple'
print("partb of question=",colour)
#in 1st part given the input of colours and than remove one color 
#in the 2nd part sameis done but this we replace two colour with purple colour



