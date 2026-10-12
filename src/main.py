from pathlib import Path

from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

import models
import schemas
from database import Base, SessionLocal, engine


app = FastAPI(
    title="Book Review API",
    version="1.0.0",
)

# Modelの定義をもとにテーブルを作成する
Base.metadata.create_all(bind=engine)


# ------------------------------------------------------------
# DB Session
# ------------------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------------------------------------------------
# API
# ------------------------------------------------------------
@app.get("/")
def root():
    return {
        "message": "Book Review API",
        "docs": "/docs",
        "frontend": "/frontend/index.html",
    }


# ============================================================
# 第3回 TODO
#
# 1. POST /books
#    BookをSQLiteへ登録する
@app.post("/books", response_model=schemas.BookResponse)
def create_book(
    book: schemas.BookCreate,
    db: Session = Depends(get_db),
):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        published_year=book.published_year,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# 2. GET /books
#    SQLiteからBook一覧を取得する
@app.get("/books", response_model=list[schemas.BookResponse])
def get_books(
    db: Session = Depends(get_db),
):
    books = db.query(models.Book).all()
    return books
# ============================================================


# ============================================================
# 第4回 TODO
#
# Book詳細取得、Review登録・取得などを追加する
# ============================================================


# ============================================================
# 第5回 TODO
#
# Book / Reviewの削除、エラー処理、整合性の確認などを追加する
# ============================================================


# ------------------------------------------------------------
# Frontend
# ------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app.mount(
    "/frontend",
    StaticFiles(directory=FRONTEND_DIR, html=True),
    name="frontend",
)