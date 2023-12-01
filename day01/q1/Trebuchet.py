
def solve_q1():
    with open ("input", "r") as myfile:
        data = myfile.read()

    data = data.split("\n")
    new_data = []
    for D in data:
        temp = []
        for d in D:
            if d in "0123456789":
                temp.append(d)
        new_data.append(temp)

    array_int = []
    for D in new_data:
        array_int.append(int(D[0] + D[-1]))

    print(sum(array_int))

if __name__ == "__main__":
    solve_q1()