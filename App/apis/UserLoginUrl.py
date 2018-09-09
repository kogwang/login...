




# 去登录  toLogin   登录 login
from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash

from App.models import UserModel

parser = reqparse.RequestParser()
parser.add_argument('username',type=str,required=True,help='请输入用户名字')
parser.add_argument('password',type=str,required=True,help='请输入密码')
# parser.add_argument()


class UserLoginResource(Resource):
    def post(self):
        parse = parser.parse_args()
        #相当于request.form.get('username')
        username = parse.get('username')
        password = parse.get('password')
        #check_password_hash(user.u_password, password)  解密
        if username:
            users = UserModel.query.filter(UserModel.u_name == username)
            if users.count() > 0:
                user = users.first()
                if user.u_password == password:
                    if user.u_active:
                        return {'messge':'登录成功'}
                    return {'message':'当前用户未激活，赶紧冲钱'}
            return {'message':"你输入错了 老铁"}



