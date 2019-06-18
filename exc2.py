import re

port = input("端口:")
f = open('exc.txt')

# 找到port所在段
while True:
  data = ''
  for line in f:
    if line != '\n':
      data += line
    else:
      break

  # 结尾退出循环
  if not data:
    print("没有这个端口")
    break

  result = re.match(port,data)
  if result:
    # pattern = r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'
    pattern = r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknown"
    try:
      address = re.search(pattern,data).group()
      print(address)
    except:
      print("No address")
    break
