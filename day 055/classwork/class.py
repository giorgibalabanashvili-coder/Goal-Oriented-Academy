def maskify(cc):
    masked=""
    for i in range(len(cc)):
        if i < len(cc)-4:
            masked += "#"
        else:
            masked += cc[i]
    return masked

def high_and_low(numbers):
    list=numbers.split()
    nums=[]
    for i in list:
        nums.append(int(i))
    return f"{max(nums)} {min(nums)}"


def vaporcode(s):
    str=""
    for i in s:
        if i !=" ":
            str+=i.upper()+"  "
    return str.rstrip()

def password(st):
    if len(st)<8:
        return False
    upper=False
    lower=False
    digit=False
    for i in st:
        if i.isupper():
            upper=True
        elif i.islower():
            lower=True
        elif i.isdigit():
            digit=True
    return upper and lower and digit