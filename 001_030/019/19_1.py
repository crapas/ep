leap = {}
for i in range(1900, 2001):
    leap[i] = False
    if i % 4 == 0:
        leap[i] = True
    leap[1900] = False

day1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(sum(day1))
print(sum(day2))

sunday_cnt = 0
md = 2
for i in range(1901, 2001):
    if leap[i]:
        day = day2
    else:
        day = day1 
    for j in day:
        if md % 7 == 0:
            sunday_cnt += 1
        md += j

print(sunday_cnt)
# 1900. 1. 1 -> mon
# 1901. 1. 2 -> tue
# 매년 1월 1일이 일요일 -> 29일 일요일
# 매년 1월 2일이 일요일 -> 30일 일요일 -> 1월 1일은 토요일
# 매년 1월 3일이 일요일 -> 31일 일요일 -> 1월 1일은 금요일
# 즉 매년 1월 1일이 금, 토, 일이면 5를 더하고
# 매년 1월 1일이 월, 화, 수, 목이면 4를 더하고

