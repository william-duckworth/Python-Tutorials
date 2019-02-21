'''

Created on Jan 8, 2019

@author: William Duckworth
'''

def main():
    number = read_number()
    print(number, ' squared is ', number**2)

    number2 = read_number_prompt('Enter a number? ')
    print(number2, ' squared is ', number2**2)

    number3 = read_number_strip('Enter a number? ')
    print(number3, ' squared is ', number3**2)

def read_number():
    line = input('Enter a number? ')
    return int(line)

def read_number_prompt(prompt):
    line = input(prompt)
    return int(line)

def read_number_strip(prompt):
    asking = True
    while asking:
        line = input(prompt).strip()
        asking = not line.isdigit()
    return int(line)

if __name__ == "__main__":
    main()