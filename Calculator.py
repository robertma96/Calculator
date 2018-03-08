from tkinter import *


root = Tk()
frame = Frame()
root.title("Calculator BMB RAU")

frame.pack(fill = BOTH, side = BOTTOM)


afisaj = Text(width = 10, height = 3, font=("Times New Roman", 25), bg = 'white')
afisaj.pack(side = TOP, fill = BOTH)
afisaj.insert(END, "0")
afisaj.config(state = DISABLED, cursor = "arrow")


numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

a = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]



astea = []
v = []
x = []
def crearenumar():
    for n in range(len(numbers)):
        if a[n] == "1":
            v.append(numbers[n])
    x.append(float(''.join(v)))
    print(x[-1])

def numar0():
    astea.append("0")
    elemente.append(float(''.join(astea)))
    if len(elemente) > 1:
        del elemente[0]
    afisaj.config(state=NORMAL)
    afisaj.delete(1.0, END)
    afisaj.insert(END, elemente)
    afisaj.config(state=DISABLED)

def numar1():
    astea.append("1")
    elemente.append(float(''.join(astea)))
    if len(elemente) > 1:
        del elemente[0]
    afisaj.config(state=NORMAL)
    afisaj.delete(1.0, END)
    afisaj.insert(END, elemente)
    afisaj.config(state=DISABLED)

def numar2():
    astea.append("2")
    elemente.append(float(''.join(astea)))
    if len(elemente) > 1:
        del elemente[0]
    afisaj.config(state=NORMAL)
    afisaj.delete(1.0, END)
    afisaj.insert(END, elemente)
    afisaj.config(state=DISABLED)

def numar3():
    astea.append("3")
    elemente.append(float(''.join(astea)))
    if len(elemente) > 1:
        del elemente[0]
    afisaj.config(state=NORMAL)
    afisaj.delete(1.0, END)
    afisaj.insert(END, elemente)
    afisaj.config(state=DISABLED)

def numar4():
    astea.append("4")
    elemente.append(float(''.join(astea)))
    if len(elemente) > 1:
        del elemente[0]
    afisaj.config(state=NORMAL)
    afisaj.delete(1.0, END)
    afisaj.insert(END, elemente)
    afisaj.config(state=DISABLED)

def numar5():
    astea.append("5")
    elemente.append(float(''.join(astea)))
    if len(elemente) > 1:
        del elemente[0]
    afisaj.config(state=NORMAL)
    afisaj.delete(1.0, END)
    afisaj.insert(END, elemente)
    afisaj.config(state=DISABLED)

def numar6():
    astea.append("6")
    elemente.append(float(''.join(astea)))
    if len(elemente) > 1:
        del elemente[0]
    afisaj.config(state=NORMAL)
    afisaj.delete(1.0, END)
    afisaj.insert(END, elemente)
    afisaj.config(state=DISABLED)


def numar7():
    astea.append("7")
    elemente.append(float(''.join(astea)))
    if len(elemente) > 1:
        del elemente[0]
    afisaj.config(state=NORMAL)
    afisaj.delete(1.0, END)
    afisaj.insert(END, elemente)
    afisaj.config(state=DISABLED)


def numar8():
    astea.append("8")
    elemente.append(float(''.join(astea)))
    if len(elemente) > 1:
        del elemente[0]
    afisaj.config(state=NORMAL)
    afisaj.delete(1.0, END)
    afisaj.insert(END, elemente)
    afisaj.config(state=DISABLED)


def numar9():
    astea.append("9")
    elemente.append(float(''.join(astea)))
    if len(elemente) > 1:
        del elemente[0]
    afisaj.config(state=NORMAL)
    afisaj.delete(1.0, END)
    afisaj.insert(END, elemente)
    afisaj.config(state=DISABLED)


def punct():
    astea.append(".")
    elemente.append(float(''.join(astea)))
    if len(elemente) > 1:
        del elemente[0]
    afisaj.config(state=NORMAL)
    afisaj.delete(1.0, END)
    afisaj.insert(END, elemente)
    afisaj.config(state=DISABLED)




add = False
sub = False
inmultire_1 = False
impartire_1 = False
egalafostapasat = False
listaadunare = []
elemente = []
x = 1


def adunare():
    global add, listaadunare, NOP, sub, inmultire_1, impartire_1
    global x, egalafostapasat
    astea[:] = []
    add = True


    if egalafostapasat == True:
        del listaadunare[1]

    listaadunare.append(float(elemente[0]))
    if len(listaadunare) > 1:
        for i in range(len(listaadunare) - x):
            x += 1
            listaadunare[0] = listaadunare[i-1] + listaadunare[i]
            afisaj.config(state=NORMAL)
            afisaj.delete(1.0, END)
            afisaj.insert(END, listaadunare[0])
            afisaj.config(state=DISABLED)
    egalafostapasat = False

def scadere():
    global add, listaadunare, sub, inmultire_1, imppartire_1
    global x, egalafostapasat
    astea[:] = []
    sub = True
    add = False
    if egalafostapasat == True:
        del listaadunare[1]

    listaadunare.append(float(elemente[0]))
    if len(listaadunare) > 1:
        for i in range(len(listaadunare) - x):
            x += 1
            listaadunare[0] = listaadunare[i] - listaadunare[i-1]
            afisaj.config(state=NORMAL)
            afisaj.delete(1.0, END)
            afisaj.insert(END, listaadunare[0])
            afisaj.config(state=DISABLED)
    egalafostapasat = False


def inmultire():
    global add, listaadunare, sub, inmultire_1, impartire_1
    global x, egalafostapasat
    astea[:] = []
    sub = False
    add = False
    inmultire_1 = True
    if egalafostapasat == True:
        del listaadunare[1]

    listaadunare.append(float(elemente[0]))
    if len(listaadunare) > 1:
        for i in range(len(listaadunare) - x):
            x += 1
            listaadunare[0] = listaadunare[i-1] * listaadunare[i]
            afisaj.config(state=NORMAL)
            afisaj.delete(1.0, END)
            afisaj.insert(END, listaadunare[0])
            afisaj.config(state=DISABLED)
    egalafostapasat = False


def impartire():
    global add, listaadunare, sub, inmultire_1, impartire_1
    global x, egalafostapasat
    astea[:] = []
    sub = False
    add = False
    inmultire_1 = False
    impartire_1 = True
    if egalafostapasat == True:
        del listaadunare[1]

    listaadunare.append(float(elemente[0]))
    if len(listaadunare) > 1:
        for i in range(len(listaadunare) - x):
            x += 1
            listaadunare[0] = listaadunare[i] / listaadunare[i-1]
            afisaj.config(state=NORMAL)
            afisaj.delete(1.0, END)
            afisaj.insert(END, listaadunare[0])
            afisaj.config(state=DISABLED)
    egalafostapasat = False

def egal():
    global egalafostapasat
    if add == True:
        adunare()
        egalafostapasat = True
        afisaj.config(state=NORMAL)
        afisaj.delete(1.0, END)
        afisaj.insert(END, listaadunare[0])
        afisaj.config(state=DISABLED)
    if sub == True:
        scadere()
        egalafostapasat = True
        afisaj.config(state=NORMAL)
        afisaj.delete(1.0, END)
        afisaj.insert(END, listaadunare[0])
        afisaj.config(state=DISABLED)
    if inmultire_1 == True:
        inmultire()
        egalafostapasat = True
        afisaj.config(state=NORMAL)
        afisaj.delete(1.0, END)
        afisaj.insert(END, listaadunare[0])
        afisaj.config(state=DISABLED)
    if impartire_1 == True:
        impartire()
        egalafostapasat = True
        afisaj.config(state=NORMAL)
        afisaj.delete(1.0, END)
        afisaj.insert(END, listaadunare[0])
        afisaj.config(state=DISABLED)

def AC():
    global add, sub, inmultire_1, impartire_1, elemente, egalafostapasat, listaadunare, x, astea
    add = False
    sub = False
    inmultire_1 = False
    impartire_1 = False
    egalafostapasat = False
    listaadunare[:] = []
    elemente[:] = []
    astea[:] = []
    x = 1
    afisaj.config(state=NORMAL)
    afisaj.delete(1.0, END)
    afisaj.insert(END, "0")
    afisaj.config(state=DISABLED)

def lasuta():
    if x == 1:
        afisaj.config(state=NORMAL)
        afisaj.delete(1.0, END)
        afisaj.insert(END, elemente[0]/100)
        afisaj.config(state=DISABLED)
        elemente[0] = elemente[0]/100
    else:
        afisaj.config(state=NORMAL)
        afisaj.delete(1.0, END)
        afisaj.insert(END, listaadunare[0]/100)
        afisaj.config(state=DISABLED)
        listaadunare[0] = listaadunare[0]/100

def plusminus():
    if x == 1:
        afisaj.config(state=NORMAL)
        afisaj.delete(1.0, END)
        afisaj.insert(END, -elemente[0])
        afisaj.config(state=DISABLED)
        elemente[0] = - elemente[0]
    else:

        afisaj.config(state=NORMAL)
        afisaj.delete(1.0, END)
        afisaj.insert(END, -listaadunare[0])
        afisaj.config(state=DISABLED)
        listaadunare[0] = - listaadunare[0]

Button1 = Button(frame, text = "AC", command = AC)
Button2 = Button(frame, text="+/-", command = plusminus)
Button3 = Button(frame, text="%", command = lasuta)
Button4 = Button(frame, text="÷", command = impartire)
Button5 = Button(frame, text="7", command =  numar7)
Button6 = Button(frame, text="8", command =  numar8)
Button7 = Button(frame, text="9", command =  numar9)
Button8 = Button(frame, text = "×", command = inmultire)
Button9 = Button(frame, text="4", command =  numar4)
Button10 = Button(frame, text="5", command = numar5)
Button11 = Button(frame, text="6", command = numar6)
Button12 = Button(frame, text="-", command = scadere)
Button13 = Button(frame, text="1", command = numar1)
Button14 = Button(frame, text="2", command = numar2)
Button15 = Button(frame, text="3", command = numar3)
Button16 = Button(frame, text="+", command = adunare)
Button17 = Button(frame, text="0", command = numar0)
Button18 = Button(frame, text=".", command = punct)
Button19 = Button(frame, text="=", command = egal)





Button1.grid(row = 0, column = 0, sticky=N+S+E+W)
Button1.config(width=5, height=2, font=("Times New Roman", 17))

Button2.grid(row = 0, column = 1, sticky=N+S+E+W)
Button2.config(width=5, height=2, font=("Times New Roman", 17))

Button3.grid(row = 0, column = 2, sticky=N+S+E+W)
Button3.config(width=5, height=2, font=("Times New Roman", 17))

Button4.grid(row = 0, column = 3, sticky=N+S+E+W)
Button4.config(width=5, height=2, font=("Times New Roman", 17))

Button5.grid(row = 1, column = 0, sticky=N+S+E+W)
Button5.config(width=4, height=2, font=("Times New Roman", 17))

Button6.grid(row = 1, column = 1, sticky=N+S+E+W)
Button6.config(width=4, height=2, font=("Times New Roman", 17))

Button7.grid(row = 1, column = 2, sticky=N+S+E+W)
Button7.config(width=4, height=2, font=("Times New Roman", 17))

Button8.grid(row = 1, column = 3, sticky=N+S+E+W)
Button8.config(width=4, height=2, font=("Times New Roman", 17))

Button9.grid(row=2, column=0, sticky=N+S+E+W)
Button9.config(width=4, height=2, font=("Times New Roman", 17))

Button10.grid(row=2, column=1, sticky=N+S+E+W)
Button10.config(width=4, height=2, font=("Times New Roman", 17))

Button11.grid(row=2, column=2, sticky=N+S+E+W)
Button11.config(width=4, height=2, font=("Times New Roman", 17))

Button12.grid(row=2, column=3, sticky=N+S+E+W)
Button12.config(width=4, height=2, font=("Times New Roman", 17))

Button13.grid(row=3, column=0, sticky=N+S+E+W)
Button13.config(width=4, height=2, font=("Times New Roman", 17))

Button14.grid(row=3, column=1, sticky=N+S+E+W)
Button14.config(width=4, height=2, font=("Times New Roman", 17))

Button15.grid(row=3, column=2, sticky=N+S+E+W)
Button15.config(width=4, height=2, font=("Times New Roman", 17))

Button16.grid(row=3, column=3, sticky=N+S+E+W)
Button16.config(width=4, height=2, font=("Times New Roman", 17))

Button17.grid(row=4, column=0, columnspan = 2, sticky=N+S+E+W)
Button17.config(width=4, height=2, font=("Times New Roman", 17))

Button18.grid(row=4, column=2, sticky=N+S+E+W)
Button18.config(width=4, height=2, font=("Times New Roman", 17))

Button19.grid(row=4, column=3, sticky=N+S+E+W)
Button19.config(width=4, height=2, font=("Times New Roman", 17))




root.resizable(width=False, height=False)
#root.geometry("300x500")
root.mainloop()


