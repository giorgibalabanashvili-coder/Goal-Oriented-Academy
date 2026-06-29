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