from sqlalchemy.sql import select, func
from Ch1A import *
from sqlalchemy import create_engine

def main():
    engine = create_engine('sqlite:///cookies1.db')
    connection = engine.connect()
    
    customer_list = [
    {
        'username': 'cookiemon',
        'email_address': 'mon@cookie.com',
        'phone': '111-111-1111',
        'password': 'password'
    },
    {
        'username': 'cakeeater',
        'email_address': 'cakeeater@cake.com',
        'phone': '222-222-2222',
        'password': 'password'
    },
    {
        'username': 'pieguy',
        'email_address': 'guy@pie.com',
        'phone': '333-333-3333',
        'password': 'password'
    }
    ]
    ins = TableUsers.insert()
    result = connection.execute(ins, customer_list)
    print(result.inserted_primary_key)
    

if __name__ == "__main__":main()
