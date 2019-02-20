'''

Created on Jan 8, 2019

@author: William Duckworth
'''

import math

GRAVITY = 9.81
VELOCITY = 100.0

def main():
  theta()
  range()
  
def theta():
  line = input('how far to the target [up to 1000]? ')
  distance = float(line)

  theta = math.asin(distance * GRAVITY / VELOCITY**2) / 2
  print('launch angle is', math.degrees(theta))
  
def range():
  line = input('what launch angle have you set? ')
  theta = math.radians(float(line))

  distance = 2 * VELOCITY**2 * math.cos(theta) * math.sin(theta) / GRAVITY
  print('your range is', distance)
  
if __name__ == '__main__':
  main()
