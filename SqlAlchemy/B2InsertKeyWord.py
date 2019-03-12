from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String,
                        DateTime, ForeignKey, create_engine, insert)
from A5CompleteCode import cookies

metadata = MetaData()
engine = create_engine('postgresql+psycopg2://@localhost:' '5432/mydb')
connection = engine.connect()

ins = cookies.insert()
result = connection.execute(
    ins, 
    cookie_name='dark chocolate chip', 
    cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
    cookie_sku='CC02',
    quantity='1',
    unit_cost='0.75'
)
print(result.inserted_primary_key)
