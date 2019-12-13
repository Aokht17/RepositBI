import matplotlib.pyplot as plt
x = [i for i in range(10)]
y = [j**2 for j in x]

plt.title('line plot')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.plot(x, y, color='green')


plt.savefig('a')