import tkinter as tk

root = tk.Tk()
root.title("Counter")
root.geometry("300x300")


global k
k =0

def lClick(event):
    global k
    k+=1
    lb.config(text = k)

def mClick(event):
    global k
    k=0
    lb.config(text = k)

def nClick(event):
    global k
    k-=1
    lb.config(text = k)
    


lb  = tk.Label(root,text = k)
lb.pack()

btn = tk.Button(root,text= "+1")
btn.bind("<Button-1>",lClick)
btn.bind("<Button-2>",mClick)
btn.bind("<Button-3>",nClick)
btn.pack()



root.mainloop()