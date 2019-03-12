from A5CompleteCode import cookies, users, orders, line_items
from sqlalchemy.sql import select
from sqlalchemy import create_engine, desc
import pprint

engine = create_engine('postgresql+psycopg2://@localhost:' '5432/mydb')
connection = engine.connect()

pp = pprint.PrettyPrinter(indent=2)

s = select([cookies.c.cookie_name, cookies.c.quantity])
rp = connection.execute(s)
pp.pprint(rp.keys())
print("\n")
print(rp.scalar())
print("\n")

# order by - to arrange the selected data desc() or not 
selection1 = select([cookies.c.cookie_name, cookies.c.quantity, cookies.c.unit_cost]).order_by(cookies.c.quantity)
selection1 = selection1.order_by(cookies.c.cookie_name)

rp = connection.execute(selection1)
for cookie in rp:
    pp.pprint('{} - {}'.format(cookie.cookie_name, cookie.quantity))

print("\n")    

selection2 = select([cookies.c.cookie_name, cookies.c.quantity, cookies.c.unit_cost])
selection2 = selection2.order_by(desc(cookies.c.quantity))
rp1 = connection.execute(selection2)    
for records in rp1:
    pp.pprint('{}-{}'.format(records.cookie_name, records.quantity))
print("\n")

'''limiting the number of records before the result proxy is executed to save time other wise the
rp would execute all the records in the database and that would take time. 
'''
sel3 = select([cookies.c.cookie_name, cookies.c.quantity])
sel3 = sel3.order_by(cookies.c.quantity)
sel3 = sel3.limit(2)
rp3 = connection.execute(sel3)
print([result.cookie_name for result in rp3])


    