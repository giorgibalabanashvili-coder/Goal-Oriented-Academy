# append-ამატებს ელემეტს ყოველთვის სიის ბოლოში
# insert-ინდექსის მიხედვით შეგვიძლია ჩავამატოთ ელემენთი ნებისმიერ ადგილას
# pop-ინდექსის მხედვით შლის სიიდან ელემენტს
list=["giorgi",54,8.4,"true"]
print(len(list))

# numbers=[]
# for i in  range(5):
#     num=int(input("შეიყვანე რიცხვი :"))
#     numbers.append(num)
#     print("შენი სია",numbers)

colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop(-1)
print(colors)

animals = ["dog", "cat", "elephant", "lion"]
animals.insert(1,"monkey")
print(animals)

students=[]
for i in range(3):
    name=(input("შეიყვანე სახელი :"))
    students.append(name)
    students.insert(0,"teacher")
    students.pop()
    print("სიის სიგრძე",len(students))