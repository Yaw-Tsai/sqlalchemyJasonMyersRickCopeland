from sqlalchemy import create_engine


#def main():

def create_engine_function():

    engine = create_engine('postgresql+psycopg2://@localhost:' '5432/mydb')
    try:
        connection = engine.connect()
        print("connection successful")
    except Exception as e :
        print(e)    

#if __name__ == "__main__":main()
