import mysql.connector 

# def availableBooks(self):
#     conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
#     mycursor=conn.cursor()     
#     sql ="SELECT * FROM books WHERE Book_title =%s"
#     val=(self.bookfindvar.get())
#     mycursor.execute(sql,(val,))
#     myresult = mycursor.fetchall()
#     if(myresult):
#         for x in myresult:
#          print(x[1])