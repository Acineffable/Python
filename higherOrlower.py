from random import randint
correct_answer = True
score = 0
previous_card = randint(1,13)

print('your first card is',previous_card)

while correct_answer:

    print('higher or lower than',previous_card,'?')
    ans = input('h or l')
    next_card = randint(1,13)
    print('your next card is',next_card)

    if ans == 'h':
        if next_card > previous_card:
            print('well done')
            score = (score) + 1
        else:
            print('Wrong')
            correct_answer = False

    if ans == 'l':
        if previous_card > next_card:
            print('well done')
            score =(score) + 1
        else:
            print('wrong')
            correct_answer = False

    previous_card=next_card
    print()

print('Your score is',score)
print('Game over')
