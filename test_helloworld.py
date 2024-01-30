""" Test the helloworld module """

from helloworld import compose_salutation

def test_compose_salutation_module():
    """ Invoke print_salutation using "Hello" & "World" defaults """
    greeting = "Hello"
    recipient = "World"
    salutation = compose_salutation(greeting, recipient)
    assert salutation == 'Hello World!'


