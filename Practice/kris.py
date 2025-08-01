import numpy as np
import copy
import matplotlib.pyplot as plt
#定義目標函數
def f(x):
    return np.sin(x) + np.cos(2 * x)
#參數設定
XU = 6.28
XL = 0
m = 5
Winit = 1
Wfinal = 0.4
c1 = 2
c2 = 2
vinit = 0
vmax = 1
vmin = -1
k=0
Iterfinal = 100
#設定一個空矩陣 儲存粒子位置跟速度
x_now = []
for i in range(m):
    xn = np.random.uniform(XL, XU)
    vel = vinit
    x_now.append([xn, vel])
p_best = copy.deepcopy(x_now)#個體最佳
g_best = min(p_best, key=lambda p: f(p[0]))#全域最佳
W = Winit
#圖表
plt.ion()
fig, ax = plt.subplots()
x_vals = np.linspace(XL, XU, 300)
y_vals = f(x_vals)
line, = ax.plot(x_vals, y_vals, label='f(x)')
scat = ax.scatter([], [], color='red', label='try')
best_point, = ax.plot([], [], 'bo', label='best')
ax.set_title("simulate")
ax.set_xlim(XL, XU)
ax.set_ylim(-2, 2)
ax.legend()
g_best_history=[]
#主迴圈
for Iter in range(Iterfinal):
    k+=1
    W = Winit-(Winit-Wfinal)*k/Iterfinal
    for i in range(m):
        xi = x_now[i][0]
        vi = x_now[i][1]
        pi = p_best[i][0]
        gi = g_best[0]
        #更新速度與位置
        vi =W*vi+c1*np.random.rand()*(pi-xi)+c2*np.random.rand()*(gi-xi)
        vi = np.clip(vi, vmin, vmax)
        xi += vi
        xi = np.clip(xi, XL, XU)
        #更新粒子位置
        x_now[i][0] = xi
        x_now[i][1] = vi
        #更新個體最佳
        if f(xi) < f(p_best[i][0]):
            p_best[i][0] = xi
            p_best[i][1] = vi
        #從個人最佳取最小為全域最佳
        g_best = min(p_best, key=lambda p: f(p[0]))
        g_best_history.append(copy.deepcopy(g_best))

    #當代全域最佳解
    print(f"\n第{Iter+1:3d}代 全域最佳解: x = {g_best[0]:.4f}, f(x) = {f(g_best[0]):.6f}")
    #粒子的位置 速度 個人最佳解
    for j, (now, best) in enumerate(zip(x_now, p_best)):
        print(f"  粒子 {j+1}: x = {now[0]:.4f}, v = {now[1]:.4f}, 個人最佳 = {f(best[0]):.6f}")
    #當代權重
    print(f"W = {W:.4f}")
    #圖表
    particle_positions = [p[0] for p in x_now]
    particle_values = [f(p[0]) for p in x_now]
    scat.set_offsets(np.c_[particle_positions, particle_values])
    best_point.set_data([g_best[0]], [f(g_best[0])])
    ax.set_title(f"{Iter+1} ")
    plt.pause(0.05)
plt.ioff()
plt.show()