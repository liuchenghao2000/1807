year = int(input('请输入年份：'))
month = int(input('请输入月份：'))
day = int(input('请输入日期：'))

months = [0,31,59,90,120,151,181,212,243,273,304]

if 0 < month <12:
    sum = months[month - 1] + day

flag = 0
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    flag = 1

if flag == 1 and month > 2:
    sum += 1 

print('%d.%d.%d是%d年的第%d天'%(year,month,day,year,sum))
