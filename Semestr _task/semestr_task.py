def summa(lst):
    if len(lst) != 4 or type(lst[0]) == str:
        return 'error'
    return [float(lst[0] + lst[2]),
            float(lst[1] + lst[3])]

def raznost(lst):
    if len(lst) != 4 or type(lst[0]) == str:
        return 'error'
    return [float(lst[0] - lst[2]),
                float(lst[1] - lst[3])]

def multi(lst):
    if len(lst) != 4 or type(lst[0]) == str:
        return 'error'
    return [float(lst[0] * lst[2] - lst[1] * lst[3]),
                float(lst[0] * lst[3] + lst[1] * lst[2])]


def divide(lst):
    try:
        if len(lst) != 4 or type(lst[0]) == str:
            return 'error'
        denominator = float(lst[2]) ** 2 + float(lst[3]) ** 2
        real_part = (float(lst[0]) * float(lst[2]) + float(lst[1]) * float(lst[3])) / denominator
        imaginary_part = (float(lst[1]) * float(lst[2]) - float(lst[0]) * float(lst[3])) / denominator
        return [(round(real_part,4)), (round(imaginary_part,4))]
    except Exception:
        return 'error'

