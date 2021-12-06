# Quiz1
x = int(input('Enter the number: '))
for x in range(x):
    print(f"{x + 1} squared is {(x + 1)**2}.")

# Quiz2
salary_month = int(input("Enter salary (Baht/Month): "))
salary_year = salary_month * 12
if salary_year < 150000:
    print("You don't have to pay tax.")
elif salary_year < 300000:
    tax = (10 / 100) * salary_year
    print(f"You have to pay tax for {tax} baht.")
elif salary_year < 600000:
    tax = (20 / 100) * salary_year
    print(f"You have to pay tax for {tax} baht.")
else:
    tax = (30 / 100) * salary_year
    print(f"You have to pay tax for {tax} baht.")

# Quiz3
a, b = input("Please enter number a and b: ").split(' ')
for x in range(int(a), int(b) + 1):
    print(x, end=" ")
