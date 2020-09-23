from flask import Flask, request, jsonify
from flask_restful import Api, Resource

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({
    'num_of_users':0
})

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {"$set":{"num_of_users":new_num}})
        return str("Hello user " + str(new_num))

def checkPostedData(postedData, functionName):
    if(functionName == "add" or functionName == "subtract" or functionName=="multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif functionName =='division':
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"] == 0):
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        #if i am here, then the resource  Add was requested using POST

        # Step 1 Get Posted Data
        postedData = request.get_json()
        
        # Step 1b verify validate posted Data
        statusCode = checkPostedData(postedData, 'add')
        if statusCode != 200:
            retJson = {
                'Message': 'An Error Occured!!',
                'Status Code': statusCode
            }
            return jsonify(retJson)

        # if i am here, then status_code == 200
        x = int(postedData["x"])
        y = int(postedData["y"])

        # Step 2 Add the Posted Data
        ret = x+y
        retMap = {
            'message': ret,
            'Status code': 200
        }
        return jsonify(retMap)

class Subtract(Resource):
    def post(self):
        #if i am here, then the resource subtract was requested using POST

        # Step 1 Get Posted Data
        postedData = request.get_json()
        
        # Step 1b verify validate posted Data
        statusCode = checkPostedData(postedData, 'subtract')
        if statusCode != 200:
            retJson = {
                'Message': 'An Error Occured!!',
                'Status Code': statusCode
            }
            return jsonify(retJson)

        # if i am here, then status_code == 200
        x = int(postedData["x"])
        y = int(postedData["y"])

        # Step 2 Add the Posted Data
        ret = x-y
        retMap = {
            'message': ret,
            'Status code': 200
        }
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        #if i am here, then the resource multiply was requested using POST

        # Step 1 Get Posted Data
        postedData = request.get_json()
        
        # Step 1b verify validate posted Data
        statusCode = checkPostedData(postedData, 'multiply')
        if statusCode != 200:
            retJson = {
                'Message': 'An Error Occured!!',
                'Status Code': statusCode
            }
            return jsonify(retJson)

        # if i am here, then status_code == 200
        x = int(postedData["x"])
        y = int(postedData["y"])

        # Step 2 Add the Posted Data
        ret = x*y
        retMap = {
            'message': ret,
            'Status code': 200
        }
        return jsonify(retMap)

class Divide(Resource):
    def post(self):
        #if i am here, then the resource division was requested using POST

        # Step 1 Get Posted Data
        postedData = request.get_json()
        
        # Step 1b verify validate posted Data
        statusCode = checkPostedData(postedData, 'division')
        if statusCode != 200:
            retJson = {
                'Message': 'An Error Occured!!',
                'Status Code': statusCode
            }
            return jsonify(retJson)

        # if i am here, then status_code == 200
        x = int(postedData["x"])
        y = int(postedData["y"])

        # Step 2 Add the Posted Data
        ret = x/y
        retMap = {
            'message': ret,
            'Status code': 200
        }
        return jsonify(retMap)

# Add resources to Api
api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')
api.add_resource(Visit, "/hello")

@app.route('/')
def home():
    return "Hemanth's Site Enjoy the Day!!!"

# @app.route('/add', methods=["POST"])
# def add():
#     dataDict = request.get_json()
#     # return jsonify(dataDict)
#     x = dataDict['x']
#     y = dataDict['y']
#     if "y" not in dataDict:
#         return "Error", 505
#     result = x+y
#     jsonData = {
#         'z': result,
#     }
#     return jsonify(jsonData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)