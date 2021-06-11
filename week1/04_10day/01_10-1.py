class Contact:
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def print_info(self):

        return print("이름: ", self.name)

    def print_info2(self):

        return print("번호: ", self.phone)

    def print_info3(self):
        if self.email.find("@") > -1:
            return print("이메일: ", self.email)
        else:
            return print("이메일 주소가 틀립니다.")
    def print_info4(self):

        return print("주소: ", self.address)

c1 = Contact("이준명", "010-1234-1111","qwerlikelion.org","경기도")
c2 = Contact("이준명", "010-1234-1111","qwerlikelion.org","경기도")
print(c1.name,c1.email,c1.address,c1.phone)
print(c2.name,c2.email,c2.address,c2.phone)

