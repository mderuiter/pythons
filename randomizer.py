#!/usr/bin/python3

import sys
import random

def main(arguments):
    
    # Vars
    numberOfArguments = len(arguments)
    
    if numberOfArguments < 3:
        error("Missing arguments.")
        return
        
    elif numberOfArguments > 3:
        error("Too many arguments.")
        return
        
    if arguments[1].isdigit() and arguments[2].isdigit():
        randomize(arguments[1], arguments[2])
        
    else:
        error("Invalid arguments.")
        

def randomize(min, max):

    if min == max:
        error("Input is equal.")
        return
        
    elif min > max:
        error("Min value is greater than max value.")
        return
        
    number = random.randint(int(min), int(max))
    print(number)
    
def error(message):
    print(f"Error: {message}")
    
if __name__ == "__main__":
    main(sys.argv)
