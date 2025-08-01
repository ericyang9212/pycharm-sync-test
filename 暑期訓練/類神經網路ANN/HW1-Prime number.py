def prime_number(x): #判斷一個整數 x 是否為質數的函數
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
Number1 = int(input("Please enter first number: "))
Number2 = int(input("Please enter second number: "))
x = 1

if Number2 < Number1:
    y = Number2
    Number2 = Number1
    Number1 = y

for i in range(Number1, Number2 + 1):
    i_is_prime = prime_number(i) #呼叫 prime_number 函數判斷 i 是否為質數
    if i_is_prime:
        print(f"Prime number",x,":",(i))
        x += 1

