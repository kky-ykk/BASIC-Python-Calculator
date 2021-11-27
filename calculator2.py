import time
import tkinter as tk
window=tk.Tk()
#window.geometry("600x500+200+200")
window.title("SRI GANESH CALCULATOR!")

window.rowconfigure([0,1,2,3,4],weight=1,minsize=1)
window.columnconfigure([0,1,2],weight=1,minsize=1)

e=tk.Entry(window,width=20,bg="#ff0a66",font=("sd",19,"bold"))
e.grid(row=0,column=0,padx=5,columnspan=2,sticky="nesw")

e1=tk.Entry(window,width=10,bg="#63e3b3",font=("sd",19,"bold"))
e1.grid(row=0,column=2,padx=10,columnspan=1,sticky="nesw")


lst=[]
operation=[]
num=0

def reset():
    #lst=[]
    #operation=[]
    e.delete(0,tk.END)
    e1.delete(0,tk.END)
def printing(n):
    global lst,operation,num
    if n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9 or n==0:
        num=(num*10)+n
    if n=="+" or n=="-" or n=="*" or n=="/":
        operation.append(n)
    e.insert(tk.END,n)

    if n=="=" or n=="+" or n=="-" or n=="*" or n=="/":
        lst.append(num)
        num=0
        
        
    if n=="=":
        equal_fun()    

def equal_fun():
    i=time.time()
    global lst,operation
   
    
    for i in range(len(operation)):
        if operation[i]=="+":
            r=lst[0]+lst[1]
        if operation[i]=="-":
            r=lst[0]-lst[1]
        if operation[i]=="*":
            r=lst[0]*lst[1]    
        if operation[i]=="/":
            r=lst[0]/lst[1] 
            #r=int("{:.2f}".format(r))   
        r=float("{:.2f}".format(r))    
        lst[0:2]=[r]
       
    e1.insert(0,r)
    operation=[]
    lst=[]
    f=time.time()
    #print(f,i)
    #print(f-i)



b1=tk.Button(text="1",width=0,height=1,fg="white",font=("a",20,"bold"),bg="black",command=lambda :printing(1))
b2=tk.Button(text="2",width=0,height=1,fg="white",font=("a",20,"bold"),bg="black",command=lambda :printing(2))
b3=tk.Button(text="3",width=0,height=1,fg="white",font=("a",20,"bold"),bg="black",command=lambda :printing(3))
b4=tk.Button(text="4",width=0,height=1,fg="white",font=("a",20,"bold"),bg="black",command=lambda :printing(4))
b5=tk.Button(text="5",width=0,height=1,fg="white",font=("a",20,"bold"),bg="black",command=lambda :printing(5))
b6=tk.Button(text="6",width=0,height=1,fg="white",font=("a",20,"bold"),bg="black",command=lambda :printing(6))
b7=tk.Button(text="7",width=0,height=1,fg="white",font=("a",20,"bold"),bg="black",command=lambda :printing(7))
b8=tk.Button(text="8",width=0,height=1,fg="white",font=("a",20,"bold"),bg="black",command=lambda :printing(8))
b9=tk.Button(text="9",width=0,height=1,fg="white",font=("a",20,"bold"),bg="black",command=lambda :printing(9))
b0=tk.Button(text="0",width=0,height=1,fg="white",font=("a",20,"bold"),bg="black",command=lambda :printing(0))

plus=tk.Button(text="+",bg="#774352",font=("s",30,"bold"),command=lambda :printing("+"))
equal=tk.Button(text="=",bg="#0600f7",font=("s",30,"bold"),command=lambda :printing("="))
minus=tk.Button(text="-",bg="#d8c5f8",font=("s",30,"bold"),command=lambda :printing("-"))
multiple=tk.Button(text="*",bg="#d8c5f8",font=("s",30,"bold"),command=lambda :printing("*"))
divid=tk.Button(text="/",bg="#d8c5f8",font=("s",30,"bold"),command=lambda :printing("/"))

plus.grid(row=4,column=1,sticky="nesw")
equal.grid(row=4,column=3,columnspan=1,sticky="nesw")
minus.grid(row=1,column=3,rowspan=2,sticky="nesw")
multiple.grid(row=3,column=3,rowspan=1,sticky="nesw")
divid.grid(row=4,column=2,sticky="nesw")

c=tk.Button(text="C",width=10,bg="#8bcf00",font=("lauda",15,"bold"),command=reset)
c.grid(row=0,column=3,columnspan=1,sticky="nesw")



b1.grid(row=1,column=0,sticky="ensw")
b2.grid(row=1,column=1,sticky="ensw")
b3.grid(row=1,column=2,sticky="ensw")
b4.grid(row=2,column=0,sticky="ensw")
b5.grid(row=2,column=1,sticky="ensw")
b6.grid(row=2,column=2,sticky="ensw")
b7.grid(row=3,column=0,sticky="ensw")
b8.grid(row=3,column=1,sticky="ensw")
b9.grid(row=3,column=2,sticky="ensw")
b0.grid(row=4,column=0,sticky="ensw")




window.mainloop()