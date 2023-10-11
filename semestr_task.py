def summa(lst):
    try:
        if len(lst) != 4 or type(lst[0]) == str:
            return 'error'
        real_part = float(lst[0]) + float(lst[2])
        imaginary_part = float(lst[1]) + float(lst[3])
        return [real_part, imaginary_part]
    except (ValueError, IndexError):
        return 'error'

def raznost(lst):
    try:
        if len(lst) != 4 or type(lst[0]) == str:
            return 'error'
        real_part = float(lst[0]) - float(lst[2])
        imaginary_part = float(lst[1]) - float(lst[3])
        return [real_part, imaginary_part]
    except (ValueError, IndexError):
        return 'error'

def multi(lst):
    try:
        if len(lst) != 4 or type(lst[0]) == str:
            return 'error'
        real_part = float(lst[0]) * float(lst[2]) - float(lst[1]) * float(lst[3])
        imaginary_part = float(lst[0]) * float(lst[3]) + float(lst[1]) * float(lst[2])
        return [real_part, imaginary_part]
    except (ValueError, IndexError):
        return 'error'

def divide(lst):
    try:
        if len(lst) != 4 or type(lst[0]) == str:
            return 'error'
        denominator = float(lst[2]) ** 2 + float(lst[3]) ** 2
        real_part = (float(lst[0]) * float(lst[2]) + float(lst[1]) * float(lst[3])) / denominator
        imaginary_part = (float(lst[1]) * float(lst[2]) - float(lst[0]) * float(lst[3])) / denominator
        return [(round(real_part,4)), (round(imaginary_part,4))]
    except (ValueError, IndexError, ZeroDivisionError):
        return 'error'

