def binary_calculator_run(bi=True,he=True,oc=False,explain=True,clip_slice=True):
    import tkinter as tk

    root=tk.Tk()

    y_size=50
    if bi:
        y_size+=25
    if he:
        y_size+=25
    if oc:
        y_size+=25
    if explain:
        y_size+=75
    w_size=str(f"300x{y_size}")
    root.geometry(w_size)
    root.title("2進数計算機")

    class Data():# 変数
        def __init__(self):
            self.a=0
            self.back_log=[]
            self.last_result=[0,0,0,0,0,0,0]
    d=Data()

    def finish(a):# 計算結果を返す
        expression = "".join(map(str, a))
        try:
            # eval で数式として計算
            result = eval(expression)
            return result
        except ZeroDivisionError:
            return "Error (0割)"
        except Exception:
            return "Error"
                

    def draw(a,f,f2,f8,f16):# 描画する
        for widget in root.winfo_children():
            widget.destroy()
        a = "".join(map(str, a)) if a else "入力待ち..."
        label=tk.Label(root,text=str(a),font=("Meiryo",10))
        label.pack()
        label2=tk.Label(root,text=str(f),font=("Meiryo",10))
        label2.pack()
        if explain:
            label3=tk.Label(root,text="q+ w- e* r/ space↑ Bquit",font=("Arial",10))
            label3.pack()
            label4=tk.Label(root,text="a128 s64 d32 f16  j8 k4 l2 ;1 :|←",font=("Arial",10))
            label4.pack()
            label5=tk.Label(root,text="Copy z2 x8 c10 v16",font=("Arial",10))
            label5.pack()
        if bi:# 表示モードによって切り替え
            labelbin=tk.Label(root,text=f"{str(f2)}",font=("Meiryo",10))
            labelbin.pack()
        if he:
            labelhex=tk.Label(root,text=f"{str(f16)}",font=("Meiryo",10))
            labelhex.pack()
        if oc:
            labelhex=tk.Label(root,text=f"{str(f8)}",font=("Meiryo",10))
            labelhex.pack()

    draw("入力欄","結果欄","2進数","8進数","16進数")#初回




    def sumlist(b):# リストを成形して式をきれいにする
        a=0
        rlist = []
        for i in b:
            if isinstance(i,(int,float)):
                a+=i
            else:
               rlist.append(a)
               rlist.append(i)
               a=0
        rlist.append(a)
        return rlist



    def key_press(event):# キー入力を受け取る
        d.a=-1
        if event.keysym == "a":# 数字
            d.a=128
        if event.keysym == "s":
            d.a=64
        if event.keysym == "d":
            d.a=32
        if event.keysym == "f":
            d.a=16
        if event.keysym == "j":
            d.a=8
        if event.keysym == "k":
            d.a=4
        if event.keysym == "l":
            d.a=2
        if event.char == ";":
            d.a=1
        if event.char == "p":
            d.a=0

        if event.char == ":":# back_space
            if not len(d.back_log) == 0:
                d.back_log.pop()

        if event.keysym == "q":# 演算子
            d.a="+"
        if event.keysym == "w":
            d.a="-"
        if event.keysym == "e":
            d.a="*"
        if event.keysym == "r":
            d.a="/"



       
        
        if d.a != -1:# 入力を式に入れる
            d.back_log.append(d.a)
        r=sumlist(d.back_log)# 成形して
        f=finish(r) # 結果を返す

        if event.keysym == "space":# 式を結果で置き換え
            d.back_log=[f]
            r=sumlist(d.back_log)
            f=finish(r)

        if isinstance(f, int):#　結果を別の形式に変換、整数以外を弾く
            f2 = bin(f)
            f8 = oct(f)
            f16 = hex(f)
            d.last_result = [f, f2, f16, f8, f2[2:], f16[2:], f8[2:]]
        else:
            f2 = f8 = f16 = "---"

        if clip_slice:# 引数でオプション、コピーしたものをきれいに
            cs=3
        else:
            cs=0

        if event.keysym == "z":#2進数コピー
            root.clipboard_clear()
            root.clipboard_append(d.last_result[1+cs])

        if event.keysym == "x":#8進数コピー
            root.clipboard_clear()
            root.clipboard_append(d.last_result[3+cs])

        if event.keysym == "c":#10進数コピー
            root.clipboard_clear()
            root.clipboard_append(d.last_result[0])

        if event.keysym == "v":#16進数コピー
            root.clipboard_clear()
            root.clipboard_append(d.last_result[2+cs])
        
        draw(r,f,f2,f8,f16)# 描画

        if event.keysym == "b":# 終了
            root.destroy()

    root.bind("<Key>",key_press)
    root.mainloop()
    return d.last_result

a=binary_calculator_run()# 単体起動用
print(a)