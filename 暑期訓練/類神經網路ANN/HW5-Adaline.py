# 載入必要套件
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# === 1. 讀取資料 ===
data = pd.read_excel(r"/Users/ericyang/Desktop/Python File/Python_Homework/Homework5.xlsx",
    sheet_name="HW_5_MP_Linear", usecols=range(1, 3))  # 讀取 Excel 檔案中第2~3欄的資料（不含標題列）
data = data.values  # 轉換為 numpy 陣列方便運算

# === 2. 資料前處理 ===
m = len(data)           # 資料筆數
X1 = data[:, 0]         # 取出第一欄作為輸入特徵 X1
T = data[:, 1]          # 取出第二欄作為目標值 T
bias = np.ones(m)       # 建立 bias 項（全為 1 的欄位）
X_total = np.c_[bias, X1]  # 合併 bias 和 X1 形成訓練資料，每筆資料為 [1, X1]

# === 3. 模型參數初始化 ===
eta = 0.01                     # 學習率
W = np.array([10.0, -1.0])     # 初始權重 [bias, weight for X1]
max_iter = 50                  # 最大訓練次數
W_best = W.copy()              # 儲存最佳權重
MSE_best = float("inf")        # 初始最佳均方誤差設為無限大

# === 4. 繪圖函數定義（每次更新後即時顯示結果） ===
def draw(X1, T, W):
    plt.cla()  # 清空前一張圖
    plt.title("Adaline")                # 圖標題
    plt.xlabel("X")                     # X 軸標籤
    plt.ylabel("Y")                     # Y 軸標籤
    plt.scatter(X1, T, color='blue', label="Target T")  # 畫出實際資料點
    x_vals = np.linspace(min(X1), max(X1), 100)         # 建立畫線用的 X 值
    y_vals = W[0] + W[1] * x_vals                       # 計算對應的模型預測 Y 值
    plt.plot(x_vals, y_vals, color='red', label="Model")# 畫出紅色預測線
    plt.pause(0.05)                                     # 暫停一下讓圖顯示出來

plt.ion()  # 啟動即時繪圖模式

# === 5. 開始訓練 Adaline 模型 ===
for Iteration in range(max_iter):
    total_error = 0
    for i in range(m):  # 對每筆資料進行訓練
        x = X_total[i]              # 取出第 i 筆輸入（含 bias）
        t = T[i]                    # 對應目標值
        y = np.dot(W, x)           # 模型輸出（線性加總：W·x）
        error = t - y              # 計算誤差
        W = W + eta * error * x    # 權重更新（Adaline 的 Delta Rule）
        total_error += error ** 2  # 累計平方誤差

    MSE = total_error / m          # 計算本輪的均方誤差

    # 如果這一輪的 MSE 小於目前最佳，就更新最佳參數
    if MSE < MSE_best:
        MSE_best = MSE
        W_best = W.copy()

    draw(X1, T, W)  # 每輪訓練後畫出當前模型

    # 印出目前權重與訓練次數
    print(f"=================================\nWeights: {W}\nIteration {Iteration+1:2d} ")

    # 若誤差極小（此處其實不太會成立，MSE 不可能 < 0），可以提前停止
    if MSE < 0:
        break

# 印出最佳結果
print("最佳權重：", W_best)

# 關閉即時繪圖並顯示最終圖形
plt.ioff()
plt.show()

# === 6. 儲存最佳權重結果至 Excel 檔案 ===
result_df = pd.DataFrame([["Bias", W_best[0]], ["Weight_X1", W_best[1]]], columns=["Name", "Value"])
result_df.to_excel("HW4_BestWeights.xlsx", index=False)  # 儲存為 Excel，不包含索引欄