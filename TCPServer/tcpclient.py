#예외처리를 한 TCP 클라이언트 프로그램

import socket

port = 2500
address = ("localhost", port)
BUFSIZE = 512

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
while True:
    msg = input("Message to send: ")
    try:
        n = s.send(msg.encode()) #메시지 전송
    except:
        print("송신 연결이 종료되었습니다")
        retry = input("계속?(y/n) ")
        if retry == 'n': #연결 종료
            s.close()
            break
        else: #메시지 전송 계속
            continue
    else:
        print("{} bytes sent".format(n)) #전송된 바이트 수
    
    try:
        data = s.recv(BUFSIZE) #receive message from server
        if not data: break
    except:
        print("수신 연결이 종료되었습니다")
        s.close()
        break
    else:
        print("Received message: %s" %data.decode())
