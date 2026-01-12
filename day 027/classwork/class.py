my_car_list=["audi","mercedes","bmw","ferrari","toyota","honda","ford","chevrolet","nissan","opel"]
print(my_car_list[4])

new_car_list=my_car_list[1:6]
print(new_car_list)
print(new_car_list[-1])

print(my_car_list[0:11:2])

print(my_car_list[3:8:3])

new_car_list2=my_car_list[9:4:-1]
print(new_car_list2)

new_car_list3=my_car_list.copy()
print(new_car_list3)

numbers=[56,43,53,65,23]
for i in range(len(numbers)):
    print(numbers[i])