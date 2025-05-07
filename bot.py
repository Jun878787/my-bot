import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters, CallbackContext
from supabase import create_client, Client
import logging

# 讀取環境變數
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# 初始化 Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_URL and SUPABASE_KEY else None

# 設定日誌
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start 指令處理
def start_command(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton('💰TW'), KeyboardButton('💰CN')],
        [KeyboardButton('📊查看本月報表'), KeyboardButton('📚歷史報表')]
    ], resize_keyboard=True)
    update.message.reply_text(
        "歡迎使用乾淨版記帳機器人！請選擇操作：",
        reply_markup=keyboard
    )

# 處理一般訊息
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    user_id = update.message.from_user.id
    if text == '💰TW':
        update.message.reply_text("請輸入台幣金額，格式如: TW+100 或 TW-50")
    elif text == '💰CN':
        update.message.reply_text("請輸入人民幣金額，格式如: CN+100 或 CN-50")
    elif text == '📊查看本月報表':
        # 範例：從 Supabase 讀取資料
        if supabase:
            data = supabase.table('records').select('*').eq('user_id', user_id).execute()
            update.message.reply_text(f"本月報表資料：{data.data}")
        else:
            update.message.reply_text("尚未設定雲端資料庫。")
    elif text == '📚歷史報表':
        buttons = [
            [InlineKeyboardButton("2023-01", callback_data="history_2023-01")],
            [InlineKeyboardButton("2023-02", callback_data="history_2023-02")],
            [InlineKeyboardButton("2023-03", callback_data="history_2023-03")]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        update.message.reply_text("請選擇月份：", reply_markup=reply_markup)
    elif text.startswith('TW+') or text.startswith('TW-'):
        # 範例：寫入 Supabase
        if supabase:
            amount = text[3:]
            supabase.table('records').insert({"user_id": user_id, "currency": "TWD", "amount": amount}).execute()
            update.message.reply_text("已記錄台幣金額。")
        else:
            update.message.reply_text("尚未設定雲端資料庫。")
    elif text.startswith('CN+') or text.startswith('CN-'):
        if supabase:
            amount = text[3:]
            supabase.table('records').insert({"user_id": user_id, "currency": "CNY", "amount": amount}).execute()
            update.message.reply_text("已記錄人民幣金額。")
        else:
            update.message.reply_text("尚未設定雲端資料庫。")
    else:
        update.message.reply_text("請選擇有效的操作或輸入正確格式。")

# 處理按鈕回調
def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    data = query.data
    if data.startswith("history_"):
        month = data.split("_")[1]
        query.edit_message_text(f"顯示 {month} 的報表...（此為範例訊息）")

# 主程式
def main():
    if not TELEGRAM_BOT_TOKEN:
        print("請設定 TELEGRAM_BOT_TOKEN 環境變數")
        return
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dispatcher.add_handler(CallbackQueryHandler(button_callback))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main() 