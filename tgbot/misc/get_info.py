import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI



async def get_profile(userid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (str(userid),)
    cur.execute('SELECT * FROM users WHERE id = %s',data)
    user = cur.fetchone()
    name = user[1]
    gets_advice = user[4]
    base.commit()
    cur.close()
    base.close()
    
    return name, gets_advice