import models, database
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from hashing import Hash
get_db = database.get_db

def create(request,db):
    hash_pass = Hash.bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hash_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id,db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with this id:{id} in not found")
    return user