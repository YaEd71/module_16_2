from fastapi import FastAPI, Path
from typing import Annotated, Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user(
    user_id: Annotated[int, Path(
        title="User ID",
        description="Enter User ID",
        ge=1,
        le=100,
        example=1
    )]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def user_info(
    username: Annotated[str, Path(
        title="Username",
        description="Enter username",
        min_length=5,
        max_length=20,
        example="UrbanUser"
    )],
    age: Annotated[int, Path(
        title="Age",
        description="Enter age",
        ge=18,
        le=120,
        example=24
    )]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}