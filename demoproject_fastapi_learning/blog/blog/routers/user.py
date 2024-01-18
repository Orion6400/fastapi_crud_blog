from fastapi import APIRouter,Depends,status,HTTPException
import schemas,models,database
from sqlalchemy.orm import Session
from hashing import Hash
from repository import user
from oaut2 import get_current_user

router = APIRouter(prefix="/user",tags=["Users"])
get_db = database.get_db

@router.post('/',response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db),get_current_user:schemas.User = Depends(get_current_user)):
    return (user.create(request,db))
    # hash_pass = Hash.bcrypt(request.password)
    # new_user = models.User(name=request.name, email=request.email, password=hash_pass)
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user


@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db),get_current_user:schemas.User = Depends(get_current_user)):
    return (user.get_user(id,db))
    # user = db.query(models.User).filter(models.User.id == id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with this id:{id} in not found")
    # return user