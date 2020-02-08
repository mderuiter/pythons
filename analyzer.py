#!/usr/bin/python3

import os
import texttable

def main():

    # Get current directory
    currentDirectory = os.getcwd()

    # Get files in current directory
    files = os.listdir(currentDirectory)

    # Print table
    print_table(files)
    
def print_table(files):

    # Configure table
    table = texttable.Texttable()

    # Add headers
    table.header(["File", "Number of lines"])

    # Add rows
    for file in files:

        # Get extension
        extension = os.path.splitext(file)[1]

        # Filter files with invalid extension
        if len(extension) != 0: 
            count = len(open(file).readlines())
            table.add_row([file, count])

    # Draw table
    table = table.draw()
    print (table)

if __name__ == "__main__":
    main()

