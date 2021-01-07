import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase

def getmarketDetails_function(request):
    """Responds to  HTTP request.
    Args:double function
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello cloud advocates!!!'


def pushDataToFireStore():
            print("sdhdjsafsdfsf")
            return f"adfadsf"
