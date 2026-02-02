names = ["Nika", "Giorgi", "Ana", "Luka", "Mariam"]


user_name = input("შეიყვანეთ სახელი: ")
names.append(user_name)

print(names)


names.insert(3, "Tarieli")
print(names)


names.pop(4)
print(names)


names.remove("Ana")
print(names)


search_name = input("შეიყვანეთ საძებნი სახელი: ")

if search_name in names:
    print("ელემენტი დგას [names.index(search_name)] index-ზე")
else:
    print("not index in list")