import http.server
import requests
import io
import os

LOGGING = os.environ.get('LOGGING')
class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.proxy_request()

    def do_POST(self):
        self.proxy_request()

    def proxy_request(self):
        # Prepare the URL to the external service
        endpoint = os.environ.get('PROXY_HOST')  + self.path
        #endpoint = "https://httpbin.org"  + self.path
 

        # Read the request body
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        if LOGGING == 'TRUE':
            print('path = ' + self.path)
            print('request headers = ' + str(self.headers))
            print('request body = ' + body.decode('utf-8'))
        
        # Forward the request to the external service
        headers = dict(self.headers)
        response = requests.post(endpoint, headers=headers, data=body.decode('utf-8'))

        # Send the response back to the client
        self.send_response(response.status_code)
        for header, value in response.headers.items():
            self.send_header(header, value)
            if LOGGING == 'TRUE':
                print('response headers =' +  str(header) + ' value = ' + str(value))
        self.end_headers()
        self.wfile.write(response.content)
        
        if LOGGING == 'TRUE':
            print('response =' + str(response.content))
            print('====================================================================================================')

def run_server():
    host = '0.0.0.0'
    port = 8081

    with http.server.HTTPServer((host, port), ProxyHandler) as server:
        print(f"Proxy server running at http://{host}:{port}")
        server.serve_forever()

if __name__ == "__main__":
    print("logging set to " + os.environ.get('LOGGING'))
    print("proxy host set to " + os.environ.get('PROXY_HOST'))
    run_server()
