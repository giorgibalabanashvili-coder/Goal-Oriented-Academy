


def get_name_characters(name="სტუმარი"):
    chars_list = []
    
   
    for char in name:
        chars_list.append(char)
        
    return chars_list


result = get_name_characters("გიორგი")
print(result) 


default_result = get_name_characters()
print(default_result)