from fastapi import APIRouter,HTTPException
from sqlmodel import select
from app.dependencies import sessionDep
from app.models import User,UserCreate,UserPublic
from app.security import hashpassword

router =APIRouter(tags="auth",prefix="/auth")

@router.post("/register",response_model=UserPublic,status_code=201)
def register(usercreate:UserCreate,session:sessionDep):
    taken=session.exec(select(User).where(usercreate.username==User.username)).first()
    if taken:
        raise HTTPException(status_code=409,detail="Username already taken")
    user=User(usercreate.username.lower(),hashpassword(usercreate.password))
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

