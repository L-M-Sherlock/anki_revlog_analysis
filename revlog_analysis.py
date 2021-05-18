import pandas as pd
from datetime import timedelta

df = pd.read_csv('anki_revlog.csv')

df = df.drop(df[df['ease'] == 0].index)

df['raw_date'] = pd.to_datetime(df['id'], unit='ms')
df['raw_date'] = df['raw_date'].dt.tz_localize('UTC').dt.tz_convert('Asia/Shanghai')

df['date'] = df['raw_date'].map(lambda x: x - timedelta(days=1) if x.hour < 5 else x)
df['date'] = df['date'].dt.floor('D')
df.drop(df[df['date'].dt.year < 2017].index, inplace=True)
df.drop_duplicates(['cid', 'date'], keep='first', inplace=True)

df.sort_values(by=['cid', 'id'], inplace=True)
df['used_ivl'] = df.date.diff().dt.days
df.loc[df['type'] == 0, 'used_ivl'] = 0
df.drop_duplicates(['cid', 'used_ivl'], keep='first', inplace=True)

for cid in df.loc[df['used_ivl'] < 0, 'cid']:
    df.drop(df[df.cid == cid].index, inplace=True)

df['feedback'] = df['ease'].map({1: 0, 2: 1, 3: 1, 4: 1})
del df['id']
del df['raw_date']
del df['date']
df['repeat_long'] = 1
df['fb_history'] = ""
df['ivl_history'] = ""


def get_feature(x):
    for idx, log in enumerate(x.itertuples()):
        if idx == x.shape[0] - 1:
            break
        x.iloc[idx + 1, 6] = x.iloc[idx, 6] + 1
        x.iloc[idx + 1, 8] = x.iloc[idx, 8] + str(int(x.iloc[idx, 4])) + ","
        if log.feedback == 1:
            x.iloc[idx + 1, 7] = x.iloc[idx, 7] + "1"
        else:
            x.iloc[idx + 1, 7] = x.iloc[idx, 7] + "0"
    return x


df = df.groupby('cid', as_index=False).apply(get_feature)
df.to_csv('revlog_history.tsv', sep="\t", index=False)
