from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    id: Any
    name: str


class ReadUsers(BaseModel):
    id: Any
    name: str
    class Config:
        from_attributes = True


class Todos(BaseModel):
    id: Any
    description: str
    user_id: int
    completed: int


class ReadTodos(BaseModel):
    id: Any
    description: str
    user_id: int
    completed: int
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostTodos(BaseModel):
    id: int = Field(...)
    description: str = Field(..., max_length=100)
    user_id: int = Field(...)
    completed: int = Field(...)

    class Config:
        from_attributes = True

