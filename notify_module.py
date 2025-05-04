# notify_module.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN   = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram(msg):
    print("▶ [DEBUG] TOKEN   =", TOKEN)
    print("▶ [DEBUG] CHAT_ID =", CHAT_ID)

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    try:
        resp = requests.post(url, data=payload, timeout=10)
        print(f"▶ [DEBUG] HTTP {resp.status_code} — {resp.text}")
    except Exception as e:
        print("▶ [ERROR] send_telegram exception:", e)

if __name__ == "__main__":
    send_telegram("✅ 테스트 메시지")