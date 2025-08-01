import numpy as np
import matplotlib.pyplot as plt

def Minimize(x):
    return np.sin(x) + np.cos(2 * x)

Xu = 6.28
Xl = 0
Tmax = 100
Tmin = 0.01
alpha = 0.99
ITERtemp = 3
R = 1

CurrentSol = np.random.uniform(Xl, Xu)
CurrentMini = Minimize(CurrentSol)
X_best = CurrentSol
F_best = CurrentMini
T = Tmax

plt.ion()
fig, ax = plt.subplots()
X_vals = np.linspace(Xl, Xu, 500)
Y_vals = Minimize(X_vals)
ax.plot(X_vals, Y_vals, label='Minimize(x)', color='blue')

point, = ax.plot([],[],"ro" , label='Current point')
best_point, = ax.plot([],[],"bo", label='Best point')
text = ax.text(0.025 , 0.975 , "" , transform=ax.transAxes , fontsize = 8,
               verticalalignment='top', bbox = dict(facecolor = "white", edgecolor = "black",alpha=0.8))

plt.title("Simulated Annealing Optimization")
plt.xlabel("x")
plt.ylabel("minimize(x)")
plt.grid(True)
plt.legend()
plt.tight_layout()

step = 0
while T > Tmin:
    for i in range(ITERtemp):
        step += 1

        TestSol = CurrentSol - R + 2 * R * np.random.rand()
        while TestSol < Xl or TestSol > Xu:
            TestSol = CurrentSol - R + 2 * R * np.random.rand()

        TestMini = Minimize(TestSol)
        delta_E = TestMini - CurrentMini

        if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / T)
            CurrentSol = TestSol
            CurrentMini = TestMini

            if CurrentMini < F_best:
                X_best = CurrentSol
                F_best = CurrentMini

        point.set_data([CurrentSol],[CurrentMini])
        best_point.set_data([X_best],[F_best])
        text.set_text(f'step: {step}\nTemp: {T:.4f}\nX:{CurrentSol:.4f}\n'
                      f'f(x): {CurrentMini:.4f}\n'
                      f'Best x: {X_best:.4f}\nBest f(x): {F_best:.4f}')
        plt.pause(0.01)
    T *= alpha
plt.ioff()

print(f'最佳解 X = {X_best:.4f}\n最小化目標函數 f(x) = {F_best:.4f}')
plt.show()