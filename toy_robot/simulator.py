import argparse
from board import Board
"""
    author: Xijing Gui
    date: 22/09/2016
    description: a simulation of a toy robot moving on a square tabletop, 
      of dimensions 5 units x 5 units.
    version: 1.00
"""
# The main simulator
if __name__ == '__main__':
    
    board = Board()
    inputStr = ""
    
    while True:
        inputStr = raw_input('')
        inputStr = inputStr.split()
        try:
            command = inputStr[0]
            args=inputStr[1].split(",")
        except IndexError:
            args=()
        
        try:
            result = getattr (board, command.lower())(*args)
            if result:
                print result
        except TypeError as err:
            print 'Invalid parameters:',err
        except AttributeError as err:
            print 'Unrecognised Command:',err



    parser = argparse.ArgumentParser()
    args = parser.parse_args()

