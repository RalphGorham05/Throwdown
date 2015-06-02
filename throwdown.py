'''
Throwdown
5/6/15
'''

from random import randint


def pick_numbers():
    player_numbers = []
    p1_number = input('Enter a number between 1-100 Player 1: ')
    if not (1 <= p1_number <= 100):
        print 'invalid number, one more chance to pick number'
        p1_number = input('Enter a number between 1-100 Player 1: ')

    player_numbers.append(p1_number)
        
        
    p2_number = input('Enter a number between 1-100 Player 2: ')
    if not (1 <= p2_number <= 100):
        print 'invalid number, one more chance to pick number'
        p2_number = input('Enter a number between 1-100 Player 2: ')

    player_numbers.append(p2_number)

    return player_numbers


numbers = pick_numbers()

home = randint(1,100)
#print home

if (abs(numbers[0] - home) < abs(numbers[1] - home)):
    print 'p1 is home'

elif(abs(numbers[0] - home) == abs(numbers[1] - home)):
    print 'What are the odds!'
    pick_numbers()
    
else:
    print 'p2 is home'
