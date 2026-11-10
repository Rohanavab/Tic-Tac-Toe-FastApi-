from sqlmodel import SQLModel,Session,create_engine
from config import settings

 
# sql engine
engine = create_engine(settings.database_url,connect_args={"check_same_thread":False})

# create all sqlmodel database tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# sessions here
def get_session():
    with Session(engine) as session:
        yield session
