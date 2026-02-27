def my_len(interable):
    count=0
    for item in interable:
        count+=1
    return count
print(my_len("hello"))


def my_find(text, target):
    target_len = my_len(target)
    text_len = my_len(text)
    
    for i in range(text_len - target_len + 1):
        if text[i : i + target_len] == target:
            return i
            
    return -1


print(my_find("პითონი მაგარია", "მაგარია"))
print(my_find("პითონი კარგია", "ეიჩტიემელი")) 

def my_range(start, stop=None,step=1):
    if my_range is None:
        stop=start
        start=0 