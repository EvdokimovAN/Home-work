import math
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
def MNK_kb(x, y):
    n = len(x)
    x_sr = sum(x) / len(x)
    x2_sr = sum([i * i for i in x]) / len(x)
    y_sr = sum(y) / len(y)
    xy_sr = sum(x[i] * y[i] for i in range(0, n)) / n
    k = (xy_sr - x_sr * y_sr) / (x2_sr - x_sr ** 2)
    b = y_sr - k * x_sr
    return [[k, b]]

def mnk_k(x, y):
    n = len(x)
    xy_sr = sum(x[i] * y[i] for i in range(0, n)) / n
    x2_sr = sum([i * i for i in x]) / len(x)
    k = xy_sr / x2_sr
    return [k]

def grafic():
    if len(x) < 2:
        label6 = Label(text="Минимальное количество точек 2!!!") 
        label6.place(x=200,y=40)
    else:
        global k_kb, b_kb, k
        k_kb = MNK_kb(x, y)[0][0]
        b_kb = MNK_kb(x, y)[0][1]
        k = mnk_k(x, y)[0]
        x_theor_kb = []
        x_theor_k = []
        start = min(x)
        finish = max(x)
        points = (finish - start) / len(x) * 100
        delta = (finish - start) / points
        while start < finish:
            x_theor_kb.append(start)
            x_theor_k.append(start)
            start = start + delta
        y_theor_kb = []
        y_theor_k = []
        for i in x_theor_kb:
            y_theor_kb.append(k_kb * i + b_kb)
        for i in x_theor_k:
            y_theor_k.append(k * i)
        y_theor_k = []
        for i in x_theor_k:
            y_theor_k.append(k * i)
        kprint = Label(text=k_kb)
        kprint.place(x=40,y=180)
        bprint = Label(text=b_kb)
        bprint.place(x=40,y=215)
        kp = Label(text=k)
        kp.place(x=40,y=250)

        plt.plot(x, y, linestyle=' ', marker='o', color='red', label="Experiment")
        plt.plot(x_theor_kb, y_theor_kb, label="Approximation kx+b")
        plt.plot(x_theor_k, y_theor_k, label="Approximation ax")
        plt.plot([0], [0], color='black')
        plt.legend()
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(which='major')
        plt.grid(which='minor')
        plt.show()
def delet():
    x.clear()
    y.clear()



y = []
x = []
root = Tk()
root.geometry("530x320")
root.title("Поствоение линейных графиков МНК")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ix = StringVar()
x_entry = ttk.Entry( width=20, textvariable=ix)
x_entry.place(x=40, y=30)
igriki = StringVar()
y_entry = ttk.Entry( width=20, textvariable=igriki)
y_entry.place(x=40, y=75)
def sox(*args):
    global igriki
    global ix
    x2 = float(ix.get())
    y2 = float(igriki.get())
    x.append(x2)
    y.append(y2)
    y_entry.delete(0, 'end')
    x_entry.delete(0,'end')
ttk.Button(text="Cохранить точку", command=sox).place(x=20,y=120)
ttk.Button(text="Построить график по заданным точкам", command=grafic).place(x=235,y=120)
ttk.Button(text="Сброс точек", command=delet).place(x=140,y=120)
label2 = Label(text="Построение графика МНК по заданным точкам") 
label2.pack()  
label = Label(text="X =") 
label.place(x=15,y=30)  
label1 = Label(text="Y =") 
label1.place(x=15,y=75) 
label3 = Label(text="k =") 
label3.place(x=15,y=180)
label4 = Label(text="b =") 
label4.place(x=15,y=215)
label5 = Label(text="a =") 
label5.place(x=15,y=250)
ps = Label(text="*Приложение строит две прямые с помощью МНК: лучшую прямую из 0 (y = ax) и (y = kx+b)") 
ps.place(x=5,y=300)
root.mainloop()
