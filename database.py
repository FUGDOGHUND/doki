database.py


from typing import Dict, List

fake_db = {
    "users": [
        {"id": 1, "username": "admin", "hashed_password": "..."},
    ],
    "articles": [
        {"id": 1, "title": "FastAPI", "content": "...", "author_id": 1},
    ],
    "comments": [
        {"id": 1, "text": "Отличная статья!", "article_id": 1, "user_id": 1},
    ],
}
