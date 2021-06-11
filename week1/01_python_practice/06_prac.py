log_database = {"toto":"1234","one":"3456","two":"0000"}
id1 = input("아이디를 입력하세요: ")
pwd = input("비밀번호를 입력하세요: ")

for i, j in log_database.items():
    if log_database[id1] == j and log_database[pwd] == i:
        print("로그인 성공")

print("로그인 실패")



