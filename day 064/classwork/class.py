def solution(text, ending):
    return text.endswith(ending)



def check_exam(arr1,arr2):
    score = 0
    for correct,student in zip(arr1,arr2):
        if student == correct:
            score +=4
        elif student == "":
            score +=0
        else:
            score -= 1
            
    if score < 0:
        return 0
    else:
        return score
  