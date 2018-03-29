from random import randint
num = int(input('Pick a number to for times table quiz:'))
score = 0
for i in range(1,13):
    z = randint(1,101)
    a = input('{}. {} x {} = '.format(i,num,z))
    if int(a) == z*num:
        score = (score) + 1
        
print(" ")
print('Your score is {}/12'.format(score))
