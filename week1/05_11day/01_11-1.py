from tkinter import *
import pandas as pd

dat = pd.read_csv("./2019_accident.csv") # 파일 불러오기

# 기능 추가
# 제출 버튼을 클릭했을 때, 동작 가능.
def click():
    word = entry.get()

    textbox.delete(0.0, END)
    dtbox.delete(0.0, END)
    itbox.delete(0.0, END)

    try:
        def_word = dat.loc[dat['area'] == word, 'acd'].values[0]
        wow = dat.loc[dat['area'] == word, 'death'].values[0]
        wow2 = dat.loc[dat['area'] == word, 'injury'].values[0]

    except:
        def_word = "결과를 찾을 수 없음"
        wow = "결과를 찾을 수 없음"
        wow2 = "결과를 찾을 수 없음"

    textbox.insert(END, def_word)
    dtbox.insert(END, wow)
    itbox.insert(END, wow2)


window = Tk()
window.title("2019_accident_statistic")
window.geometry('500x500')
window['bg'] = 'skyblue'

# 01 입력 상자 설명 레이브
label = Label(window, text="지역 입력 후, 버튼 누르기",bg='skyblue', fg='white smoke',font=('현대하모니L',15,'bold'))
label.place(x=40, y=20)

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window,width=25, bg="light yellow")
entry.place(x=40, y=50, height=25)

# 03 결과 버튼
btn = Button(window, width=7, text="조회", bg="light green", command=click)
btn.place(x=230, y=50)

# 04 결과 레이블 - 발생건수
mean = Label(window, text="발생건수",bg='skyblue', fg='purple',font=('현대하모니L',15,'bold'))
mean.place(x=35, y=100)

textbox = Text(window, width=11,height=2,wrap=WORD, bg="light yellow")
textbox.place(x=40, y=130)

# 05 결과 레이블 - 사망자수
result = Label(window, text="사망자수", bg='skyblue', fg='purple',font=('현대하모니L',15,'bold') )
result.place(x=165, y=100)

dtbox = Text(window, width=11,height=2,wrap=WORD, bg="light yellow")
dtbox.place(x=170, y=130)

# 06 결과 레이블 - 부상자수
result2 = Label(window, text="부상자수", bg='skyblue', fg='purple',font=('현대하모니L',15,'bold') )
result2.place(x=295, y=100)

itbox = Text(window, width=11,height=2,wrap=WORD, bg="light yellow")
itbox.place(x=300, y=130)

caracd = PhotoImage(file="car.PNG")

hello = Label(window, image=caracd, width=350,height=250)
hello.place(x=40, y=190)

# 메인 반복문 실행
window.mainloop()