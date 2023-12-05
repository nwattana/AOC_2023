import bpython
bpython.embed()
import os
from rich import print, inspect
from math import pow

with open ("day04/q2/input", "r") as myfile:
    data = myfile.read().split("\n")


def resolve():
    total = 0
    stack_game = {}
    for line in data:
        line = line.split(":")
        line += line[1].split("|")

        des = set(line[2].split())
        src = set(line[3].split())
        inter = des.intersection(src)
        count = len(inter)

        stack_game[line[0]] = count

    # loop create list
    anwers = [0 for i in range(len(stack_game))]
    copied = [0 for i in range(len(stack_game))]
    stack = [stack_game[i] for i in stack_game]
    for i,k in enumerate(stack_game):
        # if i == 15:
        #     break
        anwers[i] += copied[i]
        anwers[i] += 1
        if stack_game[k] > 0:
            for a in range(stack_game[k]):
                if i + a > len(anwers):
                    break
                copied[i + a + 1] += anwers[i]
    print(copied[:20])
    print("answers", anwers[:20], sum(anwers))
    print("stack", stack[:20])
    # print(sum(anwers))

    return total, stack_game
# [0, 1, 2, 4,]

s = resolve()


