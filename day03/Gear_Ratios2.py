PATH = "input"

def openfile():
    with open(PATH, "r") as myfile:
        data = myfile.read().split("\n")
    return data


def create_map(data):
    """
    Create 2-D Map from raw data
    """
    ret_map = []
    for y, line in enumerate(data):
        ret_map.append([])
        for c in line:
            ret_map[y].append(c)
    return ret_map


def valid_length(x, y, max_x, max_y):
    """
    Check index still in array length
    """
    return x < max_x and y < max_y and x >= 0 and y >= 0


def collect_number(x, y, data, max_x, max_y):
    """
    Get number in 8 direction and fill data when pass
    """
    y1 = y - 1
    number_list = []
    while y1 <= y + 1:
        x1 = x - 1
        while x1 <= x + 1:
            num = ""
            if data[y1][x1].isdigit():
                x_plus = 0
                while (
                    valid_length(x1 + x_plus, y1, max_x, max_y)
                    and data[y1][x1 + x_plus].isdigit()
                ):
                    num += data[y1][x1 + x_plus]
                    data[y1][x1 + x_plus] = "#"
                    x_plus += 1
                x_minus = -1
                while (
                    valid_length(x1 + x_minus, y1, max_x, max_y)
                    and data[y1][x1 + x_minus].isdigit()
                ):
                    num = data[y1][x1 + x_minus] + num
                    data[y1][x1 + x_minus] = "#"
                    x_minus -= 1
                number_list.append(num)
            x1 += 1
        y1 += 1
    if len(number_list) > 1:
        return int(number_list[0]) * int(number_list[1])
    return 0


def solve():
    data = openfile()
    mymap = create_map(data)
    max_x = len(mymap[0])
    max_y = len(mymap)
    total = 0
    for y, row in enumerate(mymap):
        for x, c in enumerate(row):
            if c == "*":
                number = collect_number(x, y, mymap, max_x, max_y)
                total += number
    return total


if __name__ == "__main__":
    print(solve())
