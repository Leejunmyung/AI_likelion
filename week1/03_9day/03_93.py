class CalFnc3:
    def __init__(self, result):
        self.result = result

    def plus(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

    def div(self, num):
        self.result /= num
        return self.result


class CalFnc3_change(CalFnc3):

    def __init__(self, result):
        self.result = result

    def plus(self, num):
        self.result += num

        return self.result

    def sub(self, num):
        self.result -= num

        return self.result

    def mul(self, num):

        self.result *= num
        return self.result

    def div(self, num):
        if num == 0:
            return 0

        else:
            self.result /= num
        return self.result


class CalFn4(CalFnc3_change):

    def __init__(self, result):
        self.result = result

    




c1 = CalFn4(1)
print(c1.mul(9))