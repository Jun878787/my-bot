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

## 部署到雲端
本專案可以部署到各種雲服務商，包括：
- Google Cloud Platform
- DigitalOcean
- AWS
- Heroku

詳細部署指南請參考 [部署文檔](docs/deployment.md)。

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
