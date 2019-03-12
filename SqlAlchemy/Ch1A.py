from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String, ForeignKey, DateTime, create_engine, Index)

    
metadata = MetaData()
TableCookies = Table('cookies', metadata,
                     Column('cookie_id', Integer(),  primary_key=True),
                     Column('cookie_name', String(50), index=True),
                     Column('cookie_receipe_url', String(255)),
                     Column('cookie_sku', String(55)),
                     Column('quantity', Integer()),
                     Column('unit_cost', Numeric(12, 2))              
                     )
TableUsers = Table('users', metadata,
                   Column('user_id', Integer(), primary_key=True),
                   Column('customer_number', Integer(), autoincrement=True),
                   Column('username', String(15), nullable=False, unique=True),
                   Column('email_address', String(255), nullable=False),
                   Column('phone', String(20), nullable=False),
                   Column('password', String(25), nullable=False),
                   Column('created_on', DateTime(), default=datetime.now()),
                   Column('update_on', DateTime(), default=datetime.now, onupdate=datetime.now),
                   )
TableOrders = Table('orders', metadata,
                     Column('order_id', Integer(), primary_key=True),
                     Column('user_id', ForeignKey('users.user_id'))             
                     )
TableLine_Items = Table('line_items', metadata,
                     Column('line_items_id', Integer(), primary_key=True),
                     Column('order_id', ForeignKey('orders.order_id')),
                     Column('cookie_id', ForeignKey('cookies.cookie_id')),
                     Column('quantity', Integer()),
                     Column('extended_cost', Numeric(12, 2))                     
                     )




