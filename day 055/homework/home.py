def reverse_number(n):
    reversed_num = int(str(abs(n))[::-1])ს
    return reversed_num if n >= 0 else -reversed_num

def smaller(arr):
    result = []
    for i in range(len(arr)):
        count = 0
        for l in range(i + 1, len(arr)):
            if arr[l] < arr[i]:
                count += 1
        result.append(count)
    return result