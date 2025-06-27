from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def get_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "users_one": users_one,
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    id: int = raw_data.id
    name: str = raw_data.name

    record_to_be_added = {"id": id, "name": name}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "users_inserted_record": users_inserted_record,
    }
    return res


async def put_users_id(db: Session, id: int, name: str):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {"id": id, "name": name}.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )
    res = {
        "users_edited_record": users_edited_record,
    }
    return res


async def delete_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete
    res = {
        "users_deleted": users_deleted,
    }
    return res


async def get_todos(db: Session):

    query = db.query(models.Todos)

    todos_all = query.all()
    todos_all = (
        [new_data.to_dict() for new_data in todos_all] if todos_all else todos_all
    )
    res = {
        "todos_all": todos_all,
    }
    return res


async def get_todos_id(db: Session, id: int):

    query = db.query(models.Todos)
    query = query.filter(and_(models.Todos.id == id))

    todos_one = query.first()

    todos_one = (
        (todos_one.to_dict() if hasattr(todos_one, "to_dict") else vars(todos_one))
        if todos_one
        else todos_one
    )

    res = {
        "todos_one": todos_one,
    }
    return res


async def post_todos(db: Session, raw_data: schemas.PostTodos):
    id: int = raw_data.id
    description: str = raw_data.description
    user_id: int = raw_data.user_id
    completed: int = raw_data.completed

    record_to_be_added = {
        "id": id,
        "user_id": user_id,
        "completed": completed,
        "description": description,
    }
    new_todos = models.Todos(**record_to_be_added)
    db.add(new_todos)
    db.commit()
    db.refresh(new_todos)
    todos_inserted_record = new_todos.to_dict()

    res = {
        "todos_inserted_record": todos_inserted_record,
    }
    return res


async def put_todos_id(
    db: Session, id: int, description: str, user_id: int, completed: int
):

    query = db.query(models.Todos)
    query = query.filter(and_(models.Todos.id == id))
    todos_edited_record = query.first()

    if todos_edited_record:
        for key, value in {
            "id": id,
            "user_id": user_id,
            "completed": completed,
            "description": description,
        }.items():
            setattr(todos_edited_record, key, value)

        db.commit()
        db.refresh(todos_edited_record)

        todos_edited_record = (
            todos_edited_record.to_dict()
            if hasattr(todos_edited_record, "to_dict")
            else vars(todos_edited_record)
        )
    res = {
        "todos_edited_record": todos_edited_record,
    }
    return res


async def delete_todos_id(db: Session, id: int):

    query = db.query(models.Todos)
    query = query.filter(and_(models.Todos.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        todos_deleted = record_to_delete.to_dict()
    else:
        todos_deleted = record_to_delete
    res = {
        "todos_deleted": todos_deleted,
    }
    return res


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )

    new_variable: int = "69696"

    another_variable: int = "41414"

    # "new_variable" will be changed with "another_variable"
    new_variable = another_variable

    res = {
        "users_all": users_all,
    }
    return res
