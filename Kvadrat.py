from tkinter import*
from math import*
D=0
j=0
def entry():
    global D,j
    if (a.get() and b.get() and c.get()):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1=round((-1*b_+sqrt(D))/(2*a_),1)
            x2=round((-1*b_-sqrt(D))/(2*a_),1)
            j=(f"X1={x1}, \nX2={x2}")
        elif D==0:
            x1=round((-1*b_)/(2*a_),1)
            j=(f"X1={x1}")
        else:
            j="Корней нет"
        nupp1.configure(text=f"D={D}\n{j}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
             a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
    return D,j

aken=Tk()
aken.title("𝕽𝖚𝖚𝖙𝖛õ𝖗𝖗𝖆𝖓𝖉𝖎𝖉")
aken.geometry("700x300")

lbl1=Label(aken, text = "Решение квадратного уравнения", font="Arial_Bold 30", width=30, fg="green", bg="lightblue",relief=RAISED)  
lbl1.pack()
a=Entry(aken,text="",width=2,font="Arial_Bold 30",fg="green",bg="lightblue")
a.place(x=10,y=110)
b=Entry(aken,text="",width=2,font="Arial_Bold 30",fg="green",bg="lightblue")
b.place(x=160,y=110)
c=Entry(aken,text="",width=2,font="Arial_Bold 30",fg="green",bg="lightblue")
c.place(x=260,y=110)

lbl2=Label(aken, text = "x**2+", font="Arial_Bold 25", width=4, fg="green", bg="white")
lbl2.place(x=60,y=117)
lbl3=Label(aken, text = "x+", font="Arial_Bold 25", width=2, fg="green", bg="white")
lbl3.place(x=210,y=115)
lbl6=Label(aken, text = "=0", font="Arial_Bold 25", width=2, fg="green", bg="white")
lbl6.place(x=310,y=115)

nupp=Button(aken, text = "𝕺𝖙𝖘𝖚𝖘𝖙𝖆𝖒𝖆", font="Arial_Bold 30", width=7, fg="black", bg="magenta",command=entry)
nupp.place(x=355,y=90)

nupp1=Label(aken, text = "𝕷𝖆𝖍𝖊𝖓𝖉𝖚𝖘", font="Arial_Bold 25", width=30, fg="black", bg="yellow",relief=RAISED)  
nupp1.pack(side = BOTTOM)

aken.mainloop()