from tkinter import *
from tkinter import messagebox
import random
op=[]
val1=0
opCount=0
def btn_click(btn):
    global op,val1,opCount
    if btn['text'] in ['1','2','3','4','5','6','7','8','9','0']:
        opCount=1
        for i in range(0,10):
            if btn['text']==i:
                op.append(i)
        
        if op!=[]:
            if opCount==1:
                labl.config(text=btn['text'])
                opCount=0
            else:
                labl.config(text=labl['text']+btn['text'])
        else:
            if labl['text']=="0":
                labl.config(text=btn['text'])
            else:
                labl.config(text=labl['text']+btn['text'])

    elif btn['text']=='OK':
        if labl['text']=='1234':
            messagebox.showinfo('showinfo','密碼正確')
        else:
            messagebox.showinfo('showinfo','密碼錯誤')
        op=0   
    elif btn['text']=='C':
        labl.config(text="0")
        op=[]
           

if __name__=="__main__":
    root=Tk()
    root.title("Calculator")
    root.geometry("300x500+200+100")
    
    for i in range (3):
        root.grid_rowconfigure(i,weight=1)
        root.grid_columnconfigure(i,weight=1)
    root.grid_rowconfigure(3,weight=1)   
    
    labl=Label(root,text="0",
               font=('Arial',20),
               bg="#ffcc99",
               justify=RIGHT,anchor=E)
    labl.grid(row=0,column=0,columnspan=4,sticky=NSEW)
    btn_labs=['1','2','3',
              '4','5','6',
              '7','8','9',]
    random.shuffle(btn_labs)
    btn_power=['C','0','OK']
    btns=[]
    for i in range(3):
        for j in range(3):
            btns.append(Button(root,text=btn_labs[i*3+j],
                               width=8,height=2,
                               font=('Arial',20)))
            btns[-1].config(command=lambda btn=btns[-1]:btn_click(btn))
            btns[-1].grid(row=i+1,column=j,sticky=NSEW)
    for k in range(3):
        btns.append(Button(root,text=btn_power[k],
                                width=8,height=2,
                                font=('Arial',20)))
        btns[-1].config(command=lambda btn=btns[-1]:btn_click(btn))
        btns[-1].grid(row=4,column=k,sticky=NSEW)       
    root.resizable(0,0)
    root.mainloop()