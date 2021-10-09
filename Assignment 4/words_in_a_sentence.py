def words_number_in_a_sentence(sentence):
    words = 0
    for i in range(len(sentence)):
        if (sentence[i]) == ' ':
            words = words+1

    print(f"there are {words+1} words in the sentence")

s = input("enter a sentence: ")
words_number_in_a_sentence(s)