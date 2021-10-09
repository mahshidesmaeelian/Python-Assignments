import random

options = ['rock' , 'paper' , 'scissors']

pc_score = 0
user_score= 0

def show_scores(pc_score , user_score):
    print('pc score:' , pc_score , '\n' ,'your score:' , user_score)  
    

def winner_check(user_score , pc_score):

    if pc_score > user_score:
        show_scores(pc_score , user_score)
        print('unfortunately ~ you lose :(')

    elif user_score > pc_score:
        show_scores(pc_score , user_score)
        print('congrats!you win\^o^/')

    elif user_score == pc_score:
        show_scores(pc_score , user_score)
        print('your scores are equal')
    

for i in range(5):
    
    pc_choise = random.choice(options)

    user_choice = input('Rock , Paoper Or Scissors?')
    
    print('pc choice:' , pc_choise)

    if pc_choise=='rock' and user_choice == 'rock' or pc_choise=='paper' and user_choice == 'paper' or pc_choise=='scissors' and user_choice == 'scissors':
        show_scores(pc_score , user_score)

    elif pc_choise=='scissors' and user_choice == 'rock' or pc_choise=='paper' and user_choice == 'scissors' or pc_choise=='rock' and user_choice == 'paper':
        user_score +=1
        show_scores(pc_score , user_score)

    elif pc_choise=='scissors' and user_choice == 'paper' or pc_choise=='paper' and user_choice == 'rock' or pc_choise=='rock' and user_choice == 'scissors' :
        pc_score +=1
        show_scores(pc_score , user_score)

    else:
        print('oh-uh you have played the game wrong , game over')
        show_scores(pc_score , user_score)     

     

winner_check(user_score,pc_score)
     



    
    
        

    