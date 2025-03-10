from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.routes import user
from app.services.database import engine, Base

# ✅ 1. 載入 .env 環境變數
load_dotenv()

# ✅ 2. 自動建立資料庫表格（如果還沒有）
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Cloud Gateway")

# ✅ 3. 設定 CORS，允許跨來源請求（避免前端無法請求 API）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🚨 開發環境允許所有請求，正式環境應設定特定的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 4. 註冊路由
app.include_router(user.router)

# ✅ 5. 健康檢查 API，確保系統正常運作
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Cloud Gateway!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
