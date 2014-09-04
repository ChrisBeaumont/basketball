"""
Data comes from
http://vorped.com/bball/index.php/

By copying the shots js variable on one of the shot charts pages
"""

from json import load
import pandas as pd
import numpy as np

df = pd.DataFrame(load(open('duncan_2013.json')))
df['player'] = 'Tim Duncan'

d = pd.DataFrame(load(open('leonard_2013.json')))
d['player'] = 'Kawhi Leonard'
df = pd.concat([df, d], ignore_index=True)

d = pd.DataFrame(load(open('lebron_2013.json')))
d['player'] = 'Lebron James'
df = pd.concat([df, d], ignore_index=True)

df = df.convert_objects(convert_numeric=True)

df['is_home'] = df.ish
df['margin'] = df.mgn
df['period'] = df.p
df['shot_made'] = df.shm
df['game_id'] = np.searchsorted(df.gid.unique(), df.gid)

shots = np.array(['', 'Tip', 'Dunk', 'Jump Shot',
                 'Special Jump Shot', 'Alleyoop', 'Hook', 'Layup'])
df['shot_type'] = shots[df['st'].values]

cols = ['player', 'game_id', 'is_home', 'margin', 'period', 'shot_made',
        'shot_type', 'x', 'y']
df = df[cols]

df.to_csv('2013_player_shots.csv', index=False)
