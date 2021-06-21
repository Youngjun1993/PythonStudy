from random import *

## random 사용
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다")
 
## 싸이트별 랜덤 비밀번호 생성하기
url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")] # my_str[0:5]와 같다.

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))