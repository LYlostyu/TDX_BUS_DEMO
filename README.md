# TDX Bus ETA (FastAPI + Vue)

Windows-friendly demo that proxies TDX 公車 API with FastAPI and shows ETA per stop via a Vue (Vite) UI.

## 專案結構

```
TDX_BUS_DEMO/
├─ backend/            # FastAPI service
│  ├─ app/main.py
│  ├─ requirements.txt
│  └─ .env.example        # 範例環境變數
└─ frontend/           # Vue 3 + Vite UI
   ├─ index.html
   ├─ src/
   └─ .env.example        # 範例環境變數
```

## 安裝需求
- Python 3.10+（建議使用 venv）
- Node.js 18+ / npm 8+

## Backend (FastAPI)

### 環境設置

先回到 repo 資料夾根目錄

**Windows CMD**:
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

**Windows PowerShell**:
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

**Unix shell (Mac & Linux)**:
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### 調整 .env 參數

- `.env` (位於`backend/.env`) 中填入 `TDX_APP_ID`、`TDX_APP_KEY`
- 調整 `VITE_API_BASE` 如需要

### 啟動程式
```bash
python app/main.py
```

### 主要 API
- `GET /api/routes/{route}/eta?city=Taipei` — 直通 `/v2/Bus/EstimatedTimeOfArrival/City/{City}/{RouteName}`
- `GET /api/routes/{route}/stops?city=Taipei` — 直通 `/v2/Bus/StopOfRoute/City/{City}/{RouteName}`
- `GET /api/routes/{route}/stop-etas?city=Taipei` — 後端合併站點順序與 ETA，前端使用

## Frontend（Vite + Vue）

### 環境設置

先回到 repo 資料夾根目錄

**Windows CMD & PowerShell**:
```cmd
cd frontend
copy .env.example .env
npm install
```

**Unix shell (Mac & Linux)**:
```bash
cd frontend
cp .env.example .env
npm install
```

### 啟動程式
```bash
npm run dev -- --host
```


預設會呼叫 `http://localhost:8000` 作為 API。

## 啟動 Slidev（投影片簡報）
```powershell
cd slidev
npm install
npx slidev
```
預設會在 `http://localhost:3030` 開啟投影片展示。

Slidev 是一個基於 Markdown 的投影片框架，簡報內容在 `slides.md` 中維護。

## 使用方式
1. 啟動 backend 與 frontend
2. 打開瀏覽器 `http://localhost:5173`
3. 輸入路線號碼（如 307），選擇城市（Taipei / NewTaipei 等），點擊「查詢」
4. 介面會顯示去程/回程分頁與各站預估到站時間

## 備註
- TDX City 參數請依官方代碼，常見：`Taipei`, `NewTaipei`, `Taoyuan`, `Taichung`, `Tainan`, `Kaohsiung`
- 若要修改 CORS，調整 `FRONTEND_ORIGIN`（backend `.env`）
- 如需部署，請改用正式的 Node / Uvicorn 啟動參數並處理憑證/Token 續期
123