import numpy as np
import pandas as pd

# === Step 1. 讀取加工時間資料 ===
# Excel 表格內容為 20 jobs × 5 machines 的加工時間
List = pd.read_excel(r"/Users/ericyang/Desktop/Python File/排程/排程最佳化.xlsx",
    sheet_name="20j5m", usecols=range(1, 6))
List = List.values
R, C = List.shape  # R = 工作數 (jobs), C = 機台數 (machines)

# === Step 2. 適應函數：計算總工時（Makespan） ===
def Minimize(position):
    order = np.argsort(position)  # 根據粒子位置決定的工作排序
    machine_end_time = [0] * C    # 每台機器的結束時間
    job_end_time = [0] * R        # 每個工作的結束時間

    for job in order:
        for m_id in range(C):
            start = max(machine_end_time[m_id], job_end_time[job])
            end = start + List[job, m_id]
            machine_end_time[m_id] = end
            job_end_time[job] = end

    return max(job_end_time)  # 返回最後一個完成工作的時間（Makespan）

# === Step 3. 氣泡排序函數：根據位置值決定最終工作順序 ===
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

# === Step 4. 建立甘特圖資料（Gantt Chart） ===
def build_gantt_chart(order, List):
    R, C = List.shape
    Gantt = np.zeros([R, C * 2])  # 每台機器兩欄：開始時間、結束時間

    # 處理第一個工作
    job = order[0]
    Gantt[job, 0] = 0
    Gantt[job, 1] = List[job, 0]
    for m in range(1, C):
        Gantt[job, 2 * m] = Gantt[job, 2 * m - 1]
        Gantt[job, 2 * m + 1] = Gantt[job, 2 * m] + List[job, m]

    # 處理剩下的工作
    for idx in range(1, R):
        job = order[idx]
        prev_job = order[idx - 1]

        # 第一台機器
        Gantt[job, 0] = Gantt[prev_job, 1]
        Gantt[job, 1] = Gantt[job, 0] + List[job, 0]

        # 後續機器
        for m in range(1, C):
            prev_machine_end = Gantt[job, 2 * m - 1]
            last_job_same_machine_end = Gantt[prev_job, 2 * m + 1]
            Gantt[job, 2 * m] = max(prev_machine_end, last_job_same_machine_end)
            Gantt[job, 2 * m + 1] = Gantt[job, 2 * m] + List[job, m]

    return Gantt

# === Step 5. PSO參數設定 ===
Xu = 6.28      # 位置最大值
Xl = 0         # 位置最小值
m = 30         # 粒子數
W_init = 1     # 初始慣性權重
W_final = 0.4  # 最終慣性權重
C1 = 2         # 個體學習因子
C2 = 2         # 群體學習因子
V_max = 1      # 速度最大值
V_min = -1     # 速度最小值
Iter_final = 50  # 最大迭代次數
W = W_init
# 初始化位置與速度
x = np.random.uniform(Xl, Xu, (m, R))       # 隨機位置
v = np.random.uniform(V_min, V_max, (m, R)) # 隨機速度

# 初始化個體最佳與群體最佳
pbest = x.copy()
pbest_val = np.array([Minimize(p) for p in pbest])
gbest = x[np.argmin(pbest_val)]
gbest_val = np.min(pbest_val)
print(gbest_val)

history_gbest = []  # 儲存歷代最佳值變化

# === Step 6. PSO 主迴圈 ===
for iter in range(Iter_final):

    for i in range(m):
        r1 = np.random.rand(R)
        r2 = np.random.rand(R)

        # 更新速度與位置
        v[i] = W * v[i] + C1 * r1 * (pbest[i] - x[i]) + C2 * r2 * (gbest - x[i])
        v[i] = np.clip(v[i], V_min, V_max)
        x[i] = x[i] + v[i]
        x[i] = np.clip(x[i], Xl, Xu)

        # 評估適應度
        fit = Minimize(x[i])
        if fit < pbest_val[i]:
            pbest[i] = x[i]
            pbest_val[i] = fit
            if fit < gbest_val:
                gbest = x[i]
                gbest_val = fit

    W = W_init - (iter / Iter_final) * (W_init - W_final)  # 動態調整慣性權重

    history_gbest.append(gbest_val)

best_order = bubbleSort(gbest)              # 將最佳位置轉為工作順序

print(f"\n最佳工序順序：\n{best_order}")
print(f"最短總工時（Makespan）：{gbest_val:.2f}")


all_orders = [bubbleSort(x[i]) for i in range(m)]
all_makespans = [Minimize(x[i]) for i in range(m)]

for i in range(m):
    print(f"粒子 {i+1:2d} 的排序：{all_orders[i]}, {all_makespans[i]:.2f}")