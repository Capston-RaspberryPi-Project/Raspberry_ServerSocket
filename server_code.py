import switchControl as switch
import socket
import time

host = '220.69.172.128' # 호스트 ip를 적어주세요
port = 8080            # 포트번호를 임의로 설정해주세요
result = ''

try :
    server_sock = socket.socket(socket.AF_INET)
    server_sock.bind((host, port))
    server_sock.listen(1)
    out_data = int(10)
except socket.error as err:
    print('error')

print("기다리는 중..")

try:
    switch.initSwitchControl()

    while True:
        client_sock, addr = server_sock.accept()

        if client_sock:
            print('Connect with' + addr[0] + ":" + str(addr[1]))
            buf = client_sock.recv(512)
            print(type(buf))

            # decode bytes to string
            result = buf.decode('utf-8')
            print(result)
            
            # 순서대로 ON
            # switch.individualSwitchControl()

            # 실시간 스위치 제어
            switch.realtimeSwitchControl(result)

            # 한번에 모든 전원 제어 (안드로이드 버튼 추가 개발 필요)
            # switch.allSwitchOn()
            # switch.time.sleep(2)
            # switch.allSwitchOff()

except KeyboardInterrupt:
    switch.GPIO.cleanup()
    client_sock.close()
    server_sock.close()
    pass

client_sock.close()
server_sock.close()



