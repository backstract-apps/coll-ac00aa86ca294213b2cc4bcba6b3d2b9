from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(id: int, name: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, id, name)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/todos/')
async def get_todos(db: Session = Depends(get_db)):
    try:
        return await service.get_todos(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/todos/id')
async def get_todos_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_todos_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/todos/')
async def post_todos(raw_data: schemas.PostTodos, db: Session = Depends(get_db)):
    try:
        return await service.post_todos(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/todos/id/')
async def put_todos_id(id: int, description: Annotated[str, Query(max_length=100)], user_id: int, completed: int, db: Session = Depends(get_db)):
    try:
        return await service.put_todos_id(db, id, description, user_id, completed)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/todos/id')
async def delete_todos_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_todos_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

