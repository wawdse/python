from flask import Flask, render_template, request
import random

app = Flask(__name__, template_folder='temp', static_folder='static')

def recommend_menu(category):
    menus = {
        '한식': ['제육볶음', '김치찌개', '된장찌개', '순두부찌개', '순댓국', '감자탕', '닭갈비', '삼겹살', '청국장', '육개장'],
        '중식': ['짜장면', '짬뽕', '잡채밥', '볶음밥', '탕수육', '해물쟁반짜장', '중화비빔밥', '중국냉면', '크림새우', '마파두부'],
        '일식': ['사케동', '초밥', '우동', '텐동', '라멘', '야끼소바', '오꼬노미야끼', '규동', '김치나베', '스키야키'],
        '양식': ['파스타', '스테이크', '피자', '샌드위치', '햄버거', '스크램블', '라자냐', '오믈렛', '바비큐립', '치즈오븐스파게티'],
        '분식': ['떡볶이', '김밥', '쫄면', '튀김', '라면', '라볶이', '알밥', '비빔국수', '주먹밥', '오므라이스']
    }

    if category in menus:
        return random.choice(menus[category])
    else:
        return '종류를 선택해주세요!'  

@app.route('/')
def index():
    return render_template('index.html', title='점심 메뉴 추천')

@app.route('/recommend')
def recommend():
    category = request.args.get('category')  
    menu = recommend_menu(category)  
    return menu  

if __name__ == '__main__':
    app.run(port=5000, debug=True)