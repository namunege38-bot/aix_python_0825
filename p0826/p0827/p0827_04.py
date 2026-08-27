import random
import datetime #현재시간을 가져오는 클래스선언
# from datetime import datetime

# 1-6월까지는 상반기
# 7-12월까지는 하반기
# 8월
# 현재월을 datetime함수를 사용해서 검색한 다음
# 상반기,하반기인지 출력하시오.

# 날짜함수를 사용해서 월을 변수에 저장을 한후
# 비교
# 출력

# 
now = datetime.datetime.now()
month = now.month
if month>=7:
    print("{}월 : 하반기입니다.".format(month))
else:
    print("{}월 : 상반기입니다.".format(month))



# # 현재시간
# now = datetime.datetime.now()
# print("전체:",now)       #전체시간
# print("년도:",now.year)  #년도
# print("월:",now.month) #월
# print("일:",now.day)   #일
# print("시:",now.hour)  #시
# print("분:",now.minute) #분
# print("초:",now.second) #초

# # 2026년 8월 27일 11시 12분 10초
# print("{}년{}월{}일){}시{}분{}초".format(\
#       now.year,now.month,now.day,now.hour,now.minute,now.second))
# format 함수


# year : 2026
# month : 8
# day : 27
# hour : 11
# minute : 12
# second : 10

# print("{}년 {}월 {}일 {}시 {}분 {}초",format(year,month,day,hour,minute,second))