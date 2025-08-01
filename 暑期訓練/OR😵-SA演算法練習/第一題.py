import numpy as np

Xu = 10
Xl = 0
Tmax = 100
Tmin = 0.1
alpha = 0.99
ITERtemp = 3
R = 1
D = 2

def f(x1, x2): #Max
    f = 3 * x1 + 5 * x2 #目標函數
    if x1 > 4:
        f -= (x1 - 4) * 3 * 2
    if 2 * x2 > 12:
        f -= (2 * x2 - 12) * 5 * 2
    if 3 * x1 + 2 * x2 > 18:
        f -= (3 * x1 + 2 * x2 - 18) * 8 * 2
    return f

CurrentSol = np.random.uniform(Xl, Xu, size=D)  # 初始解 [x1, x2]
CurrentMinimize = f(CurrentSol[0], CurrentSol[1])  # 初始能量
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

        TestMinimize = f(TestSol[0], TestSol[1])
        delta_E = TestMinimize - CurrentMinimize

        if delta_E > 0 or np.random.rand() < np.exp(delta_E / T):
            CurrentSol = TestSol
            CurrentMinimize = TestMinimize

            if CurrentMinimize > F_best:
                X_best = CurrentSol.copy()
                F_best = CurrentMinimize

    T *= alpha

print(f'Z* = {F_best:.0f}\nx1 = {X_best[0]:.0f}\nx2 = {X_best[1]:.0f}')