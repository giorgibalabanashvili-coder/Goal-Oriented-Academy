def high(x):
    words=x.split()
    score=0
    word=""
    for i in words:
        current_score=0
        for char in i:
            current_score += ord(char) - 96
            
        if current_score > score:
            score=current_score
            word=i
    return word


def average_string(s):
    if not s: return "n/a"
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    sum = 0
    
    for i in s.split():
        if i not in numbers: return "n/a"
    
        sum += numbers.index(i)
        
    return numbers[int(sum / len(s.split()))]