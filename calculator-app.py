import tkinter as tk

# ボタンが押されたとき
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# 計算
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)

    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# クリア
def clear():
    entry.delete(0, tk.END)

# ウィンドウ作成
root = tk.Tk()
root.title("計算機アプリ")
root.geometry("500x400")

# 入力欄
entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5, justify="right")
entry.pack(pady=10)

# ボタンの配置
frame = tk.Frame(root)
frame.pack()

buttons = [
    ('7',0,0), ('8',0,1), ('9',0,2), ('/',0,3),
    ('4',1,0), ('5',1,1), ('6',1,2), ('*',1,3),
    ('1',2,0), ('2',2,1), ('3',2,2), ('-',2,3),
    ('0',3,0), ('C',3,1), ('=',3,2), ('+',3,3)
]

for (text,row,col) in buttons:
    if text == "=":
        btn = tk.Button(frame, text=text, width=5, height=2, command=calculate)
    elif text == "C":
        btn = tk.Button(frame, text=text, width=5, height=2, command=clear)
    else:
        btn = tk.Button(frame, text=text, width=5, height=2, command=lambda t=text: click(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()