# Telegram 記帳機器人

這是一個功能強大的 Telegram 記帳機器人，專為管理個人和群組財務而設計。

## 主要功能

- 💰 記錄 TWD 和 CNY 貨幣交易
- 📊 生成月度報表
- 📚 查看歷史報表
- 💱 匯率設置與轉換
- 🔧 強大的群組管理功能
- ⚙️ 可自定義的管理員權限
- 🖥️ 網頁管理界面
- ⏰ 定時啟動與關閉功能 (每日 7:00 啟動，凌晨 2:00 關閉)

## 安裝與設置

1. 克隆此儲存庫
```bash
git clone https://github.com/Jun878787/telegram-accounting-bot.git
cd telegram-accounting-bot
```

2. 安裝依賴
```bash
pip install -r requirements.txt
```

3. 配置機器人
   - 從 BotFather 獲取 Telegram API 令牌
   - 創建 `config.py` 文件並配置必要參數

4. 啟動機器人
```bash
python bot.py
```

5. 連接到 GitHub
```bash
git remote add origin https://github.com/Jun878787/telegram-accounting-bot.git
```

## 使用網頁管理界面

本專案包含一個網頁管理界面，可以更方便地管理機器人：

1. 啟動管理伺服器
```bash
python server.py
```

2. 打開瀏覽器訪問
```
http://127.0.0.1:5000
```

3. 在網頁界面中，您可以：
   - 啟動/停止機器人
   - 查看機器人狀態
   - 查看運行日誌

## 使用方法

### 基本指令
- `/start` - 啟動機器人
- `/help` 或 `幫助` - 顯示幫助信息
- `📋指令說明` - 顯示詳細指令列表

### 記帳格式
- `TW+100` - 新增 100 TWD
- `TW-50` - 減少 50 TWD
- `CN+200` - 新增 200 CNY
- `CN-30` - 減少 30 CNY
- `2023/01/01 TW+100` - 指定日期的交易

### 管理員指令
- `💱設置匯率` - 設置當前匯率
- `⚙️群管設定` - 管理群組設置
- `🔒 權限管理` - 管理用戶權限

## 部署到 Railway

本專案已經配置好可以直接部署到 Railway 服務上，並且支援定時啟動和關閉功能。

### 部署步驟

1. 註冊 [Railway 賬號](https://railway.app/)
2. 點擊控制台中的「New Project」，選擇「Deploy from GitHub repo」
3. 授權 Railway 訪問你的 GitHub 賬號並選擇此儲存庫
4. 設置環境變數：
   - `BOT_TOKEN`: 你的 Telegram 機器人 Token
   - 其他需要的環境變數

5. 部署完成後，機器人將自動啟動，並會按照設定的時間表每日運行：
   - 每天早上 7:00 自動啟動
   - 每天凌晨 2:00 自動停止

### 手動控制

即使設定了自動開關機，管理員仍可以使用以下指令手動控制：
- `重啟` - 手動重啟機器人
- `關閉所有進程` - 手動關閉機器人

### 節約資源設置

Railway 的免費方案提供每月 500 小時的運行時間，使用定時開關機功能可以有效節約資源：
- 每天運行 19 小時 (7:00 - 2:00)
- 每月約使用 570 小時 (超出免費額度，建議調整使用時間或升級計劃)

## GitHub Actions 自動部署

此專案還配置了通過 GitHub Actions 自動部署到 Railway 的工作流程。

### 配置步驟

1. 在 GitHub 儲存庫中創建 Secrets：
   - `RAILWAY_TOKEN`: Railway 平台的 API 令牌
   - `SERVICE_ID`: 部署服務的 ID
   - `DEPLOY_KEY`: GitHub 部署 SSH 金鑰 (用於解決 OAuth 認證問題)

2. GitHub Actions 配置文件位於 `.github/workflows/deploy.yml`

### 獲取 Railway 參數

- **RAILWAY_TOKEN**:
   - 前往 [Railway 設定頁面](https://railway.app/account)
   - 生成並複製 API 令牌

- **SERVICE_ID**:
   - 在 Railway 專案頁面，從 URL 中獲取：
   - `https://railway.app/project/[PROJECT_ID]/service/[SERVICE_ID]`

- **DEPLOY_KEY**:
   - 在本機生成 SSH 密鑰對：
     ```bash
     ssh-keygen -t ed25519 -C "railway-deploy-key" -f railway_deploy_key
     ```
   - 在 GitHub 儲存庫中添加部署金鑰：
     - 前往儲存庫 > Settings > Deploy keys
     - 點擊 "Add deploy key"
     - 標題輸入 "Railway Deployment Key"
     - 金鑰欄位粘貼 `railway_deploy_key.pub` 文件內容
     - 勾選 "Allow write access"
     - 點擊 "Add key"
   - 將私鑰內容添加為 GitHub Secret

## 常見問題解決

### GitHub 身份驗證問題

如果在使用 GitHub 進行 OAuth 登錄時遇到問題，可以嘗試以下解決方案：

#### 方法 1: 清除瀏覽器緩存和 Cookie
1. 清除瀏覽器的緩存和 Cookie
2. 使用無痕/隱私瀏覽模式重新登錄
3. 確保允許第三方 Cookie

#### 方法 2: 重新授權 Railway 應用
1. 訪問 GitHub 設定 > [Applications](https://github.com/settings/applications)
2. 在「Authorized OAuth Apps」中尋找 Railway
3. 點擊「Revoke」撤銷授權
4. 重新登錄 Railway，授權應用程序

#### 方法 3: 使用 SSH 金鑰替代 OAuth 認證
1. 生成專用的 SSH 部署金鑰
2. 在 GitHub 設置中添加該公鑰作為部署金鑰
3. 在工作流程中使用 SSH 認證方式而非 HTTPS (已配置在最新版工作流程中)

#### 方法 4: 使用 Railway CLI 設備碼登錄
如果 Web 界面認證持續失敗，可使用 CLI 的設備碼登錄方式：
```bash
npm i -g @railway/cli
railway login --browserless
```
然後按照提示在瀏覽器中輸入顯示的代碼完成認證

#### 方法 5: 直接使用 Railway CLI
完成認證後，可使用以下指令管理專案：
```bash
railway link  # 連接到現有專案
railway up    # 部署應用
railway service restart  # 重啟服務
```

## 貢獻

歡迎提交 Pull Requests 和 Issues。

## 授權

[MIT License](LICENSE)

# 電報機器人定時開關機設定指南

此專案使用 GitHub Actions 實現 Railway 上部署的 Telegram 機器人定時開關機功能，以節省 Railway 免費額度。

## 功能簡介

- 每天早上 07:00 UTC (台灣時間 15:00) 自動啟動機器人
- 每天早上 01:00 UTC (台灣時間 09:00) 自動關閉機器人
- 支援手動觸發開關機操作

## 部署步驟

### 1. 在 Railway 上部署機器人

1. 在 Railway 上註冊賬號並驗證
2. 將此儲存庫連接到 Railway
3. 部署專案並確保機器人正常運作

### 2. 獲取必要參數

部署後需要獲取以下參數:

- **RAILWAY_TOKEN**: Railway 平台的 API 令牌
   - 進入 [Railway 設定頁面](https://railway.app/account)
   - 點擊「Generate Token」創建新令牌
   - 複製生成的令牌

- **SERVICE_ID**: 部署服務的 ID
   - 在 Railway 專案頁面開啟要控制的服務
   - 從網址中獲取 SERVICE_ID，格式為: `https://railway.app/project/[PROJECT_ID]/service/[SERVICE_ID]`

### 3. 配置 GitHub 儲存庫

1. 在 GitHub 儲存庫中創建 Secrets
   - 前往儲存庫頁面 -> Settings -> Secrets and variables -> Actions
   - 添加 `RAILWAY_TOKEN` 和 `SERVICE_ID` 兩個 secrets

2. 工作流程文件已設置好，位於 `.github/workflows/scheduler.yml`

### 4. 手動觸發

可通過以下方式手動觸發:
- 前往儲存庫的 "Actions" 標籤
- 選擇 "Railway 定時開關機" 工作流程
- 點擊 "Run workflow" 按鈕

## 排錯指南

如果自動開關機功能失效，請檢查:

1. GitHub Secrets 是否正確設置
2. Railway 令牌是否有效
3. 查看 GitHub Actions 的執行日誌

## 注意事項

- Railway 免費方案提供每月 500 小時運行時間
- 每天運行 8 小時的設置可以讓您的機器人在一個月中運行約 240 小時
- 請根據自己的需求調整開關機時間
