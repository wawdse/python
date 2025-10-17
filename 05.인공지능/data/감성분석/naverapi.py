# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json
from dotenv import load_dotenv

load_dotenv()

def getNew(query, start, display):
    client_id = os.getenv("NAVER_CLIENT_ID")
    client_secret = os.getenv("NAVER_CLIENT_SECRET")
    encText = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/news.json?query={encText}&start={start}&display={display}"
# JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result = response_body.decode('utf-8')
        result = json.loads(result)
        return result['items']
    else:
        print("Error Code:" + rescode)
        return None

if __name__=='__main__':
    query='인공지능'
    start=1
    display=100
    results = []
    while start<=1000:
        news = getNew(query, start, display=100)
        results.extend(news)
        start = start + display

    print('데이터갯수:', len(results))
    with open('data/감성분석/news.json', 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)