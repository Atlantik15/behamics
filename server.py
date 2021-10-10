from flask import Flask, Response, jsonify, json
import pymongo
import string
import random
from calculations import Calculations
app = Flask(__name__)
calculations = Calculations()

try:
    mongo = pymongo.MongoClient(
        host="localhost", 
        port=27017,
        serverSelectionTimeoutMS = 1000
        )
    db = mongo.behamics
    mongo.server_info() 
except:
    print("ERROR - Cannot connect to db")
##############################

@app.route('/hello/<string:name>', methods=['GET'])
def hello(name):
    return "Hello " + name

@app.route('/sum/<int:number1>/<int:number2>', methods=['GET'])
def sum(number1, number2):
    return str(calculations.sum(number1, number2))

@app.route('/calculate_exam_grade/<points>', methods=['GET'])
def calculate_exam_grade(points):
    points = int(points)
    return calculations.calculate_exam_grade(points)

gradeDict = {
  "grades": 
    {
      "math": 10,
      "literature": 1,
      "physics": 5,
      "music": 7
    }
}

@app.route("/minmax", methods=['GET'])
def minmax():
    grades = gradeDict["grades"]
    return calculations.minmax(grades)
    

def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
       return ''.join(random.choice(chars) for _ in range(size))

@app.route("/insert_product", methods=["POST"])
def insert_product():
    try:
        product = {'productID':id_generator()  ,'name':'Adidas Rivalry Low', 'category':'shirts', 'price':71.29, 'basePrice':89.95}
        dbResponse = db.products.insert_one(product)
        print(dbResponse.inserted_id)
        #for attr in dir(dbResponse):
        #    print(attr)
        return Response(
            response= json.dumps(
                {"message": "product created", 
                "id":f"{dbResponse.inserted_id}"
                }),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print("***********")
        print(ex)
        print("***********")


@app.route("/find_product", methods=["GET"])
def find_product():
    try:
        found = db.products.find({'category': 'shirts'})

        return Response(
            response= json.dumps(
                {
                "message": found,               
                }),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print("***********")
        print(ex)
        print("***********")



##############################

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)