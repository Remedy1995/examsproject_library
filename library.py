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
import book as booka
# import generatenumbers
# from generatenumbers import (GenerateBookID,Generate)
from generatenumbers import MySample
from new import User_Inter
from Adminoption import AdminOption




class Library_Management:
    # def __init__(self,root):
    def Manage(self,root):
        self.root=root
        self.root.title("Library Management System")
     
        
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
        self.bookid1=StringVar()
        self.author1=StringVar()
        self.description1=StringVar()
        self.booktitle1=StringVar()
        self.usernameid1=StringVar()
        self.oldpassword1=StringVar()
        self.newpassword1=StringVar()
        self.title2=StringVar()
        self.description2=StringVar()
        self.bookid2=StringVar()
        self.author2=StringVar()
        self.bookfindvar=StringVar()
        self.bookfindvar1=StringVar()
        self.title3=StringVar()
        self.title4=StringVar()
        self.description4=StringVar()
        self.bookid4=StringVar()
        self.author4=StringVar()
        self.description3=StringVar()
        self.bookid3=StringVar()
        self.author3=StringVar()
        # labeltitle=Label(self.root,text="Library Management System",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("Futura",30,"bold"))
        # labeltitle.pack()
        
        #============border around the input fields and output fields
        #===============make the header
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="white")
        frame.place(x=0,y=70,width=1530,height=500)
        FrameDetail=LabelFrame(self.root,bd=12,relief=RIDGE,bg="powder blue",padx=10)
        FrameDetail.place(x=0,y=500,width=900,height=300)
        Table_fram=Frame(FrameDetail,bd=6,relief=RIDGE,bg="powder blue")
        Table_fram.place(x=0,y=2,width=850,height=140)
        xscroll=ttk.Scrollbar(Table_fram,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_fram,orient=VERTICAL)
        self.library_tabl=ttk.Treeview(Table_fram,column=("ID","Book Title","Book Description","Book ID","Author Name"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set
                                         )
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_tabl.xview)
        yscroll.config(command=self.library_tabl.yview)
        
        self.library_tabl.heading("ID",text="ID")
        self.library_tabl.heading("Book Title",text="Book Title")
        self.library_tabl.heading("Book Description",text="Book Description")
        self.library_tabl.heading("Book ID",text="Book ID")
        self.library_tabl.heading("Author Name",text="Author Name")
        self.library_tabl["show"]="headings"
        self.library_tabl.pack(fill=BOTH,expand=1)
        self. fetchBooks()
        self.library_tabl.bind("<ButtonRelease-1>",self.getCursor1)

        def getCursor1(self,event=""):
         cursor_row=self.library_tabl.focus()
         content=self.library_tabl.item(cursor_row)  
         row=content["values"]
         if(row):
              
              self.title2.set(row[1])
              self.description2.set(row[2])
              self.author2.set(row[3])
              self.bookid2.set(row[4])

         UserDetail1=LabelFrame(self.root,bd=12,relief=RIDGE,bg="powder blue",padx=10)
         UserDetail1.place(x=870,y=500,width=500,height=300)
        #==================table======frame================================
         User_fram1=Frame(UserDetail1,bd=6,relief=RIDGE,bg="powder blue")
         User_fram1.place(x=0,y=2,width=460,height=140)
         xscroll=ttk.Scrollbar(User_fram1,orient=HORIZONTAL)
         yscroll=ttk.Scrollbar(User_fram1,orient=VERTICAL)
         self.library_tabl2=ttk.Treeview(User_fram1,column=("ID","First Name","Last Name","User Name"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set
                                         )
         xscroll.pack(side=BOTTOM,fill=X)
         yscroll.pack(side=RIGHT,fill=Y)
        
         xscroll.config(command=self.library_tabl2.xview)
         yscroll.config(command=self.library_tabl2.yview)
        
         self.library_tabl2.heading("ID",text="ID")
         self.library_tabl2.heading("First Name",text="First Name")
         self.library_tabl2.heading("Last Name",text="Last  Name")
         self.library_tabl2.heading("User Name",text="User Name")
         self.library_tabl2["show"]="headings"
         self.library_tabl2.pack(fill=BOTH,expand=1)
         self.fetchUsers()
         self.library_tabl2.bind("<ButtonRelease-1>",self.getCursor2)


        def getCursor2(self,event=""):
         cursor_row=self.library_tabl2.focus()
         content=self.library_tabl2.item(cursor_row)  
         row=content["values"]
         if(row):
           self.firstname1.set(row[1])
           self.lastname1.set(row[2])
           self.username1.set(row[3])
        self.root=root
        label=Label(self.root,text="Admin Dashboard",bg="powder blue",fg="green",bd=10,relief=RIDGE,font=("Futura",20,"bold"))
        label.place(y=0,x=580)
          #======================InformationFrame============
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
        # finalprice=Label(frameLeft,bg="powder blue",fg="green",text="Actual Price :",font=("times new roman",13,"bold"),padx=5)
        # finalprice.grid(row=7,column=3,sticky=W)
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
        # final_price=Entry(frameLeft,font=("arial",13,"bold"),width=15,textvariable=self.finalpricevar)
        # final_price.grid(row=7,column=4)
        
        #================frameright=========================
        frameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        frameRight.place(x=790,y=5,width=450,height=300)
        #================righttextbox==============================
        self.txtbox=Text(frameRight,font=("helvetica",10,"bold"),fg="green",width=24,height=15.5,padx=24,pady=0)
        self.txtbox.grid(row=0,column=2)
        listScrollbar=Scrollbar(frameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        ##return the books in the database
       

        Listbooks=['Numerical Methods','Research Methods','African Studies','Animal Husbandry','Linear Algebra','Agriculture',
                   'Biochemistry','Radiology','Artificial Intelligence','Psychology']
        
        conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
        mycursor=conn.cursor()     
        sql ="SELECT Book_title from books"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if(myresult):
            for x in myresult:
               new_lst=(','.join(x))
               Listbooks.append(new_lst)
        #loop item in the listbooks
   
       
        
        def Selectbox(event=""):
            

            value=listBox.get(listBox.curselection())
            print(value)
            x=value
           
            if (x==Listbooks[0]):
                self.bookid_var.set(MySample.GenerateBookID())
                self.booktitle_var.set(Listbooks[0])
                self.id_var.set(MySample.Generate())
                self.author_var.set("John legend")
                #get today's date
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("GHC 100")
                self.finalpricevar.set("GHC 0.00")
                self.dateoverdue_var.set("NO")
            elif (x==Listbooks[1]):
                    self.bookid_var.set(MySample.GenerateBookID())
                    self.id_var.set(MySample.Generate())
                    self.booktitle_var.set(Listbooks[1])
                    self.author_var.set("Kennedy Orleans")
                    #get today's date
                    d1=datetime.datetime.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("GHC 100")
                    self.finalpricevar.set("GHC 0.00")
                    self.dateoverdue_var.set("NO")
            elif (x==Listbooks[2]):
                    self.bookid_var.set(MySample.GenerateBookID())
                    self.id_var.set(MySample.Generate())
                    self.booktitle_var.set(Listbooks[2])
                    self.author_var.set("John legend")
                    #get today's date
                    d1=datetime.datetime.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("GHC 100")
                    self.finalpricevar.set("GHC 0.00")
                    self.dateoverdue_var.set("NO")
                    
            elif (x==Listbooks[3]):
                    self.bookid_var.set(MySample.GenerateBookID())
                    self.booktitle_var.set(Listbooks[3])
                    self.id_var.set(MySample.Generate())
                    self.author_var.set("John legend")
                    #get today's date
                    d1=datetime.datetime.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("GHC 100")
                    self.finalpricevar.set("GHC 0.00")
                    self.dateoverdue_var.set("NO")     
            elif (x==Listbooks[4]):
                    self.bookid_var.set(MySample.GenerateBookID())
                    self.id_var.set(MySample.Generate())
                    self.booktitle_var.set(Listbooks[4])
                    self.author_var.set("John legend")
                    #get today's date
                    d1=datetime.datetime.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("GHC 100")
                    self.finalpricevar.set("GHC 0.00")
                    self.dateoverdue_var.set("NO")  
            elif (x==Listbooks[5]):
                    self.bookid_var.set(MySample.GenerateBookID())
                    self.id_var.set(MySample.Generate())
                    self.booktitle_var.set(Listbooks[5])
                    self.author_var.set("John legend")
                    #get today's date
                    d1=datetime.datetime.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("GHC 100")
                    self.finalpricevar.set("GHC 0.00")
                    self.dateoverdue_var.set("NO") 
            elif (x==Listbooks[6]):
                    self.bookid_var.set(MySample.GenerateBookID())
                    self.id_var.set(MySample.Generate())
                    self.booktitle_var.set(Listbooks[6])
                    self.author_var.set("John legend")
                    #get today's date
                    d1=datetime.datetime.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("GHC 100")
                    self.finalpricevar.set("GHC 0.00")
                    self.dateoverdue_var.set("NO")
            elif (x==Listbooks[7]):
                    self.bookid_var.set(MySample.GenerateBookID())
                    self.id_var.set(MySample.Generate())
                    self.booktitle_var.set(Listbooks[7])
                    self.author_var.set("John legend")
                    #get today's date
                    d1=datetime.datetime.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("GHC 100")
                    self.finalpricevar.set("GHC 0.00")
                    self.dateoverdue_var.set("NO")   
            elif (x==Listbooks[8]):
                    self.bookid_var.set(MySample.GenerateBookID())
                    self.id_var.set(MySample.Generate())
                    self.booktitle_var.set(Listbooks[8])
                    self.author_var.set("John legend")
                    #get today's date
                    d1=datetime.datetime.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("GHC 100")
                    self.finalpricevar.set("GHC 0.00")
                    self.dateoverdue_var.set("NO") 
                
            elif (x==Listbooks[9]):
                    self.bookid_var.set(MySample.GenerateBookID())
                    self.id_var.set(MySample.Generate())
                    self.booktitle_var.set(Listbooks[9])
                    self.author_var.set("John legend")
                    #get today's date
                    d1=datetime.datetime.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("GHC 100")
                    self.finalpricevar.set("GHC 0.00")
                    self.dateoverdue_var.set("NO")  
            elif (x==Listbooks[10]):
                    self.bookid_var.set(MySample.GenerateBookID())
                    self.id_var.set(MySample.Generate())
                    self.booktitle_var.set(Listbooks[10])
                    self.author_var.set("John legend")
                    #get today's date
                    d1=datetime.datetime.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.lateratefine_var.set("GHC 100")
                    self.finalpricevar.set("GHC 0.00")
                    self.dateoverdue_var.set("NO")   
            else:
                print("the book you are searching for does not exist in our database sorry")
                             
        listBox=Listbox(frameRight, font=("helvetica",11,"bold"),width=22,height=13,fg="green",exportselection=False)
        listBox.bind("<<ListboxSelect>>",Selectbox)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)
     
        
        for item in Listbooks:
                listBox.insert(END,item)
            
        
 
        #=================ButtonsFrame====================
        buttonsFrame=LabelFrame(self.root,bd=12,relief=RIDGE,padx=15,bg="powder blue")
        buttonsFrame.place(x=0,y=435,width=1500,height=60)
        #===============add buttons to the buttons frame======================================
        btnadd_Data=Button(buttonsFrame,command=self.Add_Data,text="Add Data",font=("arial",12,"bold"),width=16,bg="green",fg="white")
        btnadd_Data.grid(row=0,column=0)
        btnshow_Data=Button(buttonsFrame,command=self.ShowData,text="Show Data",font=("arial",12,"bold"),width=16,bg="green",fg="white")
        btnshow_Data.grid(row=0,column=1)
        btnupdate_Data=Button(buttonsFrame,command=self.Update, text="Update ",font=("arial",12,"bold"),width=16,bg="green",fg="white")
        btnupdate_Data.grid(row=0,column=2)
        btndelete_Data=Button(buttonsFrame,text="Delete ",command=self.delete,font=("arial",12,"bold"),width=16,bg="green",fg="white")
        btndelete_Data.grid(row=0,column=3)
        btnreset_Data=Button(buttonsFrame,text="Reset ",command=self.reset,font=("arial",12,"bold"),width=16,bg="green",fg="white")
        btnreset_Data.grid(row=0,column=4)
        btnexit_Data=Button(buttonsFrame,text="Exit",command=self.Exit,font=("arial",12,"bold"),width=16,bg="green",fg="white")
        btnexit_Data.grid(row=0,column=5)
        btnexit_Data=Button(buttonsFrame,text="More options",command=self.More,font=("arial",12,"bold"),width=16,bg="green",fg="white")
        btnexit_Data.grid(row=0,column=6)
        #======================InformationFrame============
        FrameDetails=LabelFrame(self.root,bd=12,relief=RIDGE,bg="powder blue",padx=10)
        FrameDetails.place(x=0,y=500,width=1650,height=300)
        #==================table======frame================================
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1250,height=140)
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("ID","membertype","id number","first name","last name","residential address","postal code",'mobile number',"book id","book title",
         "author","date borrowed","date due","days due","late return fine","date over due","final price"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set
                                         )
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("ID",text="ID")
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("id number",text="ID Number")
        self.library_table.heading("first name",text="First Name")
        self.library_table.heading("last name",text="Last Name")
        self.library_table.heading("residential address",text="Residential Address")
        self.library_table.heading("postal code",text="Postal Address")
        self.library_table.heading("mobile number",text="Mobile  Number")
        self.library_table.heading("book id",text="Book ID")
        self.library_table.heading("book title",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("date borrowed",text="Date Borrowed")
        self.library_table.heading("date due",text="Date Due")
        self.library_table.heading("days due",text="Days On Book ")
        self.library_table.heading("late return fine",text="Late Return Fine")
        self.library_table.heading("date over due",text="Date Over Due")
        # self.library_table.heading("final price",text="Actual Price")
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        self.fetchData()
        self.library_table.bind("<ButtonRelease-1>",self.getCursor)
       




    def Add_Data(self):  
        if(self.member_var.get()==""):
           messagebox.showerror("Error","Please fill in the empty fields")
        elif(self.id_var.get()  ==""):
            messagebox.showerror("Error","Please fill in the empty fields")
        elif(self.firstname_var.get() ==""):
            messagebox.showerror("Error","Please fill in the empty fields")
        elif(self.lastname_var.get() ==""):
                messagebox.showerror("Error","Please fill in the empty fields")  
        elif(self.finalpricevar.get() ==""):
                messagebox.showerror("Error","Please fill in the empty fields")  
        elif(self.dateborrowed_var.get() ==""):
                messagebox.showerror("Error","Please fill in the empty fields")
        elif(self.datedue_var.get() ==""):
                messagebox.showerror("Error","Please fill in the empty fields")
        elif(self.dateoverdue_var.get() ==""):
                messagebox.showerror("Error","Please fill in the empty fields")
        elif(self.daysonbook_var.get() ==""):
                messagebox.showerror("Error","Please fill in the empty fields")
        elif(self.lateratefine_var.get() ==""):
                messagebox.showerror("Error","Please fill in the empty fields")
        elif(self.bookid_var.get() ==""):
                messagebox.showerror("Error","Please fill in the empty fields")
        elif(self.booktitle_var.get() ==""):
                messagebox.showerror("Error","Please fill in the empty fields")
        elif(self.author_var.get() ==""):
                messagebox.showerror("Error","Please fill in the empty fields") 
        elif(self.postcode_var.get() ==""):
                messagebox.showerror("Error","Please fill in the empty fields")  
        elif(self.address_var.get() ==""):
                messagebox.showerror("Error","Please fill in the empty fields")    
        else:
        #connect first to our mysql database
        
            conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
            mycursor=conn.cursor()
            if(mycursor):
                print('you have successfully connected to the database')
            else:
                print('there was an error in connecting to the database')
                
                #insert our data into the database
                # ("insert into mydata(%s)VALUES(self.member_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.address_var.get(),self.postcode_var.get(),self.mobilenumber_var.get(), self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.datedue_var.get()
                #                  ,self.daysonbook_var.get(),self.lateratefine_var.get(),self.dateoverdue_var.get(),self.finalpricevar.get()))"
            sql="INSERT into mydata(membertype,idnumber,firstname,lastname,residential_address,postcode,mobilenumber,bookid,booktitle,authorname,dateborrowed,datedue,daysonbook,latereturnfine,dateoverdue)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(self.member_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.address_var.get(),self.postcode_var.get(),self.mobilenumber_var.get(), self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),self.daysonbook_var.get(),self.lateratefine_var.get(),self.dateoverdue_var.get())
            mycursor.execute(sql,val)
            conn.commit()
            self.fetchData()
            # self.fetchBooks()
            # self.fetchUsers()
            self.reset()
            conn.close()        
            messagebox.showinfo("Success","messsage has been saved successfully")       
        
    def fetchData(self):
        connect=mysql.connector.connect(host="localhost",user="root",password="",database="library")   
        my_curs=connect.cursor()
        my_curs.execute("select * from mydata") 
        rows=my_curs.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            connect.commit()
        connect.close()
     #get the individual data of the member
    def fetchBooks(self):
        connect=mysql.connector.connect(host="localhost",user="root",password="",database="library")   
        my_curs=connect.cursor()
        my_curs.execute("select * from books") 
        rows=my_curs.fetchall()
        
        if len(rows)!=0:
            self.library_tabl.delete(*self.library_tabl.get_children())
            for i in rows:
                self.library_tabl.insert("",END,values=i)
            connect.commit()
        connect.close()
    def getCursor1(self,event=""):
         cursor_row=self.library_tabl.focus()
         content=self.library_tabl.item(cursor_row)  
         row=content["values"]
         if(row):
              
              self.title2.set(row[1])
              self.description2.set(row[2])
              self.author2.set(row[3])
              self.bookid2.set(row[4])
    def fetchUsers(self):
        connect=mysql.connector.connect(host="localhost",user="root",password="",database="library")   
        my_curs=connect.cursor()
        my_curs.execute("select * from users") 
        rows=my_curs.fetchall()
        
        if len(rows)!=0:
            self.library_tabl2.delete(*self.library_tabl2.get_children())
            for i in rows:
                self.library_tabl2.insert("",END,values=i)
            connect.commit()
        connect.close()
    def getCursor2(self,event=""):
         cursor_row=self.library_tabl2.focus()
         content=self.library_tabl2.item(cursor_row)  
         row=content["values"]
         if(row):
           self.firstname1.set(row[1])
           self.lastname1.set(row[2])
           self.username1.set(row[3])

    def getCursor(self,event=""):
         cursor_row=self.library_table.focus()
         content=self.library_table.item(cursor_row)  
         row=content["values"]
         if(row):
            self.member_var.set(row[0])
            self.member_var.set(row[1])
            self.id_var.set(row[2])
            self.firstname_var.set(row[3])
            self.lastname_var.set(row[4])
            self.address_var.set(row[5])
            self.postcode_var.set(row[6])
            self.mobilenumber_var.set(row[7])
            self.bookid_var.set(row[8])
            self.booktitle_var.set(row[9])
            self.author_var.set(row[10])
            self.dateborrowed_var.set(row[11])
            self.datedue_var.set(row[12])
            self.daysonbook_var.set(row[13])
            self.lateratefine_var.set(row[14])
            self.dateoverdue_var.set(row[15])
            self.finalpricevar.set(row[16])
         else:
           print('no matching data found')
    
    def ShowData(self):
        
        self.txtbox.insert(END,self.member_var.get()+"\n")   
        self.txtbox.insert(END, self.firstname_var.get()+"\n") 
        self.txtbox.insert(END,self.lastname_var.get()+"\n")    
        self.txtbox.insert(END, self.address_var.get()+"\n")   
        self.txtbox.insert(END, self.postcode_var.get()+"\n") 
        self.txtbox.insert(END, self.mobilenumber_var.get() +"\n") 
        self.txtbox.insert(END, self.bookid_var.get() +"\n")   
        self.txtbox.insert(END,self.author_var.get() +"\n")  
        self.txtbox.insert(END, self.datedue_var.get() +"\n")  
        self.txtbox.insert(END, self.datedue_var.get() +"\n") 
        self.txtbox.insert(END, self.daysonbook_var.get()+"\n")  
        self.txtbox.insert(END, self.lateratefine_var.get() +"\n") 
        self.txtbox.insert(END, self.dateoverdue_var.get() +"\n")  
        self.txtbox.insert(END, self.finalpricevar.get()+"\n")  
              
        
    def reset(self):
            
        self.member_var.set("")
        self.member_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address_var.set("")
        self.postcode_var.set("")
        self.mobilenumber_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.lateratefine_var.set("")
        self.dateoverdue_var.set("")
        self.finalpricevar.set("")
        self.txtbox.delete("1.0",END)     
    
    def Exit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return 
        



        
    def Update(self):
        if(self.id_var.get() ==""):
           messagebox.showerror("Error","Field cannot be empty")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
            mycursor=conn.cursor()
            # mycursor.execute("update mydata set  idnumber=%s,firstname=%s, membertype=%s,lastname=%s,residential_address=%s,postcode=%s,mobilenumber=%s,bookid=%s,booktitle=%s,dateborrowed=%s,datedue=%s,authorname=%s,daysonbook=%s,latereturnfine=%s,dateoverdue=%s,actualprice=%s where idnumber=%s"),(self.member_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.address_var.get(),self.postcode_var.get(),self.mobilenumber_var.get(), self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),self.daysonbook_var.get(),self.lateratefine_var.get(),self.dateoverdue_var.get(),self.finalpricevar.get())
            
            sql="UPDATE mydata SET membertype= %s,firstname = %s,lastname = %s,residential_address = %s,postcode = %s,mobilenumber = %s,bookid = %s,booktitle = %s,authorname = %s,dateborrowed = %s,datedue = %s,daysonbook = %s,latereturnfine = %s,dateoverdue = %s,actualprice = %s WHERE id"
            value=(self.member_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.address_var.get(),self.postcode_var.get(),self.mobilenumber_var.get(), self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),self.daysonbook_var.get(),self.lateratefine_var.get(),self.dateoverdue_var.get(),self.finalpricevar.get())
            mycursor.execute(sql,value)
            conn.commit()
            self.fetchData()
            # self.fetchBooks()
            # self. fetchUsers()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success","Member has been updated successfully")
            
    def delete(self):
        if self.id_var.get()=="" :
            messagebox.showerror("Error","please select the member first")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
            mycursor=conn.cursor()
            query="delete from mydata where idnumber=%s"
            value=(self.id_var.get(),)
            mycursor.execute(query,value)
            
            conn.commit()
            self.fetchData()
            # self.fetchBooks()
            # self.fetchUsers()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success","member has been deleted successfully")
            
    def More(self):
        
        #  self.username1=StringVar()
        #  self.password1=StringVar()
        #  self.firstname1=StringVar()
        #  self.password1=StringVar()
        #  root=Tk()
        #  self.root.destroy()
        #============border around the input fields and output fields
         frame=Frame(root,relief=RIDGE,bg="white")
         frame.place(width=1530,height=260)
         frameCenter=LabelFrame(frame,bg="powder blue",fg="green",relief=RIDGE,font=("times new roman",12,"bold"))
         frameCenter.place(width=1500,height=370)
         firstname=Label(frameCenter,bg="powder blue",fg="green",text="ADD A NEW USER",font=("helvetica",15,"bold"),padx=3)
         firstname.grid(row=0,column=0,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="First Name :",font=("times new roman",13,"bold"))
         lastname.grid(row=1,column=0,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Last Name :",font=("times new roman",13,"bold"))
         lastname.grid(row=2,column=0,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Username:",font=("times new roman",13,"bold"))
         lastname.grid(row=3,column=0,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Password :",font=("times new roman",13,"bold"))
         lastname.grid(row=4,column=0,sticky=W)
         
         Login=Button(frameCenter,text="Add New User", command=self.RegisterUser, font=("arial",12,"bold"),width=15,bg="green",fg="white")
         Login.grid(row=5,column=1)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.firstname1)
         username.grid(row=1,column=1,padx=0.4)
         password=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.lastname1)
         password.grid(row=2,column=1)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.username1)
         username.grid(row=3,column=1)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.password1,show="*")
         username.grid(row=4,column=1)
   
         firstname=Label(frameCenter,bg="powder blue",fg="green",text="ADD A NEW BOOK",font=("helvetica",15,"bold"),padx=3)
         firstname.grid(row=0,column=3,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Title of A Book :",font=("times new roman",13,"bold"))
         lastname.grid(row=1,column=3,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Add Description :",font=("times new roman",13,"bold"))
         lastname.grid(row=2,column=3,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Book ID:",font=("times new roman",13,"bold"))
         lastname.grid(row=3,column=3,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Author name:",font=("times new roman",13,"bold"))
         lastname.grid(row=4,column=3,sticky=W)
         
         Login=Button(frameCenter,text="Add Book",command=self.Addbooks, font=("arial",12,"bold"),width=10,bg="green",fg="white")
         Login.grid(row=5,column=4,pady=5)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20, textvariable=self.booktitle1)
         username.grid(row=1,column=4,padx=0.4)
         password=Entry(frameCenter,font=("arial",13,"bold"),width=20 ,textvariable=self.description1)
         password.grid(row=2,column=4)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20, textvariable=self.bookid1)
         username.grid(row=3,column=4)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20, textvariable=self.author1)
         username.grid(row=4,column=4)




       
         
         firstname=Label(frameCenter,bg="powder blue",fg="green",text="CHANGE ADMIN PASSWORD",font=("helvetica",15,"bold"),padx=3)
         firstname.grid(row=0,column=5,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="User ID:",font=("times new roman",13,"bold"))
         lastname.grid(row=1,column=5,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Old Password:",font=("times new roman",13,"bold"))
         lastname.grid(row=2,column=5,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="New password:",font=("times new roman",13,"bold"))
         lastname.grid(row=3,column=5,sticky=W)
       
        
         Login=Button(frameCenter,text="Change Password", command=self.ChangeAdminPassword,font=("arial",12,"bold"),width=15,bg="green",fg="white")
         Login.grid(row=5,column=5)
         usernameid=Entry(frameCenter,font=("arial",13,"bold"),width=20 ,textvariable=self.usernameid1)
         usernameid.grid(row=1,column=5,padx=150)
         oldpassword=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.oldpassword1)
         oldpassword.grid(row=2,column=5,padx=150)
         newpassword=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.newpassword1)
         newpassword.grid(row=3,column=5,padx=150)
         
         frame=Frame(root,relief=RIDGE,bg="white")
         frame.place(width=1600,height=600,y=175)
         frameCenter=LabelFrame(frame,bg="powder blue",fg="green",relief=RIDGE,font=("times new roman",12,"bold"))
         frameCenter.place(width=1500,height=310,y=3,x=0)
         firstname=Label(frameCenter,bg="powder blue",fg="green",text="SEARCH A NEW BOOK",font=("helvetica",15,"bold"),padx=3)
         firstname.grid(row=0,column=0,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Book Title:",font=("times new roman",13,"bold"))
         lastname.grid(row=1,column=0,sticky=W)
       
         Login=Button(frameCenter,text="Find Book", command=self.Findbook, font=("arial",12,"bold"),width=15,bg="green",fg="white")
         Login.grid(row=3,column=1)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.bookfindvar)
         username.grid(row=1,column=1,padx=0.4)
        
   
         firstname=Label(frameCenter,bg="powder blue",fg="green",text="EDIT BOOK DETAILS",font=("helvetica",15,"bold"),padx=3)
         firstname.grid(row=0,column=3,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Title of A Book :",font=("times new roman",13,"bold"))
         lastname.grid(row=1,column=3,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Add Description :",font=("times new roman",13,"bold"))
         lastname.grid(row=2,column=3,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Author Name:",font=("times new roman",13,"bold"))
         lastname.grid(row=3,column=3,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Book ID:",font=("times new roman",13,"bold"))
         lastname.grid(row=4,column=3,sticky=W)
         
         Login=Button(frameCenter,text="Edit Book",command=self.EditBook, font=("arial",12,"bold"),width=10,bg="green",fg="white")
         Login.grid(row=5,column=4,pady=5)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20, textvariable=self.title2)
         username.grid(row=1,column=4,padx=0.4)
         password=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.description2)
         password.grid(row=2,column=4)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.bookid2 )
         username.grid(row=3,column=4)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20, textvariable=self.author2)
         username.grid(row=4,column=4)
        
         firstname=Label(frameCenter,bg="powder blue",fg="green",text=" BOOK DETAILS",font=("helvetica",15,"bold"),padx=3)
         firstname.grid(row=0,column=5,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Title of A Book :",font=("times new roman",13,"bold"))
         lastname.grid(row=1,column=5,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Add Description :",font=("times new roman",13,"bold"))
         lastname.grid(row=2,column=5,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Add Book Type:",font=("times new roman",13,"bold"))
         lastname.grid(row=3,column=5,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Author name:",font=("times new roman",13,"bold"))
         lastname.grid(row=4,column=5,sticky=W)
         
       
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20, textvariable=self.title3)
         username.grid(row=1,column=6,padx=0.4)
         password=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.description3)
         password.grid(row=2,column=6)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.bookid3 )
         username.grid(row=3,column=6)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20, textvariable=self.author3)
         username.grid(row=4,column=6)
         
          #=================ButtonsFrame====================
         buttonsFrame=LabelFrame(self.root,bd=12,relief=RIDGE,bg="powder blue")
         buttonsFrame.place(x=200,y=400,width=710,height=60)
          #===============add buttons to the buttons frame======================================
         btnadd_Dat=Button(buttonsFrame,command=self.Exit,text="Exit",font=("arial",12,"bold"),width=16,bg="green",fg="white")
         btnadd_Dat.grid(row=0,column=0)
        
         def Exit(self):
             iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
             if iExit>0:
                self.root.destroy()
                return 
          
        #  btnshow_Dat=Button(buttonsFrame,text="Dashboard",font=("arial",12,"bold"),width=16,bg="green",fg="white")
        #  btnshow_Dat.grid(row=0,column=1)
         btnupdate_Dat=Button(buttonsFrame,command=self.deleteUsers, text="Delete Users",font=("arial",12,"bold"),width=16,bg="green",fg="white")
         btnupdate_Dat.grid(row=0,column=2)
         btndelete_Dat=Button(buttonsFrame,text="Delete Books",command=self.deleteBooks,font=("arial",12,"bold"),width=16,bg="green",fg="white")
         btndelete_Dat.grid(row=0,column=3)
         btndelete_Da=Button(buttonsFrame,text="Reset",command=self.Reset,font=("arial",12,"bold"),width=16,bg="green",fg="white")
         btndelete_Da.grid(row=0,column=4)
         
          #======================InformationFrame============
         FrameDetail=LabelFrame(self.root,bd=12,relief=RIDGE,bg="powder blue",padx=10)
         FrameDetail.place(x=0,y=700,width=900,height=300)
        #==================table======frame================================
         Table_fram=Frame(FrameDetail,bd=6,relief=RIDGE,bg="powder blue")
         Table_fram.place(x=0,y=2,width=850,height=140)
         xscroll=ttk.Scrollbar(Table_fram,orient=HORIZONTAL)
         yscroll=ttk.Scrollbar(Table_fram,orient=VERTICAL)
         self.library_tabl=ttk.Treeview(Table_fram,column=("ID","Book Title","Book Description","Book ID","Author Name"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set
                                         )
         xscroll.pack(side=BOTTOM,fill=X)
         yscroll.pack(side=RIGHT,fill=Y)
        
         xscroll.config(command=self.library_tabl.xview)
         yscroll.config(command=self.library_tabl.yview)
        
         self.library_tabl.heading("ID",text="ID")
         self.library_tabl.heading("Book Title",text="Book Title")
         self.library_tabl.heading("Book Description",text="Book Description")
         self.library_tabl.heading("Book ID",text="Book ID")
         self.library_tabl.heading("Author Name",text="Author Name")
         self.library_tabl["show"]="headings"
         self.library_tabl.pack(fill=BOTH,expand=1)
         self. fetchBooks()
         self.library_tabl.bind("<ButtonRelease-1>",self.getCursor1)
          #======================InformationFrame============
         UserDetail=LabelFrame(self.root,bd=12,relief=RIDGE,bg="powder blue",padx=10)
         UserDetail.place(x=0,y=500,width=900,height=300)
        #==================table======frame================================
         User_fram=Frame(UserDetail,bd=6,relief=RIDGE,bg="powder blue")
         User_fram.place(x=0,y=2,width=850,height=140)
         xscroll=ttk.Scrollbar(User_fram,orient=HORIZONTAL)
         yscroll=ttk.Scrollbar(User_fram,orient=VERTICAL)
         self.library_tabl=ttk.Treeview(User_fram,column=("ID","Book Title","Book Description","Book ID","Author Name"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set
                                         )
         xscroll.pack(side=BOTTOM,fill=X)
         yscroll.pack(side=RIGHT,fill=Y)
        
         xscroll.config(command=self.library_tabl.xview)
         yscroll.config(command=self.library_tabl.yview)
        
         self.library_tabl.heading("ID",text="ID")
         self.library_tabl.heading("Book Title",text="Book Title")
         self.library_tabl.heading("Book Description",text="Book Description")
         self.library_tabl.heading("Book ID",text="Book ID")
         self.library_tabl.heading("Author Name",text="Author Name")
         self.library_tabl["show"]="headings"
         self.library_tabl.pack(fill=BOTH,expand=1)
         self. fetchBooks()
         self.library_tabl.bind("<ButtonRelease-1>",self.getCursor1)
           #======================InformationFrame============
         UserDetail1=LabelFrame(self.root,bd=12,relief=RIDGE,bg="powder blue",padx=10)
         UserDetail1.place(x=870,y=500,width=500,height=300)
        #==================table======frame================================
         User_fram1=Frame(UserDetail1,bd=6,relief=RIDGE,bg="powder blue")
         User_fram1.place(x=0,y=2,width=460,height=140)
         xscroll=ttk.Scrollbar(User_fram1,orient=HORIZONTAL)
         yscroll=ttk.Scrollbar(User_fram1,orient=VERTICAL)
         self.library_tabl2=ttk.Treeview(User_fram1,column=("ID","First Name","Last Name","User Name"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set
                                         )
         xscroll.pack(side=BOTTOM,fill=X)
         yscroll.pack(side=RIGHT,fill=Y)
        
         xscroll.config(command=self.library_tabl2.xview)
         yscroll.config(command=self.library_tabl2.yview)
        
         self.library_tabl2.heading("ID",text="ID")
         self.library_tabl2.heading("First Name",text="First Name")
         self.library_tabl2.heading("Last Name",text="Last  Name")
         self.library_tabl2.heading("User Name",text="User Name")
         self.library_tabl2["show"]="headings"
         self.library_tabl2.pack(fill=BOTH,expand=1)
         self.fetchUsers()
         self.library_tabl2.bind("<ButtonRelease-1>",self.getCursor2)

         def getCursor2(self,event=""):
            cursor_row=self.library_tabl2.focus()
            content=self.library_tabl2.item(cursor_row)  
            row=content["values"]
            if(row):
              self.firstname1.set(row[1])
              self.lastname1.set(row[2])
              self.username1.set(row[3])
         
        #  firstname=Label(frameCenter,bg="powder blue",fg="green",text="CHANGE ADMIN PASSWORD",font=("helvetica",15,"bold"),padx=3)
        #  firstname.grid(row=0,column=5,sticky=W)
        #  lastname=Label(frameCenter,bg="powder blue",fg="green",text="User ID:",font=("times new roman",13,"bold"))
        #  lastname.grid(row=1,column=5,sticky=W)
        #  lastname=Label(frameCenter,bg="powder blue",fg="green",text="Old Password:",font=("times new roman",13,"bold"))
        #  lastname.grid(row=2,column=5,sticky=W)
        #  lastname=Label(frameCenter,bg="powder blue",fg="green",text="New password:",font=("times new roman",13,"bold"))
        #  lastname.grid(row=3,column=5,sticky=W)
       
        
        #  Login=Button(frameCenter,text="Change Password", font=("arial",12,"bold"),width=15,bg="green",fg="white")
        #  Login.grid(row=5,column=5)
        #  usernameid=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.username_var)
        #  usernameid.grid(row=1,column=5,padx=150)
        #  oldpassword=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.password_var)
        #  oldpassword.grid(row=2,column=5,padx=150)
        #  newpassword=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.username_var)
        #  newpassword.grid(row=3,column=5,padx=150)
    def Findbook(self):
            if(self.bookfindvar.get()==""):
               messagebox.showerror("Error","Please fill in the empty fields") 
            else:
               conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
               mycursor=conn.cursor()     
               sql ="SELECT * FROM books WHERE Book_title =%s"
               val=(self.bookfindvar.get())
               mycursor.execute(sql,(val,))
               myresult = mycursor.fetchall()
               if(myresult):
                    for x in myresult:
                     self.title3.set(x[1])
                     self.description3.set(x[2])
                     self.bookid3.set(x[3])
                     self.author3.set(x[4])
               else:
                  messagebox.showinfo("Error","Sorry this book is not available")
        #  newpassword.grid(row=3,column=5,padx=150)
    
    def RegisterUser(self):
           if(self.firstname1.get()==""):
               messagebox.showerror("Error","Please fill in the empty fields")
           elif(self.lastname1.get()  ==""):
               messagebox.showerror("Error","Please fill in the empty fields")
           elif(self.password1.get() ==""):
               messagebox.showerror("Error","Please fill in the empty fields")
           elif(self.username1.get() ==""):
                messagebox.showerror("Error","Please fill in the empty fields")  
           else:
               conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
               mycursor=conn.cursor()     
               sql="INSERT into users(firstname,lastname,username,password)VALUES(%s,%s,%s,%s)"
               val=(self.firstname1.get(),self.lastname1.get(),self.username1.get(),self.password1.get())
               mycursor.execute(sql,val)
               conn.commit()
               print("user successfully registered")
               self.fetchUsers()
               messagebox.showinfo("Success","Member has been added succesfully")
               self.firstname1.set("")
               self.lastname1.set("")
               self.username1.set("")
               self.password1.set("")
    def Addbooks(self):
           if(self.booktitle1.get()==""):
                messagebox.showerror("Error","Please fill in the empty fields")
           elif(self.description1.get()  ==""):
               messagebox.showerror("Error","Please fill in the empty fields")
           elif(self.bookid1.get() ==""):
               messagebox.showerror("Error","Please fill in the empty fields")
           elif(self.author1.get() ==""):
              messagebox.showerror("Error","Please fill in the empty fields")  
           else:
               conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
               mycursor=conn.cursor()    			

               sql="INSERT into books( Book_title,Author,BookID,BookDescription)VALUES(%s,%s,%s,%s)"
               val=(self.booktitle1.get(),self.author1.get(),self.bookid1.get(),self.description1.get())
               mycursor.execute(sql,val)
               conn.commit()
               print("book successfully added")
               messagebox.showinfo("Success","Book has been added succesfully")
               self.fetchBooks()
               self.booktitle1.set("")
               self.description1.set("")
               self.bookid1.set("")
               self.author1.set("")
    def ChangeAdminPassword(self):
           if(self.usernameid1.get()==""):
                messagebox.showerror("Error","Please fill in the empty fields")
           elif(self.oldpassword1.get()  ==""):
               messagebox.showerror("Error","Please fill in the empty fields")
           elif(self.newpassword1.get() ==""):
               messagebox.showerror("Error","Please fill in the empty fields")
           else:
                conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
                mycursor=conn.cursor()
                sql="select * from admin where username=%s and password=%s";
                val=(self.usernameid1.get(),self.oldpassword1.get())
                mycursor.execute(sql,val)
                results=mycursor.fetchall()
                if results:
                   for i in results:
                        conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
                        mycursor=conn.cursor()
                        sql = "UPDATE admin SET password = %s WHERE password = %s"
                        value=(self.newpassword1.get(),self.oldpassword1.get())
                        mycursor.execute(sql,value)
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success","Admin Password Changed Successfully")
                        self.usernameid1.set("")
                        self.oldpassword1.set("")
                        self.newpassword1.set("")
                else :
                       messagebox.showerror("error","Incoorect details entered try again")

    def EditBook(self):
        if(self.bookid2.get() ==""):
           messagebox.showerror("Error","Field cannot be empty")
        elif(self.title2.get()==""):
           messagebox.showerror("Error","Field cannot be empty")
        elif(self.description2.get()==""):
           messagebox.showerror("Error","Field cannot be empty") 
        elif(self.author2.get()==""):
           messagebox.showerror("Error","Field cannot be empty")    
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
            mycursor=conn.cursor()
            # mycursor.execute("update mydata set  idnumber=%s,firstname=%s, membertype=%s,lastname=%s,residential_address=%s,postcode=%s,mobilenumber=%s,bookid=%s,booktitle=%s,dateborrowed=%s,datedue=%s,authorname=%s,daysonbook=%s,latereturnfine=%s,dateoverdue=%s,actualprice=%s where idnumber=%s"),(self.member_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.address_var.get(),self.postcode_var.get(),self.mobilenumber_var.get(), self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),self.daysonbook_var.get(),self.lateratefine_var.get(),self.dateoverdue_var.get(),self.finalpricevar.get())
            sql="UPDATE books SET Author= %s,Book_title = %s,BookID = %s,BookDescription = %s WHERE id"
            value=(self.author2.get(),self.title2.get(),self.bookid2.get(),self.description2.get())
            mycursor.execute(sql,value)
            conn.commit()
            self.fetchBooks()
            conn.close()
            messagebox.showinfo("Success","Member has been updated successfully")
    def Reset(self):
             self.title3.set("")
             self.description3.set("")
             self.bookid3.set("")
             self.author3.set("")
             self.title2.set("")
             self.description2.set("")
             self.bookid2.set("")
             self.author2.set("")
             self.bookfindvar.set("")
             self.newpassword1.set("")
             self.oldpassword1.set("")
             self.usernameid1.set("")
             self.booktitle1.set("")
             self.description1.set("")
             self.bookid1.set("")
             self.author1.set("")
             self.firstname1.set("")
             self.lastname1.set("")
             self.password1.set("")
             self.username1.set("")
    def deleteBooks(self):
        if self.title2.get()=="" :
            messagebox.showerror("Error","please select the member first")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
            mycursor=conn.cursor()
            query="delete from books where Book_title=%s"
            value=(self.title2.get(),)
            mycursor.execute(query,value)
            conn.commit()
            self.fetchBooks()
            conn.close()

    def deleteUsers(self):
        if self.username1.get()=="" :
            messagebox.showerror("Error","please select the member first")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
            mycursor=conn.cursor()
            query="delete from users where username=%s"
            value=(self.username1.get(),)
            mycursor.execute(query,value)
            conn.commit()
            self.fetchUsers()
            conn.close()





                # sql="UPDATE users SET = %s,firstname = %s,lastname = %s,residential_address = %s,postcode = %s,mobilenumber = %s,bookid = %s,booktitle = %s,authorname = %s,dateborrowed = %s,datedue = %s,daysonbook = %s,latereturnfine = %s,dateoverdue = %s,actualprice = %s WHERE id"
                # value=(self.member_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.address_var.get(),self.postcode_var.get(),self.mobilenumber_var.get(), self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),self.daysonbook_var.get(),self.lateratefine_var.get(),self.dateoverdue_var.get(),self.finalpricevar.get())
                # mycursor.execute(sql,value)
                # conn.commit()
                # self.fetchData()
                # self.reset()
                # conn.close()
            
        #     messagebox.showinfo("Success","Member has been updated successfully")
        #        print("book successfully aded")
        #        messagebox.showinfo("Success","Book has been added succesfully")
        #        self.booktitle1.set("")
        #        self.description1.set("")
        #        self.bookid1.set("")
        #        self.author1.set("")

class Login:
  
     def getCursor1(self,event=""):
         cursor_row=self.library_tabl.focus()
         content=self.library_tabl.item(cursor_row)  
         row=content["values"]
         if(row):
              
            self.title2.set(row[1])
            self.description2.set(row[2])
            self.author2.set(row[3])
            self.bookid2.set(row[4]) 
     def Finduserbook(self):
            if(self.bookfindvar1.get()==""):
               messagebox.showerror("Error","Please fill in the empty fields") 
            else:
               conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
               mycursor=conn.cursor()     
               sql ="SELECT * FROM books WHERE Book_title =%s"
               val=(self.bookfindvar1.get())
               mycursor.execute(sql,(val,))
               myresult = mycursor.fetchall()
               if(myresult):
                    for x in myresult:
                     self.title3.set(x[1])
                     self.description3.set(x[2])
                     self.bookid3.set(x[3])
                     self.author3.set(x[4])
               else:
                  messagebox.showinfo("Error","Sorry this book is not available")
                   
       
     def log(self,root):
             
         self.username_var=StringVar()
         self.password_var=StringVar()
         #admin userinput
         self.username_var1=StringVar()
         self.password_var1=StringVar()
         self.root=root
         self.root.title("login interface")  
         labeltitle=Label(self.root,text="Library Management System",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("Futura",30,"bold"))
         labeltitle.place(x=400,y=75)
        
        #============border around the input fields and output fields

         frameCenter=LabelFrame(self.root,bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
         frameCenter.place(x=200,y=200,width=500,height=300)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Password :",font=("times new roman",13,"bold"))
         lastname.grid(row=3,column=0,sticky=W)
         firstname=Label(frameCenter,bg="powder blue",fg="green",text="ADMIN LOGIN",font=("helvetica",15,"bold"))
         firstname.grid(row=0,column=1,sticky=W,padx=70,pady=5)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Username :",font=("times new roman",13,"bold"))
         lastname.grid(row=2,column=0,sticky=W,pady=5)
         Login=Button(frameCenter,text="Login", command=self.AdminLogin, font=("arial",12,"bold"),width=10,bg="green",fg="white")
         Login.grid(row=4,column=1,padx=40,pady=10)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=32,textvariable=self.username_var1)
         username.grid(row=2,column=1,padx=2)
         password=Entry(frameCenter,font=("arial",13,"bold"),width=32,textvariable=self.password_var1,show="*")
         password.grid(row=3,column=1)
         
         
         frameCenter=LabelFrame(self.root,bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
         frameCenter.place(x=750,y=200,width=500,height=300)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Password :",font=("times new roman",13,"bold"))
         lastname.grid(row=3,column=0,sticky=W)
         firstname=Label(frameCenter,bg="powder blue",fg="green",text="USER LOGIN",font=("helvetica",15,"bold"))
         firstname.grid(row=0,column=1,sticky=W,padx=70,pady=5)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Username :",font=("times new roman",13,"bold"))
         lastname.grid(row=2,column=0,sticky=W,pady=5)
         Login=Button(frameCenter,text="Login", command=self.CheckLogin, font=("arial",12,"bold"),width=10,bg="green",fg="white")
         Login.grid(row=4,column=1,padx=40,pady=10)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=32,textvariable=self.username_var)
         username.grid(row=2,column=1,padx=2)
         password=Entry(frameCenter,font=("arial",13,"bold"),width=32,textvariable=self.password_var,show="*")
         password.grid(row=3,column=1)
         
     def AdminLogin(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
        mycursor=conn.cursor()
        if(mycursor):
            print('you have successfully connected to the database')
        else:
            print('there was an error in connecting to the database')
        sql="select * from admin where username=%s and password=%s";
        val=(self.username_var1.get(),self.password_var1.get())
        mycursor.execute(sql,val)
        results=mycursor.fetchall()
        if results:
          for i in results:
              print('hello admin')
            #   self.More(root)
              lib.Manage(root)
            #   Library_Management(root)
              
              
        else:
            print('error loggin in ')
            messagebox.showerror("Error","Incorrect login details please try again")
     def Connect(self):
            conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
            mycursor=conn.cursor()     
            sql ="SELECT Book_title from books"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if(myresult):
                for x in myresult:
                  print(x)       
                #   Listbooks.append(x)
     def CheckLogin(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
        mycursor=conn.cursor()
        if(mycursor):
            print('you have successfully connected to the database')
        else:
            print('there was an error in connecting to the database')
        sql="select * from users where username=%s and password=%s";
        val=(self.username_var.get(),self.password_var.get())
        mycursor.execute(sql,val)
        results=mycursor.fetchall()
        if results:
          for i in results:
              print('hello')
              self.More(root)
             
            #   Library_Management(root)
              
              
        else:
            print('error loggin in ')
            messagebox.showerror("Error","Incorrect login details please try again")
     def ChangeUserPassword(self):
           print(self.username_text.get())
           print(self.oldpassword_text.get())
           print(self.newpassword_text.get())
           if(self.username_text.get()==""):
                messagebox.showerror("Error","Please fill in the empty fields")
           elif(self.oldpassword_text.get()  ==""):
               messagebox.showerror("Error","Please fill in the empty fields")
           elif(self.newpassword_text.get() ==""):
               messagebox.showerror("Error","Please fill in the empty fields")
           else:
                conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
                mycursor=conn.cursor()
                sql="select * from users where username=%s and password=%s";
                val=(self.username_text.get(),self.oldpassword_text.get())
                mycursor.execute(sql,val)
                results=mycursor.fetchall()
                if results:
                   for i in results:
                        conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
                        mycursor=conn.cursor()
                        sql = "UPDATE users SET password = %s WHERE password = %s"
                        value=(self.newpassword_text.get(),self.oldpassword_text.get())
                        mycursor.execute(sql,value)
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success","User Password Changed Successfully")
                        self.usernameid1.set("")
                        self.oldpassword1.set("")
                        self.newpassword1.set("")
                else :
                       messagebox.showerror("error","Incoorect details entered try again")
 
               
     def More(self,root):
        
        #  self.username1=StringVar()
        #  self.password1=StringVar()
        #  self.firstname1=StringVar()
        #  self.password1=StringVar()
        #  root=Tk()
        #  self.root.destroy()
        #============border around the input fields and output fields
        
         frame=Frame(root,relief=RIDGE,bg="white")
         frame.place(width=1600,height=230)
         frameCenter=LabelFrame(frame,bg="powder blue",fg="green",relief=RIDGE,font=("times new roman",12,"bold"))
         frameCenter.place(width=0,height=310)

         
         frame=Frame(root,relief=RIDGE,bg="white")
         frame.place(width=1550,height=450,y=65)
         self.root=root
         label=Label(self.root,text="User Dashboard",bg="powder blue",fg="green",bd=10,relief=RIDGE,font=("Futura",20,"bold"))
         label.place(y=0,x=580)
         label1=Label(self.root,text="All Books",bg="powder blue",fg="green",bd=10,relief=RIDGE,font=("Futura",20,"bold"))
         label1.place(y=340,x=600)
         frameCenter=LabelFrame(frame,bg="powder blue",fg="green",relief=RIDGE,font=("times new roman",12,"bold"))
         frameCenter.place(width=1500,height=270)
         #=============style==================
         firstname=Label(frameCenter,bg="powder blue",fg="green",text="SEARCH A NEW BOOK",font=("helvetica",15,"bold"),padx=3)
         firstname.grid(row=0,column=0,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Book Title :",font=("times new roman",13,"bold"))
         lastname.grid(row=1,column=0,sticky=W)
         
         self.bookfindvar1=StringVar()
         Login=Button(frameCenter,text="Find Book", font=("arial",12,"bold"),width=15,bg="green",fg="white",command=self.Finduserbook)
         Login.grid(row=3,column=1)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.bookfindvar1)
         username.grid(row=1,column=1,padx=0.4)
        
   
         firstname=Label(frameCenter,bg="powder blue",fg="green",text="CHANGE USER PASSWORD",font=("helvetica",15,"bold"),padx=3)
         firstname.grid(row=0,column=3,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Username:",font=("times new roman",13,"bold"))
         lastname.grid(row=1,column=3,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Old Password:",font=("times new roman",13,"bold"))
         lastname.grid(row=2,column=3,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="New Password:",font=("times new roman",13,"bold"))
         lastname.grid(row=3,column=3,sticky=W)
         self.username_text=StringVar()
         self.oldpassword_text=StringVar()
         self.newpassword_text=StringVar()
         
         Login=Button(frameCenter,text="Change Password",command=self.ChangeUserPassword, font=("arial",12,"bold"),width=15,bg="green",fg="white")
         Login.grid(row=4,column=4)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.username_text)
         username.grid(row=1,column=4,padx=0.4)
         password=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.oldpassword_text)
         password.grid(row=2,column=4)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.newpassword_text)
         username.grid(row=3,column=4)
     
         
         firstname=Label(frameCenter,bg="powder blue",fg="green",text=" BOOK DETAILS",font=("helvetica",15,"bold"),padx=3)
         firstname.grid(row=0,column=5,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Title of A Book :",font=("times new roman",13,"bold"))
         lastname.grid(row=1,column=5,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Add Description :",font=("times new roman",13,"bold"))
         lastname.grid(row=2,column=5,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Add Book Type:",font=("times new roman",13,"bold"))
         lastname.grid(row=3,column=5,sticky=W)
         lastname=Label(frameCenter,bg="powder blue",fg="green",text="Author name:",font=("times new roman",13,"bold"))
         lastname.grid(row=4,column=5,sticky=W)
         self.title3=StringVar()
         self.description3=StringVar()
         self.bookid3=StringVar()
         self.author3=StringVar()
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20 ,textvariable=self.title3)
         username.grid(row=1,column=6,padx=0.4)
         password=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.description3)
         password.grid(row=2,column=6)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.bookid3)
         username.grid(row=3,column=6)
         username=Entry(frameCenter,font=("arial",13,"bold"),width=20,textvariable=self.author3)
         username.grid(row=4,column=6)




          #======================InformationFrame============
         FrameDetail=LabelFrame(self.root,bd=12,relief=RIDGE,bg="powder blue",padx=10)
         FrameDetail.place(x=0,y=400,width=1500,height=300)
        #==================table======frame================================
         Table_fram=Frame(FrameDetail,bd=6,relief=RIDGE,bg="powder blue")
         Table_fram.place(x=0,y=2,width=1310,height=250)
         xscroll=ttk.Scrollbar(Table_fram,orient=HORIZONTAL)
         yscroll=ttk.Scrollbar(Table_fram,orient=VERTICAL)
         self.library_tabl=ttk.Treeview(Table_fram,column=("ID","Book Title","Book Description","Book ID","Author Name"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set
                                         )
         xscroll.pack(side=BOTTOM,fill=X)
         yscroll.pack(side=RIGHT,fill=Y)
        
         xscroll.config(command=self.library_tabl.xview)
         yscroll.config(command=self.library_tabl.yview)
        
         self.library_tabl.heading("ID",text="ID")
         self.library_tabl.heading("Book Title",text="Book Title")
         self.library_tabl.heading("Book Description",text="Book Description")
         self.library_tabl.heading("Book ID",text="Book ID")
         self.library_tabl.heading("Author Name",text="Author Name")
         self.library_tabl["show"]="headings"
         self.library_tabl.pack(fill=BOTH,expand=1)
         self. fetchBooks()
         self.library_tabl.bind("<ButtonRelease-1>",self.getCursor1)
         
  
 
     def fetchBooks(self):
        connect=mysql.connector.connect(host="localhost",user="root",password="",database="library")   
        my_curs=connect.cursor()
        my_curs.execute("select * from books") 
        rows=my_curs.fetchall()
        
        if len(rows)!=0:
            self.library_tabl.delete(*self.library_tabl.get_children())
            for i in rows:
                self.library_tabl.insert("",END,values=i)
            connect.commit()
        connect.close()
     def getCursor1(self,event=""):
         cursor_row=self.library_tabl.focus()
         content=self.library_tabl.item(cursor_row)  
         row=content["values"]
         if(row):
              
              self.title2.set(row[1])
              self.description2.set(row[2])
              self.author2.set(row[3])
              self.bookid2.set(row[4])      
        



     
if __name__=='__main__':
    root=Tk()
    # root.resizable(False,False)
    root.geometry("1300x800")
    # Library_Management(root)
    lib=Library_Management()
    check=Login()
    check.log(root)
    # lib.availableBooks()
    # check.Connect()
    root.mainloop()
   

    