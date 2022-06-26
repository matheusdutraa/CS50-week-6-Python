from cs50 import get_string

people = {
    "Matheus": "+55 45 99900000",
    "Joao": "+55 45 88800000",
}

name = get_string("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")