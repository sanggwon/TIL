# Pickle

### pickle 이란?

- 파이썬 객체 직렬화



### pickle 모듈

- 일반 텍스트를 파일로 저장할 때는 파일 입출력을 이용한다.
- 하지만 `리스트나 클래스 같은 텍스트가 아닌 자료형`은 일반적인 파일 입출력 방법으로는 데이터를 저장하거나 불러올 수 없다.
- 파이썬에서는 이와 같은 텍스트 이외의 자료형을 파일로 저장하기 위하여 `pickle`이라는 모듈을 제공한다.



```python
# 파일에 텍스트 입력하기
>>> text = "hello world"
>>> with open('hello.txt', 'w') as f :
    	f.write(text)
    
>>> cat hell.txt
hello world

# 파일에 리스트 입력하기 > TypeError 발생
>>> list = ['a','b','c']
>>> with open('list.txt', 'w') as f :
    	f.write(list)
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: write() argument must be str, not list
```



### pickle 모듈을 활용하여 데이터 입력 및 로드

- `import pickle`을 통하여 모듈 임포트가 필요하다.

- pickle 모듈을 이용하면 원하는 데이터를 자료형의 변경없이 파일로 저장하여 그대로 로드할 수 있다.

  (`open('text.txt, 'w')`방식으로 데이터를 입력하면 `string 자료형`으로 저장된다. )

- pickle로 데이터를 저장하거나 불러올 때는 파일을 `바이트형식`으로 읽거나 써야한다. `(wb,rb)`

- wb로 데이터를 입력하는 경우는 .bin 확장자를 사용하는게 좋다.

- 모든 파이썬 데이터 객체를 저장하고 읽을 수 있다.



### 입력

- `pickle.dump(data, file)`

```python
>>> import pickle
>>> lisk = ['a','b','c']
>>> with open('list.txt', 'wb') as f :
    	pickle.dump(list, f)
```



### 로드

- `변수 = pickle.load(file)`
- 한줄씩 파일을 읽어오고 더이상 로드할 데이터가 없으면 `EOFError`발생

```python
>>> with open('list.txt', 'rb') as f:
...     data = pickle.load(f) # 단 한줄씩 읽어옴

>>> data
['a', 'b', 'c']
```



## 참고

- pickle.load(파일) 을 통해서 파일 내용을 읽어오려면, pickle.dump를 사용해서 데이터를 입력한 파일이어야한다.

```python
# vim으로 작성한 abc.txt 파일
❯ cat abc.txt
{'greg': 95},
{'john': 25},
{'yang': 50},
{'timothy': 15},
{'melisa': 100},
{'thor': 10},
{'elen': 25},
{'mark': 80},
{'steve': 95},
{'anna': 20}%

# pickle.dump()를 사용하여 해당 내용을 abc2.bin 파일에 입력
# abc2.txt 와 같이 txt 파일에 wb 형식으로 데이터를 입력하면 다른 메타정보도 함께 입력

In [5]: with open('abc2.bin', 'wb') as file:
   ...:     for data in text_list:
   ...:         pickle.dump(data, file)

# pickle.load()를 사용하여 파일 로드
# 데이터를 한 줄 밖에 읽어오지 못함

In [6]: with open('abc2.bin', 'rb') as file:
   ...:     data = pickle.load(file)
   ...:

In [7]: data
Out[7]: "{'greg': 95},\n"

# pickle.load()를 사용하여 파일 전체 내용 로드
In [8]: with open('abc2.bin', 'rb') as file:
   ...:     data_list = []
   ...:     while True:
   ...:         try:
   ...:             data = pickle.load(file)
   ...:         except EOFError:
   ...:             break
   ...:         data_list.append(data)
   ...:

In [9]: data_list
Out[9]:
["{'greg': 95},\n",
 "{'john': 25},\n",
 "{'yang': 50},\n",
 "{'timothy': 15},\n",
 "{'melisa': 100},\n",
 "{'thor': 10},\n",
 "{'elen': 25},\n",
 "{'mark': 80},\n",
 "{'steve': 95},\n",
 "{'anna': 20}"]
```