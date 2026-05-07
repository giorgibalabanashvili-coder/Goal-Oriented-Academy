def multiply(a, b):
    a * b
    return a * b


def even_or_odd(number):
    if number % 2 ==0:
        return "Even"
    else:
        return "Odd"


def solution(string):
    return string[::-1]



def square_sum(numbers):
    return sum(x**2 for x in numbers)




def no_space(x):
    return x.replace(" ","")