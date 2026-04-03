from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UseResponse(UserBase):
    id: int

    class config:
        from_attributes = True