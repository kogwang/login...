from flask_restful import Resource, reqparse

from App.ext import db, cache
from App.models import UserModel

parser = reqparse.RequestParser()

parser.add_argument('u_token',type=str)



class AccountResource(Resource):
    #现在
    def get(self):
        parse = parser.parse_args()

        token = parse.get('u_token')
        print('---------------------------')
        print(token)

        user_id = cache.get(token)

        users = UserModel.query.filter(UserModel.id == user_id)

        #当在页面发送过来请求之后 我想作的是把对象的u_active的值由false改为true
        #找对象
        #UserModel.query.filter_by(u_token=token)
        #users = UserModel.query.filter(UserModel.u_token==token)
        #UserModel.query.filter(UserModel.u_token.__eq__(token))

        #此时如果不从缓存中拿取会发生什么问题
        if users.count()>0:
            print(1111111111)
            user = users.first()
            user.u_active = True
            db.session.add(user)
            db.session.commit()
            return {'message':'jfjdsfjlkdsjflkds'}

        return {'message':'bu ok'}










