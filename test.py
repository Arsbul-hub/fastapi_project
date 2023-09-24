def first(line="YOOOOOOX"):
    x_index = line.find("X")
    y_index = line.find("Y")
    if x_index < 0 or y_index < 0:
        return None
    return abs(y_index - x_index)

def second(data=[1, 3, -1, -4]):
    d = 0
    indexes = (0, 0)
    started_type = None
    for i in range(len(data)):
        if i < len(data):
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


print(first())