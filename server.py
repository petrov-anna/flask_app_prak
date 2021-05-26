from flask import Flask
from flask_restful import Resource, Api, reqparse
from users import Users
from datetime import datetime

app = Flask(__name__)
api = Api(app)
users_args = reqparse.RequestParser()
users_args.add_argument('name')
users_args.add_argument('password')
users_args.add_argument('date')
users = Users()


# работа с пользователем на сервере
class Users(Resource):
    def get(self):
        return users.get_users()

    def post(self):
        args = users_args.parse_args()
        user = users.set_users(args.get('name'), args.get('password'), date=str(datetime.now()))
        return user


api.add_resource(Users, '/api/users')

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
