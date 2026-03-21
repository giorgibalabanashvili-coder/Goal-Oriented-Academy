def opposite(number):
    return -number


def reverse_seq(n):
    result=[]
    for i in range(n,0,-1):
        result.append(i)
    return result

def filter_list(l):
    new_list=[]
    for i in l:
        if type(i) == int:
            new_list.append(i)
    return new_list

def friend(x):
    friends=[]
    for name in x:
        if len(name)==4:
            friends.append(name)
    return friends