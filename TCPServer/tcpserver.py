# TCP 에코 서버
# 1명의 클라이언트만 서비스한다

from socket import *


# 서버를 실행하는 컴퓨터의 ip 주소를 입력하면됨
# ip 주소는 cmd에서 ipconfig라고 치면 나옴

PORT = 2500 #서버의 포트 번호
BUFSIZE = 512 
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
    c_sock.send(data)
    

c_sock.close()
