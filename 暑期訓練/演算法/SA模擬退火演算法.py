import numpy as np
import matplotlib.pyplot as plt

def Minimize(x):     #模擬退火之最小化目標函數
    return np.sin(x) + np.cos(2 * x)

Xu = 6.28  # 決策變數的上界
Xl = 0  # 決策變數的下界
Tmax = 100  # 初始溫度
Tmin = 0.01  # 最終溫度
alpha = 0.99  # 溫度冷卻係數
ITERtemp = 3  # 單一溫度反覆運算次數
R = 1  # 鄰近範圍

CurrentSol = np.random.uniform(Xl, Xu)  # 隨機產生初始目前解
CurrentMinimize = Minimize(CurrentSol)  # 計算初始解的能量
X_best = CurrentSol  # 最佳解初始化
F_best = CurrentMinimize  # 最佳能量初始化
T = Tmax  # 當前溫度

plt.ion()  # 開啟互動模式讓 plt.pause() 能夠即時更新畫面
fig, ax = plt.subplots()
x_vals = np.linspace(Xl, Xu, 500)
y_vals = Minimize(x_vals)
ax.plot(x_vals, y_vals, label='Minimize(x)', color='blue')

point, = ax.plot([], [], 'ro', label='current point')  # 紅點：目前解
best_point, = ax.plot([], [], 'bo', label='best point')  # 藍點：最佳解
text = ax.text(0.025, 0.975, '', transform=ax.transAxes,fontsize=8,
               verticalalignment='top',
               bbox=dict(facecolor='white', edgecolor='black', alpha=0.8))

plt.title('Simulated Annealing Optimization')
plt.xlabel('x')
plt.ylabel('minimize(x)')
plt.grid(True)
plt.legend()
plt.tight_layout()

step = 0
while T > Tmin:      # 模擬退火主迴圈
    for i in range(ITERtemp):
        step += 1

        TestSol = CurrentSol - R + 2 * R * np.random.uniform()
        while TestSol < Xl or TestSol > Xu:  # 若超出邊界就重新產生
            TestSol = CurrentSol - R + 2 * R * np.random.uniform()

        TestMinimize = Minimize(TestSol)   # 計算新解的能量
        delta_E = TestMinimize - CurrentMinimize  # delta E =試探解-目前解

        # 蒙地卡羅準則：若變好就接受，變差也可能接受
        if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / T):
            CurrentSol = TestSol
            CurrentMinimize = TestMinimize

            if CurrentMinimize < F_best:   # 若試探解優於目前佳解，則更新試探解
                X_best = CurrentSol
                F_best = CurrentMinimize

        point.set_data([CurrentSol], [CurrentMinimize])
        best_point.set_data([X_best], [F_best])
        text.set_text(f'Step: {step}\nTemp: {T:.4f}\nX: {CurrentSol:.4f}\n'
                      f'f(X): {CurrentMinimize:.4f}\n'
                      f'Best X: {X_best:.4f}\nBest f(X): {F_best:.4f}')
        plt.pause(0.001)

    T *= alpha# 降溫

plt.ioff()  # 關閉互動模式

print(f'最佳解 X = {X_best:.4f}\n最小化目標函數 f(x) = {F_best:.4f}')
plt.show()