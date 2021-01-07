import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./serviceAccountkey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

def getmarketDetails_function(request):
    """Responds to  HTTP request.
    Args:doudfsdfsdfsble function
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello cloud advocates!!!'

        
  
def pushDataToFireStore():
    today = datetime.datetime.now()
   
    # Using add to add documents with auto generated keys
db.collection('persons').add({'name':'John', 'age':40, 'address': "New York"})
db.collection('persons').add({'name':'Jane', 'age':50, 'address': "Los Angeles"})
db.collection('persons').add({'name':'Mark', 'age':40, 'address': "Paris"})
db.collection('persons').add({'name':'Harry', 'age':40, 'address': "London"})
db.collection('persons').add({'name':'Ron', 'age':40, 'address': "Mlan"})

# Create a reference for the document before setting
data = {
    'name': 'Harry Potter',
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

