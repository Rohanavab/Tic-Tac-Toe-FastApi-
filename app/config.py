from pydantic_settings import BaseSettings
import os

os.makedirs("data",exist_ok=True)
class Settings(BaseSettings):
    secret_key:str="devonlychangenme"
    token_minutes:int=720
    database_url:str="sqlite:///./data/tictac.db"

settings=Settings()

