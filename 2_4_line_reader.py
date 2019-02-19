'''

Created on Jan 8, 2019

@author: William Duckworth
'''

def main():
  running = True
  while running:
    cmd = input('Enter a command (blank or "exit" to stop)? ')
    cmd = cmd.strip().lower()
    if not cmd or cmd == 'exit':
      running = False
    else:
      print('Command entered:', cmd)
  
if __name__ = '__main__':
  main()
