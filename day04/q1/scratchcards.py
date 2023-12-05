import bpython
bpython.embed()
import os
from rich import print, inspect
from math import pow



def resolve():
    with open ("day04/q1/input", "r") as myfile:
        data = myfile.read().split("\n")
    total = 0
    stack_game = {}
    for line in data:
        line = line.split(":")
        line += line[1].split("|")

        # resolve
        des = set(line[2].split())
        src = set(line[3].split())

        inter = des.intersection(src)
        count = len(inter)
        stack_game[line[0]] = count


        point = 1 * 2 ** (count - 1) * (count > 0)
        total += point
    return total

s = resolve()