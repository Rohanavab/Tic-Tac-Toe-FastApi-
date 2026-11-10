from datetime import datetime,timezone
from pydantic import field_validator
from sqlmodel import SQLModel,Field


def now():
    return datetime.now(timezone.utc)

class User(SQLModel,table=True):
    id:int | None=Field(default=None,primary_key=True)
    username:str =Field(unique=True,index=True)
    password:str
    wins:int =0
    losses:int=0
    draws:int=0
    created_at:datetime= Field(default_factory=now)

class UserPublic(SQLModel):
    id:int
    username:str
    wins:int
    losses:int
    draws:int

class UserCreate(SQLModel):
    username:str=Field(min_length=3,max_length=20,pattern="^[A-Za-z0-9_]+$")
    password:str=Field(min_length=8,max_length=64)

    @field_validator("password")
    @classmethod
    def val_pass(cls,value):
        if not any(c.isupper() for c in value):
            raise ValueError("Passwords needs atleast one uppercase letter")
        if not any(c.islower() for c in value):
            raise ValueError("Passwords needs atleast one lower letter")
        if not any(c.isdigit() for c in value):
            raise ValueError("Passwords needs atleast one digit ")
        if not any(not c.isalnum() for c in value):
            raise ValueError("Passwords needs atleast one special character")
        return value


        
