import re
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


def print_menu():
    print("1.연락처 입력")
    print("2.연락처 출력")
    print("3.연락처 삭제")
    print("4.종료")
    menu = int(input("메뉴 선택: "))
    return run(menu)


def run(menu):
    while 1:
        if menu == 1:
            return set_contact()
        elif menu == 2:
            return print(list(db.juser.find({},{'_id':False})))
        elif menu == 3:
            name = input("Name: ")
            return db.juser.delete_one({'name':name})
        elif menu == 4:
            break


def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    email = input("E-mail: ")
    addr = input("Address: ")

    e = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    p = re.compile('\d{3}-\d{3,4}-\d{4}')

    if e.match(email) == None :
        print("이메일 형식이 일치하지 않습니다.")
    elif p.match(phone_number) == None :
        print("전화번호 형식이 일치하지 않습니다.")
    elif len(name) > 10:
        print("이름 형식이 일치하지 않습니다.")
    else:
        db.juser.insert_one({'name':name,'phone':phone_number,'email':email,'addr':addr})
    return


if __name__ == "__main__":
    print_menu()


