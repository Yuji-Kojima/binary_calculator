import tkinter as tk
class App():
    def __init__(self):
        self.root=tk.Tk()
        self.a=0
        self.back_log=[]
        self.last_result=[0,0,0,0,0,0,0]
    def binary_calculator_run(self,bi=True,he=True,oc=False,explain=True,clip_slice=True):
        self.bi=bi
        self.he=he
        self.oc=oc
        self.explain=explain
        self.clip_slice=clip_slice

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
        self.root.geometry(w_size)
        self.root.title("2進数計算機")
        self.draw("入力欄","結果欄","2進数","8進数","16進数")#初回

        self.root.bind("<Key>",self.key_press)
        self.root.mainloop()
        return self.last_result

    def finish(self,a):# 計算結果を返す
        expression = "".join(map(str, a))
        try:
            # eval で数式として計算
            result = eval(expression)
            return result
        except ZeroDivisionError:
            return "Error (0割)"
        except Exception:
            return "Error"


    def draw(self,a,f,f2,f8,f16):# 描画する
            for widget in self.root.winfo_children():
                widget.destroy()
            a = "".join(map(str, a)) if a else "入力待ち..."
            label=tk.Label(self.root,text=str(a),font=("Meiryo",10))
            label.pack()
            label2=tk.Label(self.root,text=str(f),font=("Meiryo",10))
            label2.pack()
            if self.explain:
                label3=tk.Label(self.root,text="q+ w- e* r/ space↑ Bquit",font=("Arial",10))
                label3.pack()
                label4=tk.Label(self.root,text="a128 s64 d32 f16  j8 k4 l2 ;1 :|←",font=("Arial",10))
                label4.pack()
                label5=tk.Label(self.root,text="Copy z2 x8 c10 v16",font=("Arial",10))
                label5.pack()
            if self.bi:# 表示モードによって切り替え
                labelbin=tk.Label(self.root,text=f"{str(f2)}",font=("Meiryo",10))
                labelbin.pack()
            if self.he:
                labelhex=tk.Label(self.root,text=f"{str(f16)}",font=("Meiryo",10))
                labelhex.pack()
            if self.oc:
                labelhex=tk.Label(self.root,text=f"{str(f8)}",font=("Meiryo",10))
                labelhex.pack()

        




    def sumlist(self,b):# リストを成形して式をきれいにする
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



    def key_press(self,event):# キー入力を受け取る
        self.a=-1
        if event.keysym == "a":# 数字
            self.a=128
        if event.keysym == "s":
            self.a=64
        if event.keysym == "d":
            self.a=32
        if event.keysym == "f":
            self.a=16
        if event.keysym == "j":
            self.a=8
        if event.keysym == "k":
            self.a=4
        if event.keysym == "l":
            self.a=2
        if event.char == ";":
            self.a=1
        if event.char == "p":
            self.a=0

        if event.char == ":":# back_space
            if not len(self.back_log) == 0:
                self.back_log.pop()

        if event.keysym == "q":# 演算子
            self.a="+"
        if event.keysym == "w":
            self.a="-"
        if event.keysym == "e":
            self.a="*"
        if event.keysym == "r":
            self.a="/"





        if self.a != -1:# 入力を式に入れる
            self.back_log.append(self.a)
        r=self.sumlist(self.back_log)# 成形して
        f=self.finish(r) # 結果を返す

        if event.keysym == "space":# 式を結果で置き換え
            self.back_log=[f]
            r=self.sumlist(self.back_log)
            f=self.finish(r)

        if isinstance(f, int):#　結果を別の形式に変換、整数以外を弾く
            f2 = bin(f)
            f8 = oct(f)
            f16 = hex(f)
            self.last_result = [f, f2, f16, f8, f2.replace("0b", ""), f16.replace("0h", ""), f8.replace("0o", "")]
        else:
            f2 = f8 = f16 = "---"

        if self.clip_slice:# 引数でオプション、コピーしたものをきれいに
            cs=3
        else:
            cs=0

        if event.keysym == "z":#2進数コピー
            self.root.clipboard_clear()
            self.root.clipboard_append(self.last_result[1+cs])

        if event.keysym == "x":#8進数コピー
            self.root.clipboard_clear()
            self.root.clipboard_append(self.last_result[3+cs])

        if event.keysym == "c":#10進数コピー
            self.root.clipboard_clear()
            self.root.clipboard_append(self.last_result[0])

        if event.keysym == "v":#16進数コピー
            self.root.clipboard_clear()
            self.root.clipboard_append(self.last_result[2+cs])

        self.draw(r,f,f2,f8,f16)# 描画

        if event.keysym == "b":# 終了
            self.root.destroy()

if __name__ == "__main__":# 単体起動用
    A=App()
    a=A.binary_calculator_run()
    print(a)