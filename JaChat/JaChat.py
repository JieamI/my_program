import socket
import threading
import time
import sys
import os

"""
class ServeUI:                                             #UI界面类
    localIP = "127.0.0.1"
    port = 5505
    flag = 0
    global servesock
    def __init__(self):
        self.win = tkinter.TK()
        self.win.titilt("JaChat Serve V1.0")
"""
class ServeUI:
 
    def Recmsg(self):
        self.flag = 0
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        self.sock.bind(("127.0.0.1",8888))
        self.sock.listen(5)
        print("正在等待客户端链接……\n")
        while True:
            self.sc,address = self.sock.accept()
            print("已和地址为 %s:%s 的客户端建立连接\n"% address)
            self.flag = 1
            while True: 
                self.data = self.sc.recv(1024).decode("utf-8")
                if not self.data:
                    continue
                print("%s"% self.data)
                if self.data == 'exit':
                     os._exit(0)
                    
            
           
    def Senmsg(self):
        while True:
            if self.flag == 1:
                data = input("请输入要发送内容:")
                self.sc.send(data.encode('utf-8'))
                if data == "exit":
                    break
        os._exit(0)

    


if __name__ == '__main__':
     serve = ServeUI()
     thread = threading.Thread(target = serve.Recmsg, args = ())
     thread.setDaemon(True)
     thread.start()
     while True:
         serve.Senmsg()
            
       

