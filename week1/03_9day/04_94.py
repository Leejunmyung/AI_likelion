num1 = 3
num2 = 5

try:
    result = num2/num1

except IndexError as e:
    print("체크 중입니다.", e)

except NameError as e:
    print("맞는 이름이 없습니다.",e)

except TypeError as e:
    print("타입이 다릅니다", e)

else:
    print("결과값은:",result)