import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

print(firebase_admin)
cred = credentials.Certificate('./serviceAccountkey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

def getMarketDetails(request):
    """Responds,,   to00  HTTP request.
    Args:doujdf raw pushsdfsble function"""
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello cloud advocates!!!'

        
  
def pushToFireStoreData():
    today = datetime.datetime.now()
   
##qqUsijng add t00o add documents with auto generated keys
db.collection('persons').add({'name':'John', 'age':88, 'address': "New York"})
db.collection('persons').add({'name':'Jane', 'age':50, 'address': "Los Angeles"})
db.collection('persons').add({'name':'Mark', 'age':40, 'address': "Paris"})
db.collection('persons').add({'name':'Harry', 'age':40, 'address': "London"})
db.collection('persons').add({'name':'Ron', 'age':40, 'address': "Mlan"})

# Create a reference for the document before setting
data = {
    'name': 'Harry Pottery',
    'address': 'USA'
}

# Add a new doc in collection 'persons' with ID 'HP'
db.collection('persons').document('HP').set(data)

# Merge new data with existing data for 'HP'
data = {'employed':True}
db.collection('persons').document('HP').set(data, merge=True)

# Using document() to get an auto generated ID with set()
data = {
    'name': 'Iron Man',
    'address': 'USA'

}
document_reference=db.collection('heroes').document()
document_reference.set(data)
# Adding subcollections
document_reference.collection('movies').add({'name':'Avengers'})

