dictiinary_source = open('translate.txt' , 'r')
data = dictiinary_source.read()
templist = data.split('\n')
words_list=[]
for i in range (len(templist)):
    if i%2==0:
        words_list.append({'english':templist[i]})    
    else:
        words_list.append({'persian':templist[i]})  
dictiinary_source.close()
def show_menu():
    print('1-add new word:')
    print('2-translate English to Persian:')
    print('3-translate Persian to English:')
    print('4-show dictionary')
    print('5-exit')


def show_words():
    for i in range(len(words_list)):
        print(words_list[i]['english'] , '\t' , words_list[i]['persian'])


def add_new_word():
    new_word= (input('enter your word:')) 
    new_words_traslation= (input('enter translation:')) 
    words_list.append({'persian': new_words_traslation ,'english': new_word})
    
def english2persian():
    englishtopersian_sentence = input('enter the sentence in english:')
    englishtopersian_word=englishtopersian_sentence.split(' ')
    for i in range(len(words_list)):
        for j  in range(len(words_list)):
            if words_list[j]['english'] == englishtopersian_word[i]:
                print('the translation is: ',  words_list[i]['persian'] , end=' ')
                break
            
def persian2english():
    persiantoenglish_sentence = input('enter the sentence in persian:')
    persiantoenglish_word=persiantoenglish_sentence.split(' ')
    for i in range(len(words_list)):
        for j  in range(len(words_list)):
            if words_list[j]['persian'] == persiantoenglish_word[i]:
                print('the translation is: ',  words_list[i]['english'] , end=' ')
                break

while True:
    show_menu()
    choise =  int(input('hey , what can I do for you?'))
    if choise == 1 :
        add_new_word()    
        show_words()
    if choise == 2 :
        english2persian()
        show_words()        
    if choise == 3 :
        persian2english()
        show_words
    if choise == 4 :
        show_words()
    if choise ==5 :
        exit()