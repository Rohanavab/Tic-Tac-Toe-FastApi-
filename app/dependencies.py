from typing import Annotated
from sqlmodel import Session
from fastapi import Depends
from database import get_session

sessionDep=Annotated[Session,Depends(get_session)]


