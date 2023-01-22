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

#fetch chatRooms Data
create = input('Enter Chatroom session : ')
items = db.child(create).child('chatmsg').get()
print('\nJoined Session : ',create)
firstItem = []
FnameItem = []
for item in items.each():
    f = item.val()['message']
    n = item.val()['Name']
    firstItem.append(f)
    FnameItem.append(f)
    print(n,' : ',f)
itemMsg = []
nameItem = []
while True:
  items = db.child(create).child('chatmsg').get()
  for item in items.each():
    raw = item.val()['message']
    rawName = item.val()['Name']
    temp = raw
    tempName = rawName
  if temp == firstItem[len(firstItem)-1] and tempName == FnameItem[len(firstItem)-1]:
    temp = 0
    tempName = 0
  else:
    itemMsg.append(temp)
    nameItem.append(tempName)
    print(nameItem[len(nameItem)-1],' : ',itemMsg[len(itemMsg)-1])
    firstItem.append(temp)
    FnameItem.append(tempName)