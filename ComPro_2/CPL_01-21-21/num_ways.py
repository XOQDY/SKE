import numpy as np
# def num_ways_with_1_2_to_get(n):
#     if n < 2:
#         return 1
#     return num_ways_with_1_2_to_get(n - 1) + num_ways_with_1_2_to_get(n - 2)
#
# print(num_ways_with_1_2_to_get(2))
z = 5
i = 1
def fun(x,y=0.9):
    z = x + y
    print('z =', z)
x = 6322773284
while i <= 8:
    x //= 10
    i +=1
fun(x,4)

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a[np.ndim(a)-1:, np.shape(a)[0]])
