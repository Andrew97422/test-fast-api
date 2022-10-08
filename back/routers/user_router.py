from fastapi import APIRouter, HTTPException, Response
from datetime import datetime

from routers.schemas import User, Userlist, UpdateUserSchema

users=[
    User(id=1, username='dhuasod', first_name='dlawd', last_name='dhwu', age=89, created_at=datetime.now()),
    User(id=2, username='efefod', first_name='efgawd', last_name='wefwefu', age=23, created_at=datetime.now()),
    User(id=3, username='dsefed', first_name='dwefwefd', last_name='dhwwefwefu', age=12, created_at=datetime.now()),
    User(id=4, username='dhuefefea', first_name='dwef', last_name='dwwwwwwwwwwwwhwu', age=32, created_at=datetime.now()),
    User(id=5, username='dhuawdwefod', first_name='dwwefwfwfwfd', last_name='dhweeeeeu', age=421, created_at=datetime.now())
]

user_router = APIRouter(prefix='/users', tags=['Пользователи'])

@user_router.get('/', name = 'Все пользователи', response_model = Userlist)
def get_all_users():
    return Userlist(count=len(users), users=users)

@user_router.post('/', name = 'Добавить пользователя', response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@user_router.get('/{user_id}', name='Получить пользователя', response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail='User not found')

@user_router.delete('/{user_id}', name='Удалить поьзователя', response_class=Response)
def delete_user(user_id : int):
    for i, user in enumerate(tuple(users)):
        if user.id == user_id:
            del users[i]
            break
    return Response(status_code=204)

@user_router.put('/{user_id}', name='Обновить данные пользователя', response_model=User)
def update_user(user_id: int, new_user_data: UpdateUserSchema):
    for i in range(len(users)):
        if users[i].id == user_id:
            data = new_user_data.dict()
            for key in data:
                if data[key] is not None:
                    setattr(users[i], key, data[key])
            return users[i]
    raise HTTPException(status_code=404, detail="User not found")
