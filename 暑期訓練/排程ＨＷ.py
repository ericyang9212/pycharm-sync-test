import numpy as np
import pandas as pd
#this is for test
# === 讀取機台加工時間資料（20 jobs × 5 machines） ===
List = pd.read_excel(r"/Users/ericyang/Desktop/Python File/排程/排程最佳化.xlsx",
                     sheet_name="20j5m", usecols=range(1, 6))  # 讀取加工時間矩陣
List = List.values
R, C = List.shape  # R：工作數量（20），C：機台數量（5）

# === 適應函數：計算總工時（makespan） ===
def Minimize(position):
    order = np.argsort(position)  # 將浮點位置向量轉換成工作順序
    machine_end_time = [0] * C    # 每台機台的結束時間初始化為0
    job_end_time = [0] * R        # 每個工作的結束時間初始化為0

    for job in order:             # 按照排序後的順序依序排程每個工作
        for m_id in range(C):     # 每個工作依序經過各台機台
            start = max(machine_end_time[m_id], job_end_time[job])  # 開始時間為機台與前段加工完成的最大值
            end = start + List[job, m_id]                            # 完成時間 = 開始 + 該工作在該機台的加工時間
            machine_end_time[m_id] = end                             # 更新該機台的結束時間
            job_end_time[job] = end                                  # 更新該工作的結束時間

    return max(job_end_time)  # 回傳最後一個工作完成的時間，即為 Makespan（總工時）

# === PSO參數設定 ===
Xu = 6.28      # 粒子位置的上界（數值本身無意義，只是為了產生排序順序）
Xl = 0         # 粒子位置的下界
m = 30         # 粒子數量（族群大小）
W_init = 1     # 初始慣性權重
W_final = 0.4  # 最終慣性權重（逐步下降）
C1 = 2         # 認知學習係數（個體經驗）
C2 = 2         # 社會學習係數（群體經驗）
V_max = 1      # 最大速度
V_min = -1     # 最小速度
Iter_final = 50  # 最大迭代次數

# === 粒子初始化 ===
x = np.random.uniform(Xl, Xu, (m, R))         # 隨機初始化每個粒子的位置（浮點向量）
v = np.random.uniform(V_min, V_max, (m, R))   # 隨機初始化每個粒子的速度

pbest = x.copy()                              # 個體最佳位置初始化為初始位置
pbest_val = np.array([Minimize(p) for p in pbest])  # 計算每個粒子的初始適應值
gbest = x[np.argmin(pbest_val)]               # 族群中的最佳粒子（global best）
gbest_val = np.min(pbest_val)                 # 全域最佳適應值

history_gbest = []  # 儲存每一代的最佳適應值（作圖用）

# === PSO 主迴圈 ===
for iter in range(Iter_final):
    # 線性調整慣性權重（W由大到小）
    W = W_init - (iter / Iter_final) * (W_init - W_final)

    for i in range(m):  # 對每個粒子做更新
        r1 = np.random.rand(R)  # 認知亂數向量
        r2 = np.random.rand(R)  # 社會亂數向量

        # 更新速度公式（包含慣性項、認知項、社會項）
        v[i] = W * v[i] + C1 * r1 * (pbest[i] - x[i]) + C2 * r2 * (gbest - x[i])
        v[i] = np.clip(v[i], V_min, V_max)  # 限制速度在區間內

        # 更新位置
        x[i] = x[i] + v[i]
        x[i] = np.clip(x[i], Xl, Xu)  # 限制位置在區間內

        # 計算新位置的適應值
        fit = Minimize(x[i])

        # 更新個體最佳與全域最佳
        if fit < pbest_val[i]:
            pbest[i] = x[i]
            pbest_val[i] = fit
            if fit < gbest_val:
                gbest = x[i]
                gbest_val = fit

    history_gbest.append(gbest_val)  # 儲存每代的最佳值

# === 輸出最佳結果 ===
print(f"\n最佳工作順序：\n{np.argsort(gbest)}\n最短總工時（Makespan）：\n{gbest_val:.2f}")