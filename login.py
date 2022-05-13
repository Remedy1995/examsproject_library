from cProfile import label
from cgitb import text
from msilib.schema import ListBox
from operator import ge
from tkinter import*
from tkinter import font
from tkinter import ttk
import mysql.connector 
from tkinter import messagebox
import datetime
import tkinter
import random
import string
# import generatenumbers
# from generatenumbers import (GenerateBookID,Generate)
# from generatenumbers import MySample

class Login:
      
      def loginterface():
             print ('fool')
        #   self.username_var=StringVar()
        #   self.password_var=StringVar()
        #   self.root=root
        #   self.root.title("login interface")  
        #   labeltitle=Label(self.root,text="Library Management System",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("Futura",30,"bold"))
        #   labeltitle.pack()
      
        #   frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="white")
        #   frame.place(x=0,y=90,width=1530,height=340)
         
        #   frameCenter=LabelFrame(frame,bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        #   frameCenter.place(x=390,y=5,width=500,height=300)
        #   lastname=Label(frameCenter,bg="powder blue",fg="green",text="Password :",font=("times new roman",13,"bold"))
        #   lastname.grid(row=3,column=0,sticky=W)
        #   firstname=Label(frameCenter,bg="powder blue",fg="green",text="ADMIN LOGIN",font=("helvetica",15,"bold"))
        #   firstname.grid(row=0,column=1,sticky=W,padx=70,pady=5)
        #   lastname=Label(frameCenter,bg="powder blue",fg="green",text="Username :",font=("times new roman",13,"bold"))
        #   lastname.grid(row=2,column=0,sticky=W,pady=5)
        #   Login=Button(frameCenter,text="Login", command=self.CheckLogin, font=("arial",12,"bold"),width=10,bg="green",fg="white")
        #   Login.grid(row=4,column=1,padx=40,pady=10)
        #   username=Entry(frameCenter,font=("arial",13,"bold"),width=32,textvariable=self.username_var)
        #   username.grid(row=2,column=1,padx=2)
        #   password=Entry(frameCenter,font=("arial",13,"bold"),width=32,textvariable=self.password_var)
        #   password.grid(row=3,column=1)
         
     