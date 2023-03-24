from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True)
    voted_by = relationship("User", back_populates="vote")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, unique=True)
    image_chosen_by_user = Column(Integer, ForeignKey("images.id"))
    vote = relationship("Image", back_populates="voted_by")



