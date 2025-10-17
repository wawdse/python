import requests

url = 'https://ssl.pstatic.net/melona/libs/1543/1543451/c3fbbb37d24814812ea3_20250820131021141.png'
res = requests.get(url)

file_name='data/naver.jpg'
with open(file_name, 'wb')as file:
    file.write(res.content)