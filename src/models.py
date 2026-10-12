"""
SQLAlchemy Modelを定義するファイル。

第3回:
    Book Modelを作成する。

第4回:
    Review Model、外部キー、1対多の関係を追加する。

第5回:
    制約・cascade deleteなどを確認する。
"""

from sqlalchemy import Column, Integer, String

from database import Base


# ============================================================
# 第3回 TODO
# Book Modelをここに作成する
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_year = Column(Integer, nullable=False)
# ============================================================


# ============================================================
# 第4回 TODO
# Review Modelをここに追加する
# ============================================================
