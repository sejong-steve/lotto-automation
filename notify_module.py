cat > notify_module.py << 'EOF'
# notify_module.py
import os
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))

def send_telegram(msg):
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    bot.send_message(chat_id=chat_id, text=msg)

if __name__ == "__main__":
    send_telegram("테스트 메시지")
EOF