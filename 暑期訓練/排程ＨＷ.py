import numpy as np
import pandas as pd

# === 讀取加工時間資料 ===
List = pd.read_excel(r"/Users/ericyang/Desktop/Python File/排程/排程最佳化.xlsx",
                     sheet_name="20j5m", usecols=range(1, 6))
List = List.values
R, C = List.shape

# === 適應函數：計算總工時（Makespan） ===
def Minimize(position):
    order = np.argsort(position)  # 浮點數轉換成工作順序
    machine_end_time = [0] * C
    job_end_time = [0] * R

    for job in order:
        for m_id in range(C):
            start = max(machine_end_time[m_id], job_end_time[job])
            end = start + List[job, m_id]
            machine_end_time[m_id] = end
            job_end_time[job] = end

    return max(job_end_time)

# === 氣泡排序函式（由小到大） ===
def bubbleSort(position):
    order = [(i, val) for i, val in enumerate(position)]
    n = len(order)
    for i in range(n):
        switched = False
        for j in range(n - i - 1):
            if order[j][1] > order[j + 1][1]:
                order[j], order[j + 1] = order[j + 1], order[j]
                switched = True
        if not switched:
            break
    sorted_index = [item[0] for item in order]
    return sorted_index

# === 根據工作順序建立甘特圖資料（開始/結束時間矩陣） ===
def build_gantt_chart(order, List):
    R, C = List.shape
    Gantt = np.zeros([R, C * 2])

    job = order[0]
    Gantt[job, 0] = 0
    Gantt[job, 1] = List[job, 0]

    for m in range(1, C):
        Gantt[job, 2 * m] = Gantt[job, 2 * m - 1]
        Gantt[job, 2 * m + 1] = Gantt[job, 2 * m] + List[job, m]

    for idx in range(1, R):
        job = order[idx]
        prev_job = order[idx - 1]

        Gantt[job, 0] = Gantt[prev_job, 1]
        Gantt[job, 1] = Gantt[job, 0] + List[job, 0]

        for m in range(1, C):
            prev_machine_end = Gantt[job, 2 * m - 1]
            last_job_same_machine_end = Gantt[prev_job, 2 * m + 1]

            Gantt[job, 2 * m] = max(prev_machine_end, last_job_same_machine_end)
            Gantt[job, 2 * m + 1] = Gantt[job, 2 * m] + List[job, m]

    return Gantt

# === PSO 參數設定 ===
Xu = 6.28
Xl = 0
m = 30
W_init = 1
W_final = 0.4
C1 = 2
C2 = 2
V_max = 1
V_min = -1
Iter_final = 50

x = np.random.uniform(Xl, Xu, (m, R))
v = np.random.uniform(V_min, V_max, (m, R))
pbest = x.copy()
pbest_val = np.array([Minimize(p) for p in pbest])
gbest = x[np.argmin(pbest_val)]
gbest_val = np.min(pbest_val)

history_gbest = []

# === PSO 主迴圈 ===
for iter in range(Iter_final):
    W = W_init - (iter / Iter_final) * (W_init - W_final)

    for i in range(m):
        r1 = np.random.rand(R)
        r2 = np.random.rand(R)

        v[i] = W * v[i] + C1 * r1 * (pbest[i] - x[i]) + C2 * r2 * (gbest - x[i])
        v[i] = np.clip(v[i], V_min, V_max)
        x[i] = x[i] + v[i]
        x[i] = np.clip(x[i], Xl, Xu)

        fit = Minimize(x[i])
        if fit < pbest_val[i]:
            pbest[i] = x[i]
            pbest_val[i] = fit
            if fit < gbest_val:
                gbest = x[i]
                gbest_val = fit

    history_gbest.append(gbest_val)

# === 最終輸出：排序 + 甘特圖 ===
best_order = bubbleSort(gbest)  # 用氣泡排序決定最終排程順序
Gantt = build_gantt_chart(best_order, List)  # 建立甘特圖

print(f"\n最佳工序：\n{best_order}\n最短總工時（Makespan）：\n{gbest_val:.2f}")
print(Gantt)