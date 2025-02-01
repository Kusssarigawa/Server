from sqlalchemy import Column, String, Integer, Boolean
from .database import Base

class PromoCode(Base):
    __tablename__ = "promo_codes"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    is_used = Column(Boolean, default=False)

class UserContent(Base):
    __tablename__ = "user_content"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String, index=True)
    content = Column(String)
