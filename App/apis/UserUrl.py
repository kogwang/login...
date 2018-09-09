import uuid

from flask import render_template
from flask_mail import Message
from werkzeug.security import generate_password_hash

from App.ext import db, mail, cache
from App.models import City, Letter, UserModel
from flask_restful import Resource, fields, marshal_with, reqparse, marshal





city_fields = {
    "id": fields.Integer,
    "regionName": fields.String,
    "pinYin": fields.String,
    "cityCode": fields.Integer
}

letter_fields = {
    "A": fields.List(fields.Nested(city_fields)),
    "B": fields.List(fields.Nested(city_fields)),
    "C": fields.List(fields.Nested(city_fields)),
    "D": fields.List(fields.Nested(city_fields)),
    "E": fields.List(fields.Nested(city_fields)),
    "F": fields.List(fields.Nested(city_fields)),
    "G": fields.List(fields.Nested(city_fields)),
    "H": fields.List(fields.Nested(city_fields)),
    "J": fields.List(fields.Nested(city_fields)),
    "K": fields.List(fields.Nested(city_fields)),
    "L": fields.List(fields.Nested(city_fields)),
    "M": fields.List(fields.Nested(city_fields)),
    "N": fields.List(fields.Nested(city_fields)),
    "P": fields.List(fields.Nested(city_fields)),
    "Q": fields.List(fields.Nested(city_fields)),
    "R": fields.List(fields.Nested(city_fields)),
    "S": fields.List(fields.Nested(city_fields)),
    "T": fields.List(fields.Nested(city_fields)),
    "W": fields.List(fields.Nested(city_fields)),
    "X": fields.List(fields.Nested(city_fields)),
    "Y": fields.List(fields.Nested(city_fields)),
    "Z": fields.List(fields.Nested(city_fields)),
}

result_fields = {
    "returnCode": fields.String,
    "returnValue": fields.Nested(letter_fields)
}


class CityResource(Resource):

    @marshal_with(result_fields)
    def get(self):

        returnValue = {}
        # 获取的是全部的 1 A 2 B 。。。。。。
        letters = Letter.query.all()

        for letter in letters:
            # 通过主表中的主键 来查询从表中的数据
            cities = City.query.filter_by(letter=letter.id)

            # returnValue['A']={}
            # 虽然返回的是一个字典 但是数据的结构还没有定义
            returnValue[letter.letter] = cities

        return {"returnCode": "0", "returnValue": returnValue}

    def post(self):

        letter_fields_dynamic = {}

        returnValue = {}

        letters = Letter.query.all()

        for letter in letters:
            cities = City.query.filter_by(letter=letter.id)

            letter_fields_dynamic[letter.letter] = fields.List(fields.Nested(city_fields))

            returnValue[letter.letter] = cities

        result_fields_dynamic = {
            "returnCode": fields.String,
            "returnValue": fields.Nested(letter_fields_dynamic)
        }

        result = marshal({"returnCode": "0", "returnValue": returnValue}, result_fields_dynamic)

        print(result)

        return result


'''
想使用邮箱
    pip install flask-mail

    mail = Mail()

    main.init_app(app=app)

    msg = Message('文件名字'，r = [],sender=' ')


注册： 
    model
        username
        password
        email
    apis
        class User(Resource)
             def post(self):
                 获取姓名
                 。。。。
                 user.=xx
                 session.add(user)
                 session.commit

    settings
        MAIL_SERVER='smtp。163.com'
        MAIL_USERNAME=‘xxx.163.com'
        MAIL_PASSWORD='授权名字'
                       设置   pop3...
                       授权密码的时候 需要我们绑定电话号


'''

# reqparse --- restful  required是一定要填写
parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help="请提供用户名fdfdsfdsf")
parser.add_argument("password", type=str, required=True, help="请提供密码")
parser.add_argument("email", type=str, required=True, help="邮箱")

user_fields = {
    "u_name": fields.String,
    "u_email": fields.String(attribute="u_email"),
}

result_fields = {
    "returnCode": fields.String,
    "returnValue": fields.Nested(user_fields),
    "msg": fields.String
}


class UserResource(Resource):
    def get(self):
        pass

    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()
        username = parse.get("username")
        password = parse.get("password")
        email = parse.get("email")
        print('-------------------')
        print(username)

        user = UserModel()
        user.u_name = username
        #generate_password_hash(password=password)  加密
        user.u_password = password

        user.u_email = email

        token = str(uuid.uuid4())

        user.u_token = token

        try:
            db.session.add(user)
            db.session.commit()
            # 思考set方法中的参数分别是谁？ timeout指的是缓存的生存时间
            cache.set(token,user.id,timeout=400)

            msg = Message(subject="Tpp激活邮件", recipients=[email], sender="yulin_ljing@163.com")
            body_html = render_template("UserActive.html", username=username,
                                        active_url='http://localhost:5002/account/?u_token=' + token)
            msg.html = body_html

            mail.send(msg)

        except Exception as e:
            return {"returnCode": "200", "msg": str(e)}

        return {"returnCode": "200", "msg": "ok", "returnValue": user}

    def patch(self):
        pass