from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String,
                        DateTime, ForeignKey, create_engine, insert)
from A5CompleteCode import cookies, users, orders, line_items

metadata = MetaData()
engine = create_engine('postgresql+psycopg2://@localhost:' '5432/mydb')
connection = engine.connect()
print(engine.table_names())
metadata =MetaData()
#inserting order1
ins1 = insert(orders).values(user_id=1, order_id=1)
result = connection.execute(ins1)
ins2 = insert(line_items)
order_items1 = [
    {
        'order_id': 1,
        'cookie_id': 1,
        'quantity': 2,
        'extended_cost': 1.00
    },
    {
        'order_id': 1,
        'cookie_id': 3,
        'quantity': 12,
        'extended_cost': 3.00
    }
]
result = connection.execute(ins2, order_items1)


#inserting Order2
ins3 = insert(orders).values(user_id=2, order_id=2)
result = connection.execute(ins3)
ins4 = insert(line_items)
order_items2 = [
    {
        'order_id': 2,
        'cookie_id': 1,
        'quantity': 24,
        'extended_cost': 12.00
    },
    {
        'order_id': 2,
        'cookie_id': 4,
        'quantity': 6,
        'extended_cost': 6.00
    }
]
result = connection.execute(ins4, order_items2)
