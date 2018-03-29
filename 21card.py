from random import randint
game = True

#first player
fp_answer = True
fp_input = True
fp_card = 0

#second player
sp_answer = True
sp_input = True
sp_card = 0

print('Welcome to black jack')

#-----------------------first_player-------------------------------

#begin

begin = input('First player, type begin to start:')
while fp_input:
    if begin != 'begin':
        begin = input('try again! type begin to start:')
        if begin == 'begin':
            fp_input = False
    if begin == 'begin':
        fp_input = False

#start game

print('First player playing:')
fp_first_card = randint(1,11)
print('Your card is',fp_first_card)

while game:

    while fp_answer:
        fp_second_card = randint(1,11)
        yes_or_no = input('Do you want to go again? (y/n)')
        if yes_or_no == 'y':
            print('your next card is',fp_second_card)
            fp_card = (fp_card) + fp_second_card

        if yes_or_no == 'n':
            print('Finish')
            fp_total_card = fp_card + fp_first_card
            print('The total value of your card is',fp_total_card)
            fp_answer = False

#first_player finish

    if fp_total_card == 21:
        print('First player wins')
    if fp_total_card > 21:
        print('You lose! Second player wins')
    game = False


#-----------------------Second_player-------------------------

#begin

    if fp_total_card < 21:
        if fp_total_card != 21:
            begin = input('Second player, type begin to start:')
            while sp_input:
                if begin != 'begin':
                    begin = input('try again! Type begin to start:')
                    if begin == 'begin':
                        sp_input = False
                if begin == 'begin':
                    sp_input = False


#start game

        print('Second player playing:')
        sp_first_card = randint(1,11)
        print('Your card is',sp_first_card)
        game = False

        while sp_answer:
            sp_second_card = randint(1,11)
            yes_or_no = input('Do you want to go again? (y/n)')
            if yes_or_no == 'y':
                print('your next card is',sp_second_card)
                sp_card = (sp_card) + sp_second_card

            if yes_or_no == 'n':
                print('Finish')
                sp_answer = False

#second_player finish

        sp_total_card = sp_card + sp_first_card
        print('The total value of your card is',sp_total_card)

#end of game

        if sp_total_card == fp_total_card:
            print('Draw')
        if fp_total_card > sp_total_card:
            print('First player wins')
        if sp_total_card > fp_total_card:
            if sp_total_card > 21:
                print('First player wins')
            else:
                print('Second player wins')


