var = open("hello.txt", "r",encoding="utf-8")
data = var.readlines()
print(data)
value = input("원하는 단어를 적으세요: ")
word_num = 0

for i in range(len(data)):
    if value in data[i]:
        word_num += 1

print("단어개수:",word_num)
var.close()