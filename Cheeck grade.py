# # Student grading Task 
marks=int(input("Enter your marks :"))
if marks>=80:
    print("Your Grade is A")
if marks>=70 and marks<80:
    print("Your Grade is B+")
if marks>=60 and marks<70:
    print("Your Grade is B")
if marks>=50 and marks<60:
    print("Your Grade is B-")
if marks>=40 and marks<50:
    print("Your Grade is C")
if(marks<=40 and marks>=0):
    print("You fail")
else:
    print("Something went wrong")  

