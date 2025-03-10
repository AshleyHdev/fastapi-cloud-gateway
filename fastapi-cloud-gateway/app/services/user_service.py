from sqlalchemy.orm import Session
from app.models import User  # 假設你已經有 User 模型
from app.schemas import UserCreate, UserUpdate  # 假設你有這些 schema
from sqlalchemy.exc import SQLAlchemyError

# 取得所有使用者
def get_users(db: Session):
    try:
        return db.query(User).all()
    except SQLAlchemyError as e:
        # 這裡可以做一些錯誤處理，記錄錯誤或拋出異常
        print(f"Database error: {str(e)}")
        return []

# 根據 ID 取得使用者
def get_user(db: Session, user_id: int):
    try:
        return db.query(User).filter(User.id == user_id).first()
    except SQLAlchemyError as e:
        print(f"Database error: {str(e)}")
        return None

# 創建使用者
def create_user(db: Session, user: UserCreate):
    try:
        db_user = User(name=user.name, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except SQLAlchemyError as e:
        print(f"Database error: {str(e)}")
        db.rollback()
        return None

# 更新使用者
def update_user(db: Session, user_id: int, user: UserUpdate):
    try:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            db_user.name = user.name
            db_user.email = user.email
            db.commit()
            db.refresh(db_user)
            return db_user
        return None
    except SQLAlchemyError as e:
        print(f"Database error: {str(e)}")
        db.rollback()
        return None

# 刪除使用者
def delete_user(db: Session, user_id: int):
    try:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            db.delete(db_user)
            db.commit()
            return db_user
        return None
    except SQLAlchemyError as e:
        print(f"Database error: {str(e)}")
        db.rollback()
        return None
