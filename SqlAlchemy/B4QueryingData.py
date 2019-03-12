from A5CompleteCode import cookies
from sqlalchemy.sql import select 
from sqlalchemy import create_engine
import pprint

engine = create_engine('postgresql+psycopg2://@localhost:' '5432/mydb')
connection = engine.connect()

s = select([cookies])
print(str(s))
rp = connection.execute(s)
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(rp.fetchall())
print("\n")

#using the select method on the table object 
sel = cookies.select()
result = connection.execute(sel)
results = result.fetchall()
pp.pprint(results)
print("\n")

#manipulating results 
for firs_row in results:
    for a in firs_row:
        print(a)
print("\n")
#getting only the cookie name 
for records in results:
    print(records.cookie_name)
print("\n")
#getting one result 
#one = cookies.select()
res = connection.execute(sel)
ress = res.scalar()
print(ress)
