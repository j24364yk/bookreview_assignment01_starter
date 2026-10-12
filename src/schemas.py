"""
FastAPIで使用するPydantic Schemaを定義するファイル。

第3回:
    BookCreate / BookResponse を作成する。

第4回:
    Review用Schemaを追加する。

第5回:
    ratingの入力検証などを追加する。
"""

from pydantic import BaseModel, ConfigDict


# ============================================================
# 第3回 TODO
# BookCreate と BookResponse をここに作成する
class BookCreate(BaseModel):
    title: str
    author: str
    published_year: int


class BookResponse(BookCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
# ============================================================


# ============================================================
# 第4回 TODO
# Review用Schemaをここに追加する
# ============================================================
