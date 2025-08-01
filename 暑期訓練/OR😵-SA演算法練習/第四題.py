import numpy as np

Xu = 10
Xl = 0
Tmax = 100
Tmin = 0.1
alpha = 0.99
ITERtemp = 3
R = 1
D = 4

def f(x1,x2,x3,x4):
    f = 5 * x1 + 6 * x2 + 9 * x3 + 8 * x4
    if x1 + 2 * x2 + 3 * x3 + 4 * x4 > 5:
        f -= (x1 + 2 * x2 + 3 * x3 + 4 * x4 - 5) * 28 * 1 #2 固定為懲罰值
    if x1 + x2 + 2 * x3 + 3 * x4 > 3:
        f -= (x1 + x2 + 2 * x3 + 3 * x4 - 3) * 28 * 1
    return f

CurrentSol = np.random.uniform(Xl, Xu, size=D)  # 初始解 [x1, x2,x3]
CurrentMinimize = f(CurrentSol[0], CurrentSol[1],CurrentSol[2],CurrentSol[3])  # 初始能量
X_best = CurrentSol.copy()
F_best = CurrentMinimize
T = Tmax
step = 0

while T > Tmin:
    for i in range(ITERtemp):
        step += 1
        TestSol = CurrentSol - R + 2 * R * np.random.rand(D)
        while np.any(TestSol < Xl) or np.any(TestSol > Xu):
            TestSol = CurrentSol - R + 2 * R * np.random.rand(D)

        TestMinimize = f(TestSol[0],TestSol[1],TestSol[2],TestSol[3])
        delta_E = TestMinimize - CurrentMinimize

        if delta_E > 0 or np.random.rand() < np.exp(delta_E / T):
            CurrentSol = TestSol
            CurrentMinimize = TestMinimize

            if CurrentMinimize > F_best:
                X_best = CurrentSol.copy()
                F_best = CurrentMinimize

    T *= alpha

print(f'Z* = {F_best:.0f}\nx1 = {X_best[0]:.0f}\nx2 = {X_best[1]:.0f}\nx3 = {X_best[2]:.0f}'
      f'\nx4 = {X_best[3]:.0f}')