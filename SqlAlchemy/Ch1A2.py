from datetime import datetime
from sqlalchemy import (create_engine)
from Ch1A import metadata, TableCookies

def main():

    engine2 = create_engine('sqlite:///cookies1.db', echo=True)
    metadata.create_all(engine2)
    for a in engine2.table_names():
        print(a)
    
if __name__=='__main__': main()

