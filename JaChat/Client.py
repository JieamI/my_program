import socket
import threading
import time
import sys
import os

class ClientUI:
       
    def Recmsg(self):
        self.flag = 0
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(("127.0.0.1",8888))
        except:
           sys.exit()
        print("连接成功\n")
        self.flag = 1
        while True:
            self.data = self.sock.recv(1024).decode("utf-8")
            if not self.data:
                continue
            print("%s"% self.data)
            if self.data == 'exit':
                 os._exit(0)
        
    
    def Senmsg(self):
        while True:
            if self.flag == 1:
                data = input("请输入要发送内容:")
                self.sock.send(data.encode('utf-8'))
                if data == "exit":

                     os._exit(0)
                    
        
   
if __name__ == '__main__':
   
    client = ClientUI()
    thread = threading.Thread(target = client.Recmsg, args = ())
    thread.setDaemon(True)
    thread.start()
    while True:
        client.Senmsg()