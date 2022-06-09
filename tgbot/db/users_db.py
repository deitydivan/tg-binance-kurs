import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI



# start bd/ connect and create if does'nt exists
async def postgre_start():
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    if base:
        print('data base connect Ok!')
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
        id text primary key,
        name text,
        timeframe text,
        pair text,
        gets_advice int default 0
        )''')
    
    base.commit()
    cur.close()
    base.close()