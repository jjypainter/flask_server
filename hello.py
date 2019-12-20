from flask import Flask, escape, request
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/myname')
def myname():
    return '박지영입니다'

#랜덤으로 점심메뉴 추천해주는 서버
@app.route('/lunch')
def lunch():
    menus=['양자강','김밥까페','20층','순남시래기']
    lunch=random.choice(menus)
    return lunch