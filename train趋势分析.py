import pandas as pd
import numpy as np
import datetime
import warnings
warnings.filterwarnings("ignore")

df=pd.read_csv("input/fusai_train_20180227.txt",sep="\s+")
# df0=df.groupby(["date","day_of_week"],as_index=False).cnt.sum()
# df1=pd.read_csv("input/test_A_20171225.txt",sep="\s+")
# df2=pd.read_csv("input/test_B_20171225.txt",sep="\s+")
# df=pd.concat([df0.iloc[:-1],df1,df2],ignore_index=True)
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
df["week_"]=week(df.day_of_week)
def holiday(x):
    aaa=0
    bbb=[0]
    ccc=x[0]
    for i in range(1,len(x)):
        if  x[i]<=ccc:
            bbb.append(x[i]-ccc+7)
        else:
            bbb.append(0)
        ccc=x[i]
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
        work_weekend.append([str(year) + str('-04-2') + str(i),'劳动节周末'])  # 劳动节
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
    work_weekend.append([str(year) + str('-05-04'),'劳动节周末'])  # 劳动节
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

if __name__ == "__main__":
    print('映射到真实日期')
    train = pd.read_csv("input/fusai_train_20180227.txt", sep="\s+")
    testA= pd.read_csv("input/fusai_test_A_20180227.txt", sep="\s+")
    testB=pd.read_csv("input/fusai_test_B_20180227.txt", sep="\s+")
    df=pd.concat([train,testA,testB])
    data = df.groupby(['date', 'day_of_week'], as_index=False).cnt.sum()
    print('映射到真实日期,线下')
    data=real_time(data)
    del data['day_of_week'], data['cnt']
    data = pd.merge(train, data, on='date', how='left')
    data=data[['brand','cnt','date_time']]
    print(data[(data['brand']==8)&(data['date_time']<'2014-10-30')])
    #import matplotlib.pyplot as plt
    # data.set_index(['date_time','brand']).cnt.unstack().plot()
    # print(data)
    # plt.show()
    print('----------------------------------------------------------------------------------')
    # data0=data[data['brand']==1]
    # data0.set_index(['date_time']).cnt.plot()
    # plt.show()
    #
    #
    # data0=data[data['brand']==2]
    # data0.set_index(['date_time']).cnt.plot()
    # plt.show()
    #
    # data0 = data[data['brand'] == 3]
    # data0.set_index(['date_time']).cnt.plot()
    # plt.show()
    #
    # data0 = data[data['brand'] == 4]
    # data0.set_index(['date_time']).cnt.plot()
    # plt.show()
    #
    # data0 = data[data['brand'] == 5]
    # data0.set_index(['date_time']).cnt.plot()
    # plt.show()
    #
    # data0 = data[data['brand'] == 6]
    # data0.set_index(['date_time']).cnt.plot()
    # plt.show()
    #
    # data0 = data[data['brand'] == 7]
    # data0.set_index(['date_time']).cnt.plot()
    # plt.show()
    #
    # data0 = data[data['brand'] == 8]
    # data0.set_index(['date_time']).cnt.plot()
    # plt.show()
    #
    # data0 = data[data['brand'] == 9]
    # data0.set_index(['date_time']).cnt.plot()
    # plt.show()
    #
    # data0 = data[data['brand'] == 10]
    # data0.set_index(['date_time']).cnt.plot()
    # plt.show()
    "------------------------------------------------------------------------------------------------------------"
    # print(data[data['date']==1107])
    # data=data[['date_time','cnt','holiday1']]
    # print(data)
    #print(data[data['holiday1']==1])
    # data['haha']=data.apply(lambda x:1 if (x.holiday_ahead_day!=0)&(x.holiday_next_day!=0) else 0,axis=1)
    # print(data[data['haha']==1])

# df["holiday"]=holiday(df.day_of_week)
# df["new_date"]=df.apply(lambda x:x.week_*7+x.day_of_week,axis=1)
# df["date_time"]=df.new_date.map(lambda x:int(x)*pd.Timedelta(1,"D")+datetime.date(2012,12,30))
# df["date_time"]=pd.to_datetime(df.date_time,format="%Y-%m-%d")
# df["month"]=df.date_time.dt.month
# df["day_of_month"]=df.date_time.dt.day
# df["year"]=df.date_time.dt.year
# df["day_of_year"]=df.date_time.dt.dayofyear
# df['year']=df.apply(lambda x: x.year if x.year!=2017 else 2016,axis=1)
#
# for i in range(3,9):
#     df=df[~df.date_time.isin(['2013-12-2'+str(i)])]
# for i in range(0,2):
#     df = df[~df.date_time.isin(['2013-12-3' + str(i)])]

#print(df.loc[405])

#print(df[df['date_time']>='2015-05-01'])



