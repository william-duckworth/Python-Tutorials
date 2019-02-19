'''

Created on Jan 8, 2019

@author: William Duckworth
'''

def main():
  line = input('Enter a temperature followed by K C or F? ')
  line = line.strip().upper()
  celsius = None
  number = line.rstrip('CFK')
  if line.endswith('K'):
    celsius = float(number) - 273.15
  elif line.endswith('C'):
    celsius = float(number) 
  elif line.endswith('F'):
    celsius = (float(number) - 32) * (5.0 / 9.0)
  if celsius != None:
    print('{} is:  {:.2f}K {:.2f}C {:.2f}F'.format(
      line, celsius+273.15, celsius, ((celsius) * (9.0 / 5.0)) + 32))
  else:
    print('Did not understand:', line)
  
if __name__ = '__main__':
  main()
