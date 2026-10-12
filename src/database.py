from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# プロジェクトのルートディレクトリ
BASE_DIR = Path(__file__).resolve().parent.parent

# SQLiteファイルを保存する data/ ディレクトリ
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# SQLiteファイル
DB_PATH = DATA_DIR / "bookreview.db"
DATABASE_URL = f"sqlite:///{DB_PATH.as_posix()}"

# SQLiteへの接続
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# DB操作に使用するSession
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# SQLAlchemy Modelの基底クラス
Base = declarative_base()
