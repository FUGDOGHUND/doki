from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Doki API",
    description="API для блоговой платформы Doki с возможностью публикации статей и комментариев",
    version="0.1.0",
    contact={
        "name": "Doki Support",
        "email": "support@doki.example.com",
    },
    license_info={
        "name": "MIT",
    },
)


@app.get("/", tags=["Root"])
async def root():
    """Корневой endpoint API.
    
    Returns:
        dict: Приветственное сообщение
    """
    return {"message": "Welcome to Doki API"}


@app.get("/doc", tags=["Documentation"])
async def dock():
    """Endpoint с краткой информацией о документации.
    
    Returns:
        dict: Сообщение о документации
    """
    return {"message": "This is the doc endpoint"}


# Временное "хранилище" статей
fake_db = {
    "articles": [
        {"id": 1, "title": "Первая статья", "content": "Пример содержимого"}
    ]
}


class Article(BaseModel):
    """Модель статьи для создания и возврата"""
    title: str
    content: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Заголовок статьи",
                "content": "Текст статьи..."
            }
        }


@app.get("/articles/", response_model=List[dict], tags=["Articles"])
def get_articles():
    """Получить список всех статей.
    
    Returns:
        List[dict]: Список статей с их ID, заголовками и содержимым
    """
    return fake_db["articles"]


@app.post("/articles/", response_model=dict, tags=["Articles"])
def create_article(article: Article):
    """Создать новую статью (без авторизации).
    
    Args:
        article (Article): Данные новой статьи
        
    Returns:
        dict: Созданная статья с присвоенным ID
    """
    new_article = {
        "id": len(fake_db["articles"]) + 1,
        **article.dict()
    }
    fake_db["articles"].append(new_article)
    return new_article
