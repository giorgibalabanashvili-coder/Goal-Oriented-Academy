def spot_diff(s1, s2):
    difs=[]
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            difs.append(i)
    return difs


def find_missing_numbers(arr):
    if not arr:
        return []  
    first = arr[0]
    last = arr[-1]
    result = []
    for i in range(first, last + 1):
        if i not in arr:
            result.append(i)
            
    return result



def to_camel_case(text):
    if not text:
        return ""
    text = text.replace("-", "_")
    words = text.split("_")
    result = words[0]
    
    for word in words[1:]: 
        result += word.capitalize()      
    return result
