import models, database
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
get_db = database.get_db

def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update(id, request, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog not found with this id:{id}")
    update_data = request.model_dump()
    column_updates = {getattr(models.Blog, key): value for key, value in update_data.items()}
    db.query(models.Blog).filter(models.Blog.id == id).update(column_updates, synchronize_session='fetch')
    db.commit()
    return 'Updated successfully'

def distroy(id,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {"Deleted"}