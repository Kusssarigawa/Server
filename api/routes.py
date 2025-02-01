from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.promo import PromoActivation
from db.crud import activate_promo_code

router = APIRouter()

@router.post("/activate")
async def activate_promo(data: PromoActivation, db: Session = Depends(get_db)):
    result = activate_promo_code(db, data.uid, data.code)
    if not result:
        raise HTTPException(status_code=400, detail="Invalid or used promo code")
    return {"message": "Promo code activated successfully"}

@router.get("/")
async def root():
    return {"message": "Welcome to the Promo Activation API"}