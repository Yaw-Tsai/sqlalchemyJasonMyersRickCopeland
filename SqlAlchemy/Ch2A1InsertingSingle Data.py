from sqlalchemy import (insert, create_engine, MetaData, Table)
from Ch1A import metadata, TableCookies
from lxml.html.builder import INS


def main():
    engine = create_engine('sqlite:///cookies1.db')
    connection = engine.connect()
    print(engine.table_names())
    metaData = MetaData()
    
    ins = TableCookies.insert().values(
    cookie_name="chocolate chip",
    cookie_receipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50")
    
    result = connection.execute(ins)
    
    print(str(ins))
    a = ins.compile().params
    print(a)
    
    
    ins1 = insert(TableCookies).values(cookie_name="chocolate chip",
    cookie_receipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50")
    result = connection.execute(ins1)
    
    print(result.inserted_primary_key) #this only works if only one record has been inserted into the document. 


if __name__ == "__main__":main()
