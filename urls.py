from handlers import return_offer, home, not_found


def url_handlers(environ, start_response, offer):
    # Extract the path from the environment
    path = environ.get("PATH_INFO")

    #type of response
    html_response = "text/html"
    json_response = "application/json"
    def set_response(response_type):
        start_response(
            "200 OK", [
                ("Content-Type", response_type),
                ("Content-Length", str(len(data)))
            ])
        
    # Remove trailing slash if present
    if path.endswith("/"):
        path = path[:-1]

    # Check the path and invoke corresponding functions
    if path == "":  # Handling the root of the web app
        data = home(environ)
        # Set response headers for a successful response (200 OK)
        set_response(html_response)
    elif path == "/offer":  # Handling the "/offer" path
        data = return_offer(environ, offer)
        # Set response headers for a successful response (200 OK)
        set_response(json_response)
    else:
        # If the path does not match any known route, handle as not found
        data = not_found(environ, path)
        # Set response headers for a unsuccessful response (404 not found)
        set_response(html_response)
    
    # Return an iterator containing the encoded data
    return iter([data])
