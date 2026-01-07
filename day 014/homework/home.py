# loop(ციკლი)ნიშნავს კოდის რამდენჯერმე გამეორებას.
# range არის ფუნქცია რომელიც ქმნის რიცხვთა დიაპაზონს.
for i in range(100 , 201):
    print(i)

for i in range(20,30,3):
    print(i)
    
for i in range(0,20,2):
    print(i)

sum=0
for i in range(5):
   number=int(input("enter the number :"))
   sum+=number
averaje = sum // 5
print("საშუალო არითმეტიკული არის :",averaje)