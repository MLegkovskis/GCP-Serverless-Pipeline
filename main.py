def hello_next_gate_tech(request):
    request_json = request.get_json(silent=True)
    message = ''
    if request_json and 'message' in request_json:
        message = ' ' + request_json['message']
    return 'Hello, Next Gate Tech!' + message
