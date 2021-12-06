# the average amount of money per month
money = int(input("How much money do you spend per month: "))
# the number of miles per piece of money
n_miles = 2
# earned miles
miles_per_month = money * n_miles
# the distance between London and Paris
distance = 215
# how many months do you need to get
# a free trip from London to Paris and back
print(distance * 2 / miles_per_month)