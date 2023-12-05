import re

with open('./day01/q2/input', 'r') as myfile:
    data = myfile.read()

dict_key= {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
data = data.split("\n")

def check_alpha(s1, start):
    s1 = s1[start:]
    for key in dict_key.keys():
        if s1.startswith(key):
            return dict_key[key]
    return "0"


# Dynamic
def resolve():
    res = []
    for line in data:
        temp = []
        for i, c in enumerate(line):
            if c.isdigit():
                temp += c
                continue
            text2val = check_alpha(line, i)
            if  text2val != "0":
                temp += text2val
        # print(temp)
        res.append(temp)
    return (res)

new_data = resolve()
array_int = []
for D in new_data:
    array_int.append(int(D[0] + D[-1]))


print(data)
print(sum(array_int))