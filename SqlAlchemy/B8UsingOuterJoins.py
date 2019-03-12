from A5CompleteCode import cookies
from sqlalchemy import create_engine, desc, and_, or_, not_
from sqlalchemy.sql import select, func, 
import pprint
from A5CompleteCode import cookies, orders, users, line_items
import sqlalchemy as sqal 

engine = create_engine('postgresql+psycopg2://@localhost:' '5432/mydb')
connection = engine.connect()
pp = pprint.PrettyPrinter(indent=2)

columns = [users.c.username, func.count(orders.c.order_id)]
all_orders = select(columns)
all_orders = all_orders.select_from(users.outerjoin(orders)) 
all_orders = all_orders.group_by(users.c.username)
result = connection.execute(all_orders).fetchall()
for row in result:
    print(row)