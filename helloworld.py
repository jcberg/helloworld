""" Print 'Hello World!' using:
    - a __main__ function entry point
    - collecting of CLI args with argparse
    - docstrings in modules
    - test via pytest module
"""

import argparse

def get_logging_level(logging):
    """ Set numeric logging_level value based on alphanumeric logging arg"""
    if (logging == "7") or (logging == "debugging"):
        logging_level = 7
    elif (logging == "6") or (logging == "informational"):
        logging_level = 6
    elif (logging == "5") or (logging == "notifications"):
        logging_level = 5
    elif (logging == "4") or (logging == "warnings"):
        logging_level = 4
    elif (logging == "3") or (logging == "errors"):
        logging_level = 3
    elif (logging == "2") or (logging == "critical"):
        logging_level = 2
    elif (logging == "1") or (logging == "alerts"):
        logging_level = 1
    elif (logging == "0") or (logging == "emergencies"):
        logging_level = 0
    else:
        print(f'Unknown logging value, defaulting to "0" (emergencies)')
        logging_level = 0
    return logging_level

def compose_salutation(greeting, recipient, logging_level):
    """ Combine greeting and recipient into a salutation message """
    salutation = greeting + " " + recipient + "!"
    return salutation
    

def main():
    """ Print 'Hello World!' """

    # Set defaults
    greeting = "Hello"
    recipient = "World"
    logging = 0

    parser = argparse.ArgumentParser()
    parser.add_argument("--greeting", help="choose your own greeting (Default: 'Hello')")
    parser.add_argument("--recipient", help="choose your own recipient (Default: 'World')")
    parser.add_argument("--logging", help="set your logging level: 0-7 (Default: 0 [=emgergencies])")
    cli_args = parser.parse_args()
    if cli_args.greeting:
        greeting = cli_args.greeting
    if cli_args.recipient:
        recipient = cli_args.recipient
    if cli_args.logging:
        logging = cli_args.logging

    logging_level = get_logging_level(logging)
    salutation = compose_salutation(greeting, recipient, logging_level)
    print(f'{salutation}')
    
if __name__ == "__main__":
    main()
