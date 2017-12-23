# /Users/Indra/anaconda3/envs/Default/bin/python
import sqlite3
import json
from datetime import datetime
timeframe = '2015-05'
sql_transaction = []
connection = sqlite3.connect(timeframe + '.db')
c=connection.cursor()
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS parent_reply (parent_id TEXT PRIMARY KEY,
    comment_id TEXT UNIQUE,parent TEXT,comment TEXT,subreddit TEXT,unix INT,score INT)""")
def format_data(data):
    data = data.replace('\n',' newlinechar ').replace('\r',' newlinechar ').replace('"',"'")
    return data

if _name_=='_main_':
    create_table()
    row_counter = 0
    paired_rows = 0

    with open('J:/chatdata/reddit_data/{}/RC_{}'.format(timeframe.split('-')[0],timeframe), buffering=1000) as f:
        for row in f:
            row_counter += 1
            row = json.loads(row)
            parent_id = row['parent_id']
            body = format_data(row['body'])
            created_utc = row['created_utc']
            score = row['score']
            comment_id = row['name']
            subreddit = row['subreddit']
            parent_data = find_parent(parent_id)
            # maybe check for a child, if child, is our new score superior? If so, replace. If not...