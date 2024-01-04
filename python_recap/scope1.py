from typing import Dict

name = {"Dot": "name"}


def print_name():
    global name
    name = {"Alison": name}
    b = 2 + 3j
    a = 4 + 5j
    print("name1: ", id(name), 2 * (b + a))


print_name()
print("name2: ", id(name))
