import numpy as np
import pandas as pd

# 從 Excel 檔案中讀取資料（檔案路徑為絕對路徑）
# 讀取工作排程的處理時間資料，從工作表 "5j5m"，取第2到第6欄（即 index 1~5，共5台機器）
List = pd.read_excel(r"/Users/ericyang/Desktop/Python File/排程/排程最佳化.xlsx",
                     sheet_name="5j5m", usecols=range(1, 6))

# 將 pandas 的 DataFrame 轉換成 numpy 陣列，便於後續運算
List = List.values
print(List)  # 顯示輸入的處理時間表

# R: 工作數量（rows），C: 機器數量（columns）
R, C = np.shape(List)

# 初始化 Gantt 圖的時間表（2C 是因為每台機器要記錄 start 與 end）
# Gantt[i, 2j] 是第 i 個工作的第 j 台機器的開始時間
# Gantt[i, 2j+1] 是結束時間
Gantt = np.zeros([R, C * 2])

# 第1個工作的第1台機器起始時間設為0，結束時間為該工序處理時間
Gantt[0, 0] = 0
Gantt[0, 1] = Gantt[0, 0] + List[0, 0]

# 計算第1個工作在其餘機器上的起始與結束時間（依序排下去）
for i in range(1, C):
    Gantt[0, 2 * i] = Gantt[0, (2 * i) - 1]                  # 當前工序的開始時間為上一機器的結束時間
    Gantt[0, (2 * i) + 1] = Gantt[0, 2 * i] + List[0, i]     # 結束時間 = 開始時間 + 處理時間

# 從第二個工作開始（第2列），依序處理每一筆工作的甘特圖資料
for i in range(1, R):
    # 第 i 個工作的第一台機器開始時間為前一工作在此機器的結束時間
    Gantt[i, 0] = Gantt[i - 1, 1]
    # 結束時間 = 開始時間 + 處理時間
    Gantt[i, 1] = Gantt[i, 0] + List[i, 0]

    # 從第2台機器開始安排
    for j in range(1, C):
        # 這台機器的可用時間 = max(此工作在上一機器上的結束時間, 前一工作在這台機器上的結束時間)
        if Gantt[i, 2 * j - 1] >= Gantt[i - 1, 2 * j + 1]:
            Gantt[i, 2 * j] = Gantt[i, 2 * j - 1]
        else:
            Gantt[i, 2 * j] = Gantt[i - 1, 2 * j + 1]

        # 計算結束時間
        Gantt[i, 2 * j + 1] = Gantt[i, 2 * j] + List[i, j]

# 輸出整體甘特圖結果（每筆工作的每個工序的開始與結束時間）
print(Gantt)

# 輸出總工時，即最後一個工作在最後一台機器的結束時間
print("總工時：", Gantt[-1, -1])