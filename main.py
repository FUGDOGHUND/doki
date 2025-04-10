
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Временное "хранилище" статей
fake_db = {
    "articles": [
        {"id": 1, "title": "Первая статья", "content": "Пример содержимого"}
    ]
}

# Модель для статьи
class Article(BaseModel):
    title: str
    content: str

# Получить все статьи
@app.get("/articles/", response_model=List[dict])
def get_articles():
    """Получить список всех статей"""
    return fake_db["articles"]

# Создать новую статью
@app.post("/articles/", response_model=dict)
def create_article(article: Article):
    """Создать новую статью (без авторизации)"""
    new_article = {
        "id": len(fake_db["articles"]) + 1,
        **article.dict()
    }
    fake_db["articles"].append(new_article)
    return new_article
