import bpython
bpython.embed()
import os
from rich import print, inspect

def open_file(path):
    with open (path, "r") as myfile:
        data = myfile.read()
    return data


def solve(path):
    data = open_file(path).split('\n')
    # print(data)
    game_dict = {}
    for d in data:
        d_s = d.split(":")
        game_dict[d_s[0]] = [i.strip().split(",") for i in d_s[1].split(";")]
    # print(game_dict)

    s = 0
    for game in game_dict:
        skip = 0
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

            if total_showed_in_set['red'] > 12 or total_showed_in_set['green'] > 13 or total_showed_in_set["blue"] > 14:
                skip = 1
                break
            # print(game)
        if not skip:
            print(game)
            s += int(game.strip().split(" ")[-1])
        # print(aset, total_showed_in_set, len(game_dict[game]))
    return s


if __name__ == "__main__":
    res = solve("input")
    print(res)