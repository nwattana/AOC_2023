import bpython
bpython.embed()
import os
from rich import print, inspect

def open_file(path):
    with open (path, "r") as myfile:
        data = myfile.read()
    return data

def solve2():
    data = open_file("day02/q1/input").split("\n")
    game_dict = {}
    for d in data:
        d_s = d.split(":")
        game_dict[d_s[0]] = [i.strip().split(",") for i in d_s[1].split(";")]
    s = 0
    game_lab = {}
    for game in game_dict:

        lamout_ball={
            'red':0,
            'green':0,
            'blue':0,
        }
        # a single game
        for aset in game_dict[game]:
            total_showed_in_set={
                'red':0,
                'green':0,
                'blue':0
            }
            # check amount of ball for each round
            for item in aset:
                ch = item.strip().split(" ")
                # print(ch)
                total_showed_in_set[ch[1]] += int(ch[0])
            for i in lamout_ball:
                if lamout_ball[i] < total_showed_in_set[i]:
                    lamout_ball[i] = total_showed_in_set[i]
        game_lab[game]=lamout_ball
    # print(game_lab)

    s = 0
    for game in game_lab:
        aa = game_lab[game]
        powers = aa['red'] * aa['blue'] * aa['green']
        s += powers
    return s
    


solve2()