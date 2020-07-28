from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import bcrypt
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)




class Register(Resource):
    def post(self):
    # get the data from user
    postedData = request.get_json()
    username = postedData["username"]
    password = postedData["password"]



#     hash password
    hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

    users.insert({
        "Username": username,
        "Password": hashed_pw,
        "Sentence": ""

    })


    retJson = {
        "status": 200,
        "Message": "You successfully signed up for the calc-API !!"

    }

class Store(Resource):
    def post(self):
        postedData = request.get_json()
        


def checkPostedData(postedData, functionName):
    if (functionName == "add" or functionName == "sub" or functionName == "multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif functionName == "divide":
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"]) == 0:
            return 302
        else:
            return 200


class Add(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "add")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = float(x)
        y = float(y)

        result = x + y
        resultMap = {
            'Message': result,
            'Status code': 200
        }
        return jsonify(resultMap)


class Sub(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "sub")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = float(x)
        y = float(y)

        result = x - y
        resultMap = {
            'Message': result,
            'Status code': 200
        }
        return jsonify(resultMap)


class Multi(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "multiply")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = float(x)
        y = float(y)

        result = x * y
        resultMap = {
            'Message': result,
            'Status code': 200
        }
        return jsonify(resultMap)


class Divide(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "divide")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        result = (x * 1.0) / y
        resultMap = {
            'Message': result,
            'Status code': 200
        }
        return jsonify(resultMap)


api.add_resource(Add, '/api/add')
api.add_resource(Sub, '/api/sub')
api.add_resource(Multi, '/api/multiply')
api.add_resource(Divide, '/api/divide')
api.add_resource(Register, '/register')

if __name__ == "__main__":
    app.run(debug=True)
