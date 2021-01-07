import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase

cred = credentials.Certificate('./ServiceAccountKey.json')
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
    db.collection('XXXX').document('YY').set(
      {
        'name': 'Amazon',
        'creationDate': today,
        'lastClose': 3443.63,
        'indices': [ 'NDX', 'OEX', 'S5COND', 'SPX' ]
      }
    )
