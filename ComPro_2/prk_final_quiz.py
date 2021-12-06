from math import sqrt


def calculated_distance(x, y):
    distance = sqrt(x**2 + y**2)
    return distance


def check_isnumeric(coordinate):
    try:
        x, y = coordinate.split(" ")
        x = float(x)
        y = float(y)
        return True
    except ValueError:
        return False


coordinate = input("Input a coordinate: ")
kx = []
ky = []

while check_isnumeric(coordinate):
    x, y = coordinate.split(" ")
    kx.append(float(x))
    ky.append(float(y))
    coordinate = input("Input a coordinate: ")

print(f'Total {len(kx)} coordinates')
for i in range(len(kx)):
    print(f"X={kx[i]} Y={ky[i]} dist={calculated_distance(kx[i], ky[i]):.1f}")


def check_class_member(mileage):
    if mileage > 80000:
        return "Platinum Member"
    elif mileage > 20000:
        return "Gold Member"
    elif mileage > 5000:
        return "Silver Member"
    else:
        return "Basic Member"


name = input('Please enter your full name: ')
flight = 1
all_mileage = 0
mileage = int(input(f"Enter your mileage travelled in flight No.{flight}: "))
while mileage != -1:
    if mileage >= 0:
        all_mileage += mileage
        flight += 1
    mileage = int(input(f"Enter your mileage travelled in flight No.{flight}: "))

print()
print(f"Airline passenger: {name}")
print(f"Your accumulated mileage is: {all_mileage}")
print(f"You are a {check_class_member(mileage)}.")


