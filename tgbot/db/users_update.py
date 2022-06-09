import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI



async def reg_user(userid, name):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, name)
    cur.execute('INSERT INTO users (id, name)  VALUES (%s,%s)', data)
    print('user was successfully created')
    base.commit()
    cur.close()
    base.close()
    

async def add_set(timeframe, pair,userid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (timeframe, pair,str(userid))
    cur.execute('UPDATE users SET timeframe = %s, pair = %s WHERE id = %s', data)
    base.commit()
    cur.close()
    base.close()
    
    
async def update_counter(userid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (str(userid),)
    cur.execute('UPDATE users SET gets_advice = gets_advice + 1 WHERE id = %s', data)
    base.commit()
    cur.close()
    base.close()