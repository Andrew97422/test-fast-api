from pydantic.dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

@dataclass
class User:
    id: int
    username: str
    first_name: str
    last_name: str
    age: int
    created_at: datetime

class UpdateUserSchema(BaseModel):
    id: Optional[int]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]
    create_at: Optional[str]

@dataclass
class Userlist:
    count: int
    users: List[User]