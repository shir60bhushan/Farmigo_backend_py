def getmarketDetails_function(request):
    """Responds to  HTTP request.
    Args:NEW PUSH  zip new test comment
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello cloud advocates!!!'


        def pushDataToFireStore():
            print("sdhdjf")
