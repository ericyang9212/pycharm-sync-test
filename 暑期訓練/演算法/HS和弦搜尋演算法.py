import numpy as np
import random

# 目標函數：這裡我們希望最小化 f(x) = sin(x) + cos(2x)
def f(x):
    return np.sin(x) + np.cos(2 * x)

# 氣泡排序函數，根據 f(x) 的值對 HM 中的解進行排序（由小到大）
def bubbleSort(HM):
    n = len(HM)
    for i in range(n):
        switch = False
        for j in range(n - i - 1):
            if HM[j][1] > HM[j + 1][1]:  # 如果前一項比後一項大，就交換
                HM[j], HM[j + 1] = HM[j + 1], HM[j]
                switch = True
        if not switch:
            break  # 如果這一輪沒發生交換，代表已經排好序了，提早結束
    return HM

# ========== 和弦搜尋參數設定 ==========
Xu = 6.28
Xl = 0
HMS = 5
HMCR = 0.6
PAR = 0.4        # 微調率（Pitch Adjusting Rate）
BW = (Xu - Xl) * 0.05  # 微調範圍（Bandwidth）
ITER = 20        # 演化次數

# ========== 初始化和弦記憶庫 HM ==========
# 產生 HMS 個隨機解，每個格式為 [x, f(x)]
HM = [[np.random.uniform(Xl, Xu), 0] for k in range(HMS)]
for i in range(HMS):
    HM[i][1] = f(HM[i][0])  # 計算每個解的目標函數值

# ========== 開始迭代優化 ==========
for t in range(ITER):
    r1 = np.random.rand()
    if r1 <= HMCR:
        # 從記憶庫中隨機選一個解的 x 值作為基礎
        x_new = random.choice(HM)[0]
        r2 = np.random.rand()
        if r2 <= PAR:
            r3 = np.random.rand()
            # 有機會進行微調：加上一個在 [-BW, BW] 區間內的隨機擾動
            x_new = x_new - BW + r3 * 2 * BW
    else:
        # 否則隨機產生新的 x 值
        x_new = np.random.uniform(Xl, Xu)

    # 確保新的 x 不會超出邊界
    x_new = np.clip(x_new, Xl, Xu)
    f_new = f(x_new)  # 計算新解的 f(x)

    # 對 HM 根據 f(x) 值進行排序（由小到大）
    HM = bubbleSort(HM)
    worst_idx = -1  # 最差解的索引（位於最後一個位置）

    # 如果新解比最差解還好，就取代最差解
    if f_new < HM[worst_idx][1]:
        HM[worst_idx] = [x_new, f_new]

# 最後再排序一次 HM，確保最好的解在前面
HM = bubbleSort(HM)

# 將結果轉為 NumPy 陣列並印出
result = np.array(HM)
print(result)