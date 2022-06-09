import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI

async def af_status(userid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    userid = str(userid)
    cur.execute('SELECT * FROM users ')
    users = cur.fetchall()
    answer = False
    for user in users:
        if user[0] == userid:
            answer = True
    base.commit()
    cur.close()
    base.close()
    return answer