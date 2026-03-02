def repeat_str(repeat, string):
    return string * repeat

def are_you_playing_banjo(name):
    if name[0].lower() == ('r'):
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"
    
def find_average(numbers):
    if len(numbers)==0:
        return 0
    
    sum = 0
    
    for i in numbers:
        sum+=i
    return sum / len(numbers)


def string_to_array(s):
    return s.split(" ")

def string_to_number(s):
    return int(s)


def summation(num):
    return num * (num +1 )//2


def friend(x):
    friends=[]
    for name in x:
        if len(name)==4:
            friends.append(name)
    return friends