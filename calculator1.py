from tkinter import *

def click(event):
	global scvalue
	text=event.widget.cget("text")
	#print(text)
	if text== "=":
		value = eval(screen.get())
		scvalue.set(value)
		screen.update()
				

	elif text=="C":
		scvalue.set("")
		screen.update()
	else:
		scvalue.set(scvalue.get() + text)
		screen.update()

##########################################
root=Tk()
root.geometry("600x600+100+100")
root.minsize(500, 500)
#root.wm_iconbitmap("calculator.ico")
root.title("Hp personal Calculator")

scvalue=StringVar()
scvalue.set("")

screen=Entry(root, font="couriernew 30 bold", textvariable=scvalue)
screen.pack(fill=X, side=TOP,ipadx=4, pady=15,padx=10)
###########################################
f1=Frame(root, bg="grey")
b9=Button(f1, text="9", font="lucida 20 bold", padx=8, pady=8)
f1.pack()
b9.pack(side=LEFT, padx=18, pady=10)
b9.bind()
b9.bind('<Button-1>', click)

b8=Button(f1, text="8", font="lucida 20 bold", padx=8, pady=8)
f1.pack()
b8.pack(side=LEFT, padx=18, pady=10)
b8.bind('<Button-1>', click)

b7=Button(f1, text="7", font="lucida 20 bold", padx=8, pady=8)
f1.pack()
b7.pack(side=LEFT, padx=18, pady=10)
b7.bind('<Button-1>', click)

###################################################
f2=Frame(root, bg="grey")

b6=Button(f2, text="6", font="lucida 20 bold", padx=8, pady=8)
f2.pack()
b6.pack(side=LEFT, padx=18, pady=10)
b6.bind('<Button-1>', click)

b5=Button(f2, text="5", font="lucida 20 bold", padx=8, pady=8)
f2.pack()
b5.pack(side=LEFT, padx=18, pady=10)
b5.bind('<Button-1>', click)

b4=Button(f2, text="4", font="lucida 20 bold", padx=8, pady=8)
f2.pack()
b4.pack(side=LEFT, padx=18, pady=10)
b4.bind('<Button-1>', click)

########################################################
f3=Frame(root, bg="grey")

b3=Button(f3, text="3", font="lucida 20 bold", padx=8, pady=8)
f3.pack()
b3.pack(side=LEFT, padx=18, pady=10)
b3.bind('<Button-1>', click)

b2=Button(f3, text="2", font="lucida 20 bold", padx=8, pady=8)
f3.pack()
b2.pack(side=LEFT, padx=18, pady=10)
b2.bind('<Button-1>', click)

b1=Button(f3, text="1", font="lucida 20 bold", padx=8, pady=8)
f3.pack()
b1.pack(side=LEFT, padx=18, pady=10)
b1.bind('<Button-1>', click)

##################################################
f4=Frame(root, bg="grey")

b0=Button(f4, text="0", font="lucida 20 bold", padx=8, pady=8)
f4.pack()
b0.pack(side=LEFT, padx=18, pady=10)
b0.bind('<Button-1>', click)

bplus=Button(f4, text="+", font="lucida 20 bold", padx=8, pady=8)
f4.pack()
bplus.pack(side=LEFT, padx=18, pady=10)
bplus.bind('<Button-1>', click)

bminus=Button(f4, text="-", font="lucida 20 bold", padx=8, pady=8)
f4.pack()
bminus.pack(side=LEFT, padx=18, pady=10)
bminus.bind('<Button-1>', click)

bdeci= Button(f4, text='.', font="lucida 20 bold", padx=8, pady=8)
bdeci.pack(side=LEFT, padx=18, pady=10)
bdeci.bind('<Button-1>', click)

#################################################
f5=Frame(root, bg="grey")

bmult=Button(f5, text="*", font="lucida 20 bold", padx=8, pady=8)
f5.pack()
bmult.pack(side=LEFT, padx=18, pady=10)
bmult.bind('<Button-1>', click)

bdiv=Button(f5, text="/", font="lucida 20 bold", padx=8, pady=8)
f5.pack()
bdiv.pack(side=LEFT, padx=18, pady=10)
bdiv.bind('<Button-1>', click)

bequal=Button(f5, text="=", font="lucida 20 bold", padx=8, pady=8)
f5.pack()
bequal.pack(side=LEFT, padx=18, pady=10)
bequal.bind('<Button-1>', click)

bcanc=Button(f5, text="C", font="lucida 20 bold", padx=8, pady=8)
f5.pack()
bcanc.pack(side=LEFT, padx=18, pady=10)
bcanc.bind('<Button-1>', click)



root.mainloop()