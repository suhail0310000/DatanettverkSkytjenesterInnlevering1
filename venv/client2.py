import requests
import json
url = "http://127.0.0.1:5000/"
def main():
    response = requests.get(url + "/api/users")
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)


    #Post for creating user
    send = {"userID": "2","username":"Bob"}
    response = requests.post(url + "/api/users", json=send)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)


    #delete a user
    res = requests.delete('http://127.0.0.1:5000/api/user/2')
    if res.status_code == 200:
        print(res.json())
    else:
        print(res.status_code)

    #Get one user with id:
    response = requests.get(url + "/api/user/1")
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)

    #Get all chat rooms:
    response = requests.get(url + "/api/rooms")
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)


    #add one chatroom with roomID:
    send = {"roomID": "22"}

    response = requests.post(url + "/api/rooms", json=send)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)

    #get one chatroom with roomID
    response = requests.get(url + "/api/room/20")
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)

    #Get all roomusers with spesific roomID:
    response = requests.get(url + "/api/room/20/users")
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)

    #Add one user to room with userID
    #denne som ikke funker 
    send = {"userID": "1"}

    response = requests.post(url + "/api/room/22/users", json=send)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)

    #Get all messages with roomID:
    response = requests.get(url + "/api/user/20/messages")
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)

    #Get all messages with roomID and userID
    response = requests.get(url + "/api/room/22/1/messages")
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)


    #Add message with roomID and userID
    send = {"message": "sender meld funker"}

    response = requests.post(url + "/api/room/22/1/messages", json=send)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)


if __name__ == "__main__":
    main()