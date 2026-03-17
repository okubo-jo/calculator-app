print("=== 簡単な計算機アプリ ===")

while True:
    a = input("1つ目の数字を入力 (終了するにはq): ")
    if a.lower() == 'q':
        break
    b = input("2つ目の数字を入力: ")
    if b.lower() == 'q':
        break

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("数字を入力してください！")
        continue

    op = input("計算方法を選んでください (+, -, *, /): ")
    
    if op == '+':
        print("結果:", a + b)
    elif op == '-':
        print("結果:", a - b)
    elif op == '*':
        print("結果:", a * b)
    elif op == '/':
        if b != 0:
            print("結果:", round(a / b, 2))
        else:
            print("0で割ることはできません")
    else:
        print("無効な入力です")

print("計算機アプリを終了します。")


