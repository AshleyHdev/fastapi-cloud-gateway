FastAPI Cloud Gateway

📌 專案簡介

🚀 FastAPI Cloud Gateway 是一個基於 FastAPI 的雲端 API 網關，負責處理用戶請求並與 Google Cloud SQL 進行資料交換。這個專案展示了如何使用 FastAPI、SQLAlchemy、PostgreSQL 來構建高效能 API，並確保應用程式具備良好的擴展性與安全性。

⸻

🔹 主要功能

✅ API Gateway：負責統一處理 API 請求，並將流量導向後端服務。
✅ 資料庫整合：使用 Google Cloud SQL 作為 PostgreSQL 資料庫，並透過 SQLAlchemy 進行 ORM 操作。
✅ 用戶管理 API：
 • GET /users：獲取所有用戶資料
 • POST /users：新增用戶
 • PUT /users/{id}：更新用戶資料
 • DELETE /users/{id}：刪除用戶
✅ 高效能架構：透過 FastAPI + Uvicorn 提供非同步請求處理，確保快速響應。

⸻

🛠 技術棧

🔹 FastAPI - 高效能的 Python Web 框架
🔹 SQLAlchemy - ORM，與 PostgreSQL 資料庫交互
🔹 PostgreSQL - 可靠的關聯式資料庫
🔹 Google Cloud SQL - Google 提供的雲端資料庫
🔹 Docker（可選） - 容器化 API 以利於部署
🔹 Uvicorn - 非同步 ASGI 伺服器，提升 API 響應速度

⸻

⚙️ 安裝與運行

1️⃣ 克隆專案

git clone https://github.com/AshleyHdev/fastapi-cloud-gateway.git
cd fastapi-cloud-gateway

2️⃣ 創建並啟動虛擬環境

python3 -m venv venv
source venv/bin/activate  # Windows 用戶請使用 venv\Scripts\activate

3️⃣ 安裝依賴

pip install -r requirements.txt

4️⃣ 設置 Google Cloud SQL 認證

請確保你的 Google Cloud SQL 憑證 .json 檔案已經存放在 config/ 資料夾內，然後設定環境變數：

export GOOGLE_APPLICATION_CREDENTIALS="config/your-google-cloud-key.json"

5️⃣ 啟動 API

uvicorn app.main:app --reload

API 會運行在 http://127.0.0.1:8000 🎉

⸻

🛠 API 使用方式

🚀 當 API 啟動後，妳可以使用 Swagger UI 測試 API！

打開瀏覽器，進入：

http://127.0.0.1:8000/docs

這裡妳可以直接測試 GET /users、POST /users 等 API！

⸻

📂 專案結構

fastapi-cloud-gateway/
│── app/
│   ├── main.py           # FastAPI 入口點
│   ├── config/settings.py # 環境設定
│   ├── models/user.py     # 資料庫模型
│   ├── routes/user.py     # API 路由
│   ├── services/database.py  # 資料庫連線
│   ├── services/user_service.py # 用戶管理邏輯
│── requirements.txt       # 依賴套件列表
│── .gitignore             # 忽略不必要的檔案
│── README.md              # 本文件



⸻

🌟 其他

✔ 作者：AshleyH.dev
✔ 聯絡方式：GitHub Issues
