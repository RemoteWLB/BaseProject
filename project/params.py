import os

JWT_SALT = os.environ["JWT_SALT"]
JWT_ALGO = os.environ["JWT_ALGO"]

MD5_SALT = os.environ["MD5_SALT"]
REDIS_PWD = os.environ["REDIS_PWD"]

OSS_ACCESS_KEY_ID = os.environ["OSS_ACCESS_KEY_ID"]
OSS_ACCESS_KEY_SECRET = os.environ["OSS_ACCESS_KEY_SECRET"]