print(5)
print(-10)
print("문자열")
print(True)
print(False)
print(not True)

'''
여러문장 주석
'''
# 한줄 주석

print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True

print(abs(-5)) # 5 절대값
print(pow(4, 2)) # 4^2 = 4*4 = 16 n승
print(max(5, 12)) # 12 
print(min(5, 12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

## math 라이브러리
from math import * # math 라이브러리에 모든것을 사용하겠다.
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근

## random 라이브러리
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 소수점 버리고 정수만 출력
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 출력

print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성


### 슬라이스
jumin = "930616-1015116"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2직전까지
print("월 : " + jumin[2:4])
print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:]) # 7번째부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

### 문자열 처리
python = "Python is Amazing"
print(python.lower()) # 모두 소문자로 변환
print(python.upper()) # 모두 대문자로 변환
print(python[0].isupper()) # 0번째 값이 대문자인지
print(len(python)) # 길이
print(python.replace("Python", "Java")) # 변환

index = python.index("n") # index 반환
print(index)
index = python.index("n", index + 1)
print(python.find("Java")) # 값이 없을경우 -1 
# print(python.index("Java")) # error 발생
print(python.count("n")) # 몇번 들어가있는지

### 문자열 연산
print("나는 %d살입니다." % 20) # d는 정수로 받겠다.
print("나는 %s을 좋아해요." % "파이썬") # s는 문자열만 받겠다.(정수 자동변환됨)
print("Apple은 %c로 시작해요." % "A") # c는 한글자만 받겠다.
print("나는 %s살입니다." % 20) # d는 정수로 받겠다.
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 다수출력.

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간")) # index 선언

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간")) # 변수 선언

# v3.6 이상부터 가능한 방법
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
################### 여기까지 #######################

print("백문이 불여일견 \n백견이 불여일타")
print("저는 \"나도코딩\" 입니다.") # "" 출력하기, ''도 가능

print("\\ 출력해보자") # \\ : 문장 내에서 \ 출력하기
print("Red Apple\rPine") # \r : 커서를 맨 앞으로 이동
print("Red\bApple")# \b : 백스페이스(한 글자 삭제)
print("Red\tApple")

### 리스트 []
subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)
print(subway.index("조세호")) # 배열 index 반환

subway.append("하하") # 추가
print(subway)

subway.insert(1, "정형돈") # 지정된 index에 추가
print(subway)

subway.pop() # 맨뒤값 꺼내기
print(subway)

subway.append("유재석")
print(subway.count("유재석")) # 같은값 카운트

num_list = [5,4,3,2,1]
num_list.sort() # 내림차순 정렬
print(num_list)

num_list.reverse() # 역순
print(num_list)

num_list.clear() # 모두 삭제
print(num_list)

mix_list = ["조세호", 20, True]
num_list = [5,4,3,2,1]
print(mix_list)

num_list.extend(mix_list)#  리스트 확장
print(num_list)

### 사전(딕셔너리)
cabinet = {3:"유재석", 100:"김태호"} # 키와 값으로 구성된다. 흡사 json
print(cabinet[3]) # 값이 없는경우엔 프로그램 종료됨
print(cabinet.get(3)) # 값이 없는경우엔 none이 출력되고 실행 유지
print(cabinet.get(5), "대체") # 키에 대한 값이 없을 경우 대체할 값

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

cabinet["A-3"] = "김종국" # 기존값 업데이트
cabinet["C-20"] = "조세호" # 값 추가
print(cabinet)

del cabinet["A-3"] # 값 삭제
print(cabinet)

print(cabinet.keys()) # key들만 출력
print(cabinet.values()) # 값들만 출력
print(cabinet.items()) # key, value 쌍으로 출력

cabinet.clear # 전체삭제
print(cabinet)

### 튜플 (속도가 list보다 빠름, 값추가 & 변경불가)
menu = ("돈까스", "치즈까스")
print(menu[0])

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

### 집합 (set)
# 중복 불가, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) #위와 같은 set표현 방식

# 교집합 (java와 python을 모두 할수있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊어버렸어요
java.remove("김태호")
print(java)
 
### 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))