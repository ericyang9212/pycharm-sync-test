import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# === 1. 讀取資料 ===
# 從 Excel 檔案讀取指定工作表中的第 2~4 欄（X1, X2, 目標 t）
data = pd.read_excel(r"/Users/ericyang/Desktop/Python File/Python_Homework/Homework4.xlsx",
                     sheet_name="HW_4", usecols=range(1, 4))
data = data.values  # 將 DataFrame 轉為 numpy 陣列，方便數值運算
print(data)

m = len(data)             # 樣本數（資料筆數）
bias = np.ones(m)         # 建立一個全為 1 的 bias 向量（用來模擬閾值）
X1 = data[:, 0]           # X1 為第 1 欄（橫軸）
X2 = data[:, 1]           # X2 為第 2 欄（縱軸）
t = data[:, 2]            # t 為第 3 欄（實際標籤，0 或 1）

eta = 1                             # 學習率（每次調整權重的幅度）
w = np.array([0.0, 0.0, 1.1])       # 初始權重：bias 對應 w0，其餘為 X1, X2 對應 w1, w2
max_iter = 50                      # 最多訓練 50 輪（epoch）
W_best = w.copy()                  # 儲存分類最好的權重值
CCount_Max = 0                     # 儲存分類正確數最多的輪數結果

# 將 bias、X1、X2 合併為一個矩陣 X_total（每一筆為一個輸入向量 x）
X_total = np.c_[bias, X1, X2]  # shape: (m, 3)，每筆包含 bias 項 + 兩個特徵

# === 畫圖函數 ===
def draw(data, weights):
    plt.cla()  # 清除前一張圖
    plt.title("Perceptron")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)

    # 根據目標值 t 畫點：t=0 為藍圈、t=1 為紅叉
    for i in range(len(data)):
        x1, x2, label = data[i]
        if label == 0:
            plt.scatter(x1, x2, c='b', marker='o', s=30, label='Class 0' if i == 0 else "")
        else:
            plt.scatter(x1, x2, c='r', marker='x', s=30, label='Class 1' if i == 0 else "")

    # 根據 w0 + w1*X1 + w2*X2 = 0 推導出 X2 的解，畫出分界線
    if abs(weights[2]) > 0:
        x_vals = np.array([-3, 3])
        y_vals = -(weights[1] / weights[2]) * x_vals - (weights[0] / weights[2]) #w_0 + w_1 x + w_2 y = 0 導出 y 的解
        plt.plot(x_vals, y_vals, 'k-')  # 黑色實線表示 decision boundary

    plt.pause(0.05)  # 加入短暫延遲方便觀察動畫

plt.ion()  # 開啟即時繪圖

# === 訓練感知機 ===
for epoch in range(max_iter):  # 重複訓練 max_iter 輪
    print(f"\n==========Ieration {epoch+1}==========")
    #CCount = 0  # 每輪記錄正確分類的資料數

    for i in range(m):  # 每筆資料做一次訓練
        x = X_total[i]        # 第 i 筆輸入向量（含 bias）
        target = t[i]         # 該筆的正確標籤值
        net = np.inner(w, x)  # 計算加權總和：感知機的輸出前值 net
        y = 1 if net > 0 else 0  # 根據 net 決定輸出值：超過 0 則分類為 1，否則為 0

        # 檢查是否分類錯誤，錯則更新權重
        if y != target:
            if target == 1:
                w = w + eta * x  # 若應該是 1 卻預測成 0，要增加 w
                print(f"Data: {i + 1} Modify Weight +")
            else:
                w = w - eta * x  # 若應該是 0 卻預測成 1，要減少 w
                print(f"Data: {i + 1} Modify Weight -")
        else:
            print(f"Data: {i + 1} OK")  # 表示這筆資料被正確分類

        print("w =", w)  # 輸出目前的權重
        draw(data, w)    # 畫圖顯示目前分類狀況

        CCount = 0  # 每輪記錄正確分類的資料數
        for i in range(m):  # 每筆資料做一次訓練
            x = X_total[i]  # 第 i 筆輸入向量（含 bias）
            target = t[i]  # 該筆的正確標籤值
            net = np.inner(w, x)  # 計算加權總和：感知機的輸出前值 net
            y = 1 if net > 0 else 0
            if y == target:
                CCount += 1  # 正確分類則累加

        # 若本輪正確分類數大於歷史最高，就更新最佳權重
        if CCount > CCount_Max:
            W_best = w.copy()
            CCount_Max = CCount

    # 若全部資料都正確分類，提前結束訓練
    if CCount == m:
        break

print("最佳權重 =", W_best)

plt.ioff()  # 關閉即時繪圖
plt.show()

# === 將最佳權重存成 Excel 檔 ===
df_result = pd.DataFrame(W_best.reshape(1, -1), columns=["w0", "w1", "w2"])
df_result.to_excel("HW4_BestWeights.xlsx", index=False)  # 儲存為 Excel 檔案