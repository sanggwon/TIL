# SSAFY-DAY1

## 첫번째 시간

### 파이썬 코드작성

#### 먼지광주

```python
import requests
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=YNOYgnqfckC4PbaLGyN7HiFwbGe8MPhRN%2FjqmMufa7uqAffIl7D5fO%2BSh8zbRnzYfgo%2B4%2Bife1oj187l2mejMg%3D%3D&numOfRows=10&pageSize=10&pageNo=1&startPage=1&sidoName=%EA%B4%91%EC%A3%BC&ver=1.3'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
dong = soup('item')[7]
location = dong.stationName.text
time = dong.dataTime.text
dust = int(dong.pm10Value.text)

print("{0} 기준 {1}의 미세먼지 농도는 {2}입니다.".format(time,location,dust))

```



#### 안녕

```python
hello = [1,2,3,4,5]
for i in hello :
  print ("안녕하세요")
```



####  저녁메뉴

```python
import random

menu = ["치킨","피자","짜장면","보쌈","삼겹살","스테이크","초밥"]

# 주석

pick = random.choice(menu)

print(pick)
```



#### 저녁메뉴번호

```python
import random

# 1. menu 리스트를 만들어주세요.
menu = ['영암매력한우수완점','신전떡볶이 광주수완점','양동통닭','광주식당','회마켓','원조나주곰탕50년']

choice = random.choice(menu)
print(choice)

phonebook = {'영암매력한우수완점':'062-383-8118',
            '신전떡볶이 광주수완점':'062-956-2334',
             '양동통닭':'062-471-9277',
             '광주식당':'062-962-8284 ',
             '회마켓':'062-952-2026',
             '원조나주곰탕50년':'062-951-3255'
            }

print(phonebook[choice])
```



#### 광주먼지

```python
import requests
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=' + key + '&numOfRows=10&pageSize=10&pageNo=1&startPage=1&sidoName=%EA%B4%91%EC%A3%BC&ver=1.3'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
dong = soup('item')[1]
location = dong.stationName.text
time = dong.dataTime.text
dust = int(dong.pm10Value.text)

print("{0} 기준 {1}의 미세먼지 농도는 {2}입니다.".format(time,location,dust))

if dust > 150 :
  print("매우안좋아요")
elif dust >= 80 : 
  print("안좋아요")
elif dust >= 30 :
  print("보통")
else :
  print("좋아요")
```



#### 로또

```python
import random
number = list(range(1,46))
print(number)
#list 없어도 됩니다.

a = random.sample(number,6)

print(a)
```



#### 코스피

```python
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

res = requests.get(url).text

soup = BeautifulSoup(res,'html.parser')
select = soup.select_one("#KOSPI_now")
print(select.text)
```



지금까지 한 용어 정리

```python
import = 외부툴
random.choice(listname)
random.sample(listname,value)
[] - list
{} - kiy : value
range(start,end) - start 이상 end 미만
print = output
for 임시변수 in list : - 탐색순서
while 조건 true
if 조건, elif 조건, else 조건
from bs4 import BeautifulSoup - 웹 크롤링
request.get(url).text = 요청
BeautifulSoup(요청상자,"요청 확장자")
soup.select("찾고자하는 단어") : 전부_리스트
soup.select_one("찾고자하는 단어") : 첫번째꺼 반환
```

