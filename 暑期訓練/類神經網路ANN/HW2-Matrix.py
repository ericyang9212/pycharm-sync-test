import pandas as pd
import os
desktop_path = "/Users/ericyang/Desktop/Python File"

input_path = os.path.join(desktop_path, "Homework2.xlsx")
output_path = os.path.join(desktop_path, "New_Hw2_Result.xlsx")

Matrix_1 = pd.read_excel(input_path,sheet_name = "Matrix1",header = None) #無標題行資料直接從第一格開始
Matrix_2 = pd.read_excel(input_path,sheet_name = "Matrix2",header = None)
Matrix_3 = pd.read_excel(input_path,sheet_name = "Matrix3",header = None)
#print(Matrix_1)
#print(Matrix_2)
#print(Matrix_3)

#matrix1 + matrix2
add_result = [[0 for _ in range(Matrix_1.shape[1])] for _ in range(Matrix_1.shape[0])] #2D List 結構 建立list
for i in range(Matrix_1.shape[0]):
    for j in range(Matrix_1.shape[1]):
        add_result[i][j] = Matrix_1.iloc[i,j] + Matrix_2.iloc[i,j] #根據整數位置取出 DataFrame 中的資料
add_result = [[float(x) for x in row] for row in add_result] #將所有數值轉換為 float 類型
add_result_df = pd.DataFrame(add_result)
print(add_result_df)

#matrix2 * matrix3
inner_result = [[0 for _ in range(Matrix_3.shape[1])] for _ in range(Matrix_2.shape[0])]
for i in range(Matrix_2.shape[0]): #
    for j in range(Matrix_3.shape[1]):
        for k in range(Matrix_2.shape[1]):
            inner_result[i][j] += Matrix_2.iloc[i,k] * Matrix_3.iloc[k,j]
inner_result = [[float(x) for x in row] for row in inner_result]
inner_result_df = pd.DataFrame(inner_result)
print(inner_result_df)

with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
    add_result_df.to_excel(writer, sheet_name="Add_M1_M2", index=False, header=False)
    inner_result_df.to_excel(writer, sheet_name="Inner_M2_M3", index=False, header=False)


    #利用老師給的講義了解內機背後運算邏輯，如何由page8改寫成page10