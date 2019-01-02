# SSAFY-DAY4(html, 챗봇기초)

## 네번째 시간



로또 검증페이지 만들기



app.py

```python
from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/lotto')
def lotto() :
    num_list = range(1,46)
    pick = random.sample(num_list,6)

    return render_template("lotto.html",lotto=pick)
```



app.py : import_requests , import_json(str를 dict로 변환)

```python
from flask import Flask, render_template
import requests
import random
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/lotto')
def lotto() :
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)
    # print(type(res))
    # print(type(json.loads(res)))
    
    num_list = range(1,46)
    pick = random.sample(num_list,6)
    

    return render_template("lotto.html",lotto=pick)
```



app.py :  리스트 변수 넣기

```python
 #print(lotto_dict["drwNoDate"]) #"drwNoDate" 변수를 가져옴
    week_num = []
    drwtNo = ["drwtNo1","drwtNo2","drwtNo3","drwtNo4","drwtNo5","drwtNo6"]
    for num in drwtNo :
        number = lotto_dict[num]
        week_num.append(number)
        #append : 붙여넣기
        print(week_num)
```



app.py : formating

```python
    week_format_num = []
    for i in range(1,7) :
        num = lotto_dict["drwtNo{}".format(i)]
        week_format_num.append(num)
        #formating
```



lotto.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>여기는 로또 검증페이지 입니다.</h1>
    <h4>생성된 번호 : {{lotto}}</h4>
    <h4>이번주 번호 : {{week_num}}</h4>
    <h4>얘는 포멧팅 : {{week_format_num}}</h4>
</body>
</html>
```



내가 만든 로또 검증 파이썬

```python
from flask import Flask, render_template
import requests
import random
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/lotto')
def lotto() :
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)

    # print(lotto_dict["drwNoDate"]) #"drwNoDate" 변수를 가져옴
    # week_num = []
    week_format_num = []
    # drwtNo = ["drwtNo1","drwtNo2","drwtNo3","drwtNo4","drwtNo5","drwtNo6"]
    # for num in drwtNo :
    #     number = lotto_dict[num]
    #     week_num.append(number)
    #     #append : 붙여넣기
    #     print(week_num)

    BnusNo = set([lotto_dict["bnusNo"]])

    num_list = range(1,46)
    pick = random.sample(num_list,6)
    sort_pick = sorted(pick) # set을 사용하면 sort을 안해도 됨

    for i in range(1,7) :
        num = lotto_dict["drwtNo{}".format(i)]
        week_format_num.append(num)
        sort_week_format_num = sorted(week_format_num)

    # print(type(res))
    # print(type(json.loads(res)))

        s1 = set(sort_week_format_num)
        s2 = set(sort_pick)

        s3 = s1&s2
        s5 = s1&BnusNo
        s6 = len(s5)
        s4 = len(s3)

        if s4 == 6 :
                s5 = "1등 입니다!! 축하축하"
        elif s4 == 5 and s6 == 1:
            s5 = "2등 입니다!!"
        elif s4 == 5  and s6 == 0:
            s5 = "3등 입니다"
        elif s4 == 4 :
            s5 = "4등 입니다"
        elif s4 == 3 :
            s5 = "5등 입니다"
        else :
            s5 = "꽝 ㅠㅠ"

    return render_template("lotto.html",sort_lotto=sort_pick, sort_week_format_num=sort_week_format_num,s5=s5, BnusNo=BnusNo)
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>여기는 로또 검증페이지 입니다.</h1>
    <h4>생성된 번호 : {{sort_lotto}}</h4>
    <h4>보너스 번호 : {{BnusNo}} </h4>
    <h4>이번주 번호 : {{sort_week_format_num}}</h4>
    <h4>{{s5}}</h4>
</body>
</html>
```



강사님 코드

- set()을 이용 하여 set화 시켜 &(교집합), |(합집합)

```python
from flask import Flask, render_template
import random
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/lottery')
def lottery():
    # 로또 정보를 가져온다
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)
    
    # 1등 당첨 번호를 week 리스트에 넣는다.
    week = []
    for i in range(1,7):
        num = lotto_dict["drwtNo{}".format(i)]
        week.append(num)
    
    # 보너스 번호를 bonus 변수에 넣는다.
    bonus = lotto_dict["bnusNo"]
    
    # 임의의 로또 번호를 생성한다.
    pick = random.sample(range(1,46),6)
    
    # 비교해서 몇등인지 저장한다.
    match = len(set(pick) & set(week))
    
    if match==6:
        text = "1등"
    elif match==5:
        if bonus in pick:
            text = "2등"
        else:
            text = "3등"
    elif match==4:
        text = "4등"
    else:
        text = "꽝"
    
    # 사용자에게 데이터를 넘겨준다.
    
    return render_template("lottery.html",pick=pick, week=week,text=text)
```



app.py : ping, pong : 검색과 돌아오기

```python
@app.route('/ping') #/은 우리 사이트의 루트url
def ping():
    return render_template("ping.html")

@app.route('/pong')
def pong():
    input_name = request.args.get('name')
    return render_template("pong.html", html_name=input_name)
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="/pong">
        <input type="text" name="name"/>
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <a href="/ping">핑</a>
    {{html_name}}
</body>
</html>
```

Faker

```python
from faker import Faker

@app.route('/ping') #/은 우리 사이트의 루트url
def ping():
    return render_template("ping.html")

@app.route('/pong')
def pong():
    input_name = request.args.get('name')
    fake = Faker('ko_KR')
    fake_job = fake.job()    
    return render_template("pong.html", html_name=input_name, fake_job=fake_job)
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <a href="/ping">핑</a>
    <h1>{{html_name}}님의 전생 직업은 {{fake_job}}입니다.</h1>

</body>
</html>
```



딕셔너리

```python
phonebook = {
    "치킨집" : "02:000-0000",
    "피자집" : "062-123-4567"
}
# print(phonebook["치킨집"])

izone = {"장원영" : 15 , "미야와키 사쿠라" : 21, "조유리" : 18,
"최예나" : 20, "안유진" : 16, "야부키 나코":18, "권은비":24,
"강혜원":20, "혼다 히토미":18, "김채원":19, "김민주":18, "이채연":19
}

bts = {
    "RM":20,
    "슈가":21,
    "진":22,
    "제이홉":23
}


idol ={
    "izone":izone,
    "bts":bts
}

# print(idol)
# print(idol["izone"]["장원영"])

score = {
    "수학":50,
    "국어":70,
    "영어":100
}
for key, value in score.items():
    pass
    # print(key)
    # print(value)

for key in score.keys():
    pass
    # print(key)

score_sum = 0
for value in score.values():
    score_sum = score_sum + value

print(score_sum/len(score))
```



딕셔너리 읽기

```python
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gj1":  {
            "lecturer": "ChangE",
            "manager": "pro1",
            "class president": "서희수",
            "groups": {
                "두드림": ["구종민", "김녹형", "윤은솔", "이준원", "이창훈"],
                "런치타임": ["문영국", "박나원","박희승", "서희수", "황인식"],
                "Friday": ["강민지", "박현진", "서상준", "안현상", "최진호"],
                "TMM": ["김훈", "송건희", "이지선", "정태준", "조호근"],
                "살핌": ["문동식", "이중봉", "이지희", "차상권", "최보균"]
            }
        },
        "gj2": {
            "lecturer": "teacher2",
            "manager": "pro2"
        },
        "gj3": {
            "lecturer": "teacher3",
            "manager": "pro3"
        }
    }
}

print(len(ssafy["location"]))
# 1. ssafy를 진행하는 지역(location)은 몇개 인가요?

if ssafy["language"]["python"]["python standard library"] == "requests" :
    print("T")
else :
    print("F")
# 2. python standard library 'requests'가 있나요??

print(ssafy["classes"]["gj1"]["class president"])
# 3. gj1반의 반장의 이름을 출력하세요

for key in ssafy["language"].keys():
    print(key)
# 4. ssafy에서 배우는 언어들을 출력하세요 : dictionary.keys활용

for value in ssafy["classes"]["gj2"].values():
    print(value)
# 5. ssafy gj2의 강사와 매니저의 이름을 출력하세요
    # 예시) teacher2
    #       pro2

for key, value in ssafy["language"]["python"]["frameworks"].items():
    print(key,"는", value,"이다")
# 6. framework들의 이름과 설명을 다음과 같이 출력하세요
    # 예시)
    # flask는 micro이다.
    # django는 full-functioning이다.


print("오늘 당번은", random.choice(ssafy["classes"]["gj1"]["groups"]["살핌"]),"입니다")
# 7. 오늘 당번을 뽑기 위해 '살핌'조원중 1명을 랜덤으로 뽑아주세요
    # 예시)
    # 오늘 당번은 문동식입니다.

```



```terminal
$ export TELE_TOKEN=746464234:AAGOBHn9I7hYZhXvtv2n7w5eiNiZE2MI2NQ
$ echo $TELE_TOKEN
746464234:AAGOBHn9I7hYZhXvtv2n7w5eiNiZE2MI2NQ
```

- {} 딕셔너리
- [] 리스트



챗봇

```python
import os
import json
import requests

token = os.getenv('TELE_TOKEN')
# print(os.getenv('TELE_TOKEN'))
#토큰이 환경변수에 잘 저장이 되었는지 확인하기 위해서 os를 import하고 os의 함수로 호출
method = 'getUpdates'
# url = "https://api.telegram.org/bot{}/{}".format(token,method)
url = "https://api.hphk.io/telegram/bot{}/getUpdates".format(token)
#c9에서 telegram api 막아서 우회

#token 값과 METHOD_NAME 설정
res = requests.get(url).json()

user_id = res["result"][0]["message"]["from"]["id"]
#리스트는 순서로 접근
#딕셔너리는 키값으로 접근
msg = "안녕"

method = 'sendMessage'
msg_url = "https://api.hphk.io/telegram/bot{}/{}?chat_id={}&text={}".format(token,method,user_id,msg)

print(msg_url)
requests.get(msg_url)
```



