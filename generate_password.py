#!/usr/bin/python3

import re
import random
import string
import subprocess

def main():

    # Variables
    numbers = string.digits
    characters = string.ascii_letters

    # Generate password
    password = "".join(random.choice(characters) for x in range(18))

    # Add random number to the password
    number = random.choice(numbers)
    index = random.randint(0,len(password))
    password = change_char(password, index, number)
    
    # Add dashes to the password
    password = re.sub(r'.*(\w{6})(\w{6})(\w{6}).*', r"\1-\2-\3", password)

    # Copy password to clipboard
    subprocess.run("pbcopy", universal_newlines=True, input=password)

    # Print output
    print(f"Copied password: '{password}' to clipboard")


def change_char(s, p, r):
    return s[:p]+r+s[p+1:]

if __name__ == "__main__":
    main()