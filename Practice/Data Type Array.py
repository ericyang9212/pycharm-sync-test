#array
import numpy as np

print("="*10 + "Array" + "="*10)
List_1 = [1,2,3]
import numpy as pd
#陣列轉數組
Array_1 = np.array(List_1)
print(List_1)
print(Array_1)

print(List_1 * 3)
print(Array_1 * 3)
#0矩陣
Array_2 = np.zeros([3,3])
print(Array_2)
#1矩陣
Array_3 = np.ones([3,3])
print(Array_3)
#單位矩陣
Array_4 = np.eye(3)
print(Array_4)
#亂數矩陣
Array_5 = np.random.random([3,3])
print(Array_5)
#亂數矩陣：整數
#(起始值,終點值（不包含）,矩陣大小)
Array_6 = np.random.randint(0,10,[10,10])
print(Array_6)
#直接宣告陣列，轉矩陣
Array_7 = np.array([[1,2,3],[4,5,6]])
Array_8 = np.array([[1,2],[2,4],[3,6]])
print(Array_7)
print(Array_8)

#採用矩陣行列式概念，讀取資料
#Array_8中，第2列
print(Array_8[2])
#Array_8中，第1行
print(Array_8[:,1])
#Array_8中，第2列，第1行
print(Array_8[2,1])

#採用矩陣行列式的概念，修改資料
Array_8[2,1] = 10
print(Array_8)