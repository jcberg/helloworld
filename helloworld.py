""" Print 'Hello World!' using a __main__ function entry point and collecting CLI args with argparse."""

import argparse

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

    hello_message = greeting + " " + recipient
    print(f'{greeting} {recipient}!')

if __name__ == "__main__":
    main()
