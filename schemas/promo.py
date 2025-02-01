import re
from pydantic import BaseModel,field_validator

class PromoActivation(BaseModel):
    uid: str  # Должен быть ровно 20 цифр
    code: str  # Должен быть 10 символов: только большие буквы и цифры
    
    @field_validator('uid')
    def check_uid_20_digits(cls, value):
        if not re.fullmatch(r'^\d{20}$', value): 
            raise ValueError('UID должен содержать ровно 20 цифр')
        return value

    @field_validator('code')
    def check_code_10_alphanumeric_uppercase(cls, value):
        if not re.fullmatch(r'^[A-Z0-9]{10}$', value): 
            raise ValueError('Code должен содержать ровно 10 символов: только большие буквы и цифры')
        return value