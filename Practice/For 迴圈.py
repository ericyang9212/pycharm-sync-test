print("雙重迴圈，巢狀迴圈")
for i in range(5):          # i = 0,1,2,3,4
    for j in range(5):      # j = 0,1,2,3,4
        print(i,j)
print("="*15)

print("三重巢狀迴圈")
for a in range(4):
    for b in range(4):
        for c in range(4):
            print(a,b,c,a+b+c)
print("="*15)

print("三重巢狀迴圈")
count = 0
for a in range(4):
    for b in range(4):
        for c in range(4):
            #print(a,b,c,a+b+c)
            count += 1
            print("No." + str(count),a,b,c,a+b+c)
#輸出格式對其修正
#print("No." + str(count),a,b,c,a+b+c)
if count <= 9:
    print("No." + str(count)+"  ",a,b,c,a+b+c)
else:
    print("No." + str(count),a,b,c,a+b+c)