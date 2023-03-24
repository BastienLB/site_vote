import os

from fastapi import FastAPI, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

# Database
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from database import operations, models, schemas
from database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup_event(db: Session = get_db()):
    # db: Session = Depends(get_db)
    with Session(engine) as session:
        if len(operations.get_images(session)) == 0:
            path = "static"
            obj = os.scandir(path)
            for entry in obj:
                if entry.is_file() and not entry.name.startswith('.'):
                    image = schemas.ImageCreate(filename=entry.name)
                    operations.register_image(session, image)
            obj.close()


@app.get("/")
async def root(request: Request, db: Session = Depends(get_db)):
    domain = os.getenv("DOMAIN") if os.getenv("DOMAIN") is not None else "127.0.0.1:8000"
    url = f"http://{domain}/vote"
    images = operations.get_images(db)
    users = db.query(models.User).all()

    for user in users:
        print(user.ip)

    for image in images:
        print(f"{image.filename} : {len(image.voted_by)}")

    return templates.TemplateResponse("index.html", {"request": request, "images": images, "url": url})


@app.get("/vote/{image_id}")
async def add_user_vote(image_id, request: Request, db: Session = Depends(get_db)):
    if not operations.check_if_user_exists(db, request.client.host):
        user = operations.register_user(db, schemas.UserCreate(ip=request.client.host))
        operations.register_user_vote(db, user.id, image_id)
    response = RedirectResponse(url='/')
    return response


