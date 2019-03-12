from sqlalchemy.sql import select, func
from Ch1A import *
from sqlalchemy import create_engine, cast, and_, or_, not_, update, delete
from _sqlite3 import Row



def main():
    engine = create_engine('sqlite:///cookies1.db')
    connection = engine.connect()
    '''
    s = select([TableCookies])
    print(str(s))
    rp = connection.execute(s)
    results = rp.fetchall()
    
    first_row = results[0]
    print(first_row)
    print(first_row[1])
    print(first_row.cookie_name)
    print(first_row[TableCookies.c.cookie_name])
    
    for record in results:
        print(record.cookie_name)
    '''
    
    '''slection = select([TableCookies.c.cookie_name, TableCookies.c.quantity])
    slection = slection.order_by(TableCookies.c.quantity)
    rp = connection.execute(slection)
    print(rp.keys())
    result = rp.fetchall()
    for a in result:
        print(a)
    print(result)'''
    
    '''
    s = select([TableCookies.c.cookie_name, TableCookies.c.quantity])
    s=s.order_by(TableCookies.c.cookie_name)
    s=s.limit(2)
    rp = connection.execute(s)
    print([r.cookie_name for r in rp])
    '''
    
    '''
    s = select([func.sum(TableCookies.c.quantity)])
    rp = connection.execute(s)
    print(rp.scalar())
    '''
    #Counting our inventory record 
    '''
    s = select([func.count(TableCookies.c.cookie_name)])
    rp = connection.execute(s)
    record = rp.first()
    print(record.keys())
    print(record.count_1)
    '''
    #filtering the data using the where clause
    '''
    s = select([TableCookies]).where(TableCookies.c.cookie_name == 'chocolate chip')
    rp = connection.execute(s)
    record = rp.first()
    print(record.items())
    '''
    #finding names that have chocolate in them 
    '''
    s = select([TableCookies]).where(TableCookies.c.cookie_name.like('%chocolate%'))
    rp = connection.execute(s)
    for record in rp.fetchall():
        print(record.cookie_name)
    '''
    #String Concatenation with + here sku a string is being concatenated to the cookie sku code
    '''
    s = select([TableCookies.c.cookie_name, 'SKU-' +TableCookies.c.cookie_sku])
    for rowe in connection.execute(s):
        print(rowe)
    '''
    #Inventory values by cookies 
    '''
    s = select([TableCookies.c.cookie_name, cast((TableCookies.c.quantity * TableCookies.c.unit_cost), Numeric(12,2)).label('inv_cost')])
 
    for rowe in connection.execute(s):
        print('{} - {}'.format(rowe.cookie_name, rowe.inv_cost))
        '''
    #conjunction - using more than one operator
    '''
    s = select([TableCookies]).where(and_(TableCookies.c.quantity>23, TableCookies.c.unit_cost<0.40))
    for rowe in connection.execute(s):
        print(rowe.cookie_name)
        '''
    #updating Data 
    '''
    u = update(TableCookies).where(TableCookies.c.cookie_name == "chocolate chip")
    u = u.values(quantity=(TableCookies.c.quantity + 36))
    result = connection.execute(u)
    print(result.rowcount)
    
    s = select([TableCookies]).where(TableCookies.c.cookie_name == "chocolate chip")
    resulte = connection.execute(s).first()
    for key in resulte.keys():
        print('{:>20}: {}'.format(key, resulte[key]))
    '''
    # deleting data 
    '''
    u = delete(TableCookies).where(TableCookies.c.cookie_name == "dark chocolate chip")
    result = connection.execute(u)
    print(result.rowcount)

    s = select([TableCookies]).where(TableCookies.c.cookie_name == "dark chocolate chip")
    result = connection.execute(s).fetchall()
    print(len(result))
    '''

 
    
    
if __name__ == "__main__":main()
