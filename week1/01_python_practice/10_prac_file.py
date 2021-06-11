# f1 = open("hello_myself.txt", "w") ## 읽기만 할거야.
# f1.write("hi my name is junmyung")
# f1.close()

f1 = open("hello_myself.txt", "a", encoding="utf-8") ## 읽기만 할거야.
f1.write("안녕")
f1.close()