import datetime

def ans():
    days_in_month  = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    prefix_sum = [0] * 13
    #prefix_sum[i] - количество дней в первых i месяцах, включая i
    for i in range(1,13):
        prefix_sum[i]+= days_in_month[i-1] + prefix_sum[i-1]
    #print(prefix_sum)

    f_d = [int(i) for i in input().split()]
    s_d = [int(i) for i in input().split()]
    b = datetime.datetime(*f_d)
    datetime.time()


    d = datetime.datetime(*s_d)

    def cnt_days(year_1, month_1,day_1 ,year_2, month_2, day_2):
        days = (year_2-year_1)*365 + prefix_sum[month_2-1] -  prefix_sum[month_1-1]
        return days   - day_1 + day_2

    days = cnt_days(f_d[0], f_d[1], f_d[2], s_d[0], s_d[1], s_d[2])
    time_delta = d - b
    if datetime.time(*s_d[3:]) >=datetime.time(*f_d[3:]):
        print(days, time_delta.seconds, )
    else:
        print(days -1,time_delta.seconds)

ans()