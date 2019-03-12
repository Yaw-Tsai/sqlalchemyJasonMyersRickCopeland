from A3InitializeMetaData import metadata_initialized
from sqlalchemy import Index, Table, Column, Integer, Numeric, String, ForeignKey, DateTime, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from datetime import datetime


def instantiating_table_objects():
    cookies_table = Table('cookies', initialize_meta_data().metadata_initialized,
                          Column('cookie_id', Integer(), increment=1, primary_key=True),
                          Column('cookie_name', String(50), index=True),
                          Column('cookie_reciepe_url', String(255)),
                          Column('cookie_sku', String(55)),
                          Column('quantity', Integer()),
                          Column('unit_cost', Numeric(12, 2))
                          
                          )
    users_table = Table('users', initialize_meta_data().metadatainitialized,
                        Column('user_id', Integer(), primary_key=True),
                        Column('username', String(15), nullable=False, unique=True),
                        Column('email_address', String(255), nullable=False),
                        Column('phone', String(20), nullable=False),
                        Column('password', String(25), nullable=False),
                        Column('created_on', DateTime(), default=datetime.now),
                        Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now),
                        #PrimaryKeyConstraint('user_id', name='user_pk')
                        )
    orders = Table('orders', metadata,
    Column('order_id', Integer(), primary_key=True),
    Column('user_id', ForeignKey('users.user_id'))
    )

    line_items = Table('line_items', metadata,
    Column('line_items_id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.order_id')),
    Column('cookie_id', ForeignKey('cookies.cookie_id')),
    Column('quantity', Integer()),
    Column('extended_cost', Numeric(12, 2))
    )
