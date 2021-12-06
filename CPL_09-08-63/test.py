from math import pi


def check_input(polygon):

    if polygon == "T" or polygon == "t" or polygon == "R" or polygon == "r" or polygon == "C" or polygon == "c":
        area = result(polygon)
        plural(polygon, area)
    else:
        print("Incorrect Input")


def action(polygon):
    if polygon == "T" or polygon == "t":
        base = float(input("base = "))
        height = float(input("height = "))
        return base, height
    elif polygon == "R" or polygon == "r":
        width = float(input("width = "))
        height = float(input("height = "))
        return width, height
    elif polygon == "C" or polygon == "c":
        Radius = float(input("radius = "))
        return Radius


def triangle(b, h):
    area = 1/2 * b * h
    return area


def rectangle(w, h):
    area = w * h
    return area


def circle(r):
    area = pi * (r ** 2)
    return area


def plural(polygon, area):
    if area > 1:
        if polygon == "T" or polygon == "t":
            print(f"Area of this triangle is {area:.2f} square meters.")
        elif polygon == "R" or polygon == "r":
            print(f"Area of this rectangle is {area:.2f} square meters.")
        elif polygon == "C" or polygon == "c":
            print(f"Area of this circle is {area:.2f} square meters.")
    elif area <= 1:
        if polygon == "T" or polygon == "t":
            print(f"Area of this triangle is {area:.2f} square meter.")
        elif polygon == "R" or polygon == "r":
            print(f"Area of this rectangle is {area:.2f} square meter.")
        elif polygon == "C" or polygon == "c":
            print(f"Area of this circle is {area:.2f} square meter.")


def result(polygon):
    if polygon == "T" or polygon == "t":
        base, height = action(polygon)
        area = triangle(base, height)
        return area
    elif polygon == "R" or polygon == "r":
        width, height = action(polygon)
        area = rectangle(width, height)
        return area
    elif polygon == "C" or polygon == "c":
        radius = action(polygon)
        area = circle(radius)
        return area


polygon = input("(T)riangle (R)ectangle (C)ircle : ")
check_input(polygon)
