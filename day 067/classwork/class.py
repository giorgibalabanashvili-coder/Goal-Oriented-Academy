def evaluate(equation):
    tokens = equation.split()
    result = int(tokens[0])
    
    for i in range(2, len(tokens), 2):
        b = int(tokens[i])
        if b == 0:
             return None
        result = (result + b) + (result - b) + (result * b) + (result // b)
        
    return result




def solve(st):
    if len(st) % 2 != 0:
        return -1
    stack = []
    for char in st:
        if char == '(':
            stack.append(char)
        else:
        
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
    close_count = stack.count(')')
    open_count = stack.count('(')
    
    return (close_count + 1) // 2 + (open_count + 1) // 2  


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    limit = int(num ** 0.5)
    for i in range(3, limit + 1, 2):
        if num % i == 0:
            return False
            
    return True