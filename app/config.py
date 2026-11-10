from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key:str="devonlychangenme"
    token_minutes:int=720
    database_url:str="sqlite:///./data/tictac.db"

settings=Settings()

