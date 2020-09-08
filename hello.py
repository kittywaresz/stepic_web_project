def app(environ, start_response):
    params = environ.get('QUERY_STRING').split('&')

    body = '\n'.join(params).encode()

    status = '200 OK'
    headers = [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(body)))
    ]

    start_response(status, headers)

    return [body]
