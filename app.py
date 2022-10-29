import json
from flask import Flask, render_template, request

datas = [
    '요즘 슬픈 기분인가요?',
    '미래에 대해 어떻게 생각하나요?',
    '자신이 실패자라고 생각하나요?',
    '일상에 만족 하시나요?',
    '죄책감을 느낄때가 있나요?',
    '벌을 받는 느낌이 드나요?',
    '자신에게 실망하거나 싫은 기분인가요?',
    '안 좋은 일이 생가면 자신을 탓하는 편인가요?',
    '자살에 대해서는 어떻게 생각하나요?',
    '요즘 우는 날이 많아지진 않았나요?',
    '최근에 짜증이 늘었나요?',
    '주위 또는 주변 다른 사람들에게 관심을 가지고 있나요?',
    '결정을 내릴땐 어떤가요?',
    '전과 비교해 지금 자신의 외모에 대해 어떻개 생각해요?',
    '일(공부 등 개인이 수행하는것)을 시작할 때의 의지는 어떤가요?',
    '최근 수면 패턴은 어떤가요?',
    '피로도는 어떤가요?',
    '식욕은 어떤가요?',
    '최근 심리적인 이유로 체중에 큰 변화가 있었나요?',
    '건강이 좋다고 생각하나요?',
    '성에대한 관심도는 어떤가요?',



]

app = Flask(__name__)
with open('server.env', 'r') as r:
    env = json.loads(r.read())

@app.route("/")
def main():
    return render_template('index.html', datas=enumerate(datas))


@app.route("/result", methods=['POST'])
def result():
   get = dict(request.form)
   print(get)
   maximum = len(datas)*3 # 점수의 최대값: 모두 3을 선택할 때
   total = sum(map(int, get.values()))  # 총합
   percent = int(total/maximum*100)  # 백분율로 전환
   val = "없는"
   if percent >= 80:
       val = "우울의 결정체"
   elif percent >= 60:
       val = "평범하게 우울한"
   elif percent >= 40:
       val = "평범한"
   elif percent >= 20:
       val = "평범하게 밝은"
   else:
       val = "건강하게 밝은"
   return render_template("result.html", result=val, percent=percent)

if __name__ == "__main__":
    app.run('0.0.0.0', port=80, debug=env['is_debug'])