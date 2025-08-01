import numpy as np
import matplotlib.pyplot as plt

mean = float(input("Please enter mean: "))
std = float(input("Please enter stander deviation: "))
print(mean, std)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def normal(x):
    return (1 / (np.sqrt(2 * np.pi) * std)) * np.exp(-0.5 * ((x - mean) / std) ** 2)
#生成1000數值從範圍-6~6 & -3~3
x_sigmoid = np.linspace(-6, 6, 1000)
y_sigmoid = sigmoid(x_sigmoid)
x_normal = np.linspace(-3, 3, 1000)
y_normal = normal(x_normal)
#創建圖形
#Sigmoid Function
fig, (ax_Left , ax_right) = plt.subplots(1 , 2,figsize=(10,5))
ax_Left.plot(x_sigmoid , y_sigmoid )
ax_Left.set_title('Sigmoid function')
ax_Left.set_xlabel('X')
ax_Left.set_ylabel('Y')
ax_Left.set_xlim(-6, 6)
ax_Left.set_ylim(-0.5, 1.5)
#Normal Distribution
ax_right.plot(x_normal , y_normal )
ax_right.set_title('Normal function')
ax_right.set_xlabel('X')
ax_right.set_ylabel('Y')
ax_right.set_xlim(-3, 3)


#Draw a Lovely Heart
t = np.arange(0, 6.28, 0.01)
x1 = 16 * np.sin(t) ** 3
x2 = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
plt.figure(figsize=(5,5))
plt.plot(x1,x2)
plt.show()




