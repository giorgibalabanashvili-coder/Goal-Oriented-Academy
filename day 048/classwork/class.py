def between(a,b):
    number=[]
    for i in range(a,b+1):
        number.append(i)
    return number


def powers_of_two(n):
    number=[]
    for i in range(n+1):
        number.append(2**i)
    return number
        


def odd_count(n):
    return n // 2


def sum_of_minimums(numbers):
    sum=0
    for i in numbers:
        sum += min(i)
    return sum

def in_asc_order(arr):
    return sorted(arr)==arr
