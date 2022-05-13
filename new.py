from cProfile import label
# from cgitb import text
# from msilib.schema import ListBox
# from operator import ge
from tkinter import*
from tkinter import font
from tkinter import ttk
import mysql.connector 
from tkinter import messagebox
import datetime
import tkinter
import random
import string

class User_Inter:
    def face(self,root):
        self.root=root
        self.root.title("Library Management System")
        # self.root.geometry("1550X800+0+0")
        
        #=================================variable=========================================
        self.member_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address_var=StringVar()
        self.postcode_var=StringVar()
        self.mobilenumber_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalpricevar=StringVar()
        self.username1=StringVar()
        self.password1=StringVar()
        self.firstname1=StringVar()
        self.password1=StringVar()
        self.lastname1=StringVar()
        
        # labeltitle=Label(self.root,text="Library Management System",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("Futura",30,"bold"))
        # labeltitle.pack()
        
        #============border around the input fields and output fields
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="white")
        frame.place(x=0,y=90,width=1530,height=340)
        
        #=============frame======left==========================
        frameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        frameLeft.place(x=0,y=5,width=780,height=300)
        
        #===========labels for the input fields===============
        MemberType=Label(frameLeft,bg="powder blue",fg="green",text="Member Type",font=("times new roman",13,"bold"),padx=2,pady=6)
        MemberType.grid(row=0,column=0,sticky=W)
        
        comboItems=ttk.Combobox(frameLeft,font=("times new roman",15,"bold"),width=27,state="readonly",textvariable=self.member_var)
        comboItems["value"]=("Admin Staff","Student","Lecturer")
        comboItems.grid(row=0,column=1)
        
        labelNumber=Label(frameLeft,bg="powder blue",fg="green",text="ID Number :",font=("times new roman",13,"bold"))
        labelNumber.grid(row=1,column=0,sticky=W)
        
        firstname=Label(frameLeft,bg="powder blue",fg="green",text="First Name :",font=("times new roman",13,"bold"))
        firstname.grid(row=1,column=0,sticky=W)
        lastname=Label(frameLeft,bg="powder blue",fg="green",text="Last Name :",font=("times new roman",13,"bold"))
        lastname.grid(row=2,column=0,sticky=W)
        idNumber=Label(frameLeft,bg="powder blue",fg="green",text="Id Number :",font=("times new roman",13,"bold"))
        idNumber.grid(row=3,column=0,sticky=W)
        residentialAddress=Label(frameLeft,bg="powder blue",fg="green",text="Residential Address :",font=("times new roman",13,"bold"))
        residentialAddress.grid(row=4,column=0,sticky=W)
        postalcode=Label(frameLeft,bg="powder blue",fg="green",text="Postal Address :",font=("times new roman",13,"bold"))
        postalcode.grid(row=5,column=0,sticky=W)
        mobilenumber=Label(frameLeft,bg="powder blue",fg="green",text="Mobile Number :",font=("times new roman",13,"bold"))
        mobilenumber.grid(row=6,column=0,sticky=W)
        bookid=Label(frameLeft,bg="powder blue",fg="green",text="Book Id :",font=("times new roman",13,"bold"))
        bookid.grid(row=7,column=0,sticky=W)
        booktitle=Label(frameLeft,bg="powder blue",fg="green",text="Book Title :",font=("times new roman",13,"bold"),padx=5)
        booktitle.grid(row=0,column=3,sticky=W)
        authorname=Label(frameLeft,bg="powder blue",fg="green",text="Author Name :",font=("times new roman",13,"bold"),padx=5)
        authorname.grid(row=1,column=3,sticky=W)
        dateborrowed=Label(frameLeft,bg="powder blue",fg="green",text="Date Borrowed :",font=("times new roman",13,"bold"),padx=5)
        dateborrowed.grid(row=2,column=3,sticky=W)
        datedue=Label(frameLeft,bg="powder blue",fg="green",text="Date Due :",font=("times new roman",13,"bold"),padx=5)
        datedue.grid(row=3,column=3,sticky=W)
        daysonbook=Label(frameLeft,bg="powder blue",fg="green",text="Days On Book :",font=("times new roman",13,"bold"),padx=5)
        daysonbook.grid(row=4,column=3,sticky=W)
        latereturnfine=Label(frameLeft,bg="powder blue",fg="green",text="late return fine:",font=("times new roman",13,"bold"),padx=5)
        latereturnfine.grid(row=5,column=3,sticky=W)
        dateoverdue=Label(frameLeft,bg="powder blue",fg="green",text="Date Over Due :",font=("times new roman",13,"bold"),padx=5)
        dateoverdue.grid(row=6,column=3,sticky=W)
        finalprice=Label(frameLeft,bg="powder blue",fg="green",text="Actual Price :",font=("times new roman",13,"bold"),padx=5)
        finalprice.grid(row=7,column=3,sticky=W)
        #for the firstname text field
        first_name=Entry(frameLeft,font=("arial",13,"bold"),width=32,textvariable=self.firstname_var)
        first_name.grid(row=1,column=1,pady=4)
        last_name=Entry(frameLeft,font=("arial",13,"bold"),width=32,textvariable=self.lastname_var)
        last_name.grid(row=2,column=1,pady=4)
        id_number=Entry(frameLeft,font=("arial",13,"bold"),width=32 ,textvariable=self.id_var,state="readonly")
        id_number.grid(row=3,column=1,pady=4)
        postal_code=Entry(frameLeft,font=("arial",13,"bold"),width=32,textvariable=self.postcode_var)
        postal_code.grid(row=4,column=1,pady=4)
        residential_address=Entry(frameLeft,font=("arial",13,"bold"),width=32,textvariable=self.address_var)
        residential_address.grid(row=5,column=1,pady=4)
        mobile_number=Entry(frameLeft,font=("arial",13,"bold"),width=32,textvariable=self.mobilenumber_var)
        mobile_number.grid(row=6,column=1,pady=4)
        book_id=Entry(frameLeft,font=("arial",13,"bold"),width=32,textvariable= self.bookid_var)
        book_id.grid(row=7,column=1,pady=4)
        book_title=Entry(frameLeft,font=("arial",13,"bold"),width=15,textvariable=self.booktitle_var)
        book_title.grid(row=0,column=4)
        author_name=Entry(frameLeft,font=("arial",13,"bold"),width=15,textvariable=self.author_var)
        author_name.grid(row=1,column=4)
        date_borrowed=Entry(frameLeft,font=("arial",13,"bold"),width=15,textvariable=self.dateborrowed_var)
        date_borrowed.grid(row=2,column=4)
        date_due=Entry(frameLeft,font=("arial",13,"bold"),width=15,textvariable=self.datedue_var)
        date_due.grid(row=3,column=4)
        days_on_book=Entry(frameLeft,font=("arial",13,"bold"),width=15,textvariable=self.daysonbook_var)
        days_on_book.grid(row=4,column=4)
        late_return_fine=Entry(frameLeft,font=("arial",13,"bold"),width=15,textvariable=self.lateratefine_var)
        late_return_fine.grid(row=5,column=4)
        date_overdue=Entry(frameLeft,font=("arial",13,"bold"),width=15,textvariable=self.dateoverdue_var)
        date_overdue.grid(row=6,column=4)
        final_price=Entry(frameLeft,font=("arial",13,"bold"),width=15,textvariable=self.finalpricevar)
        final_price.grid(row=7,column=4)
        
        #================frameright=========================
        frameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        frameRight.place(x=790,y=5,width=450,height=300)
        #================righttextbox==============================
        self.txtbox=Text(frameRight,font=("helvetica",10,"bold"),fg="green",width=24,height=15.5,padx=24,pady=0)
        self.txtbox.grid(row=0,column=2)
        listScrollbar=Scrollbar(frameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        Listbooks=['Numerical Methods','Research Methods','African Studies','Animal Husbandry','Linear Algebra','Agriculture',
                   'Biochemistry','Radiology','Artificial Intelligence','Psychology']
       
        #loop item in the listbooks
   
       
        