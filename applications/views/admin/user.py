from flask_restful import Resource, reqparse

users = [
    {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    },
    {
        "id": 2,
        "name": "Bob",
        "email": "bob@example.com"
    },
    {
        "id": 3,
        "name": "Charlie",
        "email": "charlie@example.com"
    }
]


class User(Resource):
    def get(self, user_id):
        return {
            "code": 20000,
            "data": {'token': "1234567890",
                     'roles': 'admin'}
        }

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("email")
        args = parser.parse_args()
        for user in users:
            if user["id"] == user_id:
                user["name"] = args["name"] if args["name"] is not None else user["name"]
                user["email"] = args["email"] if args["email"] is not None else user["email"]
                return user, 200

        user = {
            "id": user_id,
            "name": args["name"],
            "email": args["email"]
        }
        users.append(user)
        return user, 201

    def delete(self, user_id):
        global users
        users = [user for user in users if user["id"] != user_id]
        return "", 204


class Users(Resource):
    def get(self):
        return {
                "code": 20000,
                "data": {'token':"1234567890"}
                }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True)
        parser.add_argument("email", required=True)
        args = parser.parse_args()

        user_id = users[-1]["id"] + 1 if len(users) > 0 else 1
        user = {
            "id": user_id,
            "name": args["name"],
            "email": args["email"]
        }
        users.append(user)
        return user, 201
