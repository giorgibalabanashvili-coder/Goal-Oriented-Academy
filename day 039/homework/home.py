def greet():
    return 'hello world!'

def string_to_number(s):
    return int(s)

def summation(num):
    return sum(range(1,num + 1))
    
def find_smallest_int(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest