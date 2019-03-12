from A5CompleteCode import cookies
from sqlalchemy import create_engine, desc, and_, or_, not_
from sqlalchemy.sql import select, func
import pprint
from A5CompleteCode import cookies, orders, users, line_items
import sqlalchemy as sqal 

engine = create_engine('postgresql+psycopg2://@localhost:' '5432/mydb')
connection = engine.connect()
pp = pprint.PrettyPrinter(indent=2)


columns = [orders.c.order_id, users.c.username, users.c.phone,\
           cookies.c.cookie_name, line_items.c.quantity,\
           line_items.c.extended_cost]
cookiemon_orders = select(columns)
cookiemon_orders = cookiemon_orders.select_from(orders.join(users).join(\
                        line_items).join(cookies)).where(users.c.username ==\
                            'cookiemon')
result = connection.execute(cookiemon_orders).fetchall()
for row in result:
    print(row)
