from sqlalchemy import (insert, create_engine)
from Ch1A import TableCookies


def main():
    engine = create_engine('sqlite:///cookies1.db')
    connection = engine.connect()
    ins = TableCookies.insert()
    
    inventory_list = [ 
    {
        'cookie_name': 'peanut butter',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
        'cookie_sku': 'PB01',
        'quantity': '24',
        'unit_cost': '0.25'
    },
    {
        'cookie_name': 'oatmeal raisin',
        'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
        'cookie_sku': 'EWW01',
        'quantity': '100',
        'unit_cost': '1.00'
    }
    ]


    
    result = connection.execute(ins, inventory_list)
    print(str(ins))
    a = ins.compile().params
    print(a)
    


if __name__ == "__main__":main()
