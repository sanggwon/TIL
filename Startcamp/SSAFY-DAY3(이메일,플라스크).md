# SSAFY-DAY3(이메일,플라스크)

## 세번째 시간

첫번째 작업공간 - 이메일 보내보기, 플라스크 사용해보기



Cloud9 : 여러 환경에서 다양한 버전 사용 가능

- 리눅스 환경이라 파이썬.exe가 열리지 않음

- pyenv 검색

- Installation 클릭

- Clound9 터미널에 복붙

  ```
  1) $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv 
  => 복제해서 ~/.pyenv에 설치
  
  2) $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  
  3) $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
  
  4) $ exec "$SHELL"
  ```

```
$ pyenv install 3.6.7
$ pyenv global 3.6.7
$ pyenv rehash : 재부팅
$ pyenv versions : 설정 완료
#ck2570:~/workspace : ~/ => /home/ubuntu/ (줄임말)
```



send_email

```python
#F6 : 터미널 켜기

import smtplib : 전자우편 전송 프로토콜
    
from email.message import EmailMessage

import getpass
#비밀번호 보안
password = getpass.getpass('비밀번호 입력하세요')

msg = EmailMessage()
msg['Subject'] = "제목입니다!!!"
msg['From'] = "ck2570@naver.com" : 보내는 메일
msg['TO'] = "ck2570@hanmail.net" : 받는 메일
msg.set_content('내용입니다')

smtp_url = 'smtp.naver.com'
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)
#보안연결에 필요

s.login('ck2570', password)
s.send_message(msg)

#tab 들여쓰기
#shift + tab 왼쪽으로 
```

```python
import smtplib
from email.message import EmailMessage

import getpass
#비밀번호 보안
password = getpass.getpass('비밀번호 입력하세요')

email_list = ['ck2570@hanmail.net, ck3929@gmail.com']

for email in email_list : 
    msg = EmailMessage()
    msg['Subject'] = "제목"
    msg['From'] = "ck2570@naver.com"
    msg['TO'] = email
    msg.set_content('내용')
    smtp_url = 'smtp.naver.com'
    smtp_port = 465
    
    s = smtplib.SMTP_SSL(smtp_url, smtp_port)
    #보안연결에 필요
    
    s.login('ck2570', password)
    s.send_message(msg)
```

#### csv 열기

```python
import csv

f = open('pygj - email.csv', 'r', encoding = 'utf-8')
#r : 읽다
read_csv = csv.reader(f)

for line in read_csv :
    print(line[0] + '/' + line[1])
    
f.close()
```

#### csv 열고 보내기

```python
import csv
import smtplib
from email.message import EmailMessage

import getpass

password = getpass.getpass('비밀')

f = open('pygj - email.csv', 'r', encoding = 'utf-8')
#r : 읽다
read_csv = csv.reader(f)

smtp_url = 'smtp.naver.com'
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)
s.login('ck2570@naver.com', password)

for line in read_csv :
    msg = EmailMessage()
    msg['Subject'] = "차상권입니다"
    msg['From'] = "ck2570@naver.com"
    msg['TO'] = line[1]
    msg.set_content(line[0]+ '님 '+'배고파요')

        #보안연결에 필요
     
    s.send_message(msg)
f.close()
```

#### 텍스트 넣기(크기)

```python
import smtplib
from email.message import EmailMessage

import getpass
#비밀번호 보안
password = getpass.getpass('비밀번호 입력하세요')

# email_list = ['ck2570@hanmail.net, ck3929@gmail.com']

# for email in email_list : 
msg = EmailMessage()
msg['Subject'] = "제목"
msg['From'] = "ck2570@naver.com"
msg['TO'] = "ck2570@naver.com"
# msg.set_content('내용')

msg.add_alternative('''
<h1>안녕하세요!!!</h1>
<p>저는 차상권입니다.</p>
''', subtype = "html")

smtp_url = 'smtp.naver.com'
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)
#보안연결에 필요

s.login('ck2570', password)
s.send_message(msg)
```



""와 ''의 차이점

- 1월 커밍순.....



플라스크

```python
from flask import Flask
app = Flask(__name__)

@app.route("/") # "/" => 루트지정
def hello(): 
    return "내용을 입력"
```



app.py

```python
from flask import Flask
app = Flask(__name__)

@app.route("/") # "/" => 루트지정
                # 경로지정
def hello():
    return "<h1>서버가 html도 보내주나??</h1>"
    
@app.route("/html_tag")
def html_tag():
    return """
    <h1>첫번째 줄!!!</h1>
    <h2>두번째 줄!!!</h2>
    """
```



```
$ pip install Flask
$ FLASK_APP=app.py flask run
$ FLASK_APP=app.py flask run --host=$IP --port=$PORT
#ctrl+C : 서버 닫기
```



#### Html 문서를 만들어보자

- http://python-ck2570-1.c9users.io:8080 => 루트주소
- http://python-ck2570-1.c9users.io:8080/html_tag => 만든거
- http://python-ck2570-1.c9users.io:8080/html_file => 만든거

app.py

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # "/" => 루트지정
                # 경로지정
def hello(): #메소드
    return "<h1>서버가 html도 보내주나??</h1>"

@app.route("/html_file")
def html_file():
    return render_template("html_file.html") #render_template를 가져와야 사용 가능
# 폴더는 반드시 templates 이름으로 생성
# 폴더 안에 html_file.html 생성
    
#html_file.html 파일 안에
=> <h1>여기는 html_file.html입니다.</h1> 입력
```



- https://www.w3schools.com/tags/tag_html.asp => html tag 보는곳



#### html_file.html

```html
<!--<태그명 속성명1 = "속성1" 속성명2 = "속성2"> 내용 </태그명>-->
<!--속성은 색깔같은 거-->

<!doctype html> 
<!--네임택. 이건 html문서야-->

<html>
    <head>
    
    </head>
    
    <body> 
    <!--보여주는 곳은 body-->
        <h3>html을 배워봅시다.</h3>
        <!--tag만 입력하고 tab누르면 자동 tag-->
        <a href="https://naver.com/">네이버</a>
        <!--a는 링크, 클릭하면 이동시켜주는 것-->
        
    </body>
    
</html>
```



app.py

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # "/" => 루트지정
                # 경로지정
def hello(): #메소드
    return "<h1>서버가 html도 보내주나??</h1>"
                                             
@app.route("/welcome/<string:name>")
def welcome(name):
    return render_template("welcome.html", people=name)
```



welcom.html

```html
<h1>{{people}}님 안녕하세요!!</h1>
```



#### app.py : 3제곱 해보기

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # "/" => 루트지정
                # 경로지정
def hello(): #메소드
    return "<h1>서버가 html도 보내주나??</h1>"

@app.route("/cube/<int:num>")
def cube(num):
    triple = num**3 # 제곱근 : **
    return render_template("cube.html", number=triple)
```



cube.html

```python
<h1>{{number}}</h1>
```



#### 점심메뉴와   로또

```python

from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/") # "/" => 루트지정
                # 경로지정
def hello(): #메소드
    return "<h1>서버가 html도 보내주나??</h1>"

@app.route('/lunch')
def lunch() :
    menu = ['삼겹살','짜장면','피자','치킨']
    choice = random.choice(menu)
    return render_template("lunch.html",choice=choice)
    
@app.route('/lotto')
def lotto() :
    number = range(1,46)
    pick = random.sample(number,6)
    sort_pick = sorted(pick)
    return render_template("lotto.html",sort_pick = sort_pick)
    #url이름과 html의 이름을 통일 시킬 것
```



lunch.html

```html
<h1>오늘은 점심 메뉴는 {{choice}}입니다.</h1>
```



lotto

```html
<h1>{{sort_pick}}</h1>
```

### 

- ! + tab : 구조 편리 기능



#### 검색 전송

```python

from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/") # "/" => 루트지정
                # 경로지정
def hello(): #메소드
    return "<h1>서버가 html도 보내주나??</h1>"
    
@app.route('/naver')
def naver() :
    return render_template("naver.html")
```

#### 

naver.html

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
    <form action="https://search.naver.com/search.naver">
        <input type="text" name="query"/> 
        <!--input은 예외로 닫는 태그가 없음-->
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```



Git 저장

```
$ touch .gitignore : 숨김파일
$ git init
$ git add . : 임시저장
$ git status : 상태확인
```

