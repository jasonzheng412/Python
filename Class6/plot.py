import matplotlib.pyplot as plt

list_x = []
for i in range (200):
    list_x.append(i * 0.1 - 10)

list_y = []
for x in list_x:
    list_y.append(x ** x)

plt.plot(list_x, list_y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('my function plot')

#plt.show()
plt.savefig('plot.png')