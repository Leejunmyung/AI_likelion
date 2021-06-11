import random
community = ["안녕 로봇아","날씨 어때", "점심 뭐먹지?"]
value = input("질문을 해주세요: ")

if value in community:
    if value == "안녕 로봇아":
        print("반가워")
    elif value == "날씨 어때":
        print(random.choice(["맑음","흐림","구름낌"]))
    elif value == "점심 뭐먹지?":
        print(random.choice(["돈가스","냉면","파스타"]))
else:
    print("등록된 답변이 없습니다.")
