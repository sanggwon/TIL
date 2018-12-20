# SSAFY-DAY2

## 두번째 시간

### 파이썬 심화

#### GIT 설치

- 리눅스환경 - use git and optional unix tools from the command prompt
- Git bash 열기



GIT BASH

```
$ - 명령의 시작
pwd - 현재 위치
ls - 현재 디렉토리의 내용들을 나열
clear - 리플래쉬
mkdir (name)- 폴더 생성
cd (name) - 현재 작업하는 디렉토리를 변경
touch (name.txt) - 메모 생성
python -V - 버전확인
```



#### PYTHON 설치

- 3.6.7 DOWNLOADS 
- Windows x86-64 web-based installer
- Add python 3.6 to PATH  - 환경변수



#### VSCODE 설치

- Windows 클릭
- code를 지원되는 파일 형식에 대한 편집기로 등록합니다. 체크
- EXTENSIONS (CTRL + SHIFT + X)  >>  KOREA  >> 한글 설치
- CTRL + SHIFT + P  >> shell 기본 설정  >> git bash
- 터미널 (CTRL + `) >> 보기(터미널)



#### import webbrowser

```python
webbrowser.open(url)
webbrowser.open_new
webbrowser.open_new_tab

import webbrowser

q_list = ["광주날씨","광주미세먼지","길찾기"]

url ="https://www.google.com/search?q="

for q in q_list :
    webbrowser.open(url+q)
```



#### 정보 스크랩하기(자주 확인하는 정보)

pip install requests : 호환

```python
import requests

url = "https://www.google.com"
#res = requests.get(url)
#res = requests.get(url).text
res = requests.get(url).status_code

print(res)
```



```python
import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net/"
res = requests.get(url).text

soup = BeautifulSoup(res,'html.parser')
soup.select("#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > ol > li:nth-child(1) > div > div:nth-child(1) > span.txt_issue > a")

#head / body
#nth-child bs4에서 호환이 안됨
#nth-of-type로 고침
#nth-of-type("인기검색어 순위")

print(soup)
```



```python
import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net/"
res = requests.get(url).text

soup = BeautifulSoup(res,'html.parser')

picks = soup.select("#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li > div > div:nth-of-type(1) > span.txt_issue > a")
for p in picks : 
    print(p.text)
    #.text 는 태그 사이에 있는 글자만 가져오는 것
```



#### 비트코인

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.bithumb.com/"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')

coins = soup.select('tbody.coin_list tr')

for coin in coins :
    print(coin.select_one("td:nth-of-type(1) a strong").text)
    print(coin.select_one("td:nth-of-type(2) strong").text)

```



#### kbs편성표

```python
import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=kbs"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')

kbsdays1 = soup.select('tr.on td:nth-of-type(2) a')
# print(kbsdays1)
for kbstv in kbsdays1 :
    print(kbstv.text)
```



#### daum 환율

```python
import requests
from bs4 import BeautifulSoup

url = "http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')

exc = soup.select('tbody tr')

for daum in exc :
    print(daum.select_one("td.name a").text)
    print(daum.select_one("td:nth-of-type(2)").text)
    print(daum.select_one("td:nth-of-type(3)").text)
    print(daum.select_one("td:nth-of-type(4)").text)
```



#### url 축약

https://zzu.li/



#### MELON

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # headers에 정보를 넣어줘야 함, 401은 허용 안함
}
response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response,'html.parser')
music_table = soup.select("table tr.lst50")

for music in music_table:
    number = music.select_one("span.rank").text
    title = music.select_one("div.wrap_song_info a").text
    print(number +"위 : "+ title)
```



#### +파일명 바꾸기

- os.chdir(r'폴더주소')

```python
import os

os.chdir(r'C:\Users\student\CHANGE\SSAFY지원자')

for filename in os.listdir(".") :
    os.rename(filename, "SAMSUNG_" + filename)
#.은 현재폴더

import os

os.chdir(r'C:\Users\student\CHANGE\SSAFY지원자')

for a in os.listdir(".") :
    a_r = a.replace("SSAFY","SAMSUNG_")
    os.renames(a,a_r)
#.은 현재폴더
```



#### GIT

- #### add : 커밋할 목록에 추가

- commit : 커밋 만들기

- push : 현재까지의 역사가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기

```
$ git init
$ ls
$ ls -a

$ git add python.py
$ git commit -m "python.py 추가함"
$ git log

$ git config --global user.name "sanggwon"
$ git config --global user.email "ck2570@naver.com"
```

#### 

#### add

```
$ git add .
```

- git이라는 프로그램한테 add라는 명령을 시킨다.
- . => 현재폴더에 있는 모든 파일과 모든 폴더
- 모든파일을 add 시켜줘

#### commit

```
$ git commit -m "메세지"
```

- git 프로그램아 현재 index에 모아진 파일들을 저장시켜줘
- 저장할 때 메세지는 "메세지" <= 이거야

#### remote

```
$ git remote add origin <주소>
```

- 원격저장소 <주소>를 add해줘, 별명은 origin으로 지어줄께

### push

```
$ git push -u origin master
```

- git아 mater를 origin으로 push해줘
- 야 너 누구야?? => 아이디. 패스워드 



## 블로그 만들기

https://startbootstrap.com/template-categories/all/  >> Resume >> Download

=> 압축풀기

=> VScode >> $ git init >> $ git add . >> $ git commit -m "메세지" 

=> $ git remote add origin <주소> >> $ git push -u origin master

=> github >> new repository >>  Repository name : sanggwon.github.io



index.html

