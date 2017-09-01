
# global import
import pandas as pd
import sys
import argparse


def main():
    # Parse arguments from command line
    parser = argparse.ArgumentParser()

    # Set up required arguments this script
    parser.add_argument('function', type=str, help='function to call')
    parser.add_argument('first_arg', type=str, help='first argument')
    #parser.add_argument('second_arg', type=str, help='second argument')

    # Parse the given arguments
    args = parser.parse_args()

    # Get the function based on the command line argument and 
    # call it with the other two command line arguments as 
    # function arguments
    eval(args.function)(args.first_arg)


def load_arg(first_arg):
	print first_arg + " Hello!"
	#sys.stdout.flush()


if __name__ == '__main__':
	main()