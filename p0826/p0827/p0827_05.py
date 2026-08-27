import datetime

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print("{:02d}월".format(now.month))
print("{:02d}분".format(now.minute))
print("{:02d}초".format(now.second))
# 2026년 8월 27일 22시 57분 20초
print(now)
f_date = now.strftime("%y년%m월%d일 %H시%M분%S초")
print(f_date)

# 월 출력하는데, 1,2,3....9월 01월,02월,03월,10월,11월,12월





# # format
# # 123 -> 5자리 빈공백 0으로 채워서 출력하시오.
# print("{:015,d}".format(123456789))
# print("{:02d}.format(12))