def order(sentence):
    if not sentence:
        return ""
    def extract_number(word):
        return next(char for char in word if char.isdigit())
    words = sentence.split()
    sorted_words = sorted(words, key=extract_number)
    
    return " ".join(sorted_words)