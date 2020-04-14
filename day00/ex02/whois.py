'''
- Make a program that checks if a number is odd, even or zero.
- The program will accept only one parameter, an integer.
'''

import sys

if len(sys.argv) > 2:
    print ('ERROR')
elif len(sys.argv) == 2:
    if sys.argv[1].isdigit():
        sys.argv[1] = int(sys.argv[1])
        if sys.argv[1] == 0:
            print("I'm Zero.")
        elif sys.argv[1] % 2 == 1:
            print("I'm Odd.")
        else:
            print("I'm Even.")
    else:
        print('ERROR')
