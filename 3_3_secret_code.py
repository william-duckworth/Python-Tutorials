'''

Created on Jan 8, 2019

@author: William Duckworth
'''

import random

def main():
  code = random.randint(1, 99)
  running = True

  while running:
    guess = int(input('guess my secret code? '))
    if guess == 0 or guess == code:
      if guess == code:
        print('you got it')
        running = False
      else:
        diff = abs(code-guess)
      if diff >= 50:
        print('cold', end=' ')
      elif 25 <= diff < 50:
        print('warm', end=' ')
      elif 6 <= diff < 25:
        print('hot', end=' ')
      else:
        print('smoking', end=' ')
      if code < guess:
        print('try lower')
      else:
        print('try higher')

  print('my code was', code)

if __name__ = '__main__':
  main()
