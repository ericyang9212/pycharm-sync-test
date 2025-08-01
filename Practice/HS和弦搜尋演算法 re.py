import numpy as np
import random


def f(x):
    return np.sin(x) + np.cos(2 * x)

def bubblesort(HM):
    n = len(HM)
    for i in range(n):
        switch = False
        for j in range(n-i-1):
            if HM[j][1] > HM[j+1][1]:
                HM[j],HM[j+1] = HM[j+1],HM[j]
                switch = True
        if not switch:
            break
    return HM

Xu = 6.28
Xl = 0
HMS = 5
HMCR = 0.6
PAR = 0.4
BW = (Xu - Xl) * 0.05
ITER = 20

HM = [[np.random.uniform(Xl,Xu), 0] for k in range(HMS)]

for i in range(HMS):
    HM[i][1] = f(HM[i][0])

    for t in range(ITER):
        r1 = np.random.rand()

        if r1 < HMCR:
            x_selected = random.choices(HM)[0][0]  # 選取一個 x
            x_new = x_selected
            r2 = np.random.rand()
            if r2 < PAR:
                x_new += np.random.uniform(-BW, BW)
        else:
            x_new = np.random.uniform(Xl, Xu)

        x_new = np.clip(x_new, Xl, Xu)
        f_new = f(x_new)

        HM = bubblesort(HM)
        if f_new < HM[-1][1]:
            HM[-1] = [x_new, f_new]

HM = bubblesort(HM)

result = np.array(HM)
print(result)