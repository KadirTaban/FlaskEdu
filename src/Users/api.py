from flask import request
from flask_restful import Resource,Api
from src import app
from src.Users.models import Users
from src.Users.models import UserQuery
import json
import sqlite3

@app.route("/users/add", methods=['POST'])
def users():
    requestData = json.loads(request.data)
    print(requestData)
    user = Users(requestData['ID'],requestData['name'],requestData['email'],requestData['phoneNumber'])
    ret = user.insertUser()
    #ret=True
    if ret:
        return "success", 200
    else:
        return "fail", 400



@app.route("/users/get", methods=['GET'])


def home():
    dbCon = sqlite3.connect("test.db")
    cursor = dbCon.cursor()
    cursor.execute('''SELECT * FROM Users where Name = ?''')
    data = cursor.fetchall()
    result =json.dumps(data)
    return result

@app.route("/users/update", methods=['PUT'])

def update():
    #dbCon = sqlite3.connect("test.db")
    #cursor = dbCon.cursor()
    #cursor.execute('''UPDATE Users
    #SET ID,Name,PhoneNumber,Email
    #WHERE Email;''')
    requestData = json.loads(request.data)
    user = Users(requestData['ID'], requestData['name'], requestData['email'], requestData['phoneNumber'])
    ret = user.updateUser()


    if ret:
        return "success", 200
    else:
        return "fail", 400
@app.route("/users/delete", methods=['DELETE'])

def delete():
    requestData=json.loads(request.data)
    user = Users(requestData['ID'], requestData['name'], requestData['email'], requestData['phoneNumber'])
    ret=user.deleteUser()
    if ret:
        return "success", 200
    else:
        return "fail", 400

@app.route("/users/query/select",methods=['GET'])

def selector():
    requestData=json.loads(request.data)
    user=UserQuery(requestData['gender'])
    ret=user.userSelector()
    return ret
    if ret:
        return "success", 200
    else:
        return "fail", 400
@app.route("/users/query/add",methods=['POST'])
def add():
    requestData=json.loads(request.data)
    user=UserQuery(requestData['ID'], requestData['name'], requestData['email'], requestData['phoneNumber'],requestData['gender'],requestData['country'])
    ret=user.collector()
    if ret:
        return "success", 200
    else:
        return "fail", 400