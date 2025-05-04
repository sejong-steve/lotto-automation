# check_results.py
import json
from fetch_module import fetch_latest_results
from purchase_module import purchase_lotto
from notify_module import send_telegram

# TODO: purchase_module에서 저장된 last_tickets.json 불러와 비교
print("결과 확인 및 알림 함수 호출")