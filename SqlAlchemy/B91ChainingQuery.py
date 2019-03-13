from A5CompleteCode import cookies
from sqlalchemy import create_engine, desc, and_, or_, not_
from sqlalchemy.sql import select, func
import pprint
from A5CompleteCode import cookies, orders, users, line_items
import sqlalchemy as sqal 

engine = create_engine('postgresql+psycopg2://@localhost:' '5432/mydb')
connection = engine.connect()
pp = pprint.PrettyPrinter(indent=2)
'''
def get_orders_by_customer(customer_name):
    columns=[orders.c.order_id, users.c.username, users.c.phone, cookies.c.cookie_name,\
             line_items.c.quantity, line_items.c.extended_cost]
    cust_orders = select(columns)
    cust_orders = cust_orders.select_from(users.join(orders).join(line_items).join(cookies))
    cust_orders = cust_orders.where(users.c.username == customer_name)
    result = connection.execute(cust_orders).fetchall()
    return result
print(get_orders_by_customer("cakeeater"))
'''


''' now we re going to add another dimension to the parameters about shipped '''
def get_orders_by_customer(customer_name, shipped=None, details=False):
    columns=[orders.c.order_id, users.c.username, users.c.phone, cookies.c.cookie_name,\
             line_items.c.quantity, line_items.c.extended_cost]
    cust_orders = select(columns)
    cust_orders = cust_orders.select_from(users.join(orders).join(line_items).join(cookies))
    cust_orders = cust_orders.where(users.c.username == customer_name)
    if shipped is not None:
        cust_orders = cust_orders.where(orders.c.shipped == shipped)
    result = connection.execute(cust_orders).fetchall()
    return result

#print(get_orders_by_customer('cakeeater'))

#print(get_orders_by_customer('cakeeater', details=True)) 

#print(get_orders_by_customer('cakeeater', shipped=True))

print(get_orders_by_customer('cakeeater', shipped="shipped")) 

#get_orders_by_customer('cakeeater', shipped=False, details=True)
    