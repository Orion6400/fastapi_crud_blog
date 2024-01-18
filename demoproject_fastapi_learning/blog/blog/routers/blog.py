from fastapi import APIRouter,Depends,status,HTTPException
import schemas,models,database
from typing import List
from sqlalchemy.orm import Session
from repository import blog
from oaut2 import get_current_user

router = APIRouter(prefix="/blog",tags=['Blogs'])
get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db),get_current_user:schemas.User = Depends(get_current_user)):
    return blog.create(request, db)
    


@router.get('/', response_model=List[schemas.ShowBlog])
def all_blog(db: Session = Depends(get_db),get_current_user:schemas.User = Depends(get_current_user)):
    return blog.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db),get_current_user:schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db),get_current_user:schemas.User = Depends(get_current_user)):
    return blog.update(id, request, db)
    


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db),get_current_user:schemas.User = Depends(get_current_user)):
    return blog.distroy(id,db)
    






