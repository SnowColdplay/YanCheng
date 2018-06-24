import pandas as pd
import numpy as np
import datetime
import lightgbm as lgb
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings("ignore")

def week(x):
    aaa=0
    bbb=[0]
    ccc=x[0]
    for i in range(1,len(x)):
        if  x[i]<=ccc:
            aaa+=1
        ccc=x[i]
        bbb.append(aaa)
    return bbb

def hol():
    hol_2013 = []
    for i in range(1, 4):
        hol_2013.append([str('2013-01-0') + str(i), "元旦"])  # 元旦
    hol_2013.append([str('2013-02-09'), "春节"]);
    hol_2013.append([str('2013-02-10'), "春节"])
    for i in range(1, 6):
        hol_2013.append([str('2013-02-1') + str(i), "春节"])  # 春节
    for i in range(4, 7):
        hol_2013.append([str('2013-04-0') + str(i), "清明"])  # 清明
    hol_2013.append([str('2013-04-29'), "劳动节"]);
    hol_2013.append([str('2013-04-30'), "劳动节"]);
    hol_2013.append([str('2013-05-01'), "劳动节"])  # 劳动节
    for i in range(0, 3):
        hol_2013.append([str('2013-06-1') + str(i), "端午"])  # 端午
    hol_2013.append([str('2013-09-19'), "中秋"])
    for i in range(0, 2):
        hol_2013.append([str('2013-09-2') + str(i), "中秋"])  # 中秋
    for i in range(1, 8):
        hol_2013.append([str('2013-10-0') + str(i), "国庆"])  # 国庆

    hol_2014 = []
    hol_2014.append([str('2014-01-01'), "元旦"])  # 元旦
    hol_2014.append([str('2014-01-30'), "春节"]); #除夕
    hol_2014.append([str('2014-01-31'), "春节"]);
    for i in range(1, 7):
        hol_2014.append([str('2014-02-0') + str(i), "春节"])  # 春节
    for i in range(5, 8):
        hol_2014.append([str('2014-04-0') + str(i), "清明"])  # 清明
    for i in range(1, 4):
        hol_2014.append([str('2014-05-0') + str(i), "劳动节"])  # 五一
    hol_2014.append([str('2014-05-31'), "端午"])
    for i in range(1, 3):
        hol_2014.append([str('2014-06-0') + str(i), "端午"])  # 端午
    for i in range(6, 9):
        hol_2014.append([str('2014-09-0') + str(i), "中秋"])  # 中秋
    for i in range(1, 8):
        hol_2014.append([str('2014-10-0') + str(i), "国庆"])  # 国庆

    hol_2015 = []
    for i in range(1, 4):
        hol_2015.append([str('2015-01-0') + str(i), "元旦"])  # 元旦
    for i in range(8, 10):
        hol_2015.append([str('2015-02-1') + str(i), "春节"])  # 春节
    for i in range(0, 5):
        hol_2015.append([str('2015-02-2') + str(i), "春节"])  # 春节
    for i in range(4, 7):
        hol_2015.append([str('2015-04-0') + str(i), "清明"])  # 清明
    for i in range(1, 4):
        hol_2015.append([str('2015-05-0') + str(i), "劳动节"])  # 五一
    for i in range(0, 3):
        hol_2015.append([str('2015-06-2') + str(i), "端午"])  # 端午
    for i in range(3, 6):
        hol_2015.append([str('2015-09-0') + str(i), "胜利日"])  # 胜利日
    hol_2015.append([str('2015-09-26'), "中秋"])  # 中秋
    hol_2015.append([str('2015-09-27'), "中秋"])  # 中秋
    for i in range(1, 8):
        hol_2015.append([str('2015-10-0') + str(i), "国庆"])  # 国庆

    hol_2016 = []
    for i in range(1, 4):
        hol_2016.append([str('2016-01-0') + str(i), "元旦"])  # 元旦
    for i in range(7, 10):
        hol_2016.append([str('2016-02-0') + str(i), "春节"])  # 春节
    for i in range(0, 4):
        hol_2016.append([str('2016-02-1') + str(i), "春节"])  # 春节
    for i in range(2, 5):
        hol_2016.append([str('2016-04-0') + str(i), "清明"])  # 清明
    hol_2016.append(["2016-04-30", "劳动节"])
    for i in range(1, 3):
        hol_2016.append([str('2016-05-0') + str(i), "劳动节"])  # 五一
    hol_2016.append([str('2016-06-09'), "端午"])
    for i in range(0, 2):
        hol_2016.append([str('2016-06-1') + str(i), "端午"])  # 端午

    for i in range(5, 8):
        hol_2016.append([str('2016-09-1') + str(i), "中秋"])  # 中秋
    for i in range(1, 8):
        hol_2016.append([str('2016-10-0') + str(i), "国庆"])  # 国庆

    hol_2017 = []
    hol_2017.append([str('2016-12-31'), "元旦"])
    for i in range(1, 3):
        hol_2017.append([str('2017-01-0') + str(i), "元旦"])  # 元旦
    for i in range(7, 10):
        hol_2017.append([str('2017-01-2') + str(i), "春节"])  # 春节
    hol_2017.append(['2017-1-30', '春节'])
    hol_2017.append(['2017-1-31', '春节'])
    for i in range(1, 3):
        hol_2017.append([str('2017-02-0') + str(i), "春节"])  # 春节
    for i in range(2, 5):
        hol_2017.append([str('2017-04-0') + str(i), "清明"])  # 清明
    hol_2017.append([str('2017-04-29'), "劳动节"]);
    hol_2017.append([str('2017-04-30'), "劳动节"]);
    hol_2017.append([str('2017-05-01'), "劳动节"]);  # 五一
    hol_2017.append([str('2017-05-30'), "端午"])
    for i in range(8, 10):
        hol_2017.append([str('2017-05-2') + str(i), "端午"])  # 端午
    for i in range(1, 9):
        hol_2017.append([str('2017-10-0') + str(i), "国庆"])  # 国庆(国庆之后的一天，target很大)

    dfxz = pd.concat([pd.DataFrame(hol_2013), pd.DataFrame(hol_2014), pd.DataFrame(hol_2015), pd.DataFrame(hol_2016),
                      pd.DataFrame(hol_2017)], ignore_index=True)
    dfxz.columns = ["date_time", "holiday_name"]
    dfxz["date_time"] = pd.to_datetime(dfxz.date_time, format="%Y-%m-%d")
    return dfxz

def work_weekend():
    year = 2013
    work_weekend = []
    for i in range(5, 7):
        work_weekend.append([str(year) + str('-01-0') + str(i),'元旦周末'])  # 元旦
    for i in range(6, 8):
        work_weekend.append([str(year) + str('-02-1') + str(i),'春节周末'])  # 春节
    work_weekend.append([str(year) + str('-04-07'),'清明周末'])  # 清明节
    for i in range(7, 9):
        work_weekend.append([str(year) + str('-04-2') + str(i),'劳动周末'])  # 劳动节
    for i in range(8, 10):
        work_weekend.append([str(year) + str('-06-0') + str(i),'端午周末'])  # 端午节
    work_weekend.append([str(year) + str('-09-22'),'中秋周末'])  # 中秋节
    work_weekend.append([str(year) + str('-09-29'), '国庆周末'])
    work_weekend.append([str(year) + str('-10-12'), '国庆周末'])
    work_weekend_2013 = work_weekend
    year = 2014
    work_weekend = []
    work_weekend.append([str(year) + str('-01-26'), '春节周末'])
    work_weekend.append([str(year) + str('-02-08'), '春节周末'])
    work_weekend.append([str(year) + str('-05-04'),'劳动周末'])  # 劳动节
    work_weekend.append([str(year) + str('-09-28'),'国庆周末']);
    work_weekend.append([str(year) + str('-10-11'),'国庆周末'])  # 国庆节
    work_weekend_2014 = work_weekend
    year = 2015
    work_weekend = []
    work_weekend.append([str(year) + str('-01-04'),'元旦周末'])  # 元旦
    work_weekend.append([str(year) + str('-02-15'),'春节周末']);
    work_weekend.append([str(year) + str('-02-28'),'春节周末'])  # 春节
    work_weekend.append([str(year) + str('-09-06'),'胜利日周末']);  # 胜利日
    work_weekend.append([str(year) + str('-10-10'),'国庆周末']);  # 国庆
    work_weekend_2015 = work_weekend

    year = 2016
    work_weekend = []
    work_weekend.append([str(year) + str('-02-06'),'春节周末']);
    work_weekend.append([str(year) + str('-02-14'),'春节周末'])  # 春节
    work_weekend.append([str(year) + str('-06-12'),'端午周末']);  # 端午
    work_weekend.append([str(year) + str('-09-18'),'中秋周末']);  # 中秋
    work_weekend.append([str(year) + str('-10-08'),'国庆周末']);
    work_weekend.append([str(year) + str('-10-09'),'国庆周末'])  # 国庆节
    work_weekend_2016 = work_weekend

    year = 2017
    work_weekend = []
    work_weekend.append([str(year) + str('-01-22'),'春节周末']);
    work_weekend.append([str(year) + str('-02-04'),'春节周末'])  # 春节
    work_weekend.append([str(year) + str('-04-01'),'清明周末']);  # 清明
    work_weekend.append([str(year) + str('-05-27'),'端午周末']);  # 端午
    work_weekend.append([str(year) + str('-09-30'),'中秋周末']);
    work_weekend_2017 = work_weekend

    dfxzz = pd.concat([pd.DataFrame(work_weekend_2013), pd.DataFrame(work_weekend_2014), pd.DataFrame(work_weekend_2015), pd.DataFrame(work_weekend_2016),
                      pd.DataFrame(work_weekend_2017)], ignore_index=True)
    dfxzz.columns = ["date_time", "work_weekend_name"]
    dfxzz["date_time"] = pd.to_datetime(dfxzz.date_time, format="%Y-%m-%d")
    return dfxzz

def real_time(data):
    dfxz=hol()
    dfxzz=work_weekend()
    df=data
    df["week_"] = week(df.day_of_week)
    df["new_date"] = df.apply(lambda x: x.week_ * 7 + x.day_of_week, axis=1)
    df["date_time"] = df.new_date.map(lambda x: int(x) * pd.Timedelta(1, "D") + datetime.date(2012, 12, 30))
    df["date_time"] = pd.to_datetime(df.date_time, format="%Y-%m-%d")
    df["month"] = df.date_time.dt.month
    df["day_of_month"] = df.date_time.dt.day
    df["year"] = df.date_time.dt.year
    df["day_of_year"] = df.date_time.dt.dayofyear
    dfzx = pd.read_excel("input/公农历转换.xlsx", header=None)
    dfzx.columns = ["date_time", "china_date"]
    dfzx["date_time"] = pd.to_datetime(dfzx.date_time, format="%Y-%m-%d")
    dfzx["china_year"] = dfzx.china_date.map(lambda x: int(x[:4]))
    dfzx["china_month"] = dfzx.china_date.map(lambda x: x[5:])
    dfzx["china_day"] = dfzx.china_month.map(lambda x: int(x[x.find("/") + 1:]))
    dfzx["china_month"] = dfzx.china_month.map(lambda x: int(x[:x.find("/")]))
    dfzx["china_month"] = dfzx.apply(lambda x: x.china_month - 1 if (x.china_year == 2012) or (x.china_year == 2014 and x.china_month > 9) else x.china_month, axis=1)
    dfzx["china_month_day"] = dfzx.apply(lambda x: "-".join([str(x.china_month), str(x.china_day)]), axis=1)
    dfzx = pd.merge(dfzx, dfxz, on="date_time", how="left")
    df = pd.merge(df, dfzx, on="date_time", how="left")
    df["month_day"] = df.apply(lambda x: "-".join([str(x.month), str(x.day_of_month)]), axis=1)
    df["holiday"] = (df.new_date - df.new_date.shift(1)).fillna(1) #当天之前车管所放假几天
    df["holiday"]=df["holiday"]-1
    df["holiday1"] = df.holiday_name.notnull().astype(int)
    df= pd.merge(df, dfxzz, on="date_time", how="left")
    df["work_weekend"] = df.work_weekend_name.notnull().astype(int)
    df['timestamp'] = (df['date'].map(lambda x: x * 24 * 3600)-24*3600)
    df['last_year'] = df.apply(lambda x: 2013 if x.year == 2013 else x.year - 1, axis=1)

    df['date_time1'] = df.apply(lambda x: x.date_time.strftime('%Y-%m-%d'), axis=1)
    year = [2013, 2014, 2015, 2016, 2017]
    work_weekend_1 = []
    shijian = []
    for y in year:
        df1 = df[df['year'] == y]
        holi = ['元旦', '春节', '清明', '劳动节', '端午', '中秋', '国庆', '胜利日']
        # holi=['元旦']
        for h in holi:
            df2 = df1[df1['work_weekend_name'] == h + '周末']
            df3 = df1[df1['holiday_name'] == h]
            if len(df3):
                a = list(df2.date_time1.values)
                b = list(df2.date.values)
                c = list(df3.date_time1.values)
                for i in range(len(a)):
                    if a[i] > max(c):       #节假日之前标记为1，节假日之后标记为2
                        work_weekend_1.append(1)
                        shijian.append(b[i])
                    else:
                        work_weekend_1.append(2)
                        shijian.append(b[i])
    df_w = pd.concat([pd.DataFrame(work_weekend_1), pd.DataFrame(shijian)], axis=1, ignore_index=True)
    df_w.columns = ["work_weekend_1", "date"]
    df = pd.merge(df, df_w, on='date', how='left')
    df['work_weekend_1'] = df['work_weekend_1'].fillna(0)
    del df['date_time1']

    df['holiday_next_day1'] = (df.holiday1 - df.holiday1.shift(1).fillna(0)).map(lambda x: 1 if x == -1 else 0)
    df['holiday_next_name1']=np.nan
    for i in df[df.holiday_next_day1 ==1].index:
        df.holiday_next_name1[i] = df['holiday_name'][i - 1] + str('过后')

    df['holiday_next_day'] = 0
    for i in df[df.holiday_next_name1=='春节过后'].index:
        df.holiday_next_day[(df.index - i < 5) & (df.index - i >= 0)]=df.index - i+1
    for i in df[df.holiday_next_name1 == '元旦过后'].index:
        df.holiday_next_day[(df.index - i < 10) & (df.index - i >= 0)] = df.index - i+1
    for i in df[df.holiday_next_name1 == '清明过后'].index:
        df.holiday_next_day[(df.index - i < 3) & (df.index - i >= 0)] = df.index - i+1
    for i in df[df.holiday_next_name1 == '端午过后'].index:
        df.holiday_next_day[(df.index - i < 2) & (df.index - i >= 0)] = df.index - i+1
    for i in df[df.holiday_next_name1 == '国庆过后'].index:
        df.holiday_next_day[(df.index - i < 10) & (df.index - i >= 0)] = df.index - i+1
    for i in df[df.holiday_next_name1 == '劳动节过后'].index:
        df.holiday_next_day[(df.index - i < 10) & (df.index - i >= 0)] = df.index - i+1
    for i in df[df.holiday_next_name1 == '中秋过后'].index:
        df.holiday_next_day[(df.index - i < 3) & (df.index - i >= 0)] = df.index - i+1

    df['holiday_next_name'] = np.nan
    for i in df[df.holiday_next_name1=='春节过后'].index:
        for j in range(5):
            df.holiday_next_name[i+j]=df['holiday_name'][i - 1] + str('过后')
    for i in df[df.holiday_next_name1 == '元旦过后'].index:
        for j in range(10):
            df.holiday_next_name[i+j] = df['holiday_name'][i - 1] + str('过后')
    for i in df[df.holiday_next_name1 == '清明过后'].index:
        for j in range(3):
            df.holiday_next_name[i+j] = df['holiday_name'][i - 1] + str('过后')
    for i in df[df.holiday_next_name1 == '端午过后'].index:
        for j in range(2):
            df.holiday_next_name[i+j] = df['holiday_name'][i - 1] + str('过后')
    for i in df[df.holiday_next_name1 == '国庆过后'].index:
        for j in range(10):
            df.holiday_next_name[i+j] = df['holiday_name'][i - 1] + str('过后')
    for i in df[df.holiday_next_name1 == '劳动节过后'].index:
        for j in range(10):
            df.holiday_next_name[i+j] = df['holiday_name'][i - 1] + str('过后')
    for i in df[df.holiday_next_name1 == '中秋过后'].index:
        for j in range(3):
            df.holiday_next_name[i+j] = df['holiday_name'][i - 1] + str('过后')
    del df['holiday_next_name1'],df['holiday_next_day1']

    #2014年特殊，2014年元旦就1天(周三）,标记不上holiday next day
    for i in df[(df['date_time']=='2014-01-02')].index:
        df.holiday_next_day[(df.index - i < 10) & (df.index - i >= 0)] = 1
        df.holiday_next_name[(df.index - i < 10) & (df.index - i >= 0)] = '元旦过后'

    #把工作日周末标记为星期8
    df['day_of_week1']=df['day_of_week']
    df['day_of_week1']=df.apply(lambda x: 8 if x.work_weekend_1==1 else 9 if x.work_weekend_1==2 else x.day_of_week1,axis=1)

    #把假期之后的周末单独标记出来
    df['holiday_next_day'] = df.apply(lambda x: -1 if (x.holiday_next_day == 1) & ((x.day_of_week1 == 6) or (x.day_of_week1 == 7)) else x.holiday_next_day, axis=1)
    #df['week_of_month']=df['date_time'].dt.weekofyear

    #向前填充 (春节前一周，国庆前一周）
    df['holiday2']=df.apply(lambda x: 1 if (x.holiday_name=='春节')|(x.holiday_name=='国庆') else 0,axis=1)
    df['holiday_ahead_day1'] = (df.holiday2 - df.holiday2.shift(-1).fillna(0)).map(lambda x: 1 if x == -1 else 0)
    df['holiday_ahead_name1'] = np.nan
    for i in df[df.holiday_ahead_day1 == 1].index:
        df.holiday_ahead_name1[i] = df['holiday_name'][i + 1] + str('之前')
    df['holiday_ahead_day'] = 0
    for i in df[df.holiday_ahead_name1 == '春节之前'].index:
        df.holiday_ahead_day[(i - df.index < 7) & (i - df.index >= 0)] = i - df.index + 1
    for i in df[df.holiday_ahead_name1 == '国庆之前'].index:
        df.holiday_ahead_day[(i - df.index < 7) & (i - df.index >= 0)] = i - df.index + 1

    df['holiday_ahead_name'] = np.nan
    for i in df[df.holiday_ahead_name1 == '春节之前'].index:
        for j in range(7):
            df.holiday_ahead_name[i - j] = df['holiday_name'][i + 1] + str('之前')
    for i in df[df.holiday_ahead_name1 == '国庆之前'].index:
        for j in range(7):
            df.holiday_ahead_name[i - j] = df['holiday_name'][i + 1] + str('之前')
    del df['holiday_ahead_name1'], df['holiday_ahead_day1'],df['holiday2']
    df['holiday_ahead_day'] = df.apply(lambda x: -1 if (x.holiday_ahead_day == 1) & ((x.day_of_week1 == 6) or (x.day_of_week1 == 7)) else x.holiday_ahead_day, axis=1)
    df['holiday_ahead_day'] = df.apply(lambda x: x.holiday_ahead_day if (x.holiday_next_day == 0)&(x.holiday1 == 0) else 0, axis=1)
    df['holiday_ahead_name'] = df.apply(lambda x: x.holiday_ahead_name if (x.holiday_next_day == 0) &(x.holiday1 == 0) else np.nan, axis=1)

    df['day_of_week1']=df.apply(lambda x:x.day_of_week1 if x.holiday1==0 else 10,axis=1)
    #df['count1']=df.apply(lambda x:x.count1 if x.holiday1==0 else x.count1 if (x.holiday1==1)&(x.count1<=80) else np.nan if x.count1==None else 80,axis=1)
    # df['count1'] = df.apply(lambda x: np.nan if x.count1 is None else x.count1 if x.holiday1==0 else x.count1 if (x.holiday1 == 1) & (
    # x.count1 <= 80) else  80, axis=1)
    return df


def ewm(data):
    #正常dow
    data0=data[(data['holiday1']==0)& (data['holiday_next_day'] == 0)& (data['work_weekend'] == 0)&(data['holiday_ahead_day'] == 0)]
    data0=data0.sort_values(by=['month','day_of_week1'] ,ascending=True)
    tmp = data0.groupby(['month','day_of_week1']).count1.shift(1).reset_index()[['count1']].rename(columns={"count1":"ewm_cnt0"})
    tmp=tmp.ewm_cnt0.ewm(alpha=0.2).mean().reset_index()[['ewm_cnt0']].rename(columns={"ewm_cnt0":"ewm_cnt"})
    data00=data0[['date']].reset_index()[['date']]
    data000 = pd.concat([data00, tmp], axis=1, ignore_index=True)
    data000.columns=['date','ewm_cnt']

    #节假日
    data0=data[data['holiday1']==1]
    data0 = data0.sort_values(by=['holiday_name','date'], ascending=True)
    tmp = data0.groupby(['holiday_name']).count1.shift(1).reset_index()[['count1']].rename(columns={"count1": "ewm_cnt0"})
    tmp = tmp.ewm_cnt0.ewm(alpha=0.2).mean().reset_index()[['ewm_cnt0']].rename(columns={"ewm_cnt0": "ewm_cnt"})
    data00=data0[['date']].reset_index()[['date']]
    data001 = pd.concat([data00, tmp], axis=1, ignore_index=True)
    data001.columns=['date','ewm_cnt']

    #节假日之后
    data0=data[data['holiday_next_day']!=0]
    data0 = data0.sort_values(by=['holiday_next_name','holiday_next_day'], ascending=True)
    tmp = data0.groupby(['holiday_next_name','holiday_next_day']).count1.shift(1).reset_index()[['count1']].rename(
        columns={"count1": "ewm_cnt0"})
    tmp = tmp.ewm_cnt0.ewm(alpha=0.2).mean().reset_index()[['ewm_cnt0']].rename(columns={"ewm_cnt0": "ewm_cnt"})
    data00 = data0[['date']].reset_index()[['date']]
    data002 = pd.concat([data00, tmp], axis=1, ignore_index=True)
    data002.columns=['date','ewm_cnt']

    #节假日之前
    data0 = data[data['holiday_ahead_day'] != 0]
    data0 = data0.sort_values(by=['holiday_ahead_name', 'holiday_ahead_day'], ascending=True)
    tmp = data0.groupby(['holiday_ahead_name', 'holiday_ahead_day']).count1.shift(1).reset_index()[['count1']].rename(
        columns={"count1": "ewm_cnt0"})
    tmp = tmp.ewm_cnt0.ewm(alpha=0.2).mean().reset_index()[['ewm_cnt0']].rename(columns={"ewm_cnt0": "ewm_cnt"})
    data00 = data0[['date']].reset_index()[['date']]
    data003 = pd.concat([data00, tmp], axis=1, ignore_index=True)
    data003.columns = ['date', 'ewm_cnt']

    #周末工作日
    # data0 = data[(data['work_weekend'] == 1)&(data['holiday_ahead_day'] == 0)&(data['holiday_next_day'] == 0)]
    #
    data0000=pd.concat([data000,data001,data002,data003])
    data=pd.merge(data,data0000,on='date',how='left')
    data['ewm_cnt']=data['ewm_cnt'].fillna(-999)

    data['hol_ewm']=data.apply(lambda x:x.ewm_cnt if x.holiday1==1 else -500,axis=1)
    return data

def rolling_fun(data,df,group_by_list):
    stats = {'mean': [], 'median': [], 'std': [], 'max': [], 'min': []}
    exp_alphas = [0.1, 0.25, 0.3, 0.5, 0.75]
    stats.update({'exp_{}_mean'.format(alpha): [] for alpha in exp_alphas})

    group_by = group_by_list
    on = 'count1'
    groups = df.groupby(group_by, sort=False)
    for _, group in groups:
        shift = group[on].shift()
        roll = shift.rolling(window=len(group), min_periods=1)
        stats['mean'].extend(roll.mean())
        stats['median'].extend(roll.median())
        stats['std'].extend(roll.std())
        stats['max'].extend(roll.max())
        stats['min'].extend(roll.min())
        for alpha in exp_alphas:
            exp = shift.ewm(alpha=alpha, adjust=False)
            stats['exp_{}_mean'.format(alpha)].extend(exp.mean())

    suffix = '_&_'.join(group_by)
    for stat_name, values in stats.items():
        df['{}_{}_by_{}'.format(on, stat_name, suffix)] = values

    group_by=group_by.append('date')
    data = pd.merge(data, df.drop('count1', axis=1), on=group_by, how='left')
    return data

def rolling(data):

    #正常dow
    data0=data[(data['holiday1']==0)& (data['holiday_next_day'] == 0)& (data['work_weekend'] == 0)]
    df=data0[['month','day_of_week1','date','count1']]
    group_by_list=['month','day_of_week1']
    data=rolling_fun(data,df,group_by_list)

    #节假日
    data0=data[data['holiday1']==1]
    df =data0[['holiday_name','date','count1']]
    group_by_list = ['holiday_name']
    data = rolling_fun(data, df, group_by_list)

    #节假日之后
    data0 = data[data['holiday_next_day'] != 0]
    df = data0[['holiday_next_name', 'date', 'count1']]
    group_by_list = ['holiday_next_name']
    data = rolling_fun(data, df, group_by_list)

    return data


def weather(data):
    wea=pd.read_csv('input\盐城天气_new.csv',header=None,encoding='utf-8')
    wea.columns=['date_time','high','low','weather','wind_direction','wind_power']
    wea["date_time"] = pd.to_datetime(wea.date_time, format="%Y-%m-%d")
    wea['high'] = wea['high'].str[:-1]
    wea['low'] = wea['low'].str[:-1]
    wea['is_rain'] = wea['weather'].apply(lambda x: 1 if '雨' in x else 1 if '雪' in x else 0)
    wea=wea[['date_time','is_rain']]
    data=pd.merge(data,wea,on='date_time',how='left')

    return data

def hol_f(data):
    #一个月有多少正常周末，周末所占比例，效果变差 #车管所假期不管用
    col=['year','month']
    hol_month_cnt = data.groupby(col, as_index=False)['holiday1'].agg({'month_holiday1_sum': np.sum}) #一个月多少法定节假日(不包括周末）
    hol_month_cnt["month_holiday1_last_diff"]=hol_month_cnt.month_holiday1_sum-hol_month_cnt.month_holiday1_sum.shift(1).fillna(0) #与上月节假日差值,下个月差值无用
    data = pd.merge(data, hol_month_cnt, on=col, how='left')
    month_cnt = data.groupby(col, as_index=False)['holiday1'].agg({'month_day_count': np.size}) #一个月有多少天
    data = pd.merge(data, month_cnt, on=col, how='left')
    data['month_hol_prob']=data['month_holiday1_sum']/data['month_day_count'] #法定节假日所占比例
    del data['month_day_count']
    col=['china_year','china_month']
    hol_month_cnt = data.groupby(col, as_index=False)['holiday1'].agg({'cmonth_holiday1_sum': np.sum}) #农历一个月多少法定节假日(不包括周末）,差值无用
    data = pd.merge(data, hol_month_cnt, on=col, how='left')
    return data

def label_f(data):
    from sklearn import preprocessing
    lbl = preprocessing.LabelEncoder()
    data['holiday_name']=data['holiday_name'].fillna('不是假期')
    data['holiday_name'] = lbl.fit_transform(data['holiday_name'])
    data['work_weekend_name'] = data['work_weekend_name'].fillna('正常周末')
    data['work_weekend_name'] = lbl.fit_transform(data['work_weekend_name'])
    data['holiday_next_name'] = data['holiday_next_name'].fillna('不是节假日之后')
    data['holiday_next_name'] = lbl.fit_transform(data['holiday_next_name'])
    data['holiday_ahead_name'] = data['holiday_ahead_name'].fillna('不是节假日之前')
    data['holiday_ahead_name'] = lbl.fit_transform(data['holiday_ahead_name'])
    return data

def remove(data):
    data=data[data['date']!=125]
    data = data[data['date'] != 15]
    #去掉胜利日，和胜利日之后的三天
    # for i in [850,851,852,853,854,855]:
    #     data=data[data['date']!=i]
    # #去掉2013年12月份最后一周
    # for i in range(3, 9):
    #     data = data[~data.date_time.isin(['2013-12-2' + str(i)])]
    # for i in range(0, 2):
    #     data = data[~data.date_time.isin(['2013-12-3' + str(i)])]
    return data


def lgbCV(train,test,seed):
    col = [c for c in train if c not in  ['count1','date_time','date','china_date','china_month_day','month_day',
                                          'week_', 'new_date','holiday_ahead_day1','timestamp',
                                          'china_year','day_of_year','day_of_week','last_month','last_year','work_weekend'
                                           ]]
    X = train[col]
    y = train['count1'].values
    X_tes=test[col]
    y_tes=test['count1'].values
    print('Training LGBM model...')
    lgb0= lgb.LGBMRegressor(
        objective='regression',
        num_leaves=12,
        depth=6,
        learning_rate=0.05,
        seed=seed,
        colsample_bytree=0.9,
        subsample=0.9,
        n_estimators=20000)
    lgb_model = lgb0.fit(X,y, eval_set=[(X_tes,y_tes)],early_stopping_rounds=2000)
    best_iter=lgb_model.best_iteration_
    predictors = [i for i in X.columns]
    feat_imp = pd.Series(lgb_model.feature_importance(), predictors).sort_values(ascending=False)
    print(feat_imp)
    print(feat_imp.shape)
    pred= lgb_model.predict(test[col]).clip(30)
    #print(lgb_model.feature_importance())
    test['pred']=pred
    print('MSE lgb ',mean_squared_error(pred, test['count1']))
    test[['count1','pred','day_of_week','date_time', 'holiday1','year','month']].to_csv('result/result_xianxia1.txt', index=False, sep='\t')
    # import matplotlib.pyplot as plt
    # plt.plot(test['date_time'], test['count1'])
    # plt.plot(test['date_time'], test['pred'])
    # plt.show()
    return best_iter

def sub(train,test,best_iter,i,seed):
    ##'timestamp', 'year', 'china_year'
    col = [c for c in train if c not in  ['count1','date_time','date','china_date','china_month_day','month_day',
                                          'week_', 'new_date','holiday_ahead_day1','timestamp',
                                          'china_year','day_of_year','day_of_week','last_month','last_year','work_weekend',
                                          ]]
    X = train[col]
    y = train['count1'].values
    # print('——————————————————————————————————————————')
    # print(test['optimized_ewm'].value_counts())
    # print(test['optimized_ewm'].unique())
    # print(len(test.optimized_ewm.unique()))
    print('Training LGBM model...')
    lgb0 = lgb.LGBMRegressor(
        objective='regression',
        num_leaves=12,
        depth=6,
        learning_rate=0.05,
        seed=seed,
        colsample_bytree=0.9,
        subsample=0.9,
        n_estimators=best_iter)
    lgb_model = lgb0.fit(X, y, eval_set=[(X, y)])
    pred = lgb_model.predict(test[col]).clip(20)
    test['cnt']=pred
    # done save
    test[['cnt','date','day_of_week']].to_csv('merge_result/result_0222_RE_'+str(seed)+'_'+str(i)+'.txt', index=False,sep='\t')
    #test[['date', 'cnt']].to_csv('result/result_0213.txt', index=False, header=False, sep='\t')
    return pred

def offline(seed):
    print('映射到真实日期')
    train = pd.read_csv("input/train_20171215.txt", sep="\s+")
    test = pd.read_csv("input/test_A_20171225.txt", sep="\s+")
    testB = pd.read_csv("input/test_B_20171225.txt", sep="\s+")
    df = train.groupby(['date', 'day_of_week'], as_index=False)['cnt'].agg({'count1': np.sum})
    df1 = test
    print('映射到真实日期,线下')
    data = pd.concat([df, df1.iloc[1:]], ignore_index=True)
    data = real_time(data)
    data = remove(data)
    data = ewm(data)
    #data = rolling(data)
    data = label_f(data)
    data = weather(data)
    print('线下的train,test')
    DATA = data.loc[:len(df) - 1]
    DATA = DATA[DATA.count1.notnull()]

    train = DATA[DATA['date'] <= 850]  # 2013年1月到2016年4月6日  #722
    test = DATA[DATA['date'] > 850]  # 2015年4月7日到2016年4月7日
    print("线下lgb")
    best_iter=lgbCV(train, test,seed)
    return best_iter

def online(best_iter,i,seed):
    train= pd.read_csv("input/train_20171215.txt", sep="\s+")
    test=pd.read_csv("input/test_A_20171225.txt",sep="\s+")
    testB=pd.read_csv("input/test_B_20171225.txt",sep="\s+")
    df =train.groupby(['date','day_of_week'], as_index=False)['cnt'].agg({'count1': np.sum})
    df1=test
    df2=testB
    print('映射到真实日期,线上')
    data=pd.concat([df.iloc[:-1],df1,df2],ignore_index=True)
    print(data[data.count1.isnull()].shape)
    data=real_time(data)
    data = remove(data)
    data=ewm(data)
    #data=rolling(data)
    data = label_f(data)
    data = weather(data)
    train = data[data.count1.notnull()]
    test = data[data.count1.isnull()]
    print(data[data.count1.isnull()].shape)
    print("线上lgb")
    pred=sub(train, test,best_iter,i,seed)
    return pred

if __name__ == "__main__":
    print('线上取平均')
    j=0
    for seed in [2019,2020,2021,2022,2023,2024,2025,2026,2027,2029]:
        j=j+1
        for i in range(1):
            best_iter=offline(seed)
            pred=online(best_iter,i,seed)
            if (i==0)&(j==1):
                Pred=pred
            else:
                Pred+=pred
    Pred=Pred/(j)

    sub=pd.read_csv("merge_result/result_merge_0218.txt",sep="\s+")
    print(len(Pred))
    print(len(sub))
    del sub['cnt']
    sub['cnt']=Pred
    sub.to_csv('merge_result/result_merge_0223_10_E.txt', index=False, sep='\t')
    #print('线下取平均')

    # print('映射到真实日期')
    # train= pd.read_csv("input/train_20171215.txt", sep="\s+")
    # test=pd.read_csv("input/test_A_20171225.txt",sep="\s+")
    # testB=pd.read_csv("input/test_B_20171225.txt",sep="\s+")
    # df =train.groupby(['date','day_of_week'], as_index=False)['cnt'].agg({'count1': np.sum})
    # df1=test
    # df2=testB
    #
    #
    # print('映射到真实日期,线下')
    # data=pd.concat([df,df1.iloc[1:]],ignore_index=True)
    # data=real_time(data)
    # data = remove(data)
    # data=ewm(data)
    # data=rolling(data)
    # data = label_f(data)
    # data = weather(data)
    # print('线下的train,test')
    # DATA=data.loc[:len(df)-1]
    # DATA=DATA[DATA.count1.notnull()]
    #
    # train=DATA[DATA['date']<=850] #2013年1月到2016年4月6日  #722
    # test=DATA[DATA['date']>850]   #2015年4月7日到2016年4月7日
    # print(train.shape)
    # print(test.shape)
    # print("线下lgb")
    # lgbCV(train, test)

    # print('映射到真实日期,线上')
    # data=pd.concat([df.iloc[:-1],df1,df2],ignore_index=True)
    # data=real_time(data)
    # data = remove(data)
    # data=ewm(data)
    # data=rolling(data)
    # data = label_f(data)
    # data = weather(data)
    # train = data[data.count1.notnull()]
    # test = data[data.count1.isnull()]
    # print(train.shape)
    # print("线上lgb")
    # sub(train, test)





