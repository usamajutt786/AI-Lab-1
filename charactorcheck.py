# check how many time the charactor is in the string

name=input("Enter the string:")
char=input("Enter the charactor you wanna search ")
count=0
for i in name:
    if i==char:
        count+=1
print("You char exist", count,"Time")