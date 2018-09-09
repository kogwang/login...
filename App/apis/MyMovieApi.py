from flask_restful import Resource, reqparse, abort
from App.models import UserModel
parser = reqparse.RequestParser()
parser.add_argument("u_token", required=True, help="请登录")
"""
权限值

1      浏览权限
2      回复权限
4   
8
16
"""
LOOK = 1
WRITE = 2
def check_permission(permission):
    def check_permission_fun(func):
        def check(*args, **kwargs):
            parse = parser.parse_args()
            u_token = parse.get("u_token")

            users = UserModel.query.filter(UserModel.u_token.__eq__(u_token))

            if users.count() > 0:
                user = users.first()
                if user.check_permission(permission):
                    print("用户是拥有权限的，准备查看电影")
                    return func(*args, **kwargs)
                else:
                    abort(403, message="你没有权限查看此模块，请联系系统管理员")
            else:
                abort(401, message="您还没有登录，请登录查看")
        return check
    return check_permission_fun

class MyMovieResource(Resource):

    @check_permission(WRITE)
    def get(self):
        # 直接查询就行
        return {"msg": "ok", "data": "你的电影资源"}
