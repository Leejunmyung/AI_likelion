result = 0
def plus1(num):
    global result
    result += num
    return result

print(plus1(3))
print(plus1(7))

result1 = 0
def plus2(num):
    global result1
    result1 += num
    return result1

print(plus2(2))
print(plus2(10))

result2 = 0
def minus(num):
    global result2
    result2 -= num
    return result2

print(minus(2))
print(minus(15))

result3 = 1
def multiplied(num):
    global result3
    result3 *= num
    return result3

print(multiplied(15))
print(multiplied(10))

result4 = 1
def division(num):
    global result4
    result4 /= num
    return result4

print(division(2))