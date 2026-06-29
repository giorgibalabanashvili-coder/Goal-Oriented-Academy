def get_sum(a,b):
    if a == b:
        return a
    start = min(a, b)
    end = max(a, b)
    count = end - start + 1
    return count * (start + end) // 2 


def find_next_square(sq):
    root = sq ** 0.5
    if root % 1 == 0:
        return int((root + 1) ** 2)
    return -1



def divisors(integer):
    res = [i for i in range(2, integer) if integer % i == 0]
    if not res:
        return f"{integer} is prime"
    
    return res



def duplicate_count(text):
    text_lower = text.lower()
    unique_chars = set(text_lower)
    count = 0
    for char in unique_chars:
        if text_lower.count(char) > 1:
            count += 1
            
    return count