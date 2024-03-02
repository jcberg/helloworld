""" Test the helloworld module """

from helloworld import compose_salutation
from helloworld import get_logging_level

def test_get_logging_level():
    """ Invoke get_logging_level testing various logging values"""

    logging = "7"
    logging_level = get_logging_level(logging)
    assert logging_level == 7
    logging = "debugging"
    logging_level = get_logging_level(logging)
    assert logging_level == 7

    logging = "6"
    logging_level = get_logging_level(logging)
    assert logging_level == 6
    logging = "informational"
    logging_level = get_logging_level(logging)
    assert logging_level == 6

    logging = "5"
    logging_level = get_logging_level(logging)
    assert logging_level == 5
    logging = "notifications"
    logging_level = get_logging_level(logging)
    assert logging_level == 5

    logging = "4"
    logging_level = get_logging_level(logging)
    assert logging_level == 4
    logging = "warnings"
    logging_level = get_logging_level(logging)
    assert logging_level == 4

    logging = "3"
    logging_level = get_logging_level(logging)
    assert logging_level == 3
    logging = "errors"
    logging_level = get_logging_level(logging)
    assert logging_level == 3

    logging = "2"
    logging_level = get_logging_level(logging)
    assert logging_level == 2
    logging = "critical"
    logging_level = get_logging_level(logging)
    assert logging_level == 2

    logging = "1"
    logging_level = get_logging_level(logging)
    assert logging_level == 1
    logging = "alerts"
    logging_level = get_logging_level(logging)
    assert logging_level == 1

    logging = "0"
    logging_level = get_logging_level(logging)
    assert logging_level == 0
    logging = "emergencies"
    logging_level = get_logging_level(logging)
    assert logging_level == 0

    logging = "8"
    logging_level = get_logging_level(logging)
    assert logging_level == 0
    logging = "unknown"
    logging_level = get_logging_level(logging)
    assert logging_level == 0

def test_compose_salutation_module():
    """ Invoke print_salutation using "Hello" & "World" defaults """
    greeting = "Hello"
    recipient = "World"
    logging_level = 0
    salutation = compose_salutation(greeting, recipient, logging_level)
    assert salutation == 'Hello World!'


