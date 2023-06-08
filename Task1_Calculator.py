#import tkinter
from tkinter import *
import math
root=Tk()
blank_space= ""
root.title(50*blank_space + 'Codeclause calculator')
root.resizable(width=False,height=False)
root.geometry('438x573+460+40')

coverFrame= Frame (root, bd =20, pady=2,bg='blue', relief=RIDGE)
coverFrame.grid()

covermainFrame= Frame (coverFrame, bd =10, pady=2, bg='black', relief=RAISED)
covermainFrame.grid()

mainFrame= Frame (covermainFrame, bd =5, pady=2,bg='green' ,relief=RIDGE)
mainFrame.grid()

class calculator():
    def __init__(self):
        self.total=0
        self.curr=""
        self.input_val=True
        self.check_sum=False
        self.op=""
        self.result=False

    def Enternumber(self,num):
        self.result=False
        firstnum=entDisplay.get()
        
        secondnum=str(num)
        if self.input_val:
            self.curr=secondnum
            self.input_val=False
        else:
            if secondnum =='.':
                if secondnum in firstnum:
                   return
            self.curr=firstnum+secondnum
        self.display(self.curr)
    def display(self,value):
        entDisplay.delete(0,END)
        entDisplay.insert(0,value)

    def sum_of_total(self):
        self.result=True 
        self.curr=float(self.curr)
        if self.check_sum==True:
            self.valid_function()
        
        else:
            self.total=float(entDisplay.get())
    
    def valid_function(self):
        if self.op=='add':
            self.total+=self.curr 
        if self.op=='sub':
            self.total-=self.curr
        if self.op=='mul':
            self.total*=self.curr 
        if self.op=='div':
            self.total/=self.curr
        if self.op=='mod':
            self.total%=self.curr

        self.input_val=True
        self.check_sum=False
        self.display(self.total)

    def operation(self,op):
        self.curr=float(self.curr)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.curr
            self.input_val=True
        self.check_sum=True
        self.op=op
        self.result=False

    def backspace(self):
        numLen=len(entDisplay.get())
        entDisplay.delete(numLen-1,'end')
        if numLen==1:
            entDisplay.insert(0,'0')
              
    def ClearEntry(self):
        self.result=False
        self.curr='0'
        self.display(0)
        self.input_val=True 
    def all_clear_Entr(self):
        self.ClearEntry()
        self.total=0

    def sqrt(self):
        self.result=False
        self.curr=math.sqrt(float(entDisplay.get()))
        self.display(self.curr)
    
    def plsmins(self):
        self.result=False
        self.curr=-(float(entDisplay.get()))
        self.display(self.curr)
    
    def cos(self):
        self.result=False
        self.curr=math.cos(math.radians(float(entDisplay.get())))
        self.display(self.curr)
    
    def tan(self):
        self.result=False
        self.curr=math.tan(math.radians(float(entDisplay.get())))
        self.display(self.curr)

    def sin(self):
        self.result=False
        self.curr=math.sin(math.radians(float(entDisplay.get())))
        self.display(self.curr)


added_value=calculator()
entDisplay = Entry(mainFrame, font=('arial' , 18, 'bold'),bd=14 ,width=26,bg='grey', justify=RIGHT)
entDisplay.grid(row=0,column=0,columnspan=4,pady=1)
entDisplay.insert(0,"0")

numberpad="789456123"
i=0
btn=[]

for j in range(3,6):
    for k in range(3):
        btn.append(Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text=numberpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]['command']=lambda x=numberpad[i]: added_value.Enternumber(x)
        i+=1

btnB_space=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text="←" ,bg='cadetblue', command=added_value.backspace)
btnB_space.grid(row=1,column=0,pady=1)

btn_clear=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text=chr(67) ,bg='cadetblue', command=added_value.ClearEntry)
btn_clear.grid(row=1,column=1,pady=1)

btn_clearAll=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text=chr(67)+chr(69) ,bg='cadetblue',command=added_value.all_clear_Entr)
btn_clearAll.grid(row=1,column=2,pady=1)

btn_PM=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text=chr(177) ,bg='cadetblue',command=added_value.plsmins)
btn_PM.grid(row=1,column=3,pady=1)

btn_sqrt=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text="√" ,bg='cadetblue', command=added_value.sqrt)
btn_sqrt.grid(row=2,column=0,pady=1)

btn_cos=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text="Cos" ,bg='cadetblue',command=added_value.cos)
btn_cos.grid(row=2,column=1,pady=1)

btn_Tan=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text="Tan" ,bg='cadetblue', command=added_value.tan)
btn_Tan.grid(row=2,column=2,pady=1)

btn_Sin=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text="Sin" ,bg='cadetblue',command=added_value.sin)
btn_Sin.grid(row=2,column=3,pady=1)


btn_div=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text="/" ,bg='cadetblue' ,command=lambda:added_value.operation('div'))
btn_div.grid(row=3,column=3,pady=1)

btn_mul=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text="*" ,bg='cadetblue',command=lambda:added_value.operation('mul'))

btn_mul.grid(row=4,column=3,pady=1)

btn_add=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text="+" ,bg='cadetblue',command=lambda:added_value.operation('add'))

btn_add.grid(row=6,column=3,pady=1)

btn_sub=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text="-" ,bg='cadetblue',command=lambda:added_value.operation('sub'))

btn_sub.grid(row=5,column=3,pady=1)

btn_zero=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text="0" ,bg='cadetblue',command=lambda:added_value.Enternumber(0))

btn_zero.grid(row=6,column=1,pady=1)

btn_dot=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text="." ,bg='cadetblue',command=lambda:added_value.Enternumber("."))
btn_dot.grid(row=6,column=2,pady=1)

btn_eql=Button(mainFrame,width=6,height=2,font=('arial',16,'bold'), bd=4,text="=" ,bg='cadetblue',command=lambda:added_value.sum_of_total())
btn_eql.grid(row=6,column=0,pady=1)



root.mainloop()
