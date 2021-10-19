from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import json
import pprint
from datetime import datetime

app = Flask(__name__)
api = Api(app)

user_post = reqparse.RequestParser()
user_post.add_argument("userID", type=int, help="ID is required...", required=True)
user_post.add_argument("username", type=str, help="username is required...", required=True)

room_post = reqparse.RequestParser()
room_post.add_argument("roomID", type=int, help="ID is required...", required=True)


class User(Resource):
    def get(self):
        with open('users.json', 'r') as json_file:
            data = json.load(json_file)
        return data

    
    def post(self):
        args = user_post.parse_args()
        userID = request.json['userID']
        name = request.json['username']
        user = {"id": userID, 'username': name}
        with open("users.json", "r+") as file:
            data = json.load(file)
            for u in data:
                print(u)
                if u['id'] == userID:
                    return {'erorr': 'userID is taken'}
            data.append(user)
            file.seek(0)
            json.dump(data, file)
        return data

api.add_resource(User, "/api/users", methods = ['GET', 'POST']) 



class Userid(Resource):

    def get(self, userID):
        with open('users.json', 'r') as json_file:
            data = json.load(json_file)
            for user in data:
                if user['id'] == str(userID):
                    return user
        return {'erorr': 'user not exists'}

        

    def delete(self, userID):
        
        with open('users.json', 'r+') as json_data:
            user = json.load(json_data)
            for z, x in enumerate(user):
                if x['id'] == str(userID):
                    del user[z]
                    json_data.seek(0)
                    json_data.write(json.dumps(user))
                    json_data.truncate()
                    return {'msg': 'deleted user'}
            return {'erorr': 'user not exists'}

            
                
api.add_resource(Userid, "/api/user/<int:userID>", methods = ['GET', 'DELETE']) 




class Chatrooms(Resource):
    def get(self):
        with open('rooms.json', 'r') as json_file:
            data = json.load(json_file)
        return data

    def post(self):
        args = room_post.parse_args()
        roomID = request.json['roomID']
        room = {"id": roomID, 'users_id': []}
        with open("rooms.json", "r+") as file:
            data = json.load(file)
            for r in data:
                if r['id'] == roomID:
                    return {'erorr': 'roomID is taken'}
            data.append(room)
            file.seek(0)
            json.dump(data, file)
        return data

api.add_resource(Chatrooms, "/api/rooms", methods = ['GET', 'POST'])   



class ChatroomId(Resource):
    def get(self, roomID):
        with open('rooms.json', 'r') as json_file:
            data = json.load(json_file)
            for room in data:
                if room['id'] == str(roomID):
                    return room
        return {'erorr': 'room not exists'}

api.add_resource(ChatroomId, "/api/room/<int:roomID>", methods = ['GET'])   



class Roomusers(Resource):
    def get(self, roomID):
        
        with open('rooms.json', 'r') as json_file:
            data = json.load(json_file)
            for room in data:
                if room['id'] == str(roomID):
                    return {'users_id':  room['users_id']}
        return {'erorr': 'room not exists'}
       

    def post(self,roomID):
        userID = request.json['userID']
        users_id = {'users_id': []}

        users = ''        
        with open('users.json', 'r') as json_file:
            users = json.load(json_file)

        with open("rooms.json", "r+") as file:
            data = json.load(file)
            for r in data:
                if r ['id'] == str(roomID):
                    for u in r['users_id']:
                        if str(userID) == u:
                            return {'msg': 'user exists in room'}
                    for x in users:
                        if x['id'] == str(userID):
                            r['users_id'].append(str(userID))
                            #add user to list
                            pprint.pprint(data)
                            file.seek(0)
                            file.write(json.dumps(data))
                            file.truncate()
                            return {'msg': 'added user to list'}
                    return {'msg': 'user not allowed'}
            return {'msg': 'room not exists'}
                


api.add_resource(Roomusers, "/api/room/<int:roomID>/users", methods = ['GET', 'POST'])   



class Message(Resource):

    def get(self, roomID):

        with open('messages.json', 'r') as file:
            data = json.load(file)
            dictx = []
            for x in data:
                if x['roomID'] == str(roomID):
                    print(x)
                    dictx.append(x)
            return dictx
        return {'msg':'fail'}

    

api.add_resource(Message, "/api/user/<int:roomID>/messages", methods = ['GET'])   

class Message2(Resource):

    def get(self, roomID, userID):
        x = 0
        z = 0
    
        with open('rooms.json', 'r') as json_file:
            rooms = json.load(json_file)
            for room in rooms:
                if room['id'] == str(roomID):
                    z = 1
                    for user in room['users_id']:
                        if str(userID) == user:
                            print('yes')
                            x = 1
                            break
        if z == 0:
            return {'fail': 'room not exists'}
        if x == 0:
            return {'fail': 'user not exists'}
        

        with open("messages.json", "r") as file:
            data = json.load(file)  
                     
        return {"Data": data}
    

    
    def post(self,roomID,userID):
        message = request.json['message']
        x = 0
        z = 0
        print(str(datetime.now()))


        with open('rooms.json', 'r') as json_file:
            rooms = json.load(json_file)
            for room in rooms:
                if room['id'] == str(roomID):
                    z = 1
                    for user in room['users_id']:
                        if str(userID) == user:
                            print('yes')
                            x = 1
                            break
        if z == 0:
            return {'fail': 'room not exists'}
        if x == 0:
            return {'fail': 'user not exists'}
        

        with open("messages.json", "r+") as file:
            data = json.load(file)
            #get last id 
            for x, m in enumerate(data):
                pass
            message = {
                'id': str(x+2),
                'roomID': str(roomID),
                'users_id': str(userID),
                'message': message,
                'time': str(datetime.now())
            }

            data.append(message)
            file.seek(0)
            json.dump(data, file)
        return message
        

api.add_resource(Message2, "/api/room/<int:roomID>/<int:userID>/messages", methods=['GET','POST']) 


if __name__ == "__main__":
    app.run(debug=True)