""" Print 'Hello World!' using:
    a __main__ function entry point
    collection of CLI args with argparse
    docstrings in modules
    test via pytest module
"""

import argparse

def compose_salutation(greeting, recipient):
    """ Combine greeting and recipient into a salutation message """
    salutation = greeting + " " + recipient + "!"
    return salutation
    

def main():
    """ Print 'Hello World!' """

    # Set defaults
    greeting = "Hello"
    recipient = "World"

    parser = argparse.ArgumentParser()
    parser.add_argument("--greeting", help="choose your own greeting (Default: 'Hello')")
    parser.add_argument("--recipient", help="choose your own recipient (Default 'World')")
    cli_args = parser.parse_args()
    if cli_args.greeting:
        greeting = cli_args.greeting
    if cli_args.recipient:
        recipient = cli_args.recipient

    salutation = compose_salutation(greeting, recipient)
    print(f'{salutation}')
    
if __name__ == "__main__":
    main()
