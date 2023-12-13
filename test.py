import math


def first(line: list):
    if "X" not in line or "Y" not in line:
        return 0
    x_index = line.index("X")
    y_index = line.index("Y")
    return abs(y_index - x_index)


def second(data=[1, 3, -1, -4]):
    d = 0
    indexes = (0, 0)
    started_type = None
    for i in range(len(data)):
        if i + 1 < len(data):
            num = data[i]
            next_num = data[i + 1]
            if num < next_num:
                if started_type is None or started_type == "lower":
                    d = 1
                    started_type = "bigger"
                else:
                    d += 1
            elif num > next_num:
                if started_type is None or started_type == "bigger":
                    d = 1
                    started_type = "lower"
                else:
                    d += 1

    return d


def third(nums: list, target: int):
    for i in nums:
        s_num = target - i
        if s_num in nums:
            return nums.index(i), nums.index(s_num)


print(third([1, 2, 3, 4, 5], 7))


def fourth(num):
    string_num_reversed = list(str(num))
    string_num_reversed.reverse()
    if list(str(num)) == string_num_reversed:
        return True
    return False


def five(list1: list, list2: list):
    out_list = list1 + list2
    out_list.sort()
    return out_list


from math import ceil, sqrt, floor


def six(x: int):
    x = sqrt(x)
    if x % int(x) >= 0.5:
        return ceil(x)
    else:
        return floor(x)
