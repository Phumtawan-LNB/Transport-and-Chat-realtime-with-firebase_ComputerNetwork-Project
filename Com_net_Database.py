from multiprocessing.managers import SyncManager
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin, pyrebase, random, string, sys, Com_net_Mail
#config
credpath = r"C:\Users\koonp\Desktop\Github\Project Comnet\com-net-database-firebase-adminsdk-yhwsd-d531100120.json"
login = credentials.Certificate(credpath)
firebaseConfig = {
  'apiKey': "AIzaSyC-Bdm76v3HmLkD2khy8ea24r_-OubrAog",
  'authDomain': "com-net-database.firebaseapp.com",
  'projectId': "com-net-database",
  'storageBucket': "com-net-database.appspot.com",
  'messagingSenderId': "806860514555",
  'appId': "1:806860514555:web:c92714e808ef9fd257bc5e",
  'measurementId': "G-3MWBSTH3YJ",
  'databaseURL': ''
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# initialize firebase
firebase_admin.initialize_app(login)
db = firestore.client()

#Read File in firebase
def readProduct():
    Productkey = input('Primary key : ')
    try:
        readData = db.collection('customers').document(Productkey).get()
        if readData.exists:
            print(readData.to_dict())
            ch = input('Do you want to read more product?[y/n] : ')
            if ch == 'y':
                readProduct()
            else:
                admin()
    except:
        print('Not match!')

#Write File in firebase
def createProduct():
    Productkey = input('Primary key : ')
    name = input('Customer name : ')
    age = input('Customer age : ')
    contact = input('Customer Phone number : ')
    address = input('Customer Address : ')
    mail = input('Customer Mail : ')
    #random key generate
    def random_string(length = 10):
        charactor_set = string.ascii_letters
        return ''.join(random.choice(charactor_set) for i in range(length)) 
    key = random_string(10)

    customers = db.collection("customers")
    customers.document(Productkey).set({
    'name': name,
    'age': age,
    'contact': contact,
    'address': address ,
    'track_id': key,
    'status': 'waiting product'
    })
    print('created product')
    Com_net_Mail.runMail(name, key, 'waiting product',mail)
    ch = input('Do you want to create more product?[y/n] : ')
    if ch == 'y':
        createProduct()
    else:
        admin()

#query Data from firebase
def queryProduct():
    while True:
        track_id = input('Enter Tracking-ID : ')
        queryData = db.collection('customers').where('track_id', '==', track_id).get()
        for data in queryData:
            print(data.to_dict())
            if data == None:
                print('Tracking ID not found!')
        ch = input('Do you want to Track another ID?[y/n] : ')
        if ch == 'y':
            queryProduct()
        else:
            sys.exit()

#update File in firebase
def updateStatusProduct():
    while True:
        productKey = input('Primary key : ')
        updateStatus = input('Enter update : ')
        mails = input('Enter Mail : ')
        update = db.collection('customers').document(productKey).update({'status': firestore.ArrayUnion([updateStatus])})
        queryData = db.collection('customers').document(productKey).get()
        if queryData.exists:
            mail = []
            mail.append(queryData.to_dict())
            Com_net_Mail.updateMail(mail,mails)
        ch = input('Do you want to update more product status?[y/n] : ')
        if ch == 'y':
            updateStatusProduct()
        else:
            admin()

def signup():
    email = input("Enter email : ")
    password = input('Enter password : ')
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print('Created\nDo you want to Login?[y/n]')
        ch = input('Enter you choice : ')
        if ch == 'y':
            login()
    except:
        print('Email already exists!')
        signup()

def login():
    email = input("Enter email : ")
    password = input('Enter password : ')
    try:
        logins = auth.sign_in_with_email_and_password(email, password)
        print('Logged-in!')
        if email == 'admin@mail.com':
            admin()
        else:
            queryProduct()
    except:
        print('Incorrect username or password !')
        login()

def admin():
    print('You are now in admin mode\n=========================')
    print('1. Create customer product\n2. Read Data customer\n3. Read Product\n4. Update Product')
    adAns = (input('Your Answer : '))
    if adAns == '1':
        createProduct()
    elif adAns == '2':
        readProduct() #กรณีไม่ทราบ Primary key ของลูกค้า
    elif adAns == '3':
        queryProduct()
    elif adAns == '4':
        updateStatusProduct()

#============== initialization Project ==============
print('Welcome to transportation system simulation')
def _init_():
    ans = input('Do you want to create or login account?[y/n] : ')
    if ans =='y':
        signup()
    elif ans == 'n':
        login()
    else:
        quit()
_init_()