def fib(n):
    """This function prints a Fibonacci sequence up to the nth Fibonacci
    """

# fill me in
    x = 0
    y = 1
    print(y, end=" ")
    for i in range(-1, n):
        z = x
        x = y
        y = z + y
        print(y, end=" ")


print("fib(n) result:")
n = 0
while n < 10:
    fib(n)
    print("")
    n += 1


def diamond(n):
    """This function prints a diamond shape of size n as shown in loop_exercise_result.txt
    """

# fill me in
    if n == 0:
        pass
    else:
        for i in range(1, n + 1):
            print(" " * (n - i), "*" * (i * 2))
        for i in range(n, 0, -1):
            print(" " * (n - i), "*" * (i * 2))


print("diamond(n) result:")
for i in range(0, 8):
    diamond(i)
    print("")


def hailstone(n):
    """This function prints a hailstone sequence whose details can be found in this link:
        http://mathworld.wolfram.com/CollatzProblem.html
    """

# fill me in
    while n != 1:
        print(int(n), end="  ")
        if n % 2 == 0:
            n = (1 / 2) * n
        else:
            n = 3 * n + 1
    print("1", end="")


print("hailstone(n) result:")
for i in range(1, 8):
    hailstone(i)
    print("")


def arith_sum(n):
    """This function prints the arithmetic sequence starting from 1 to nth together with its sum
    """

# fill me in
    result = 0
    for i in range(1, n + 1):
        result += i
        if i == 1:
            print(i, end="")
        else:
            print(f" + {i}", end="")
    print(f" = {result}", end="")


print("arith_sum(n) result:")
for i in range(1, 10):
    arith_sum(i)
    print("")  
