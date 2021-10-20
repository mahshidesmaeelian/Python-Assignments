import random


first_rivil_score = 0
second_rivil_score = 0
user_score = 0 


rivals_choices = ['✋🏻' , '🤚🏻']


def options():
    print('1.✋🏻' , '\n' , '2.🤚🏻')



def check_winner(user_score , second_rivil_score , first_rivil_score):
    
    if user_score > first_rivil_score and user_score > second_rivil_score:
        print('you win!')

    elif first_rivil_score > user_score and first_rivil_score > second_rivil_score:
        print('Pc1 wins!')

    elif second_rivil_score > first_rivil_score and second_rivil_score > user_score:
        print('Pc2 wins!')

    elif second_rivil_score == first_rivil_score and second_rivil_score != user_score:
        print('Pc1 and Pc2 win!')

    elif first_rivil_score == user_score and user_score != second_rivil_score:
        print('You and Pc1 win!')

    elif second_rivil_score == user_score and user_score != first_rivil_score:
        print('You and Pc2 win!')

def show_choices():
    print(f'Your choice:{user} \n Pc1 choice:{first_rivil} \n Pc2 choice:{second_rivil}')


def show_scores():
    print(f'Current scores are: \n Your score:{user_score} \n Pc1 score:{first_rivil_score} \n Pc2 score:{second_rivil_score}')



for play in range(5):

    first_rivil = random.choice(rivals_choices)
    second_rivil = random.choice(rivals_choices)

    options()

    user = int(input('choose one of the options:'))

    if user == 1 :
        user = '✋🏻'

    else:
        user = '🤚🏻'

    if first_rivil == second_rivil and first_rivil!= user and second_rivil!= user:
        user_score += 1

    elif first_rivil == user and first_rivil!= second_rivil and first_rivil!= second_rivil:
        second_rivil_score += 1

    elif  second_rivil == user and second_rivil!= first_rivil and user!= first_rivil:
        first_rivil_score += 1

    show_choices()
    print('\n')
    show_scores()
    print('\n')

check_winner(user_score , second_rivil_score , first_rivil_score)




    
            


    