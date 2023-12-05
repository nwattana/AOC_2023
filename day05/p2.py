from copy import deepcopy
from rich import inspect, print

PATH = "input"


def openfile():
    with open(PATH, "r") as myfile:
        # seperate formula
        data = myfile.read().split("\n\n")
    return data


data = openfile()

# s2 = [i for i in range(100)]
# for i in range(2):
#     s2[98 + i] = 50 + i
# for i in range(48):
#     s2[50 + i] = 52 + i
# print(s2[79], s2[14], s2[55], s2[13])

# def find_item(i):
#     if 98 <= i and i < 100:
#         return 50 + (i - 98)
#     elif i >= 50 and i < 98:
#         return 52 + (i - 50)
#     else:
#         return i

# for i in range(14):
#     print(find_item(79 + i))
# for i in range(13):
#     print(find_item(55 + i))
# # 81 14 57 13


class Convertor:
    def __init__(self, start, ranges, des):
        self.start = start
        self.ranges = ranges
        self.des = des
        self.stop = self.start + self.ranges  # inclusive

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

    def get_convertor(self):
        return self.convertor_list


class ConvertedSeed:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __repr__(self) -> str:
        return f"start:{self.start},stop:{self.stop}"

    def get_min(self):
        return self.start
    
    def is_valid(self):
        # print(f"{self.start} {self.stop}", self.start < self.stop)
        return self.start < self.stop


class SeedBag:
    def __init__(self, start, lens):
        self.main_bag = [ConvertedSeed(start, start + lens - 1)]

    def __repr__(self) -> str:
        return f"{self.main_bag}"

    def applied_formular(self, formular: Formula):
        convertors = formular.get_convertor()
        mb = self.main_bag
        des = []
        for s in mb:
            for c in convertors:
                if c.start >= s.stop or c.stop <= s.start:
                    continue
                new_seed_m = ConvertedSeed(start=max(s.start, c.start), stop=min(s.stop, c.stop))
                new_seed_r = ConvertedSeed(start=new_seed_m.stop, stop=s.stop)
                new_seed_l = ConvertedSeed(start=s.start, stop=new_seed_m.start)
                if new_seed_r.is_valid():
                    mb.append(new_seed_r)
                if new_seed_l.is_valid():
                    mb.append(new_seed_l)
                des.append(
                    ConvertedSeed(
                        start=c.get_des(new_seed_m.start),
                        stop=c.get_des(new_seed_m.stop)
                        )
                )
                break
            else:
                des.append(s)
        self.main_bag = deepcopy(des)



def resolve():
    seeds_raw, *formulas = openfile()
    seeds = seeds_raw.split(":")[-1].strip().split(" ")
    seed_l = []
    skip = 0
    for i, _ in enumerate(seeds):
        if skip:
            skip = 0
            continue
        sb = SeedBag(int(seeds[i]), int(seeds[i + 1]))
        seed_l.append(sb)
        skip = 1

    form_list = []
    for v in formulas:
        name, *reps = v.split("\n")
        form = Formula(name[:-1])
        for rep in reps:
            form.add_convertor(rep)
        form_list.append(form)
    for i in seed_l:
        for form in form_list:
            i.applied_formular(form)
    mins = seed_l[0].main_bag[0].start
    for bag in seed_l:
        for item in bag.main_bag:
            mins = min(mins, item.start)


    return mins


if __name__ == "__main__":
    print(resolve())
