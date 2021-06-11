sum5 = 0
sum7 = 0
for i in range(1,1001,1):
    if i % 5 == 0:
        sum5 += i
    elif i % 7 == 0:
        sum7 += i

print("5의 누적함:", sum5)
print("7의 누적함:", sum7)

