from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float
from sqlalchemy.orm import relationship

from database import Base


#class User(Base):
 #   __tablename__ = "users"
#
 #   id = Column(Integer, primary_key=True, index=True)
  #  email = Column(String, unique=True, index=True)
   # hashed_password = Column(String)
    #is_active = Column(Boolean, default=True,ForeignKey("users.id"))

    #items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(20), index=True)
    description = Column(String(50), index=True)
    quant = Column(Float)
