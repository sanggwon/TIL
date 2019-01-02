# SSAFY-DAY5(챗봇)

## 다섯번째 시간



챗봇

```python
import os
from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

api_url = 'https://api.hphk.io/telegram'
           # 우회
token = os.getenv('TELE_TOKEN')

@app.route(f'/{token}',methods = ['POST'])
def telegram():
    print(request.get_json())

    return '',200

app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))
```

```terminal
 $ FLASK_APP=app.py flask run -- host=$IP --port+$PORT
 >>Error: Got unexpected extra arguments (host=0.0.0.0 --port+8080
 $ python app.py
```

'''참고

```python
a = 123
"asdf{}".format(a) = f"asdf{a}" 
>> asdf123

a = 안녕하세요 #리스트와 비슷
a[0] = 안
a[:2] = 안녕
```

'''url

https://api.telegram.org/bot<token>/setWebhook?url=https://<python-ck2570-1.c9users.io(flask웹페이지)>/<token>



유저에게 그대로 돌려주기

```python
import os
from flask import Flask,request
from pprint import pprint as pp
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

api_url = 'https://api.hphk.io/telegram'
           # 우회
token = os.getenv('TELE_TOKEN')

@app.route(f'/{token}',methods = ['POST'])
def telegram():
    tele_dict = request.get_json()
    pp(request.get_json())

    #유저 정보
    chat_id = tele_dict["message"]["from"]["id"]
    #유저가 입력한 데이터
    text = tele_dict["message"]["text"]
    # print(chat_id, text)

    #유저에게 그대로 돌려주기
    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')


    return '',200

app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))
```



환경설정

```terminal
$ c9 ~/.bashrc
$ export TELE_TOKEN="토큰" #띄어쓰기 조심

#토큰 설정 확인
$ exec $SHELL # 새로고침
$ echo $TELE_TOKEN
```





번역시켜보기

https://developers.naver.com

```terminal
$ c9 ~/.bashr
```

```python
export TELE_TOKEN="토큰" #띄어쓰기 조심
export NAVER_ID="아이디"
export NAVER_SECRET="시크릿값"
```

```terminal
curl "https://openapi.naver.com/v1/papago/n2mt" \
-H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
-H "X-Naver-Client-Id: 아이디" \
-H "X-Naver-Client-Secret: 시크릿값" \
-d "source=ko&target=en&text=만나서 반갑습니다." -v
```

```python
import os
from flask import Flask,request
from pprint import pprint as pp
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

api_url = 'https://api.hphk.io/telegram' # 우회

token = os.getenv('TELE_TOKEN')

@app.route(f'/{token}',methods = ['POST'])
def telegram():
    # naver api를 사용하기 위한 변수
    naver_client_id = os.getenv('NAVER_ID')
    naver_client_secret = os.getenv('NAVER_SECRET')
    tele_dict = request.get_json()
    pp(request.get_json())

    #유저 정보
    chat_id = tele_dict["message"]["from"]["id"]
    #유저가 입력한 데이터
    text = tele_dict["message"]["text"]
    # print(chat_id, text)

    # text(유저가 입력한 데이터) 제일 앞 두글자가 번역
    tran = False
    if text[:2] == "번역":
        # 번역 안녕하세요
        tran = True
        text = text.replace("번역","")
        # 안녕하세요

    if tran :
        papago = requests.post("https://openapi.naver.com/v1/papago/n2mt", # 파파고 NMT API 가이드
                    headers = {
                        "X-Naver-Client-Id" : naver_client_id,
                        "X-Naver-Client-Secret" : naver_client_secret
                    },
                    data = {
                        'source' : 'ko',
                        'target' : 'en',
                        'text' : text
                    }
        )
        text = papago.json()["message"]["result"]["translatedText"]

    return '',200

app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))
```



사진 검색하고 네이버 인식정보 확인하기

```python
import os
from flask import Flask,request
from pprint import pprint as pp
import requests
import random
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

api_url = 'https://api.hphk.io/telegram' # 우회
url = 'https://finance.naver.com/sise/'
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')
select = soup.select_one("#KOSPI_now")

token = os.getenv('TELE_TOKEN')

@app.route(f'/{token}',methods = ['POST'])
def telegram():
    # naver api를 사용하기 위한 변수
    naver_client_id = os.getenv('NAVER_ID')
    naver_client_secret = os.getenv('NAVER_SECRET')
    tele_dict = request.get_json()
    #데이터 덩어리
    pp(request.get_json())

    #유저 정보
    chat_id = tele_dict["message"]["from"]["id"]
    
    #유저가 입력한 데이터
    if tele_dict.get("message").get("text") is None:
        text = "임시 텍스트"
    else:
        text = tele_dict.get("message").get("text")

    tran = False
    img = False

    # 사용자가 이미지를 넣었는지 체크
    if tele_dict.get('message').get('photo') is not None :
        img = True


    # text(유저가 입력한 데이터) 제일 앞 두글자가 번역
    else:
        text_list = text.split(' ')
        if text_list[0] == '번역':
            # 번역 안녕하세요
            tran = True
            text = text.replace("번역","하이")
            # 안녕하세요

    if tran :
        print(text)
        papago = requests.post("https://openapi.naver.com/v1/papago/n2mt", 
                               # 파파고 NMT API 가이드
                    headers = {
                        "X-Naver-Client-Id":naver_client_id,
                        "X-Naver-Client-Secret":naver_client_secret
                    },
                    data = {
                        'source':'ko',
                        'target':'en',
                        'text':text
                    }
        )

        pp(papago.json())
        text = papago.json().get('message').get('result').get('translatedText')


    elif img:
        text = "사용자가 이미지를 넣었어요"
        
        # 텔레그램에게 사진 정보 가져오기
        file_id = tele_dict['message']['photo'][-1]['file_id']
        file_path = requests.get(f"{api_url}/bot{token}/getFile?file_id={file_id}").json()['result']['file_path']
        file_url = f"{api_url}/file/bot{token}/{file_path}"
        print(file_url)
        
        # 사진을 네이버 유명인 인식api로 넘겨주기
        file = requests.get(file_url, stream=True)
        clova = requests.post("https://openapi.naver.com/v1/vision/celebrity",
                    headers = {
                        "X-Naver-Client-Id":naver_client_id,
                        "X-Naver-Client-Secret":naver_client_secret
                    },
                    files = {
                        'image':file.raw.read()
                    }
        )
        
        # 가져온 데이터 중에서 필요한 정보 빼오기
        pp(clova.json())
        
        #인식이 되었을 때
        if clova.json().get('info').get('faceCount'):
            text = clova.json()['faces'][0]['celebrity']['value']
            
        # 인식이 되지 않았을때
        else:
            text = "얼굴이 없어요 ㅠㅠㅠ"

    elif text == "메뉴":
        menu_list = ["한식","중식","양식","분식","선택식"]
        text = random.choice(menu_list)
    elif text == "로또" :
        lotto = range(1,46)
        text = random.sample(lotto,6)
    elif text == "코스피":
        text = select.text

    # 유저에게 그대로 돌려주기
    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    return '',200

app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))
```



heroku

```terminal
$ git add .
$ git commit -m "챗봇 테스트"
$ heroku login
$ touch runtime.txt
$ touch Procfile
$ touch requirements.txt
$ pip freeze > requirements.txt
$ git add .
$ git commit -m "sever setting"
$ heroku create sang-chatbot
$ git push heroku master
```