def get_db_uri(dbinfo):
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")
    db = dbinfo.get("DB")
    driver = dbinfo.get("DRIVER")

    return "{}+{}://{}:{}@{}:{}/{}".format(db, driver, user, password, host, port, name)


class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "110"


class DevelopConfig(Config):
    DEBUG = True

    MAIL_SERVER = "smtp.163.com"
    MAIL_USERNAME = "yulin_ljing@163.com"
    #这个是授权密码
    MAIL_PASSWORD = "lijing0501115"

    DATABASE = {
        "USER": "root",
        "PASSWORD": "1234",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "Tpp",
        "DB": "mysql",
        "DRIVER": "pymysql"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    "develop": DevelopConfig,
}

