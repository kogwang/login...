'''
邮箱验证激活
   -- 注册
         username
         password
         email

         ----postman来发送请求
         ----使用


'''
from flask_restful import Api

from App.apis.AccountUrl import AccountResource
from App.apis.MyMovieApi import MyMovieResource
from App.apis.UserLoginUrl import UserLoginResource
from App.apis.UserUrl import CityResource, UserResource

api = Api()


def init_api(app):
    api.init_app(app=app)






api.add_resource(CityResource, "/cities/")
api.add_resource(UserResource,"/users/")
api.add_resource(AccountResource,"/account/")
api.add_resource(UserLoginResource,'/login/')


api.add_resource(MyMovieResource, "/mymovies/")


