from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL and extract the route and parameters
        url_parts = urlparse(self.path)
        route = url_parts.path
        parameters = parse_qs(url_parts.query)

        # Get the HTTP headers
        headers = self.headers

        print(f"Received GET request:")
        print(f"  Route: {route}")
        print(f"  Parameters: {parameters}")
        print("  Headers:")
        for header, value in headers.items():
            print(f"    {header}: {value}")


        # Create the HTML response
        html = f"""
        <html>
        <body>
            <h1>Request received</h1>
            <p>Route: {route}</p>
            <p>Parameters: {parameters}</p>
            <h2>Headers:</h2>
            <ul>
        """

        # Add each header to the HTML response
        for header, value in headers.items():
            html += f"<li>{header}: {value}</li>"

        html += """
            </ul>
        </body>
        </html>
        """

        # Send the HTML response back to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

def run_server(port=80):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f'Server running on http://localhost:{port}')
    httpd.serve_forever()

run_server(port=8000)

