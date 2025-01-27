import pymysql # application pgm interface(API) helps to connect python and mysql 
db = pymysql.connect(user = 'root',password = '', host = 'localhost', database = 'temp_db') #connect is a class
cursor=db.cursor() # creates a cursor object to create table,insert  and fetch data from table

def insert_data(qry):
    cursor.execute(qry)
    db.commit()   
    
def selectonerecord(qry):
    cursor.execute(qry)
    d=cursor.fetchone()
    return d

def update_data(qry):
    cursor.execute(qry)
    db.commit()#permanently saves modifications to the db
    
def selectrecord(qry):
    cursor.execute(qry)
    d=cursor.fetchall()
    return d
    
    