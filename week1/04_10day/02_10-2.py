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

def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    lee = Contact(name, phone_number, e_mail, addr)
    print("-------------------")
    lee.print_info()


def run():
    set_contact()


if __name__ == "__main__":
    run()

