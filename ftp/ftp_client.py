"""
ftp 客户端
"""
from socket import *

ADDR = ('127.0.0.1',8080) # 服务器地址

#　客户端功能处理类
class FTPClient:
  def __init__(self,sockfd):
    self.sockfd = sockfd

  def do_list(self):
    self.sockfd.send(b'L')  #　发送请求
    # 等待回复
    data = self.sockfd.recv(128).decode()
    if data == 'OK':
      #　一次接收文件列表字符串
      data = self.sockfd.recv(4096)
      print(data.decode())
    else:
      print(data)

#　创建客户端网络
def main():
  sockfd = socket()
  try:
    sockfd.connect(ADDR)
  except Exception as e:
    print(e)
    return

  ftp = FTPClient(sockfd) #　实例化对象

  #　循环发送请求
  while True:
    print("\n=========命令选项==========")
    print("****      list         ****")
    print("****    get file       ****")
    print("****    put file       ****")
    print("****      quit         ****")
    print("=============================")

    cmd = input("输入命令：")

    if cmd.strip() == 'list':
      ftp.do_list()



if __name__ == "__main__":
  main()