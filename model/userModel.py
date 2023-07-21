import datetime
from sysApp.auth import login
from sysApp.db import conect


def insert_user(name, email, password):
    hashed_password = login.hash_password(password)
    hashs = hashed_password[0]
    new_password = hashed_password[1]
    created_at = datetime.datetime.now()
    sql = "INSERT INTO user (name, email, password, hash, created_at) VALUES (%s, %s, %s, %s, %s)"
    values = (name, email, new_password, hashs, created_at)
    # cursor.execute(sql, values)
    print(sql, values)




