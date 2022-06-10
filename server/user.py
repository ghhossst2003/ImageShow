# coding = "utf-8"

from system_exception import UsersException
import json
import database
import session


def login(username, password):
    userinfo = get_userinfo_from_db(username)
    if userinfo is None:
        raise UsersException("username or password don't correct!")
    if is_password_correct(password, userinfo.get('password')) is False:
        raise UsersException("username or password don't correct!")
    if user_status(userinfo.get('status')) is False:
        raise UsersException("user's status has some problem, please connect administrator! ")
    user_session = session.create_session(userinfo.get('id'))
    loginInfo = {}
    loginInfo['id'] = userinfo.get('id')
    loginInfo['token'] = user_session
    return json.dumps(loginInfo)


@database.select(database.db_pool)
def get_userinfo_from_db(cursor, username):
    sql = "select * from cs_user where username='%s'" %username
    cursor.execute(sql)
    return cursor.fetchone()


def is_password_correct(user_password, database_password):
    return True if user_password == database_password else False


def user_status(status):
    return True if status is 0 else False


