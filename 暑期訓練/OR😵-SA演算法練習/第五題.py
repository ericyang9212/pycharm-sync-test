import numpy as np

Xu = 100
Xl = -100
Tmax = 100
Tmin = 0.1
alpha = 0.99
ITERtemp = 3
R = 1
D = 30

def function(x): #Min
    z = 0
    for i in range(len(x)):
        z += x[i] ** 2  #Sphere Function: f(x) = Σ(xi^2)
    return z

CurrentSol = np.random.uniform(Xl, Xu, size=D)  # 初始解 [x1, x2,x3]
CurrentMinimize = function(CurrentSol)  # 初始能量
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

        TestMinimize = function(TestSol)
        delta_E = TestMinimize - CurrentMinimize

        if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / T):
            CurrentSol = TestSol
            CurrentMinimize = TestMinimize

            if CurrentMinimize < F_best:
                X_best = CurrentSol.copy()
                F_best = CurrentMinimize

    T *= alpha

print(f'Z* = {F_best:.0f}')
for i, x in enumerate(X_best, start=1):
    print(f"x{i:2d} = {x:.6f}")