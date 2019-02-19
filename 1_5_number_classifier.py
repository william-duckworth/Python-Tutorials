'''

Created on Jan 8, 2019

@author: William Duckworth
'''

def main():
    x = int(input('Think of a number? '))
  if x < 0:
    print('negative')
  elif x > 0:
    if x >= 1000:
      print('large', end='')
    elif x < 100:
      print('small', end='')
    else:
      print('medium', end='')
    print('positive')
else:
    print('zero')

if __name__ = '__main__':
  main()
