import random

class food:
    def __init__(self,name):
        self.name = name

    def lunch_choice(self,cag):
        lst_food = ["비빔밥", "김치", "미역국", "갈비"]
        lst_food2 = ["돈가스", "스테이크", "햄버거"]
        lst_food3 = ["짜장면", "짬뽕", "탕수육"]

        if cag == "한식":
            result = random.choice(lst_food)
            return result
        elif cag == "양식":
            result2 = random.choice(lst_food2)
            return result2
        elif cag == "중식":
            result3 = random.choice(lst_food3)
            return result3