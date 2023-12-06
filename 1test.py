#Exersize 2 


def count_word_frequencies(text):
    
    words = [word.strip('.,?!()[]{}"\'') for word in text.lower().split()]

    
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


input_text = "A a a  an  an an array array abstract a"
result = count_word_frequencies(input_text)
print(result)



