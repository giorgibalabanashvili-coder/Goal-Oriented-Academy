num=int(input("enter the number :"))
if num >= 50:
    print(num*5)
else:
    print(num*50)
    
password=input("please enter password")
if password=="goa123":
    print("password is correct!")
else:
    print("incorrect password!")

number=int(input("enter the number"))
for i in range(1,number+1):
    print(i)