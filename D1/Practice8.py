#연월일 달력 
T=int(input())
for tc in range(1,T+1):
    date = input()
    # if date[4:6] in ["01","02","03","05","07","08","10","12"]:
    #     if date[6:8] in ""
        #여기서 막혔는데(일일이 다 적어야 할까? 에서)
        # => 해결방법 딕셔너리
    date_dic = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    year = date[0:4]
    month=date[4:6]
    day=date[6:]
    if 0<int(month)<13 and int(day)<=date_dic[int(month)]:
        print(f"#{tc} {year}/{month}/{day}")
    else:
        print(f"#{tc} -1")