import math


def mysqrt(a):
    x = 3
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return x


def mathsqrt(a):
    x = math.sqrt(a)
    return x


def test_square_root():
    print("a    mysqrt(a)     math.sqrt(a)   diff")
    print("-    ---------     ------------   ----")
    a = 1.0
    while a < 10:
        my_sqrt = mysqrt(a)
        math_sqrt = mathsqrt(a)
        diff = abs(my_sqrt - math_sqrt)
        float_my_sqrt = float(my_sqrt)
        float_math_sqrt = float(math_sqrt)
        decimal_my_sqrt = f"{float_my_sqrt:.12}"
        decimal_math_sqrt = f"{float_math_sqrt:.12}"
        print(f"{a}  {decimal_my_sqrt:<13} {decimal_math_sqrt:<13} {diff}")
        a += 1


test_square_root()
