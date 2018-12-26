#输入一个日期 年月日 然后算出来这是这一年的哪一天
#eg:  input 2018 3 18
#     output  77
mou_mod=[[31,28,31,30,31,30,31,31,30,31,30,31],[31,23,31,30,31,30,31,31,30,31,30,31]]
year=int(input())
mou=int(input())
day=int(input())
i=0
num = 0
if ( year % 4 == 0 and year % 100 != 0 ) or year % 400 ==0 :
    i=1
    for j in range(mou-1):
        
        num += mou_mod[i][j]
        
else:
     for j in range(mou-1):
         
        num += mou_mod[i][j]
        
num += day
print(num)
