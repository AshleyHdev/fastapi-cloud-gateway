FastAPI Cloud Gateway

📌 專案簡介

🚀 FastAPI Cloud Gateway 是一個基於 FastAPI 的雲端 API 網關，負責處理用戶請求並與 Google Cloud SQL 進行資料交換。這個專案展示了如何使用 FastAPI、SQLAlchemy、PostgreSQL 來構建高效能 API，並確保應用程式具備良好的擴展性與安全性。

⸻

📌 FastAPI Cloud Gateway - 作品介紹

🔹 作品背景

在現代 Web 應用中，API Gateway 扮演著至關重要的角色，它不僅能統一管理 API 請求，還能提供身份驗證、流量管理、錯誤處理等功能。為了讓後端架構更加靈活並提升 API 效能，我開發了 FastAPI Cloud Gateway，這是一個基於 FastAPI 的高效能 API 網關，並整合了 Google Cloud SQL 作為資料庫後端。

⸻

🔹 作品目標

本作品旨在提供：
 1. 一個靈活的 API Gateway 架構，適用於微服務或單體應用後端。
 2. 快速且可擴展的 API 服務，透過 FastAPI 和 Uvicorn 來實現非同步請求處理，提高效能。
 3. 與 Google Cloud SQL 整合，讓資料儲存更穩定，並支援雲端環境的部署。

⸻

🔹 核心功能

✅ API Gateway 設計：統一管理 API 入口，負責轉發請求並處理錯誤。
✅ 用戶管理 API：提供 CRUD 操作，讓前端或其他服務能夠存取用戶資訊。
✅ 資料庫整合：使用 PostgreSQL + SQLAlchemy 來確保資料的一致性與可擴展性。
✅ 環境變數管理：支援 .env 檔案與 Google Cloud 憑證，確保應用程式的安全性與可移植性。
✅ Swagger UI 測試：內建 API 文件，可透過 http://127.0.0.1:8000/docs 直接進行 API 測試。

⸻

🔹 技術特色

🚀 FastAPI + Uvicorn：使用 Python 3.9+ 的高效能 Web 框架，提供比傳統 Flask 更快的非同步處理能力。
💾 PostgreSQL + SQLAlchemy：採用關聯式資料庫技術，確保資料的一致性與安全性。
☁ Google Cloud SQL 整合：支援雲端部署，適用於大型系統架構。
🔐 環境變數與 .gitignore：確保 API 金鑰與敏感資料不會洩漏，提高安全性。

⸻

🔹 作品應用場景

🔹 企業內部後端 API Gateway：適合處理多個微服務 API，統一管理請求。
🔹 SaaS 服務 API 平台：可以作為 SaaS 應用的後端 API，支援多租戶架構。
🔹 個人專案 / Side Project：適合作為後端學習 FastAPI 和雲端技術的基礎範例。

⸻

🔹 作品價值

💡 這個專案不僅是一個技術實作，更是我在 後端開發、雲端技術與 API 設計 上的深入探索。透過這個作品，我學習了：
 • 如何設計高效能 API
 • 如何將資料庫與 API 完美整合
 • 如何確保 API 安全性
 • 如何使用 FastAPI 快速開發後端服務

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

📄 **專案目錄結構**
```bash
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
