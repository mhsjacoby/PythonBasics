import os
import json
import pandas as pd


def mylistdir(directory, bit='', end=True):
    filelist = os.listdir(directory)

    if end:
        dir_list = [
            x for x in filelist if x.endswith(f'{bit}') 
            and not x.endswith('.DS_Store') 
            and not x.startswith('Icon')
            ]

    else:
        dir_list = [
            x for x in filelist if x.startswith(f'{bit}') 
            and not x.endswith('.DS_Store') 
            and not x.startswith('Icon')
            ]

    return dir_list
        

def make_storage_directory(target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    return target_dir


def get_date_list(read_file, H_num):

    with open(read_file) as f:
        all_homes = json.load(f)
    
    home_st = all_homes[H_num]
    all_days = []

    for st in home_st:
        start, end = st[0], st[1]
        pd_days = pd.date_range(start=start, end=end).tolist()
        days = [d.strftime('%Y-%m-%d') for d in pd_days]
        all_days.extend(days)

    return all_days