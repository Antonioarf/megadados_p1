from sqlalchemy.orm import Session

import models, schemas



def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item_id(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_item_title(db: Session, title: str):
    return db.query(models.Item).filter(models.Item.title == title).first()


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
#crud.mod_item(db, item_id=item_id,item = item
def mod_item(db: Session, item: schemas.Item):
    db_item = db.query(models.Item).filter(models.Item.id == item.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    item_data = item.dict(exclude_unset=True)
    for key, value in item_data.items():
            setattr(db_item, key, value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    
    return db_item

def del_item(db: Session, item_id: int):
    db_item =db.query(models.Item).filter(models.Item.id == item_id).first()
    db.delete(db_item)
    db.commit()
    #db.refresh(db_item)
    return db_item 
