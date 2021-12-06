def rectangle_area_and_perimeter(x, y):
    a = x * y
    b = x*2 + y*2
    return a, b


def read_rectangle():
    e = float(input("Enter rectangle length: "))
    c = float(input("Enter rectangle width: "))
    return e, c


length, width = read_rectangle() # 10, 20
area, peri = rectangle_area_and_perimeter(length, width)
print(area)
print(peri)
