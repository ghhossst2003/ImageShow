# coding = "utf-8"
import time
import uuid

from hashlib import md5
import database

uid_session = {}


@database.select(database.db_pool)
def get_session_from_db(cursor):
    sql = "select uid, session from cs_session"
    cursor.execute(sql)
    return cursor.fetchall()


@database.update(database.db_pool)
def save_session_to_db(cursor, uid, session):
    timestamp = int(time.time()*1000)
    sql = "replace into cs_session (uid, session, timestamp) value (%d, '%s', %d)" %(
        uid, session, timestamp)
    cursor.execute(sql)


def init_session():
    sessions = get_session_from_db()
    for session in sessions:
        uid_session[session['uid']] = session['session']


def get_md5(info):
    m = md5()
    m.update(info.encode('utf-8'))
    return m.hexdigest()


def create_session(uid):
    u = uuid.uuid1().hex
    session = get_md5(u)
    uid_session[uid] = session
    save_session_to_db(uid, session)
    return session

