class Cal:
    result = 0


    def plus(self, num):
        self.result += num
        return self.result

    def minus(self, num):
        self.result -= num
        return self.result

    def divided(self, num):
        self.result /= num
        return self.result

class my_Cal(Cal):
    message = "안녕하세요"
    color = "blue"
    print(message,color)
    def divided(self, num):
        if num == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            self.result /= num
        return self.result

    def multiplied(self, num):
        self.result = 1
        self.result *= num
        return self.result

c6 = my_Cal()
print(c6.divided(0))