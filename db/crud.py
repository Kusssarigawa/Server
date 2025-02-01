from sqlalchemy.orm import Session
from .models import PromoCode, UserContent
import logging

def activate_promo_code(db: Session, uid: str, code: str) -> bool:
    logging.info(f"Activating promo code: uid={uid}, code={code}")

    # Simulate checking if the promo code exists and is not used
    promo_code = db.query(PromoCode).filter(PromoCode.code == code, PromoCode.is_used == False).first()
    if not promo_code:
        logging.warning("Promo code not found or already used")
        return False

    # Simulate checking if the user exists
    # user = db.query(UserContent).filter(UserContent.uid == uid).first()
    # if not user:
    #     logging.warning("User not found")
    #     return False
    new_user_content = UserContent(uid=uid)
    db.add(new_user_content)
    # Simulate activating the promo code
    promo_code.is_used = True
    db.commit()
    logging.info("Promo code activated successfully")
    return True