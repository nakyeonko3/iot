from socket import *
import random
from datetime import datetime
import schedule
import time
import threading



watta_db = [{'time': '18d 23h 20m 11s', 'num': 1217}] #초기값을 넣어둠

def 날짜_난수_생성기():  
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
        # print(len(watta_db))
        # if len(watta_db) == 3:
        #     break


t = threading.Thread(target=날짜_난수_생성기)
t.daemon = True 
t.start()
    
# 서버를 실행하는 컴퓨터의 ip 주소를 입력하면됨
# ip 주소는 cmd에서 ipconfig라고 치면 나옴



PORT = 2500 #서버의 포트 번호
BUFSIZE = 1024 
IP = '' #서버의 IP주소

sock = socket(AF_INET, SOCK_STREAM)
sock.bind((IP, PORT)) #자신의 주소 사용
sock.listen(1) #최대 대기 틀라이언트 수
print("Waiting for clients...")

#클라이언트의 연결 요청을 받는다
c_sock, (r_host, r_port) = sock.accept()
print('connected by', r_host, r_port)


while True:
    #상대방 메시지 수신
    data = c_sock.recv(BUFSIZE)
    if not data: #연결이 종료되었으면
        break
    print("Received message: ", data.decode("utf-8"))


    #수신 메시지를 다시 전송

    if (data.decode("utf-8") == "on"):
        c_sock.send("plug on".encode("utf-8"))
        
    elif(data.decode("utf-8") == "off"):
        c_sock.send("plug off".encode("utf-8"))
        
    elif(data.decode("utf-8") == "w"):
        currentdata = watta_db[-1]
        c_sock.send(f'{ currentdata }'.encode("utf-8"))
    else:
        c_sock.send('error'.encode("utf-8"))






c_sock.close()