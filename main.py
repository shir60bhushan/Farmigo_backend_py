def getmarketDetails_function(request):
    """Responds to any HTTP request.
    Args:NEW PUSH Trigger
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello cloud advocates!!!'