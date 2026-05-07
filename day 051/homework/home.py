def number(bus_stops):
    people=0
    for i in bus_stops:
        people+=i[0]-i[1]
    return people

def sum_digits(number):
    result=0
    if number < 0:
        number = number * -1
    number=str(number)
    for i in number:
        result += int(i)
    return result