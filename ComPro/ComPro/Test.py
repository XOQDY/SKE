i = int(input("The input format: "))
for i in range(2, i):
    if i % 2 == 0:
        print(i)

input_string = input("Input string: ")
count = 0
for letter in input_string:
    if letter == "a":
        count += 1
print(count)
