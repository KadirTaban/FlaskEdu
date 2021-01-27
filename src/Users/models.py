from src import dbCon
import sqlite3
import json



class Users:
    def __init__(self,ID,name,email,phoneNumber=None):
        self.ID=ID
        self.name=name
        self.email=email
        self.phoneNumber=phoneNumber

    def insertUser(self):
        try:
            with dbCon:
                cursor = dbCon.cursor()
                cursor.execute('''INSERT INTO users(ID, Name, Email, PhoneNumber) VALUES (?,?,?,?)''',(self.ID,self.name,self.email,self.phoneNumber))
                dbCon.commit()
            return True
        except Exception as e:
            print(e)
            return False
    def updateUser(self):
        try:
            with dbCon:
                cursor=dbCon.cursor()
                cursor.execute("update users set Name=?,PhoneNumber=?,Email=? where ID=?",(self.name,self.phoneNumber,self.email,self.ID))
                #values = (self.name, self.phoneNumber, self.email,self.ID)
                #cursor.execute(sql, values)
                dbCon.commit()
            return True
        except Exception as e :
            print(e)
            return False
    def deleteUser(self):
        try:
            with dbCon:
                cursor=dbCon.cursor()
                cursor.execute("DELETE FROM users where ID ")
                dbCon.commit()
            return True
        except Exception as e :
            print(e)
            return False

class UserQuery:
    def __init__(self,country,name=None,ID=None,email=None,phoneNumber=None,gender=None):
        self.ID=ID
        self.name=name
        self.email=email
        self.phoneNumber=phoneNumber
        self.gender=gender
        self.country=country


    def userSelector(self):
        try:
            with dbCon:
                cursor=dbCon.cursor()
                cursor.execute("SELECT * from users where Gender")
                data=cursor.fetchall()
                result=json.dumps(data)

                return result
                dbCon.commit()

            return True
        except Exception as e:
            print(e)
            return False
    def collector(self):
        try:
            with dbCon:
                cursor=dbCon.cursor()
                cursor.execute('''INSERT INTO users(ID, Name, Email, PhoneNumber,Gender,Country) VALUES (?,?,?,?,?,?)''',(self.ID,self.name,self.email,self.phoneNumber,self.gender,self.country))
                dbCon.commit()
            return True
        except Exception as e:
            print(e)
            return False


