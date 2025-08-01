# 獨立的if判斷式
'''
Age = int(input("請輸入年齡："))

print("獨立的if判斷式:")
if Age <= 20:
    print("You are teenager")
if Age <= 40:
    print("You are adulthood")
if Age <= 60:
    print("You are mature adulthood")
if Age > 60:
    print("You are old")

print("="*20)

#聯合的if判斷式

print("聯合的if判斷式：")
if Age <= 20:
    print("You are teenager")
elif Age <= 40:
    print("You are adulthood")
elif Age <= 60:
    print("You are mature adulthood")
else:
    print("You are old")

print("="*20)

#錯誤的邏輯順序

print("錯誤順序：")
if Age <= 40:
    print("You are adulthood")
elif Age <= 20:
    print("You are teenager")
elif Age <= 60:
    print("You are mature adulthood")
else:
    print("You are old")

print("="*20)
#嚴謹的if判斷式
print("嚴謹的判別式")
if Age <= 20:
    print("You are teenager")
elif Age > 20 and Age <= 40:
    print("You are adulthood")
elif Age > 40 and Age <= 60:
    print("You are mature adulthood")
elif Age > 60:
    print("You are old")

print("="*20)

#隨機變數
print("隨機產生0~1之間的浮點數")

import numpy as np
RandomNum1 = np.random.random()
print(RandomNum1)

print("隨機產生a~b-1之間的整數")
RandomNum2 = np.random.randint(0,5)
print(RandomNum2)

print("="*20)
'''
# Practice
# 猜拳遊戲
a = ["剪刀","石頭","布"]

