number=10
while number>=-10:
    print(number)
    number+=-1

number=1
while number<=100:
    print(number)
    number+=2

correct_password="goa1234"
attempts=3
password=""
while password != correct_password and attempts<3:
    password=input("enter password: ")
    print(password == correct_password)
    attempts+=1
    print("password is incorrect! try again")
    print("remaining attempts: " )