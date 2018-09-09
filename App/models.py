from App.ext import db


class Letter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    letter = db.Column(db.String(2))


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    regionName = db.Column(db.String(16))
    cityCode = db.Column(db.Integer)
    pinYin = db.Column(db.String(128))
    #外键设置的语法  是 ForeignKey（类名.主键名字）
    letter = db.Column(db.Integer, db.ForeignKey(Letter.id))


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(32), unique=True)
    u_password = db.Column(db.String(256))
    u_email = db.Column(db.String(64), unique=True)
    u_active = db.Column(db.Boolean,default=False)
    u_token = db.Column(db.String(256))
    u_promission = db.Column(db.Integer,default=1)
