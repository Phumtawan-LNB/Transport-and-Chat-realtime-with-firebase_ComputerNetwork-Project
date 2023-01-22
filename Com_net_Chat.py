import pyrebase, datetime, time
from datetime import datetime

firebaseConfig = {
  'apiKey': "AIzaSyC-Bdm76v3HmLkD2khy8ea24r_-OubrAog",
  'authDomain': "com-net-database.firebaseapp.com",
  'projectId': "com-net-database",
  'storageBucket': "com-net-database.appspot.com",
  'messagingSenderId': "806860514555",
  'appId': "1:806860514555:web:c92714e808ef9fd257bc5e",
  'measurementId': "G-3MWBSTH3YJ",
  'databaseURL': 'https://com-net-database-default-rtdb.firebaseio.com/'
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

#============= chat server =============
#Create Users Data
print('Welcome to chat by Firebase')
id = input('Enter your ID : ')
name = input('Enter your Name : ')
address = input('Enter your location : ')
create = input('Enter Chatroom session : ')
def createUser():
    data = {'id': id, 'name': name, 'address': address}
    db.child('Users').child(id).set(data)
    db.child(create).child('attendees').child(id).set(data)
createUser()

#Create chatRooms Data
def joinSession():
  print('\nJoined Session : ',create)
  while True:
    msg = input('Says : ')
    datetimes = time.asctime( time.localtime(time.time()))
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    datas = {'Name': name, 'id': id, 'message': msg, 'time': dt_string}
    db.child(create).child('chatmsg').child(datetimes).set(datas)
    if msg == 'exit':
      break
joinSession()
