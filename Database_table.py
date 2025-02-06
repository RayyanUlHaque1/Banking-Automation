import sqlite3
con_obj=sqlite3.connect(database='bank.sqlite') #CWD
cur_obj=con_obj.cursor()
try:
      cur_obj.execute('''create table users(
                users_acn integer primary key autoincrement ,
                users_pass text,
                users_name text,
                users_email text,
                users_mob text,
                users_bal float, 
                users_adhar text,
                users_OpenDate text)''')


      cur_obj.execute('''create table Txn(
                txn_id integer primary key autoincrement ,
                txn_acno text,
                txn_type text,
                txn_date text,
                txn_amt float,
                txn_update_bal float)''')
      print ('Table Created')
except:
  pass 




con_obj.close()
