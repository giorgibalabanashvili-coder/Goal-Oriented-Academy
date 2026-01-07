number=int(input("enter the number: "))
result=1
for i in range(1, number * 1):
     result *= i
     print(result)

 # % გაყოფა ნიშნავს ნაშთით გაყოფას.
 # ეს ოპერაცია გვიბრუნებს მხოლოდ ნაშთს.
 # ის გვჭირდება ლუწი და კენტი რიცხვების გამოტვლისთვის.
number = int(input("enter the number :"))
if number % 2 == 0:
     print("number is even")
else:
     print("number is odd")

num=int(input("enter the number :"))
print("separators:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)