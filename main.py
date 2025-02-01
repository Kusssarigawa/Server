from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from db.database import init_db

app = FastAPI(title="Promo Code Activation API")

# Настройка CORS (если фронт будет на другом домене)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем маршруты API
app.include_router(router)

# Инициализация БД при запуске
@app.on_event("startup")
def startup():
    init_db()

