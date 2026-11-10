from pwdlib import PasswordHash

passhash=PasswordHash.hash()

def hashpassword(password:str)->str:
    return passhash.hash(password)

def password_verify(password:str,hashedpass:str)->bool:
    return passhash.verify(password,hashedpass)

