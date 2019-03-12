from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Ch6A1ORMIntro import Cookie

def main():
    
    engine = create_engine('sqlite:///cookie.db', echo=True)
    Session = sessionmaker(bind=engine) 
    session = Session() 
    cc_cookie = Cookie(cookie_name='chocolate chip', 
                   cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
                   cookie_sku='CC01',
                   quantity=12,
                   unit_cost=0.50)
    session.add(cc_cookie) 
    session.commit() 
    #print (cc_cookie.cookie_id)
    session.close_all()

if __name__ == "__main__":main()
