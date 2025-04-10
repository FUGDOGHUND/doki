# 🚀 Doki - FastAPI Project
## 📋 Требования
- Python 3.7+
- pip
- venv (для виртуального окружения)
## ⚙️ Установка и запуск
### 1. Клонирование репозитория
```bash
git clone https://github.com/FUGDOGHUND/doki.git
cd doki
```
### 2. Настройка виртуального окружения
```bash
# Установка venv (если не установлен)
sudo apt install python3-venv

# Создание виртуального окружения
python3 -m venv venv

# Активация окружения
source venv/bin/activate  # Linux/macOS
# Для Windows: venv\Scripts\activate
```
### 3. Установка зависимостей
```bash
pip install fastapi uvicorn
```
### 4. Запуск сервера
```bash
uvicorn main:app --reload
```
Сервер будет доступен по адресу:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)
### 5. Документация API
- **Swagger UI**: [/docs](http://127.0.0.1:8000/docs)  
- **ReDoc**: [/redoc](http://127.0.0.1:8000/redoc)
### 6. Деактивация окружения
```bash
deactivate
```
```
pip install fastapi uvicorn
```
```
uvicorn main:app --reload
```
```
http://127.0.0.1:8000/docs  # Документация FastAPI/Swagger
http://127.0.0.1:8000/redoc  # Альтернативная документация
```
