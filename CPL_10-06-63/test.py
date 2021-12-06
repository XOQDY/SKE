import matplotlib.pyplot as plt

x = [0,1,2,3,4]
y = [10,15,20,25,50]

plt.plot(x, y, color='green',marker='o', linestyle='dashed', linewidth=2, markersize=12)
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('test.png')
plt.show()