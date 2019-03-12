from sqlalchemy import (select, create_engine)
def main():
    engine = create_engine('sqlite:///cookies1.db', echo=True)
    connection = engine.connect()
    s = select([cookies])
    rp = connection.execute(s)
    results = rp.fetchall()



if __name__ == "__main__":main()
