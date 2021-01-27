# Pandas Notes
Author: Maggie Jacoby<br>
Date: January 2021


### Note:
For bringing up an interactive console outside jupyter (helpful for copying to output)

```%qtconsole```

***
### Code for creating a toy df 

look here too: https://realpython.com/python-pandas-tricks/#2-make-toy-data-structures-with-pandas-testing-module

```python
import pandas as pd
import numpy as np

ind = pd.Index([pd.Timestamp('2019-03-17'), 
                pd.Timestamp('2019-03-18'), 
                pd.Timestamp('2019-03-20'),
                pd.Timestamp('2019-03-21'),
                pd.Timestamp('2019-03-22'),
                pd.Timestamp('2019-03-24'),
                pd.Timestamp('2019-03-25')])
data = {'col':[25,25,24,3,25,24, np.nan]}
df = pd.DataFrame(data, ind)
```

```
             col
2019-03-17  25.0
2019-03-18  25.0
2019-03-20  24.0
2019-03-21   3.0
2019-03-22  25.0
2019-03-24  24.0
2019-03-25   NaN
```

### Make a pandas range of dates

```python
def make_date_range(day1, dayn = None, t1 = '0000', tn = '2359', f='10s'):
    range_start = str(day1 + ' ' + t1[0:2] + ':' + t1[2:4] + ':00')
    range_end = str(day1 + ' ' + tn[0:2] + ':' + tn[2:4] + ':50')
    date_range = pd.date_range(start=range_start, end=range_end, freq=f)
    return date_range   

day_one = make_date_range(day1 = '2019-03-17')
```

## Modifying Dataframes

### Change value with .loc


```python
df.loc[df.rh_percent > limit, 'rh_percent'] = np.NaN
```

replaces all values in  ```df['rh_percent']``` that are greater than ```limit``` with ```np.NaN``` 

### Drop or replace values

drop the last 24 rows of data from the df or series `Baseline`
```python
Baseline = Baseline.drop(Baseline.tail(24).index)
```

drop particular columns:
```python
df = df.drop(columns = ['str_datetime', 'time'])
```

or:
```python
df.drop(columns = ['str_datetime', 'time'], inplace=True)
```

or, get a subset of a df, without certain columns
```python
    skip_cols = ['day', 'hr_min_sec', 'hub', 'occupied']
    df[df.columns.difference(skip_cols)]
```

### Subsetting Dataframes

```python
gt_day = groundTruth.loc[groundTruth['day'] == day]
```

***
## Combining dataframes
(join/concat/merge)


#### Join together different columns, when indices are the same

Includes all indices ("outer" merge) - this does for a number of dfs
```python
dfs = []
for hub in hubs:
    hub_df = ...
    dfs.append(hub_df)
df = pd.concat(dfs, axis=1)
```
handy to add:
```python
df = df.sort_index()
df = df.fillna(0)
```

***
### take a string datetime column and create dates and times

```python
df['date'] = df.timestamp
df['date'] = pd.to_datetime(df['date']) 
df.insert(loc=0, column='day', value=df['date'].dt.date)
df.insert(loc=1, column='hr_min_sec', value=df['date'].dt.time)
df.insert(loc=2, column='hub', value=hub)
print(df)
df.drop(columns=['date', 'timestamp'], inplace=True)
```