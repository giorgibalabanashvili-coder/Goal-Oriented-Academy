# / ჩვეულებრივად ყოფს რიცხვს.
print(10 / 3)
print(24 / 3)
print(14 / 7)
# // აჩვენებს მთელ ნაწილს.
print(10 // 3)
print(24 // 4)
print(21 // 3)
# % აბრუნებს გაყოფის ნაშთს.
print(28 % 5)
print(14 // 4)
print(19 % 3)
# elif ნიშნავს სხვა შემთხვევაში თუ.
# elif გამოოიყენება მასინ როცა რამდენიმე პირობა გვაქვს.
year =int(input("enter year :"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("leap year")
else:
    print("not leap year")