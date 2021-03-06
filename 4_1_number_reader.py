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

    number4 = read_number_loop('Enter a number? ')
    print(number4, ' squared is ', number4**2)

    number5 = read_number_low_high('Enter a number between 1 and 10? ', 1, 10)
    print(number5, ' squared is ', number5**2)

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

def read_number_loop(prompt):
    while True:
        line = input(prompt).strip()
        if line.isdigit():
            return int(line)

def read_number_low_high(prompt, low, high):
    while True:
        line = input(prompt).strip()
        if line.isdigit():
            number = int(line)
            if low <= number <= high:
                return number
            print('Number must be between '+str(low)+' and '+str(high))

if __name__ == "__main__":
    main()