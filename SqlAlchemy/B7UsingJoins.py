from A5CompleteCode import cookies
from sqlalchemy import create_engine, desc, and_, or_, not_
from sqlalchemy.sql import select, func
import pprint
from A4TableObject import cookies
import sqlalchemy as sqal 

engine = create_engine('postgresql+psycopg2://@localhost:' '5432/mydb')
connection = engine.connect()
pp = pprint.PrettyPrinter(indent=2)

s = select([func.sum(cookies.c.quantity)])
rp1 = connection.execute(s)
print([result  for result in rp1]) 

'''this will give you the current time stamp from the database server. 
there are various functions that at available and to see those functions one would need to command click 
func in the import statement. '''
print(connection.execute(func.current_timestamp()).scalar())
print("\n")


sel1 = select([func.count(cookies.c.cookie_name)]) 
rp2 = connection.execute(sel1)
record = rp2.first()
print(record.keys())
print(record.count_1)
print("\n")

'''fixing the column name of the result proxy above using the label function '''
sel2 = select([func.count(cookies.c.cookie_name).label('inventory_count')]) 
rp3 = connection.execute(sel2)
record1 = rp3.first()
print(record1.keys())
print(record1.inventory_count)
print("\n")

sel3 = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')
rp4 = connection.execute(sel3)
record2 = rp4.first()
pp.pprint(record2.items()) 
print("\n")

'''finding all cookie names that contain chocolate'''
sel4 = select([cookies]).where(cookies.c.cookie_name.like('%chocolate%'))
rp5 = connection.execute(sel4)
for record3 in rp5.fetchall():
    print(record3.cookie_name)
print("\n")

''' concatinating string with data from the table'''
sel5 = select([cookies.c.cookie_name, 'SKU-' + cookies.c.cookie_sku])
for row in connection.execute(sel5):
    print(row)
print("\n")

sel6 = select([cookies]).where( and_(cookies.c.quantity>23, cookies.c.unit_cost<.4))

for row in connection.execute(sel6):
    print(row.cookie_name)
print("\n")

upd1 = sqal.update(cookies).where(cookies.c.cookie_name == "chocolate chip")
upd1 = upd1.values(quantity=(cookies.c.quantity + 120)) 
result = connection.execute(upd1)
print(result.rowcount) 

sel7 = select([cookies]).where(cookies.c.cookie_name == "chocolate chip")
result = connection.execute(sel7).first()
for key in result.keys():
    print(key)
    print('{:>25}: {}'.format(key, result[key]))#the :>25 is just a print format changes the print 


