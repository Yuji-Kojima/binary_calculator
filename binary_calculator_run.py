def binary_calculator_run():
    import tkinter as tk

    root=tk.Tk()
    root.geometry("300x100")
    root.title("2進数計算機")
    class Data():
        def __init__(self):
            self.a=0
            self.back_log=[]
    d=Data()

    def finish(a):
        expression = "".join(map(str, a))
        try:
            # eval で数式として計算
            result = eval(expression)
            return result
        except ZeroDivisionError:
            return "Error (0割)"
        except Exception:
            return "Error"
                

    def draw(a,f):
        for widget in root.winfo_children():
            widget.destroy()
        a = "".join(map(str, a)) if a else "入力待ち..."
        label=tk.Label(root,text=str(a),font=("Arial",10))
        label.pack()
        label2=tk.Label(root,text=str(f),font=("Arial",10))
        label2.pack()
        label3=tk.Label(root,text="q+ w- e* r/ space↑ Bquit",font=("Arial",10))
        label3.pack()
        label4=tk.Label(root,text="a128 s64 d32 f16  j8 k4 l2 ;1 :|←",font=("Arial",10))
        label4.pack()

    draw("入力欄","結果欄")




    def sumlist(b):
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



    def key_press(event):
        d.a=-1
        if event.keysym == "a":
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
        if event.char == ":":
            if not len(d.back_log) == 0:
                d.back_log.pop()
        if event.keysym == "q":
            d.a="+"
        if event.keysym == "w":
            d.a="-"
        if event.keysym == "e":
            d.a="*"
        if event.keysym == "r":
            d.a="/"

       
        
        if d.a != -1:
            d.back_log.append(d.a)
        r=sumlist(d.back_log)
        f=finish(r)
        if event.keysym == "space":
            d.back_log=[f]
            r=sumlist(d.back_log)
            f=finish(r)
        draw(r,f)
        if event.keysym == "b":
            root.quit()


    root.bind("<Key>",key_press)
    root.mainloop()
binary_calculator_run()