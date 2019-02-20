'''

Created on Jan 8, 2019

@author: William Duckworth
'''

from datetime import datetime as dt

def main():
  dob = input('Enter your DOB in the format dd/mm/yyyy?')
  dt_dob = dt.strptime(dob, '%d/%m/%Y')
  print(dt_dob.strftime('%A %B %d, %Y'))

if __name__ = '__main__':
  main()
