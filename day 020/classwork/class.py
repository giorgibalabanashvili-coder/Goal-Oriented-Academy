sumi=0
count=0
while count < 5:
    number = int(input("enter the number :"))
    sumi+=number
    count += 1
print("the sum is :",sumi)
if sumi % 2 == 0:
    print("the sum is even")
else:
    print("the sum is odd")

num=int(input("enter the number :"))
while not(num % 5 ==0 and num % 7==0):
    num=int(input("thid number is not divisible by both 5 and 7,try again :"))
print("correct number")
    
balance=int(input("enter your balance :"))
if balance >= 1500:
    print("ლეპტოპი")
elif balance>=1000:
    print("ტელეფონი") 
elif balance >= 100:
    print("ფეხსაცმელი")
elif balance >=50:
    print("პერანგი")
elif balance >=5:
    print("რვეული")
else:
    print("ვერაფერს ვერ იყიდი შენი სიიდან")

num=int(input("enter the number :"))
if num > 0:
    print("the number is positive")
elif num < 0:
    print("number is negative")
else:
    print("numberis zero")