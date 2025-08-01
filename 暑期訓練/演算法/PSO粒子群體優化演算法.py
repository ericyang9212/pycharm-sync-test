import numpy as np
import matplotlib.pyplot as plt

# 目標函數
def Minimize(x):
    return np.sin(x) + np.cos(2 * x)

Xu = 6.28     # 上界
Xl = 0        # 下界
m = 5         # 粒子數量
W_init = 1    # 初始慣性權重
W_final = 0.4 # 終止慣性權重
C1 = 2        # 認知參數
C2 = 2        # 社群參數
V_max = 1     # 最大速度
V_min = -1    # 最小速度
Iter_final = 10  # 總反覆運算次數

x = np.random.uniform(Xl, Xu, m)        # 初始位置
v = np.random.uniform(V_min, V_max, m)  # 初始速度
pbest = x.copy()
pbest_val = Minimize(x)
gbest = x[np.argmin(pbest_val)]
gbest_val = np.min(pbest_val)

history_gbest = [] #設定一個空矩陣 儲存粒子位置跟速度

plt.ion()
fig, ax = plt.subplots()
x_vals = np.linspace(Xl, Xu, 500)
y_vals = Minimize(x_vals)
ax.plot(x_vals, y_vals, label='Minimize(x)', color='blue')

point, = ax.plot([], [], 'ro', label='current points')      # 所有粒子紅點
best_point, = ax.plot([], [], 'bo', label='global best')    # 群體最佳藍點
text = ax.text(0.025, 0.975, '', transform=ax.transAxes, fontsize=8,
               verticalalignment='top', bbox=dict(facecolor='white', edgecolor='black', alpha=0.8))

plt.title('Particle Swarm Optimization')
plt.xlabel('x')
plt.ylabel('Minimize(x)')
plt.grid(True)
plt.legend()
plt.tight_layout()

for iter in range(Iter_final):

    W = W_init - (iter / Iter_final) * (W_init - W_final) # 更新慣性權重（線性遞減）

    for i in range(m):
        r1 = np.random.rand()
        r2 = np.random.rand()

        # 更新速度與位置
        v[i] = (W * v[i] +
                C1 * r1 * (pbest[i] - x[i]) +
                C2 * r2 * (gbest - x[i]))
        v[i] = np.clip(v[i], V_min, V_max)

        x[i] = x[i] + v[i]
        if x[i] > Xu:
            x[i] = Xu
            v[i] = V_max
        elif x[i] < Xl:
            x[i] = Xl
            v[i] = V_min

        # 計算適應值並更新個人最佳與群體最佳
        fit = Minimize(x[i])
        if fit < pbest_val[i]:
            pbest[i] = x[i]
            pbest_val[i] = fit
            if fit < gbest_val:
                gbest = x[i]
                gbest_val = fit

    history_gbest.append(gbest_val)

    # ===== 更新動畫繪圖 =====
    point.set_data(x, Minimize(x))             # 所有粒子紅點
    best_point.set_data([gbest], [gbest_val])      # 全域最佳藍點
    text.set_text(f'Iter: {iter+1}\nBest Value: {gbest_val:.4f}')
    plt.pause(0.05)

print(f"最佳解位置 gbest = {gbest:.4f}\n最佳解能量值 Minimize(gbest) = {gbest_val:.4f}")

plt.ioff()
plt.show()