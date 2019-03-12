from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String,
                        DateTime, ForeignKey, create_engine, insert)
from A5CompleteCode import cookies

metadata = MetaData()
engine = create_engine('postgresql+psycopg2://@localhost:' '5432/mydb')
connection = engine.connect()
print(engine.table_names())
metadata =MetaData()

users = Table('users', metadata, autoload=True, autoload_with=engine)
print(repr(users),"\n") 
print("\n")


ins = cookies.insert().values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
)
print(str(ins))
print("\n")
print(ins.compile().params)
result = connection.execute(ins)
print(result.inserted_primary_key)