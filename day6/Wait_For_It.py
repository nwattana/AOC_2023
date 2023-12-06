import os
import numpy as np
import math as m

from rich import inspect, print
PATH = "day6/input"

def openfile():
    with open(PATH, "r") as myfile:
        data = myfile.read()
    return data

def p1(f):
    speeds, distances = f.split("\n")
    _, *speeds = speeds.strip().split()
    speeds = [int(i) for i in speeds]
    _, *distances = distances.strip().split()
    distances = [int(i) for i in distances]

    avail = []
    for s, d in zip(speeds, distances):
        p1d = np.poly1d([1, -s, d])
        root = np.roots(p1d)
        a = m.floor(max(root))
        if (a == max(root)):
            a = max(root) - 1
        b = m.ceil(min(root))
        if b == min(root):
            b = min(root) + 1
        avail.append(a - b + 1 * (a != b))
    res = 1
    for p in avail:
        res = res * p
    print(res)

def p2(f):
    speeds, distances = f.split("\n")
    _, *speeds = speeds.strip().split()
    speeds = int("".join(speeds))
    _, *distances = distances.strip().split()
    distances = int("".join(distances))

    p1d = np.poly1d([1, -speeds, distances])
    root = np.roots(p1d)
    a = m.floor(max(root))

    if (a == max(root)):
        a = max(root) - 1
    b = m.ceil(min(root))
    if b == min(root):
        b = min(root) + 1
    res = (a - b + 1) * (a != b)
    print(res)


if __name__ == "__main__":
    f = openfile()
    p1(f)
    p2(f)