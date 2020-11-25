#there is a small bug, fix it then post it
from replit import clear
from art import logo
from random import randint

def total_chances():
  diff=input('Choose a difficulty level, hard gives 5 chances easy gives 10 chances\nhard or easy: ')
  if(diff=='hard'):
    chs=5
  elif(diff=='easy'):
    chs=10
  return chs
def game():
  print(logo)
  chances=total_chances()
  guess=0
  answer=randint(1,101)
  while(chances>0 and guess!=answer):
    guess=int(input('Guess the number: '))  
    if(guess==answer):
      print('You guessed it right, You won!')
      break
    elif(guess!=answer):
      chances-=1
      if(chances>0):
        if(guess>answer):
          print('Your guess value is higher')
          print(f'total chances left {chances}')
        elif(guess<answer):
          print('Your guess value is lower')
          print(f'total chances left {chances}')
      elif(chances==0):
        print('You ran out of chances')
        print(f'The correct answer is: {answer}')
game()