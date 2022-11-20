import random
from datetime import datetime
import schedule
import time


watta_db = []

def job():
    num = random.randrange(1000, 10000) # 1부터 10 사이의 난수 생성
    now = datetime.now() # 날짜 시간 출력
    data = {'time':f'{now.day}d {now.hour}h {now.minute}m {now.second}s', 'num':num}
    # print(num, now)
    watta_db.append(data)


schedule.every(1).seconds.do(job) # 10초마다 job 실행



while True:
    schedule.run_pending()
    time.sleep(1)

while True:
    schedule.run_pending()
    time.sleep(1)
    print(len(watta_db))
    if len(watta_db) == 3:
        print(watta_db[-1])
        print(watta_db) #마지막 값이 현재 시간 값이겠지?
        break