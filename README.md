### 📌 Promo Code Activation API  

**Promo Code Activation API** — это сервис на **FastAPI**, который позволяет активировать промокоды и привязывать их к пользователям в базе данных.  

---  
Пока это очень сырой фунционал который будет дорабатываться)


```
По умолчанию сервер будет доступен по адресу:  
🔗 `http://127.0.0.1:8000`

---  

## 📜 Описание  

- **FastAPI** используется для создания REST API.  
- **SQLAlchemy** работает с базой данных.  
- **CORS Middleware** настраивает доступ для фронтенда.  

### 🛠 Основные модули  

- **`main.py`** — инициализация FastAPI и подключение API-маршрутов.  
- **`models.py`** — описание моделей БД (`PromoCode`, `UserContent`).  
- **`database.py`** — подключение к БД.  
- **`routes.py`** — обработка HTTP-запросов.  
- **`promo_service.py`** — логика активации промокода.  

---  

## 🔥 Пример работы API  

### ✅ Активация промокода  
**Запрос:**  
```http
POST /activate
Content-Type: application/json
```
```json
{
  "uid": "20 цифр",
  "code": "10 символов"
}
```
**Ответ:**  
```json
{
  "success": true
}
```

---  

## 🛠 Технологии  

- Python 3.x  
- FastAPI  
- SQLAlchemy  
- SQLite/PostgreSQL (по выбору)  
- Uvicorn  

👨‍💻 **Автор:** Kusssarigawa 🚀
