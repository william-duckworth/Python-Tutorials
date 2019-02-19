'''

Created on Jan 8, 2019

@author: William Duckworth
'''

def main():
  year = int(input('Enter a year? '))
  if year > 0:
    if year%400 == 0:
      print('leap year')
    elif year%4==0 and year%100!=0:
      print('leap year')
    else:
      print('not a leap year')
  else:
    print('Must be greater than zero')

if __name__ = '__main__':
  main()
