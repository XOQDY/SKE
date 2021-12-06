import math


def check_unit(area):
    if area > 1:
        return "meters"
    elif area <= 1:
        return "meter"


def cal_circle(radius):
    area = math.pi * (radius ** 2)
    return area


def cal_triangle(base, height):
    area = 1/2 * base * height
    return area


def cal_rectangle(width, height):
    area = width * height
    return area


def print_result(polygon, area):
    print(f"Area of this {polygon} is {area:.2f} square {check_unit(area)}")


def check_float_input(n, word):
    while n not in float:
        print("Please enter a number!")
        n = input(f"{word} = ")
        if n in float:
            break
    n = float(n)
    return n


def result(polygon):
    if polygon == "T" or polygon == "t":
        base, height = action(polygon)
        area = cal_triangle(base, height)
        return area
    elif polygon == "R" or polygon == "r":
        width, height = action(polygon)
        area = cal_rectangle(width, height)
        return area
    elif polygon == "C" or polygon == "c":
        radius = action(polygon)
        area = cal_circle(radius)
        return area


def action(polygon):
    if polygon == "T" or polygon == "t":
        base = input("base = ")
        base = check_float_input(base, "base")
        print("")
        height = input("height = ")
        height = check_float_input(height, "height")
        return base, height
    elif polygon == "R" or polygon == "r":
        width = input("width = ")
        width = check_float_input(width, "width")
        print("")
        height = input("height = ")
        height = check_float_input(height, "height")
        return width, height
    elif polygon == "C" or polygon == "c":
        radius = input("Radius = ")
        radius = check_float_input(radius, "Radius")
        return radius


def full_polygon(polygon):
    if polygon == "T" or polygon == "t":
        return "triangle"
    elif polygon == "R" or polygon == "r":
        return "rectangle"
    elif polygon == "C" or polygon == "c":
        return "circle"


polygon = ""

while polygon != "Q":
    polygon = input("(T)riangle (R)ectangle (C)ircle (Q)uit : ")
    if polygon == "T" or polygon == "t" or polygon == "R" or polygon == "r" or polygon == "C" or polygon == "c":
        print("")
        area = result(polygon)
        print_result(polygon, area)
        print("")
    elif polygon == "Q":
        print("Bye")
    else:
        print("Incorrect Input")
        print("")
        polygon = input("(T)riangle (R)ectangle (C)ircle (Q)uit : ")
        area = result(polygon)
        print_result(polygon, area)

