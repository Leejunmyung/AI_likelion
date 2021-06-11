from tkinter import *
import pandas as pd
import os

print(os.getcwd())

dat = pd.read_csv("./2019_accident.csv") # 파일 불러오기

# 기능 추가
# 제출 버튼을 클릭했을 때, 동작 가능.
def click():
    word = entry.get()

    textbox.delete(0.0, END)

    try:
        def_word = dat.loc[dat['area']==word, 'def'].values[0]
    except:
        def_word = "단어의 뜻을 찾을 수 없음"

    textbox.insert(END, def_word)

window = Tk()
window.title("My Dictionary")

# 01 입력 상자 설명 레이브
label = Label(window, text="원하는 단어 입력 후, 엔터 키 누르기")
label.grid(row=0, column=0, sticky=W)

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window,width=25, bg="light yellow")
entry.grid(row=1, column=0, sticky=W)

# 03 제출 버튼
btn = Button(window, width=15, text="제출", bg="light green", command=click)
btn.grid(row=1, column=1,columnspan=2 ,sticky=W)

# 04 설명 레이블 - 의미
mean = Label(window, text="\n단어의 의미")
mean.grid(row=3, column=0, sticky=W)

# 05 텍스트 박스 입력 상자
textbox = Text(window, width=50,height=7,wrap=WORD, bg="light yellow")
textbox.grid(row=4, column=0, sticky=W)

# 메인 반복문 실행
window.mainloop()