import pandas as pd

data1 = pd.read_csv('startup_users_visits.csv')

data1["date"] = pd.to_datetime(data1["date"])

print(data1)

"""
data = {
    'user_id': pd.Series(dtype='float64'),
    'date_start': pd.Series(dtype='datetime64'),
    'date_expired': pd.Series(dtype='datetime64'),
    'pay': pd.Series(dtype='bool'),
    'pay_in_time': pd.Series(dtype='bool')
}
df = pd.DataFrame(data)
"""
def expired_date():
    pass
res = data1.pivot_table(['user_id'], aggfunc=expired_date, fill_value = 0)

