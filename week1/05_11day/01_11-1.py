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
        def_word = dat.loc[dat['area'] == word, 'acd'].values[0]

    except:
        def_word = "결과를 찾을 수 없음"

    textbox.insert(END, def_word)


def click2():
    word = entry.get()

    dtbox.delete(0.0, END)

    try:
        wow = dat.loc[dat['area'] == word, 'death'].values[0]
    except:
        wow = "결과를 찾을 수 없음"

    dtbox.insert(END, wow)

window = Tk()
window.title("My Dictionary")

# 01 입력 상자 설명 레이브
label = Label(window, text="원하는 단어 입력 후, 엔터 키 누르기")
label.grid(row=0, column=0, sticky=W)

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window,width=25, bg="light yellow")
entry.grid(row=1, column=0, sticky=W)

# 03 결과 버튼
btn = Button(window, width=7, text="발생건수", bg="light green", command=click)
btn.grid(row=1, column=1,columnspan=2 ,sticky=W)

btn2 = Button(window, width=7, text="사망수", bg="light blue", command=click2)
btn2.grid(row=1, column=2,columnspan=2 ,sticky=W)

# 04 결과 레이블 - 발생건수
mean = Label(window, text="\n발생건수")
mean.grid(row=3, column=0, sticky=W)

# 05 결과 레이블 - 사망자수
result = Label(window, text="\n사망자수")
result.grid(row=3, column=1, sticky=W)

# 05 텍스트 박스 입력 상자
textbox = Text(window, width=10,height=2,wrap=WORD, bg="light yellow")
textbox.grid(row=4, column=0, sticky=W)

dtbox = Text(window, width=10,height=2,wrap=WORD, bg="light yellow")
dtbox.grid(row=4, column=1, sticky=W)

# 메인 반복문 실행
window.mainloop()