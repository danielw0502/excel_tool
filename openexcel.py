# This Python file uses the following encoding: utf-8

from Tkinter import *
from tkFileDialog import askopenfilename
from readexcel_column import *
from writeexcel_column import *
from itertools import compress


def topLevel():

    file_name = askopenfilename()
    column_1rowname, column_name = draw_column(file_name)

    top = Toplevel()

    frame=Frame(top)
    frame.pack(fill="both")


    S = Scrollbar(frame, orient="vertical")
    text = Text(frame, width=20, height=20, yscrollcommand=S.set)
    S.config(command=text.yview)
    S.pack(side="right",fill="y")
    text.pack(side="left",fill="x")


    #put the checkbutton into a frame
    small_frame=Frame(frame)
    global vars
    vars=[]

    for i, j in enumerate(column_1rowname):
        var = IntVar()
        chk = Checkbutton(small_frame, text=j, variable=var)
        chk.pack()
        vars.append(var)

    #add the frame to the text
    text.window_create("end", window=small_frame)
    text.config(state=DISABLED)


    #separator=Frame(top,height=21,bd=1,relief=SUNKEN)
    #separator.pack(fill="x")



    #choose the file
    frame2=Frame(top)
    frame2.pack()
    Label(frame2,text="File you want to save").pack(side="left")

    e1=Entry(frame2)
    e1.pack(side="left")

    global dest_file
    dest_file = ""

    def choose():
        name=askopenfilename()
        e1.insert(0,name)


    bton=Button(frame2,text="Browse",command=choose)
    bton.pack(side="right")

    #buttom button in a frame
    frame3=Frame(top)
    frame3.pack(side="bottom")

    def select_column(a=column_name):


        global dest_file
        dest_file = e1.get()

        global index_column,vars
        index_column = list(map((lambda var: var.get()), vars))
        #print index_column
        select_column_name = list(compress(a, index_column))
        top.quit()

        write_column(dest_file=dest_file , original_file=file_name, column_name=select_column_name)

    bt=Button(frame3,text="Confirm",command=select_column)
    bt.pack(fill="x")


    top.resizable(width=False, height=False)




root = Tk()
root.geometry('200x100')
root.resizable(width=False,height=False)
root.wm_title("Choose The Column")


def About():
    top=Toplevel()
    w=Label(top,text="LTE 解决方案设计部 \n Author:王先达")
    w.pack()


menu=Menu(root)
helpmenu=Menu(root)
root.config(menu=menu)
menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About...",command=About)


errmsg='Error!'
Label(text="Choose a File").pack(side="left")
Button(text='File Open',command=topLevel).pack(side="left",fill=X)



mainloop()