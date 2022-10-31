from tkinter import *
from os import abort
import tkinter
import pandas as pd
import math, getpass
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import sys,os

us=getpass.getuser()

root=tkinter.Tk()
root.title('File Splitter')
# root.iconbitmap('immy-logo.ico')
root.geometry('350x250')
root.maxsize(350,250)
root.minsize(350,250)

def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )
path=resource_path('bg-1.png')
bg=PhotoImage(file=path)
bk=Label(root,image=bg)
bk.place(x=0,y=0,relwidth=1,relheight=1)

def split(strval,endval):
    
    if var.get()==str('csv'):
        
        file2=askopenfilename(title='Choose CSV file only',filetypes=[("CSV files", ".csv")])
        file=pd.read_csv(file2,low_memory=False,on_bad_lines='skip')
        if len(file2) > 0:
    
            df=pd.DataFrame(file)
                    
                    
            for i in range(0,math.ceil(len(df)/strval)):
                    cn=(math.ceil(len(df)/strval))
                    a=strval*i #start range is 0
                    b=endval*i #last range
                    if i > 0:
                                   a=a+1
                    res=df.loc[a+0:endval+b]
                    res.to_csv('SplitFile_'+str(i+1)+'_.csv',index=False) 
                    a=0
        messagebox.showinfo('Done',"Split into "+str(cn)+' Files')            
    elif var.get()==str('excel'):
        
        file2=askopenfilename(title='Excel file only',filetypes=[("Excel files", ".xlsx .xls")])
        if len(file2) > 0:
    
            file=pd.read_excel(file2)

            df=pd.DataFrame(file)
                    
                    
            for i in range(0,math.ceil(len(df)/strval)):
                    cn=(math.ceil(len(df)/strval))
                    a=strval*i #start range is 0
                    b=endval*i #last range
                    if i > 0:
                                   a=a+1
                    res=df.loc[a+0:endval+b]
                    res.to_excel('SplitFile_'+str(i+1)+'_.xlsx',index=False) 
                    a=0
        messagebox.showinfo('Done',"Split into "+str(cn)+' Files')

def num():
    strval=div_value.get()
    endval=div_value.get()
    split(strval,endval)


var=StringVar(None)
div_value=IntVar(value='500000')
rd1=Radiobutton(root,text='CSV File',variable=var,value='csv')
rd1.place(x=90,y=80)
rd2=Radiobutton(root,text='Excel File',variable=var,value='excel')
rd2.place(x=180,y=80)
inp=Entry(root,textvariable=div_value)
inp.place(x=190,y=115)
vv=Label(root,text='Default rows divide value is :',fg='white',bg='#000000',font=("Helvetica", 8, "bold"))
vv.place(x=28,y=115)
vv=Label(root,text='You can change the above value',fg='red',bg='#000000')
vv.place(x=75,y=150)
wel=Label(root,text='Welcome!',font=('Calibri', 25),fg='white',bg='#000000').pack(pady=9)
nam=Label(root,text=us,font=('Calibri', 10),fg='white',bg='#000000')
nam.place(x=130,y=50)
bt=Button(root,text='OK',command=num,width=10,font=("Helvetica", 10, "bold"))
bt.place(x=130,y=180)
cc=Label(root,text='© Imtiyaz Shaikh',fg='white',bg='#000000')
cc.place(x=250,y=230)
ver=Label(root,text='Version_1.0',fg='white',bg='#000000')
ver.place(x=3,y=3)




root.mainloop()
