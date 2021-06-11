class CalFnc2:

    def __init__(self, result, color, type):
        self.result = result
        self.col = color
        self.type = type

    def plus(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result


a1 = CalFnc2(3, 'blue', 'a타입')  # 계산기 한대
a2 = CalFnc2(3, 'black', 'b타입')  # 계산기 한대
a3 = CalFnc2(3, 'orange', 'c타입')  # 계산기 한대
print(a1.type)
print(a2.type)
print(a3.type)
