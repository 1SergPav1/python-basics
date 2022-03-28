from functools import wraps

def val_checker(func_check):
    def val_checker_deco(calc_cube):
        @wraps(calc_cube)
        def wrapper(x):
            if func_check(x):
                return calc_cube(x)
            else:
                raise ValueError('wrong val')
        return wrapper
    return val_checker_deco

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x**3

a = calc_cube(-5)
print(a)
