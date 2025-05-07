# Clean Telegram Bot

這是一個最乾淨、可直接部署到免費平台（如 Render、Railway、Heroku）的 Telegram Bot 範例，並支援雲端數據庫（以 Supabase 為例）。

## 快速開始

1. **安裝依賴**
   ```bash
   pip install -r requirements.txt
   ```

2. **設定環境變數**
   - `TELEGRAM_BOT_TOKEN`：7695972838:AAGCnvhFJ-Bd3QujawanExduClUNUf-eG3Y
   - `SUPABASE_URL`：https://avatars.githubusercontent.com/u/208156424?v=4
   - `SUPABASE_KEY`：3619a251-71c3-4812-98c2-9f550f5c6706

3. **啟動機器人**
   ```bash
   python bot.py
   ```

## 雲端資料庫（Supabase）
- 前往 [supabase.com](https://supabase.com) 註冊帳號並建立專案
- 取得 `SUPABASE_URL` 與 `SUPABASE_KEY`
- 可在 `bot.py` 內直接使用 supabase-py 進行資料存取

## 免費平台部署
- Render、Railway、Heroku 皆可直接部署
- 建議將 `requirements.txt`、`bot.py`、`Procfile`（內容：`worker: python bot.py`）一併上傳

## 其他
- 若需改用 Firebase，請安裝 `firebase-admin` 並參考官方文件設定金鑰 