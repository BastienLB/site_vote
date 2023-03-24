from sqlalchemy.orm import Session
from sqlalchemy import select

from . import models, schemas


def register_image(db: Session, image: schemas.ImageCreate):
    db_image = models.Image(filename=image.filename)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image


def register_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(ip=user.ip)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_images(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Image).offset(skip).all()


def register_user_vote(db: Session, user_id: int, image_id: int):
    user = db.query(models.User).get(user_id)
    user.image_chosen_by_user = image_id
    db.commit()
    db.refresh(user)
    return user


def check_if_user_exists(db: Session, ip: str):
    result = db.query(models.User.id).where(models.User.ip.in_([ip])).all()
    return True if len(result) > 0 else False

