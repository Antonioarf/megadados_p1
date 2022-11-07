from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
 

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


#GET http://127.0.0.1:8000/itens pedir lista 



#get_items(db: Session, skip: int = 0, limit: int = 100)
@app.get("/itens/", response_model=List[schemas.Item])
def read_itens(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    itens = crud.get_items(db, skip=skip, limit=limit)
    return itens

#create_item(db: Session, item: schemas.ItemCreate):
@app.post("/item/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_user = crud.get_item_title(db, title=item.title)
    if db_user:
        raise HTTPException(status_code=400, detail="Item already registered")
    return crud.create_item(db=db, item=item)

#get_item_id(db: Session, item_id: int)
@app.get("/item/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_item_id(db, item_id=item_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="item not found")
    return db_user

#@mod_item(db: Session, item: schemas.ItemCreate)
@app.put("/item", response_model=schemas.Item)
def mod_item(item: schemas.Item, db: Session = Depends(get_db)):
    db_user = crud.mod_item(db, item = item)
    if db_user is None:
        raise HTTPException(status_code=404, detail="item not found")
    return db_user

#del_item(db: Session, item_id: int)
@app.delete("/item/{item_id}", response_model=schemas.Item)
def del_item(item_id: int, db: Session = Depends(get_db)):
    itens = crud.del_item(db, item_id= item_id)
    return itens
