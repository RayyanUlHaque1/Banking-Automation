#Import all libraries and pre build Class ,Other Python files::
from tkinter import Tk,Label,Frame,Entry,Button,messagebox,filedialog,simpledialog
from tkinter.ttk import Combobox
import time,gmail
import random,sqlite3
from PIL import Image,ImageTk
import Database_table
from tkintertable import TableCanvas, TableModel
import re
import shutil
import os

#Title And Window Configuration BG colors , FG colors 
win=Tk()
win.title('Banking Automation')
win.state('zoomed')
win.resizable(width=False,height=False)
win.configure(bg='#3D3D3D')

#Header 
hearder_title=Label(win,text="Banking Automation",font=('Helvetica', 40,'bold','underline'),bg='#3D3D3D', fg='#E5D9F2')
hearder_title.pack()

#Date.time
current_date=time.strftime('%d-%b-%Y')
hearder_date=Label(win,text=f'Date:{current_date}',font=('Helvetica', 18,'bold'),bg='#3D3D3D', fg='#E5D9F2')
hearder_date.pack(pady=10)

#Footer
footer_title=Label(win,text="BY: Rayyan Ul Haque\n E-mail:rayyansiddiqui@gmail.com\n Phone no:7665931215",font=('Helvetica',20,'bold'),bg='#3D3D3D',fg='#E5D9F2')
footer_title.pack(side='bottom')

#Logo img
img=Image.open('logo.png').resize((220,170))
bitmap_img=ImageTk.PhotoImage(img,master=win)
logo_label=Label(win,image=bitmap_img )
logo_label.place(relx=0,rely=0)

#Inserting Frames First Screen:
def main_screen():
  frm=Frame(win,highlightbackground='black',highlightthickness=1.5)
  frm.configure(bg='#578E7E')
  frm.place(relx=0,rely=.15,relwidth=1,relheight=.72)
#Captcha Function for randomly genrated captcha::
  global cap
  cap=''
  def genrate_captacha():
     global cap
     d=str(random.randint(0,9))
     cap=cap+d
     ch=chr(random.randint(65,90))
     cap=cap+ch

     d=str(random.randint(0,9))
     cap=cap+d
     ch=chr(random.randint(65,90))
     cap=cap+ch

     d=str(random.randint(0,9))
     cap=cap+d
     ch=chr(random.randint(65,90))
     cap=cap+ch
     return cap
  
  def reset():
     acn_entry.delete(0,"end")
     pass_entry.delete(0,"end")
     acn_entry.focus()
#Action On Login click Button Open New frame(Function run),Authentication:
  def login_click():
    global uacn
    uacn=acn_entry.get()
    upass=pass_entry.get()
    urole=role_combox.get()
#Validation For Acn number::
    if not re.fullmatch('[0-9]{1}',uacn):
             messagebox.showwarning('Login','Fields Required')
             return

##Condition to Check user enter Acn no or pass: If not show warning::
    if len (uacn)==0 or len (upass)==0:
       messagebox.showwarning('Login',"Account no or Password can't be empty")
       return
    if captcha_entry.get()!=cap:
       messagebox.showwarning('login','Invalid Captcha')
       return
    uacn=int(uacn)
##Conditon to set admin acn no (0) And pass "admin"
    if uacn==0 and upass=='admin' and urole=='Admin':
        frm.destroy()
        welcome_admin_screen()
      
    elif urole=='User':
        con_obj=sqlite3.connect(database='bank.sqlite')
        cur_boj=con_obj.cursor()
        cur_boj.execute('select * from users where users_acn=? and users_pass=?',(uacn,upass))
        tup=cur_boj.fetchone()
        if tup==None:
          messagebox.showerror('login','invalid Acn/Pass')
        else:
         global uname
         uname=tup[2]
        # messagebox.showerror('login','Invalid Credentials')
         frm.destroy()
         welcome_user_screen()
    else:
        messagebox.showerror('login','Invalid Role')
#For Lable and Entry Details on Main Screen:
  acn_label=Label(frm,width=8,font=('arial',20,'bold'),bg='#3D3D3D',fg='#E5D9F2',text='Account')
  acn_label.place(relx=.3,rely=.1)

  acn_entry=Entry(frm,font=('Helvetica',20,'bold'),bd=3)
  acn_entry.place(relx=.4,rely=.1)
  acn_entry.focus()

  pass_label=Label(frm,width=8,font=('Helvetica',20,'bold'),bg='#3D3D3D',fg='#E5D9F2',text='Password')
  pass_label.place(relx=.3,rely=.2)

  pass_entry=Entry(frm,font=('Helvetica',20,'bold'),bd=3,show='*')
  pass_entry.place(relx=.4,rely=.2)

  role_label=Label(frm,width=8,font=('Helvetica',20,'bold'),bg='#3D3D3D',fg='#E5D9F2',text='Role')
  role_label.place(relx=.3,rely=.3)

#For drop down we use Combobox and in list values will be pass:
  role_combox=Combobox(frm,width=19,font=('Helvetica',20,'bold'),values=['User','Admin'])
  role_combox.current(0)
  role_combox.place(relx=.4,rely=.3)
#Captcha Label ,Entry and Captcha itself::
  gen_captcha_label=Label(frm,width=8,font=('Helvetica',20,'bold'),bg='#3D3D3D',fg='#E5D9F2',text=genrate_captacha())
  gen_captcha_label.place(relx=.45,rely=.42)

  captcha_label=Label(frm,width=8,font=('Helvetica',20,'bold'),bg='#3D3D3D',fg='#E5D9F2',text='Captcha')
  captcha_label.place(relx=.3,rely=.53)

  captcha_entry=Entry(frm,font=('Helvetica',20,'bold'),bd=3)
  captcha_entry.place(relx=.4,rely=.53)
#Login Button ,Reset Button ,Forgot Button::
  loging_btn=Button(frm,text='Login',font=('Helvetica',17,'bold'),bg='#3D3D3D',fg='#E5D9F2',bd=5,command=login_click)
  loging_btn.place(relx=.43,rely=.65)

  reset_btn=Button(frm,command=reset,text='Reset',font=('Helvetica',17,'bold'),bg='#3D3D3D',fg='#E5D9F2',bd=5)
  reset_btn.place(relx=.52,rely=.65)

  forgot_btn=Button(frm,command=forgot_password_screen ,width=16 ,text='Forgot Password',font=('Helvetica',18,'bold'),bg='#3D3D3D',fg='#E5D9F2',bd=5)
  forgot_btn.place(relx=.42,rely=.78)

#Frame for admin Screen / Admin page
def welcome_admin_screen():
  frm=Frame(win,highlightbackground='black',highlightthickness=2)
  frm.configure(bg='#578E7E')
  frm.place(relx=0,rely=.15,relwidth=1,relheight=.73)
  
#Logout
  def logout_click():
    resp=messagebox.askyesno('Logout','Confirm Logout')#Ask before logout::
    if resp:
      frm.destroy()
      main_screen()
  
#Buttons (Logout ,Create ,View ,Delete) for Admin access:
  logout_btn=Button(frm,command=logout_click,text='Logout',font=('Helvetica',20,'bold'),bg='#3d3d3d',bd=5,fg='#ffffff')
  logout_btn.place(relx=.92 , rely=0)
  
#Create Function to create nested Frame:
  def create_click():
     ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
     ifrm.configure(bg='white')
     ifrm.place(relx=.2,rely=.15,relwidth=.65,relheight=.7)
     title_ifrm=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='This is create User Screen')
     title_ifrm.pack()

#OPEN ACN Function
     def open_click():
#User credentials while creating acn
          uname=name_entry.get()
          umob=mob_entry.get()
          umail=email_entry.get()
          uadhar=adhar_entry.get()
          ubal=0
          upass=str(random.randint(10000000,99999999))
          ##Condition to Check user enter Acn no or pass: If not show warning::
          if len (uname)==0 or len (umob)==0 or len (umail)==0 or len (uadhar)==0:
            messagebox.showwarning('Account Open',"Fields Required")
            return
  #Validation For mobile number it has to be Integer only::
          if not re.fullmatch('[6-9][0-9]{9}',umob):
             messagebox.showwarning('Mobile','Mobile Number Only')
             return
  #Validation for email it has to include (@.) ::
          if not re.fullmatch('[a-z0-9]+@[a-z]+[.][a-z]+',umail):
             messagebox.showwarning('E-mail','Missing important Symbols(@)')
             return
  #Validation for adhar limit it to 12 digits::
          if not re.fullmatch('[0-9]{12}',uadhar):
             messagebox.showwarning('Adhar','Numeric Values Only')
             return
  #Validation For name it has to be Alphabetic only::
          if not re.fullmatch('[a-zA-Z ]+',uname):
             messagebox.showwarning('User Name','User Name Characters Only')
             return 
          con_obj=sqlite3.connect(database='bank.sqlite')
          cur_obj=con_obj.cursor()
          cur_obj.execute('insert into users (users_pass,users_name,users_email,users_mob,users_bal,users_adhar,users_OpenDate) values(?,?,?,?,?,?,?)',(upass,uname,umail,umob,ubal,uadhar,current_date))
          con_obj.commit()
          con_obj.close()

          con_obj=sqlite3.connect(database='bank.sqlite')
          cur_obj=con_obj.cursor()
          cur_obj.execute('select max(users_acn) from users')
          tup=cur_obj.fetchone()
          uacn=tup[0]
          con_obj.close()
#Sending e-mail with msg (Account created) and auto generated password init:
          try:
            gmail_con=gmail.GMail('rayyanulhaque512@gmail.com','fntt otwo frgh waor')
            umsg=f'''"Dear {uname},
                          Your recent transaction has been successfully processed.
                          Account Number:{uacn}.
                          Account Pass:{upass}.
                          Your Current Balance:{ubal}.
                          Kindly change your password when you login for the first time 
                          For any query, please contact our support team at  My Bank
                          Thank you for banking with My Bank.........
'''
            msg=gmail.Message(to=umail,subject='Account Opened',text=umsg) 
            gmail_con.send(msg)
            messagebox.showinfo('Open acount','Acount Created Check your email for Acn/Pass')
          except:
            messagebox.showerror('Check Your Internet Connection','Try again')     
     def reset():
      name_entry.delete(0,"end")
      email_entry.delete(0,"end")
      mob_entry.delete(0,"end")
      adhar_entry.delete(0,"end")
      name_entry.focus()   
#Name Label and Entry
     name_label=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='User Name')
     name_label.place(relx=.14,rely=.2,)
     
     name_entry=Entry(ifrm,font=('arial',14),bd=1,bg='#3d3d3d',fg='white')
     name_entry.place(relx=.14,rely=.3)
     name_entry.focus()

#Mobile num Label and Entry
     mob_label=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='Phone no.')
     mob_label.place(relx=.14,rely=.4,)

     mob_entry=Entry(ifrm,font=('arial',14),bd=1,bg='#3d3d3d',fg='white')
     mob_entry.place(relx=.14,rely=.5)

#Email Label and Entry
     email_label=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='Email')
     email_label.place(relx=.65,rely=.2,)

     email_entry=Entry(ifrm,font=('arial',14),bd=1,bg='#3d3d3d',fg='white')
     email_entry.place(relx=.65,rely=.3)

#Adhar num Label and Entry
     adhar_label=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='Adhar no.')
     adhar_label.place(relx=.65,rely=.4,)

     adhar_entry=Entry(ifrm,font=('arial',14),bd=1,bg='#3d3d3d',fg='white')
     adhar_entry.place(relx=.65,rely=.5)

#Open Account,Reset Button:
     open_btn=Button(ifrm, command=open_click,width=13,text='Open Account',font=('arial',18,'bold'),bg='#3d3d3d',fg='white')
     open_btn.place(relx=.29,rely=.7)

     reset_btn=Button(ifrm,command=reset,width=13,text='Reset',font=('arial',18,'bold'),bg='#3d3d3d',fg='white')
     reset_btn.place(relx=.54,rely=.7)
#View User Screen:

  def view_click():
    ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
    ifrm.configure(bg='white')
    ifrm.place(relx=.2,rely=.15,relwidth=.65,relheight=.7)

    title_ifrm=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text="This is Account Holder's Screen:")
    title_ifrm.pack()

    frame = Frame(ifrm)
    frame.pack(expand=True,fill="both")

    data={}
    i=1
    con_obj=sqlite3.connect(database='bank.sqlite')
    cur_obj=con_obj.cursor()
    cur_obj.execute("select * from users")
#For loop to  fetch data to preview User table

    for tup in cur_obj:
            data[f"{i}"]= {"Account No.": tup[0], "Name":tup[2], " Account OpenDate": tup[7],"Adhar":tup[6],"Contact No.":tup[4],"E-mail":tup[3],"Balance":tup[5]}
            i+=1

    con_obj.close()
        # Create Table Model
    model = TableModel()
    model.importDict(data)  # Load data into the model

        # Create Table Canvas inside Frame (Important Fix)
    table = TableCanvas(frame, model=model, editable=True)
    table.show()

# Create Table Model
    model = TableModel()
    model.importDict(data)  # Load data into the model

# Create table canvas
    table = TableCanvas(frame, model=model, editable=True)
    table.show() 

#Delete Click Function:
  def delete_click():
    ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
    ifrm.configure(bg='white')
    ifrm.place(relx=.2,rely=.15,relwidth=.65,relheight=.7)

    title_ifrm=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='This is Delete User Screen:')
    title_ifrm.pack()

    def delete_db():
       uacn=acn_entry.get()
       con_obj=sqlite3.connect(database='bank.sqlite')
       cur_obj=con_obj.cursor()
       cur_obj.execute("delete from users where users_acn=?",(uacn,))
       cur_obj.execute("delete from Txn where txn_acno=?",(uacn,))
       con_obj.commit()
       con_obj.close()
       if len (uacn)==0:
          messagebox.showwarning('Delete','Mention Account No. to Delete')
          return
       messagebox.showinfo('Delete',f'User With Account no.. {uacn} is Deleted')
  ##Reset Button function::
    def reset():
     acn_entry.delete(0,"end")
     acn_entry.focus()
    acn_label=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='Acount no.')
    acn_label.place(relx=.3 , rely=.3)

    acn_entry=Entry(ifrm,font=('arial',14),bg='#3d3d3d',bd=3,fg='white')
    acn_entry.place(relx=.45,rely=.3)
    acn_entry.focus()
#Reset and Delete buttons:

    reset_btn=Button(ifrm,command=reset,width=8,text='Reset',font=('arial',15,'bold'),bg='#3d3d3d',fg='white',bd=5)
    reset_btn.place(relx=.35,rely=.6)

    delete_btn =Button(ifrm,command=delete_db,width=8,text='Delete',font=('arial',15,'bold'),bg='#3d3d3d',fg='white',bd=5)
    delete_btn.place(relx=.48,rely=.6)

#welcome_label And Buttons [Create,View,Delete]:
  wel_label=Label(frm,font=('arial',20,'bold'),bg='#578E7E',text='Welcome Admin....')
  wel_label.place(relx=0,rely=0)
 
  create_btn=Button(frm,command=create_click,width=12,text='Create user',font=('arial',20,'bold'),bg='#3d3d3d',bd=5,fg='#E5D9F2')
  create_btn.place(relx=0,rely=.2)

  view_btn=Button(frm,command=view_click,width=12,text='Acn Users',font=('arial',20,'bold'),bg='#3d3d3d',bd=5,fg='#E5D9F2')
  view_btn.place(relx=0,rely=.4)

  delete_btn=Button(frm,command=delete_click,width=12,text='Delete user',font=('arial',20,'bold'),bg='#3d3d3d',bd=5,fg='#E5D9F2')
  delete_btn.place(relx=0,rely=.6)
#Forgot password function:

def forgot_password_screen():
  frm=Frame(win,highlightbackground='black',highlightthickness=2)
  frm.configure(bg='#578E7E')
  frm.place(relx=0,rely=.15,relwidth=1,relheight=.73)
  def back_click():
    frm.destroy()
    main_screen()
#Fetching Forgotten Password From Database :Validation  

  def get_pass():
    uacn=acn_entry.get()
    umob=phone_no_entry.get()
    uemail=email_entry.get()
    if len (uacn)==0 or len (umob)==0 or len (uemail)==0:
            messagebox.showwarning('Forgot',"Fields required")
            return
#Fetching Database:

    con_obj=sqlite3.connect(database='bank.sqlite')
    cur_obj=con_obj.cursor()
    cur_obj.execute('select users_name,users_pass from users where users_acn=? and users_email=? and users_mob=?',(uacn,uemail,umob))
    tup=cur_obj.fetchone()
    con_obj.close()
    if tup == None:
      messagebox.showerror('Forgot password','Inavlid Details')
    else:

#E-mail sending with Forgotten Password(e-mail for forgotten password)
      try:
            gmail_con=gmail.GMail('rayyanulhaque512@gmail.com','fntt otwo frgh waor')
            umsg=f'''Dear {tup[0]},
We received a request to reset your password. Please find your updated password below:
Your Password:({tup[1]})
For your security, we recommend that you change your password once you log in to your account. You can do this by navigating to the "Account Settings" section.
If you did not request a password reset or have any issues accessing your account, please contact our support team immediately at 7665931215 or rayyanulhaque512@gmail.com.

Thank you,  
My Bank Support Team'''
            msg=gmail.Message(to=uemail,subject='Password Recovery',text=umsg) 
            gmail_con.send(msg)
            messagebox.showinfo('Forgot Password','Kindly check your email for Password')
      except:
            messagebox.showerror('Check Your Internet Connection','Try again')
#Back Button :
  back_btn=Button(frm,command=back_click,text='Back',font=('arial',20,'bold'),bg='#3D3D3D',bd=5,fg='#ffffff')
  back_btn.place(relx=0,rely=0)
#Forgot Password Frame :
##Reset button Function::
  def reset():
     acn_entry.delete(0,"end")
     email_entry.delete(0,"end")
     phone_no_entry.delete(0,"end")
     acn_entry.focus()
#Lables and Entries for Forgot Password frame
  acn_label=Label(frm,font=('arial',20,'bold'),bg='#578E7E',text="Account")
  acn_label.place(relx=.3,rely=.1)

  acn_entry=Entry(frm,font=('arial',20,'bold'),bd=3,bg='#E5D9F2',fg='#000000')
  acn_entry.place(relx=.4,rely=.1)
  acn_entry.focus()

  email_label=Label(frm,font=('arial',20,'bold'),bg='#578E7E',text="Email")
  email_label.place(relx=.3,rely=.2)

  email_entry=Entry(frm,font=('arial',20,'bold'),bd=3,bg='#E5D9F2',fg='#000000')
  email_entry.place(relx=.4,rely=.2)

  phone_no_label=Label(frm,font=('arial',20,'bold'),bg='#578E7E',text="Phone no.")
  phone_no_label.place(relx=.3,rely=.3)

  phone_no_entry=Entry(frm,font=('arial',20,'bold'),bd=3,bg='#E5D9F2',fg='#000000')
  phone_no_entry.place(relx=.4,rely=.3)

  submit_btn=Button(frm,command=get_pass,text='submit',font=('arial',19,'bold'),bg='#3d3d3d',bd=5,fg='#ffffff')
  submit_btn.place(relx=.43,rely=.4)

  reset_btn=Button(frm,command=reset,text='Reset',font=('arial',19,'bold'),bg='#3d3d3d',bd=5,fg='#ffffff')
  reset_btn.place(relx=.51,rely=.4)

#Frame for User Screen / User page
def welcome_user_screen():
  frm=Frame(win,highlightbackground='black',highlightthickness=2)
  frm.configure(bg='#E5D9F2')
  frm.place(relx=0,rely=.15,relwidth=1,relheight=.73)
#User image on user Screen ::
  if os.path.exists(f"{uacn}.png"):
   img=ImageTk.PhotoImage(Image.open(f"{uacn}.png").resize((120,120)),master=win)
  else:
   img=ImageTk.PhotoImage(Image.open('User.png').resize((120,120)),master=win)
     
  img_label=Label(frm,image=img)
  img_label.image=img
  img_label.place(relx=.03,rely=.06)

  def update_image():
     path=filedialog.askopenfilename()
     shutil.copy(path,f"{uacn}.png")

     img=ImageTk.PhotoImage(Image.open(path).resize((120,120)),master=win)
     img_label=Label(frm,image=img)
     img_label.image=img
     img_label.place(relx=.03,rely=.06)
#Update Users Image Button::
  btn_update_img=Button(frm,command=update_image,width=13,text='Update Image',font=('arial',10,'bold'),bg='#3d3d3d',bd=3,fg='#ffffff')
  btn_update_img.place(relx=.03,rely=.27)
#Logout
  def logout_click():
    resp=messagebox.askyesno('Logout','Confirm Logout')#Ask before logout::
    if resp:
      frm.destroy()
      main_screen()
   

####Check Balance Function:
  def check_click():
    ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
    ifrm.configure(bg='white')
    ifrm.place(relx=.17,rely=.12,relwidth=.70,relheight=.8)

    title_ifrm=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='This is Check Balance Screen:')
    title_ifrm.pack() 

###Fetching data From database to show User's current Avialable balance:
    con_obj=sqlite3.connect(database='bank.sqlite')
    cur_obj=con_obj.cursor()
    cur_obj.execute('select users_bal,users_OpenDate,users_adhar from users where users_acn=?',(uacn,))
    tup=cur_obj.fetchone()
    con_obj.commit()
    con_obj.close()

    label_bal=Label(ifrm,text=f"Available Balance :\t\t{tup[0]}",font=('arial',18,'bold'),bg='#ffffff' )
    label_bal.place(relx=.2 ,rely=.2)

    label_opendate=Label(ifrm,text=f"Account Opendate :\t{tup[1]}" ,font=('arial',18,'bold'),bg='#ffffff' )
    label_opendate.place(relx=.2,rely=.4)

    label_adhar=Label(ifrm,text=f"Users Adhar No :\t\t{tup[2]}",font=('arial',18,'bold'),bg='#ffffff' )
    label_adhar.place(relx=.2 ,rely=.6)
     
###Update Balance Funtion 
  def update_click():
    ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
    ifrm.configure(bg='white')
    ifrm.place(relx=.17,rely=.12,relwidth=.70,relheight=.8)

    title_ifrm=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='This is Update Balance Screen:')
    title_ifrm.pack() 

#Getting users Update credentials from Database:
    def update_details():
      uname=name_entry.get()
      umob=mob_entry.get()
      uemail=email_entry.get()
      upass=pass_entry.get()
      if len (uname)==0 or len (umob)==0 or len (uemail)==0 or len (upass)==0:
            messagebox.showwarning('Update',"Fields required")
            return
#Connection from database:

      con_obj=sqlite3.connect(database='bank.sqlite')
      cur_boj=con_obj.cursor()
      cur_boj.execute('update users set users_name=?,users_mob=?,users_email=?,users_pass=? where users_acn=?',(uname,umob,uemail,upass,uacn))
      con_obj.commit()
      con_obj.close()
      messagebox.showinfo('Update','Details Updated')      
#Create connection from Database: for Update user credentials

    con_obj=sqlite3.connect(database='bank.sqlite')
    cur_boj=con_obj.cursor()
    cur_boj.execute('select * from users where users_acn=?',(uacn,))
    tup=cur_boj.fetchone()
    con_obj.close()
#Name label and Entry

    name_label=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='User Name:')
    name_label.place(relx=.14,rely=.2,)

    name_entry=Entry(ifrm,font=('arial',14),bd=1,bg='#3d3d3d',fg='white')
    name_entry.place(relx=.14,rely=.3)
    name_entry.insert(0,tup[2])
    name_entry.focus()

#Mobile num Label and Entry
    mob_label=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='Phone no:')
    mob_label.place(relx=.14,rely=.4,)

    mob_entry=Entry(ifrm,font=('arial',14),bd=1,bg='#3d3d3d',fg='white')
    mob_entry.place(relx=.14,rely=.5)
    mob_entry.insert(0,tup[4])

#Email Label and Entry
    email_label=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='Email:')
    email_label.place(relx=.65,rely=.2,)

    email_entry=Entry(ifrm,font=('arial',14),bd=1,bg='#3d3d3d',fg='white')
    email_entry.place(relx=.65,rely=.3)
    email_entry.insert(0,tup[3])

    pass_label=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='Password:')
    pass_label.place(relx=.65,rely=.4,)

    pass_entry=Entry(ifrm,font=('arial',14),bd=1,bg='#3d3d3d',fg='white')
    pass_entry.place(relx=.65,rely=.5)
    pass_entry.insert(0,tup[1])
##Reset button function::
    def reset():
       name_entry.delete(0,"end")
       mob_entry.delete(0,"end")
       email_entry.delete(0,"end")
       pass_entry.delete(0,"end")
       name_entry.focus()
#Update Details and Reset Button:
    update_btn=Button(ifrm,command=update_details,width=8,text='Update',font=('arial',18,'bold'),bg='#3d3d3d',bd=2,fg='#ffffff')
    update_btn.place(relx=.37,rely=.7)

    reset_btn=Button(ifrm,command=reset,width=8,text='Reset',font=('arial',18,'bold'),bg='#3d3d3d',bd=2,fg='#ffffff')
    reset_btn.place(relx=.5,rely=.7)
   
###Deposite Button Function
  def deposite_click():
    ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
    ifrm.configure(bg='white')
    ifrm.place(relx=.17,rely=.12,relwidth=.70,relheight=.8)

    title_ifrm=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='This is Deposite Amount Screen:')
    title_ifrm.pack() 

##Deposite balance Function
    def deposite_amt():
     uamt=float(amount_entry.get()) 

#Connection from database:for get acn no.:
     con_obj=sqlite3.connect(database='bank.sqlite')
     cur_obj=con_obj.cursor()
     cur_obj.execute('select users_bal from users where users_acn=?' ,(uacn,))
     ubal=cur_obj.fetchone()[0]
     con_obj.close()

#Connection From database: for update balance After adding :
     con_obj=sqlite3.connect(database='bank.sqlite')
     cur_obj=con_obj.cursor()
     cur_obj.execute('update users set users_bal=users_bal+? where users_acn=?' ,(uamt,uacn,))
     con_obj.commit()
     con_obj.close()

#Connection from databases:For insert into database after updating values.. provide date also:
     con_obj=sqlite3.connect(database='bank.sqlite')
     cur_obj=con_obj.cursor()
     cur_obj.execute('insert into Txn (txn_acno,txn_type,txn_date,txn_amt,txn_update_bal)values(?,?,?,?,?)',(uacn,'Creadit.',time.strftime('%d-%b-%Y %r'),uamt,ubal+uamt))
     con_obj.commit()
     con_obj.close()
     
     messagebox.showinfo('Deposite',f'Amount: {uamt} is Creadited to your Account Update Balance: {ubal+uamt}')
#Amount label and Entry:
    amount_label=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='Enter Amount:')
    amount_label.place(relx=.26,rely=.38)

    amount_entry=Entry(ifrm,font=('arial',18),bd=3,bg='#3d3d3d',fg='white')
    amount_entry.place(relx=.42,rely=.38)
    ##Reset button function::
    def reset():
       amount_entry.delete(0,"end")
#Reset Amount Button:
    reset_btn=Button(ifrm,command=reset,width=9,text='Reset',font=('arial',15,'bold'),bg='#3d3d3d',fg='white')
    reset_btn.place(relx=.43,rely=.56)
#Deposite Amount Button:
    deposite_btn=Button(ifrm,command=deposite_amt,width=9,text='Deposite',font=('arial',15,'bold'),bg='#3d3d3d',fg='white')
    deposite_btn.place(relx=.56,rely=.56) 

###Withdraw Click Function
  def withdram_click():
    ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
    ifrm.configure(bg='white')
    ifrm.place(relx=.17,rely=.12,relwidth=.70,relheight=.8)

    title_ifrm=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='This is Withdraw Balance Screen:')
    title_ifrm.pack()  

###Withdrawn Amount function
    def withdrawn_amt():
      uamt=float(withdraw_entry.get()) 

#Connection from databases t0o get Acn no.:
      con_obj=sqlite3.connect(database='bank.sqlite')
      cur_obj=con_obj.cursor()
      cur_obj.execute('select users_bal from users where users_acn=?' ,(uacn,))
      ubal=cur_obj.fetchone()[0]
      con_obj.close()

#Condition to Check were the amount of withdrawn is lessthen or equal to the amount in user's ACN::
      if ubal>=uamt:

          con_obj=sqlite3.connect(database='bank.sqlite')
          cur_obj=con_obj.cursor()
          cur_obj.execute('update users set users_bal=users_bal-? where users_acn=?' ,(uamt,uacn,))
          con_obj.commit()
          con_obj.close()

          con_obj=sqlite3.connect(database='bank.sqlite')
          cur_obj=con_obj.cursor()
          cur_obj.execute('insert into Txn (txn_acno,txn_type,txn_date,txn_amt,txn_update_bal)values(?,?,?,?,?)',(uacn,'Debit.',time.strftime('%d-%b-%Y %r'),uamt,ubal-uamt))
          con_obj.commit()
          con_obj.close()
          
          messagebox.showinfo('Withdrawn',f'Amount: {uamt} is Debited from your Account Update Balance: {ubal-uamt}')
      else:
         messagebox.showerror('withdrawn',f'Insufficient Balance {ubal}')

#Withdrawn Amount label and Entry::
    withdraw_label=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='Enter Amount:')
    withdraw_label.place(relx=.26,rely=.38)

    withdraw_entry=Entry(ifrm,font=('arial',18),bd=3,bg='#3d3d3d',fg='white')
    withdraw_entry.place(relx=.42,rely=.38)
#Reset Buttom function:
    def reset():
       withdraw_entry.delete(0,"end")
#Reset Amount Button:
    reset_btn=Button(ifrm,command=reset,width=9,text='Reset',font=('arial',15,'bold'),bg='#3d3d3d',fg='white')
    reset_btn.place(relx=.43,rely=.56)
#Withdraw Amount Button:
    withdraw_btn=Button(ifrm,command=withdrawn_amt,width=9,text='Withdraw',font=('arial',15,'bold'),bg='#3d3d3d',fg='white')
    withdraw_btn.place(relx=.56,rely=.56)

###Trasfer Click Function and Title::
  def transfer_click():
    ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
    ifrm.configure(bg='white')
    ifrm.place(relx=.17,rely=.12,relwidth=.70,relheight=.8)

    title_ifrm=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='This is Transfer Balance Screen:')
    title_ifrm.pack()

##Transfer Amount Function
    def transfer_amt():
      #get amount entery::
      uamt=float(amount_entry.get()) 
      to_acn=int(to_entry.get())

##Connection to get Users details from database ::
      con_obj=sqlite3.connect(database='bank.sqlite')
      cur_obj=con_obj.cursor()
      cur_obj.execute('select users_email,users_bal from users where users_acn=?' ,(uacn,))
      tup=cur_obj.fetchone()
      ubal=float(tup[1])
      uemail=tup[0]
      con_obj.close()

##Condition to check were the amount of transfer is lessthen or equal to the amount user enter to transfer::
      if ubal>=uamt:
        con_obj=sqlite3.connect(database='bank.sqlite')
        cur_obj=con_obj.cursor()
        cur_obj.execute('select * from users where users_acn=?',(to_acn,))
        tup=cur_obj.fetchone()
        con_obj.close()

##Condition to check Acn no is correct or Not 
        if tup==None:
           messagebox.showerror('transfer','Acn Does not match try again after some time')
##Generate OTP Randomly Everytime
        else:
            otp=random.randint(1000,9999)

##Sending OTP email to user who is transfering amount::
            try:
               gmail_con=gmail.GMail('rayyanulhaque512@gmail.com','fntt otwo frgh waor')
               umsg=f'''Dear {uname},
               Your Generated Otp Is ({otp}) kindly verify this Otp to continue'''
               msg=gmail.Message(to=uemail,subject='OTP Verification',text=umsg) 
               gmail_con.send(msg)
               messagebox.showinfo('Transaction','We have otp to your registered e-mail')

               uotp=simpledialog.askinteger('OTP','Enter OTP')
##Condition for Matching OTP::
               if otp == uotp:
                 con_obj=sqlite3.connect(database='bank.sqlite')
                 cur_obj=con_obj.cursor()
                 cur_obj.execute('update users set users_bal=users_bal-? where users_acn=?' ,(uamt,uacn,))
                 cur_obj.execute('update users set users_bal=users_bal+? where users_acn=?' ,(uamt,to_acn,))

                 con_obj.commit()
                 con_obj.close()

                 to_bal=tup[5]
##Connection to insert amount after and before tranfering::
                 con_obj=sqlite3.connect(database='bank.sqlite')
                 cur_obj=con_obj.cursor()
                 cur_obj.execute('insert into Txn (txn_acno,txn_type,txn_date,txn_amt,txn_update_bal)values(?,?,?,?,?)',(uacn,'Debit.',time.strftime('%d-%b-%Y %r'),uamt,ubal-uamt))
                 cur_obj.execute('insert into Txn (txn_acno,txn_type,txn_date,txn_amt,txn_update_bal)values(?,?,?,?,?)',(to_acn,'Creadit.',time.strftime('%d-%b-%Y %r'),uamt,ubal+uamt))
                 con_obj.commit()
                 con_obj.close()
              
                 messagebox.showinfo('Transfer',f'Amount: {uamt} is Debited from your Account Update Balance: {ubal-uamt}')
               else:
                     messagebox.showerror('OTP','Invalid OTP')

            except:
                 messagebox.showerror('Check Your Internet Connection:','Try again')
                  
      else:
         messagebox.showerror('Transfer',f'Insufficient Balance {ubal}')

##Label for To Acn no.:
    to_label=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='To Acn:')
    to_label.place(relx=.26,rely=.35)

    to_entry=Entry(ifrm,font=('arial',18),bd=3,bg='#3d3d3d',fg='white')
    to_entry.place(relx=.39,rely=.35)

    amount_label=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='Amount:')
    amount_label.place(relx=.26,rely=.45)

    amount_entry=Entry(ifrm,font=('arial',18),bd=3,bg='#3d3d3d',fg='white')
    amount_entry.place(relx=.39,rely=.45)
#Reset Button Function::
    def reset():
       amount_entry.delete(0,"end")
       to_entry.delete(0,"end")
    #Reset button:
    reset_btn=Button(ifrm,command=reset,width=8,text='Reset',font=('arial',15,'bold'),bg='#3d3d3d',fg='white')
    reset_btn.place(relx=.41,rely=.58)
#Transfer Amount Button:
    transfer_btn=Button(ifrm,command=transfer_amt,width=8,text='Transfer',font=('arial',15,'bold'),bg='#3d3d3d',fg='white')
    transfer_btn.place(relx=.53,rely=.58)

###Transaction History Balance Function:
  def tnx_click():
    ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
    ifrm.configure(bg='white')
    ifrm.place(relx=.17,rely=.12,relwidth=.70,relheight=.8)

    title_ifrm=Label(ifrm,font=('arial',18,'bold'),bg='#ffffff',text='This is Transaction History Screen:')
    title_ifrm.pack() 

###Txn Datatable for txn History:
    # Create a Frame (Fix for NoneType error)
    frame = Frame(ifrm)
    frame.pack(expand=True,fill="both")

    data={}
    i=1
    con_obj=sqlite3.connect(database='bank.sqlite')
    cur_obj=con_obj.cursor()
    cur_obj.execute("select * from Txn where txn_acno=?",(uacn,))
#Loop for everytime TXN Done by user::
    for tup in cur_obj:
            data[f"{i}"]= {"Txn Id": tup[0], "Txn Amt":tup[4], "Txn Date": tup[3],"Txn Type":tup[2],"Updated Bal":tup[5]}
            i+=1

    con_obj.close()
        # Create Table Model
    model = TableModel()
    model.importDict(data)  # Load data into the model

        # Create Table Canvas inside Frame (Important Fix)
    table = TableCanvas(frame, model=model, editable=True)
    table.show()

# Create Table Model
    model = TableModel()
    model.importDict(data)  # Load data into the model

# Create table canvas
    table = TableCanvas(frame, model=model, editable=True)
    table.show() 

  wel_label=Label(frm,font=('arial',18,'bold'),bg='#E5D9F2',text=f'Welcome, {uname}')
  wel_label.place(relx=.01,rely=0) 

  logout_btn=Button(frm,command=logout_click,text='Logout',font=('Helvetica',20,'bold'),bg='#3d3d3d',fg='white',bd=5)
  logout_btn.place(relx=.92 , rely=0)

##### All Buttons in Welcome User screen :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: 
  check_btn=Button(frm,command=check_click, width=16,text='Check Balance',font=('arial',13,'bold'),bg='#3d3d3d',bd=3,fg='#ffffff')
  check_btn.place(relx=.01,rely=.35)

  Update_btn=Button(frm,command=update_click,width=16,text='Update Balance',font=('arial',13,'bold'),bg='#3d3d3d',bd=3,fg='#ffffff')
  Update_btn.place(relx=.01,rely=.45) 

  deposit_btn=Button(frm,command=deposite_click,width=16,text='Deposite Amount',font=('arial',13,'bold'),bg='#3d3d3d',bd=3,fg='#ffffff')
  deposit_btn.place(relx=.01,rely=.55)

  withdram_btn=Button(frm,command=withdram_click,width=16,text='Withdraw Amount',font=('arial',13,'bold'),bg='#3d3d3d',bd=3,fg='#ffffff')
  withdram_btn.place(relx=.01,rely=.65)

  transfer_btn=Button(frm,command=transfer_click,width=16,text='Transfer Amount',font=('arial',13,'bold'),bg='#3d3d3d',bd=3,fg='#ffffff')
  transfer_btn.place(relx=.01,rely=.75)

  tnx_history_btn=Button(frm,command=tnx_click,width=16,text='Tnx History',font=('arial',13,'bold'),bg='#3d3d3d',bd=3,fg='#ffffff')
  tnx_history_btn.place(relx=.01,rely=.85)
main_screen()
win.mainloop()