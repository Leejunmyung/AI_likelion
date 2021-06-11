import re

class Contact:
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def print_info(self):
        print("이름: ", self.name)
        print("번호: ", self.phone)
        print("이메일: ", self.email)
        print("주소: ", self.address)


def print_menu():
    print("1.연락처 입력")
    print("2.연락처 출력")
    print("3.연락처 삭제")
    print("4.종료")
    menu = input("메뉴 선택: ")
    return int(menu)


def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()


def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]


def run():
    contact_list = []
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name: ")
            delete_contact(contact_list, name)
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
        lee = Contact(name, phone_number, email, addr)
        return lee



if __name__ == "__main__":
    run()

