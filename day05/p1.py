import bpython
bpython.embed()
import os

from rich import inspect, print
PATH = "day05/input"

def openfile():
    with open(PATH, "r") as myfile:
        data = myfile.read().split("\n")
    return data

data = openfile()

s2 = [i for i in range(100)]
for i in range(2):
    s2[98 + i] = 50 + i
for i in range(48):
    s2[50 + i] = 52 + i
print(s2[79], s2[14], s2[55], s2[13])

def find_item(i):
    if 98 <= i and i < 100:
        return 50 + (i - 98)
    elif i >= 50 and i < 98:
        return 52 + (i - 50)
    else:
        return i
print(find_item(79), find_item(14), find_item(55), find_item(13))
# 81 14 57 13

class Convertor:

    def __init__(self, start, ranges, des):
        self.start = start
        self.ranges = ranges
        self.des = des
    
    def __repr__(self) -> str:
        return f"{self.des} {self.start} {self.ranges}"
    
    def is_mylength(self, i):
        return i >= self.start and i < self.start + self.ranges
    
    def get_des(self, i):
        return self.des + (i - self.start)

class Formula:

    def __init__(self, name):
        self.name = name
        self.convertor_list = []
    
    def __repr__(self) -> str:
        return self.name
    
    def add_convertor(self, convertor_str):
        splited = convertor_str.split(" ")
        args = {
            "start": int(splited[1]),
            "des": int(splited[0]),
            "ranges": int(splited[2]),
        }
        self.convertor_list.append(Convertor(**args))
    
    def cale_des_seed(self, i):
        des = i
        for converter in self.convertor_list:
            if converter.is_mylength(i):
                des = converter.get_des(i)
        return des


def resolve():
    data = openfile()
    seed = [int(i) for i in data.pop(0).split(" ")[1:]]
    form_list = []
    form = Formula("Empty")
    con = 0
    for i, v in enumerate(data):
        if v == '':
            form_list.append(form)
            form = Formula(data[i + 1].strip(":,"))
            con += 2
        if con > 0:
            con -= 1
            continue
        form.add_convertor(v)
        # print(v)
    form_list.append(form)
    new_seed = []
    for x in seed:
        for i in form_list:
            des = i.cale_des_seed(x)
            x = des
        new_seed.append(des)
    print(min(new_seed))
    return "finale value"

if __name__ == "__main__":
    print(resolve())