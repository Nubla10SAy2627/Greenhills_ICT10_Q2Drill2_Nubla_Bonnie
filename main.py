# Finding surnames
from pyscript import display, document


def name_finder(e):
    document.getElementById('result').innerHTML = ' '
    last_name = document.getElementById('lastname').value.lower().strip()
    first_name = document.getElementById('firstname').value.lower().strip()
    name = first_name + " " + last_name
    accepted = ["alexa agnote", "lj gabia", "keane pacaña", "franco deocampo"]
    student_checker = name in accepted

    display_message = (f'Sorry, no {name} in the list :(', f'{name} is in the list!')
    display(display_message[student_checker], target='result')


