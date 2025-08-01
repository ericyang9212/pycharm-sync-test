import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel(r"/Users/ericyang/Desktop/Python File/Python_Homework/Homework5.xlsx",
    sheet_name="HW_5_MP_Linear",usecols=range(1, 3))
data = data.values  # 轉換成 numpy 陣列

m = len(data)
X1 = data[:, 0]             # 特徵 X1
T = data[:, 1]              # 目標值 T
bias = np.ones(m)
X_total = np.c_[bias, X1]   # 加入 bias 項

eta = 0.01
W = np.array([10.0, -1.0])   # 初始權重 [bias, w1]
max_iter = 50
W_best = W.copy()
MSE_best = float("inf")      # 初始化最佳誤差

# === 4. 畫圖函數 ===
def draw(X1, T, W):
    plt.cla()
    plt.title("Adaline")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.scatter(X1, T, color='blue', label="Target T")
    x_vals = np.linspace(min(X1), max(X1), 100)
    y_vals = W[0] + W[1] * x_vals
    plt.plot(x_vals, y_vals, color='red', label="Model")
    plt.pause(0.1)

plt.ion()  # 即時繪圖啟動

# === 5. 開始訓練 Adaline ===
for Iteration in range(max_iter):
    total_error = 0
    for i in range(m):
        x = X_total[i]
        t = T[i]
        y = np.dot(W, x)            # 輸出
        error = t - y
        W = W + eta * error * x     # 梯度更新
        total_error += error ** 2

    MSE = total_error / m

    if MSE < MSE_best:
        MSE_best = MSE
        W_best = W.copy()

    draw(X1, T, W)
    print(f"=================================\nWeights: {W}\nIteration {Iteration+1:2d} ")

    if MSE < 0:  # 若誤差已非常小則提早停止
        break
print("最佳權重：", W_best)
plt.ioff()
plt.show()


result_df = pd.DataFrame([["Bias", W_best[0]],["Weight_X1", W_best[1]]], columns=["Name", "Value"])
result_df.to_excel("HW4_BestWeights.xlsx", index=False)
