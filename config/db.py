from sqlalchemy import create_engine, MetaData
from config.key import username,password



# engine=create_engine("mysql+pymysql://root:Abhi@123@localhost:3306/my_db")

engine = create_engine(f"mysql+pymysql://{username}:{password}@localhost:3306/books")
meta=MetaData()
conn=engine.connect()

# engine.execute("CREATE DATABASE dbname") #create db
# engine.execute("USE dbname")