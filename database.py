import sqlite3
con=sqlite3.connect('d:/taha123.db')
cur=con.cursor()
def craet():
    cur.execute('CREATE TABLE IF NOT EXISTS taha(id integer primary key,fname text,lname text,email text,password)')
    con.commit()
def signup(fname,lname,email,password):
    cur.execute('INSERT INTO taha VALUES(NULL,?,?,?,?)',(fname,lname,email,password))
    con.commit()
def signin(fname,lname,email,password):
    cur.execute('select * from taha where fname=? and lname=? and email=? and password=?',(fname,lname,email,password))
    return cur.fetchall()