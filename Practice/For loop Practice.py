正確密碼 = "1234"
for 次數 in range(5):
    密碼 = input("請輸入密碼:")
    if 密碼 == 正確密碼:
        print("密碼正確")
        break
    elif 密碼 != 正確密碼 and 次數 < 4:
        print("密碼不正確，請重新輸入")
        print(f"您還剩下{4-次數}次機會")
    else:
        print("您已輸入太多次錯誤密碼，帳號已被鎖定")