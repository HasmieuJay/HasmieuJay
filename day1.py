def round_func(val): #A float type
    if val % 2 == 0: #For even numbers
        remainder = val % 2
        if remainder >= 0.5:
            to_add_to_val = 1 - remainder
            return val + to_add_to_val
        else:
            return val - remainder
    else:
        remainder = val % 1
        if remainder >= 0.5:
            to_add_to_val = 1 - remainder
            return val + to_add_to_val
        else:
            return val - remainder

print(round_func(3.2))