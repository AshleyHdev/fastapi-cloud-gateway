from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# 載入 .env 設定
load_dotenv()

# 讀取 DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# 建立資料庫引擎
engine = create_engine(DATABASE_URL, pool_size=5, max_overflow=10)

# 建立 SessionLocal 來處理資料庫操作
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 建立 Base 類別，之後所有 ORM Model 會繼承它
Base = declarative_base()
