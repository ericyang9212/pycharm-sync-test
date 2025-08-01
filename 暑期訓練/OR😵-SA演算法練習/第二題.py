import numpy as np

Xu = 15
Xl = 0
Tmax = 100
Tmin = 0.1
alpha = 0.99
ITERtemp = 3
R = 1
D = 3

def f(x1,x2,x3):
    f = 4 * x1 + 5 * x2 + 3 * x3
    if x1 + x2 + 2 * x3 < 15:
        f -= (x1 + x2 + 2 * x3 + 15) * 12 * 2 #2 固定為懲罰值
    if 5 * x1 + 6 * x2 - 5 * x3 > 60:
        f -= (5 * x1 + 6 * x2 - 5 * x3 - 60) * 12 * 2
    if x1 + 3 * x2 + 5 * x3 > 40:
        f -= (x1 + 3 * x2 + 5 * x3 - 40) * 12 * 2
    return f

CurrentSol = np.random.uniform(Xl, Xu, size=D)  # 初始解 [x1, x2,x3]
CurrentMinimize = f(CurrentSol[0], CurrentSol[1],CurrentSol[2])  # 初始能量
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

        TestMinimize = f(TestSol[0],TestSol[1],TestSol[2])
        delta_E = TestMinimize - CurrentMinimize

        if delta_E > 0 or np.random.rand() < np.exp(delta_E / T):
            CurrentSol = TestSol
            CurrentMinimize = TestMinimize

            if CurrentMinimize > F_best:
                X_best = CurrentSol.copy()
                F_best = CurrentMinimize

    T *= alpha

print(f'Z* = {F_best:.0f}\nx1 = {X_best[0]:.0f}\nx2 = {X_best[1]:.0f}\nx3 = {X_best[2]:.0f}')