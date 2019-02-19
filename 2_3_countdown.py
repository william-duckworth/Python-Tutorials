'''

Created on Jan 8, 2019

@author: William Duckworth
'''

def main():
  n = int(input('Starting number for countdown? '))
  while n >= 0:
    print(n, end='')
    n -= 1
  print()

if __name__ = '__main__':
  main()
