import tkinter
from tkinter import messagebox
import tkinter as tk


num = 0 # 追加したウィジェットの数                   
w_y = 160 # 追加していくウィジェットの縦位置                        

# ウィジェットを増やす関数                                                      
def add_widget(widget):
    global w_y
    w_y = w_y +	20
    widget.place(x=50, y=w_y)

# ボタンの動作関数                                                      
def clicked_button(widget):
    global num
    if num < 5: # 上限５個
        global var
        date_field =tkinter.Entry(width=20)
        add_widget(date_field) # 追加関数に投げる
        var = date_field.get()
        num = num + 1

window = tkinter.Tk()
window.geometry("400x400")
window.title("con-date")

canvas = tkinter.Canvas(width=410, height=410, background="#ccb")
canvas.place(x=-5, y=-5)

# 下の引数の中にcommandを追加する。
button = tkinter.Button(canvas, text="add", width=5, command=lambda:clicked_button(canvas))
button.place(x=200, y=200)

lbl = tkinter.Label(text='日付')
lbl.place(x=10, y=100)
datet_field = tkinter.Entry(width=20)
datet_field.place(x=50, y=100)

#複数行テスト
lbl = tkinter.Label(text='複数行入力')
lbl.place(x=10, y=200)
text_box = tk.Text()
text_box.pack()
text_box.place(x=50, y=200)

lbl = tkinter.Label(text='献立名')
lbl.place(x=10, y=150)
koudate_field = tkinter.Entry(width=40)
koudate_field.place(x=50, y=150)

def click_botton():
    """
    入力欄の値をget()にて取得。
    入力値をダイアログに表示する。
    """
    global var
    input_value = text_box.get()
    messagebox.showinfo("確認",input_value + ","+var+ "で保存されました。")

button = tkinter.Button(canvas, text="保存", width=5, command=click_botton)
button.place(x=200, y=30)

window.mainloop()