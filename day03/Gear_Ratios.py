import bpython
bpython.embed()
import os
from rich import print, inspect


with open ("day03/input", "r") as myfile:
    data = myfile.read().split("\n")


def check_sign(c, x, y, max_x, max_y):
    return (x - 1 >= 0 and y - 1 >= 0 and data[y - 1][x - 1] not in "0123456789." ) or \
        (x - 1 >= 0 and y + 1 < max_y and data[y + 1][x - 1] not in "0123456789." )or \
        (x + 1 < max_x and y - 1 >= 0 and data[y - 1][x + 1] not in "0123456789." )or \
        (x + 1 < max_x and y + 1 < max_y and data[y + 1][x + 1] not in "0123456789." )or \
        (y - 1 >= 0 and data[y - 1][x] not in "0123456789." ) or \
        (x - 1 >= 0 and data[y][x - 1] not in "0123456789." ) or \
        (y + 1 < max_y and data[y + 1][x] not in "0123456789." ) or \
        (x + 1 < max_x and data[y][x + 1] not in "0123456789.")
        

def collect_number(c, x, y, max_x):
    number = []
    x2 = x + 1
    number.append(data[y][x])
    while (x2 < max_x and data[y][x2] in "0123456789"):
        number.append(data[y][x2])
        x2 += 1
    lens = len(number) - 1
    x3 = x - 1
    while (x3 >= 0 and data[y][x3] in "0123456789"):
        number.insert(0, data[y][x3])
        x3 -= 1
    number = int("".join(number))
    return number, lens



def resolve():
    max_x = len(data[0])
    max_y = len(data)
    number_list = []
    lens = 0
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if lens > 0:
                lens -= 1
                continue
            if c in "0123456789":
                if check_sign(c, x, y, max_x, max_y):
                    number, lens = collect_number(c, x, y, max_x)
                    print(number, lens, x, y, c)
                    number_list.append(number)

    
        # if y > 4:
        #     # print(data[y][x])
    # print(number_list)
        #     break
    
    return sum(number_list)
resolve()
