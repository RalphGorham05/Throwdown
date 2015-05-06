'''
Throwdown
5/6/15
'''

from random import randint

p1_number = input('Enter a number between 1-100 Player 1: ')
p2_number = input('Enter a number between 1-100 Player 2: ')

home = randint(1,100)
print home

if (abs(p1_number - home) < abs(p2_number - home)):
    print 'p1 is home'

elif(abs(p1_number - home) == abs(p2_number - home)):
    print 'do over'
    
else:
    print 'p2 is home'

