import random
import os
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

def purchase_lotto(amount: int = 5000):
    """
    amount 원어치 Quick-Pick(자동번호) 로또 구매 후,
    생성된 티켓 번호 리스트를 반환합니다.
    """
    tickets = []

    # 한 장당 1000원(6개 번호)이니, amount//1000 장 생성
    num_tickets = amount // 1000
    for _ in range(num_tickets):
        ticket = sorted(random.sample(range(1, 46), 6))
        tickets.append(ticket)

    # **여기서 생성된 번호를 출력**
    print("🔢 Generated tickets:", tickets)

    # (실제 Selenium 구매 로직은 생략)
    # ...
    return tickets

if __name__ == "__main__":
    purchase_lotto(5000)
