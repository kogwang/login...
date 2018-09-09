#获得一个user  然后判断该用户的权限 然后再根据权限判断响应内容
#这个文件是权限底层。。。
from flask_restful import reqparse, Resource

from App.models import UserModel

parser = reqparse.RequestParser()
parser.add_argument('token',type=str,required=True)

class MovieResource(Resource):
      def get(self):
          parse = parser.parse_args()
          token = parse.get('token')
          users = UserModel.query.filter(UserModel.u_token == token)
          if users.count() > 0:
              user = users.first()
              if user.u_promission == 1:
                  return {'message':'1'}
              elif user.u_promission == 2:
                  return {'message': '2'}
              else:
                  return {'message': '3'}





