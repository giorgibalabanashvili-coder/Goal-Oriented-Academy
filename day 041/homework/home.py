def reverse_words(text):
    words_list = text.split(' ')
    reversed_list = []
    
    for word in words_list:
        reversed_word = word[::-1]
        reversed_list.append(reversed_word)
    result = ' '.join(reversed_list)
    return result


def odd_or_even(arr):
    shayu=sum(arr)
    if shayu % 2 ==0:
        return "even"
    else:
        return "odd"