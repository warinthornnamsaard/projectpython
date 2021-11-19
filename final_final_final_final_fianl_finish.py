from tkinter import *
from tkinter import ttk
from openpyxl import load_workbook
from openpyxl import workbook
import csv

lst0 = ['Security','Keep clean','Accounting Manager','Employees','IT Support','System Admin']
lst1 = {'Security':'Security','Keep clean':'Keep clean','Accounting Manager':'Accounting Manager',
'Employees':'Employees','IT Support':'IT Support','System Admin':'System Admin'}                                       
lst2 = ['ลามากว่า 3 วันกดปุ่ม click']

salary = Tk()
salary.title('Salay pay')
salary.config(bg='wheat')
salary.minsize(700,600)
myinput1=StringVar()
myinput2=StringVar()
display1=StringVar()
display2=StringVar()
display3=StringVar()
display4=StringVar()
display5=StringVar()

clicklabel=Label(salary)
a=10000
leave = 250
SS = 750

N = StringVar()
SN = StringVar()
lstEP = StringVar()
lstEP.set('Security')
thb=0

#
allname = []
lst = []
#



def leave_():
    try:
        global thb
        input_usd = eval(myinput1.get())
        thb = input_usd*leave
        display1.set('เงินที่หักตามจำนวนวันหยุดของคุณ={0:.2f} THB'.format(thb))
        print(thb)
        return thb
    except Exception:
        print('ค่าที่ใส่ต้องเป็นตัวเลขเท่านั้น')
    
#แสดงData file
def number():
    global Netsalary
    IN = eval(myinput2.get())
    try:
        with open('Employees.csv','r',encoding='utf-8')as infile:       #Data file
            rd = csv.reader(infile)
            mylist =  list(rd)
        for row in mylist:
            row = len(mylist)
        i=101
        n=0
        for v in range(0,row):
            number = i + v
            if IN == number:
                information=mylist[IN-i]
        salary=information[4]
        department=information[3]
        sname=information[2]
        name=information[1]
        ID=information[0]
    
        display2.set('Your ID :{} Your name is :{} {}\n Your departmant :{} Your salary :{} '.format(ID,name,sname,department,salary))
        totalsalary=(int(salary))
        Netsalary=totalsalary-thb-SS
        display3.set('NetSalary = {} THB'.format(Netsalary))
        display5.set('Social security = {} THB'.format(SS))

    except Exception as e:
        print('เลขประจำตัวเริ่มจาก 101 เป็นต้นไป')
    
    
#ขึ้นหน้าต่างใหม่
def NewWindow():                                            #fucntion
    NW = Toplevel()
    NW.title('Register')
    NW.config(bg='#FFFFCC')
    def click_(C=0):                                        #fucntion
        global ent
        ent = Label(NW,text = lstEP.get())
        ent.grid(row=2,column=4)
        lb = Label(NW, text='แผนกของคุณคือ')
        lb.grid(row=2 ,column= 3)
        return C

    def cancel_():                                          #fucntion
        ent.destroy()
        

    command = ""
    username = ""
    lst=[]

    def Register():                                         #fucntion
        global YN
        global YSN
        global EMP
        global lst
        v = len(lst0)
        i=101
        number_=0
        YN = N.get()
        YSN = SN.get()
        EMP = lstEP.get()
        try:
            with open('Employees.csv','r',encoding='utf-8')as infile:       #read file
                rd = csv.reader(infile)
                mylist =  list(rd)
            for row in mylist:
                row = len(mylist)
                number_=i+row
                
        except Exception as e:
            print('file not found')
        
        for i in range(v):
            if EMP == lst0[0]:                      #if else
                salary = 15000
            elif EMP == lst0[1]:
                salary = 13500
            elif EMP == lst0[2]:
                salary = 25000
            elif EMP == lst0[3]:
                salary = 20000
            elif EMP == lst0[4]:
                salary = 33000
            else :
                salary = 35500

        lst.append(number_)
        lst.append(YN)
        lst.append(YSN)
        lst.append(EMP)
        lst.append(salary)
        
        try:
            with open("Employees.csv", "a",encoding='utf-8')as f:           #write file
                R = csv.writer(f,lineterminator='\n')
                R.writerow(lst)
        
            display4.set('Your ID= {} '.format(number_))
            NoID=Label(NW,textvariable=display4,font='Helvetica 11',bg='white')
            NoID.grid(row=9,column=2,pady=2)
        except Exception as e:
            print(e)

        lst.clear()
        
    ls = Entry(NW, textvariable = SN )
    ls.grid(row = 2, column = 2, pady = 10)

    ls_2 = Entry(NW, textvariable = N )
    ls_2.grid(row = 1, column = 2, pady = 10)

    lbs_2 = Label(NW, text = 'Name', font='Helvetica 11',bg='white')
    lbs_2.grid(row = 1, column = 1)

    
    lbs_3 = Label(NW, text = 'Surename', font='Helvetica 11',bg='white')
    lbs_3.grid(row = 2, column = 1)


    lbs = Label(NW, text = 'Select Department', font='Helvetica 11',bg='white')
    lbs.grid(row = 3, column = 1)

    i = 2
    for t, v in lst1.items():                                       #loop
        Depart = Radiobutton(NW, text=t, value=v ,width=18 ,anchor=W, variable=lstEP)
        Depart.grid(row=i+1, column=2)
        i += 1


    btClick = Button(NW, text='Click',command = click_,width = 15,bg='green')
    btClick.grid(row=3, column=4)
    btClick.bind('<Button-1>',click_)

    btCancel = Button(NW, text='Cancel',command = cancel_,width = 15,bg='red',fg='white')
    btCancel.grid(row=4, column=4)

    btWrite = Button(NW, text='Confirm',command = Register,width = 15,bg='lightgreen')
    btWrite.grid(row=5, column=4)



    NW.mainloop()



#
lea=()

Salay=Label(salary,text='Salay Pay',font='Helvetica 11',bg='white')
Salay.grid(row=0, column=2,pady=10)

photo = PhotoImage(file = 'history-04.png')                         #Data File
pt = Label(salary, image = photo)
pt.grid(row = 1, column = 1, columnspan = 4)

myinput = StringVar()
display = StringVar()
le = StringVar()

Newemp=Label(salary,text='New Employees please Enter register here--->!!!',font='Helvetica 11',bg='red',fg='white')
Newemp.grid(row=10,column=2,pady=10)

IDNUM=Label(salary,text='Enter you identification number',font='Helvetica 11',bg='white')
IDNUM.grid(row=4,column=1,pady=10)

inp2 = Entry(salary,textvariable=myinput2,width=10)
inp2.grid(row=4,column=2,sticky=W)

inp2.focus()


lb0=Label(salary,text='Leave Work',font='Helvetica 15',bg='white')
lb0.grid(row=3,column=1,padx=2,pady=5)

inp = Entry(salary,textvariable=myinput1,width=10)
inp.grid(row=3,column=2,sticky=W)

lb3=Label(salary,textvariable=display3,font='Helvetica 11',width = 30,bg='white')
lb3.grid(row=9,column=2,pady=2)

#
lb2=Label(salary,textvariable=display2,font='Helvetica 11',width = 50,bg='white')
lb2.grid(row=7,column=2,pady=2)


#
lbl=Label(salary,textvariable=display1,font='Helvetica 11',bg='white')
lbl.grid(row=5,column=2,pady=2)


lb4=Label(salary,textvariable=display5,font='Helvetica 11',width = 50,bg='white')
lb4.grid(row=8,column=2,pady=2)


btOK = Button(salary ,  text = 'OK', command = leave_,width = 15,bg='green')
btOK.grid(row = 3, column = 3,pady = 10)

btclose = Button(salary, text = 'Close', command = salary.destroy, width = 15,bg='red',fg='white')
btclose.grid(row = 5, column = 3,pady = 10)

btregis =Button(salary,text='Register',command = NewWindow,width=15,bg='yellow')
btregis.grid(row = 10, column =3 ,pady= 10)

#
btregis =Button(salary,text='Confirm',command = number,width=15,bg='green')
btregis.grid(row = 4, column =3 ,pady= 10)
#
salary.mainloop()


'''lm = ttk.Combobox(salary, values = list(lst0), textvariable = lstm )
lm.grid(row = 3, column = 2, pady = 10)''' #เลือกโดยมีแถบ
