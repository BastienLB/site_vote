from pydantic import BaseModel
from typing import Union


class UserBase(BaseModel):
    ip: str
    image_chosen_by_user: Union[int, None] = None       # ID of the image the user has voted for


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True

#  ======


class ImageBase(BaseModel):
    filename: str


class ImageCreate(ImageBase):
    pass


class Image(ImageBase):
    id: int
    voted_by: list[User] = []

    class Config:
        orm_mode = True


class ImageVotedBy(ImageBase):
    id: int
    voted_by: list[User] = []
