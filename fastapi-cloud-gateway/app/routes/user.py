from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import user_service  # 引入服務層的函數
from app.database import SessionLocal
from app.schemas import UserCreate, UserUpdate  # 假設你有這些 schema

router = APIRouter(prefix="/users", tags=["Users"])

# 取得資料庫 session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 取得所有使用者
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    users = user_service.get_users(db)
    return users

# 根據 ID 取得單一使用者
@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user(db, user_id)
    if user:
        return user
    return {"message": "User not found"}

# 創建新使用者
@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = user_service.create_user(db, user)
    if new_user:
        return new_user
    return {"message": "Error creating user"}

# 更新使用者
@router.put("/{user_id}")
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = user_service.update_user(db, user_id, user)
    if updated_user:
        return updated_user
    return {"message": "User not found or update failed"}

# 刪除使用者
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = user_service.delete_user(db, user_id)
    if deleted_user:
        return {"message": "User deleted"}
    return {"message": "User not found"}
