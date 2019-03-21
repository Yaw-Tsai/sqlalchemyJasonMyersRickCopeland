from sqlalchemy import create_engine, desc, and_, or_, not_
from sqlalchemy.sql import select, func, insert
import pprint
from A5CompleteCode import cookies, orders, users, line_items
import pprint


engine = create_engine('postgresql+psycopg2://@localhost:' '5432/mydb')
connection = engine.connect()
pp = pprint.PrettyPrinter(indent=2)

''' the first step is to check for attribute error here we will try to access an attribute
that does not exist and we will get an attribute erroe
s = select([users.c.username])
results = connection.execute(s)
for result in results:
    print(result.username)
    print(result.password)'''
    
''' now we are going to try to enter a second cookiemon user in the table which will give us 
an integrity error 
ins = insert(users).values(
    username="cookiemon",
    email_address="damon@cookie.com",
    phone="111-111-1111",
    password="password"
)
result = connection.execute(ins) ''' 

'''
now instead of letting the program get terminated by the interruption we can use the try exception 
block of code to make sure that we capture the exception'''
from sqlalchemy.exc import IntegrityError

ins = insert(users).values(
    username="cookiemon",
    email_address="damon@cookie.com",
    phone="111-111-1111",
    password="password"
)
try:
    result = connection.execute(ins)
except IntegrityError as error: 
    pp.pprint((error.args, error.params))
    