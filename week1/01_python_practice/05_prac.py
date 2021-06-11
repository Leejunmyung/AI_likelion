id1 = "toto"
pwd = "1234"

num = 0

while num != 5:
    yid = input("아이디 입력: ")
    ypwd = input("비밀번호 입력: ")

    if (id1 == yid) and (pwd == ypwd):
        print("로그인 성공")
        break
    else:
        print("로그인 실패")
        num +=1