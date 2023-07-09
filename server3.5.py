import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

logging.basicConfig(filename='logfile.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info(f'GET request received: {self.path}')
        print(f'GET request received: {self.path}')
        logging.info(f'Request headers: {self.headers}')
        print(f'Request headers: {self.headers}')
        logging.info(f'Request version: {self.request_version}')
        print(f'Request version: {self.request_version}')
        logging.info(f'Client address: {self.client_address}')
        print(f'Client address: {self.client_address}')
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info(f'POST request received: {post_data}')
        print(f'POST request received: {post_data}')
        logging.info(f'Request headers: {self.headers}')
        print(f'Request headers: {self.headers}')
        logging.info(f'Request version: {self.request_version}')
        print(f'Request version: {self.request_version}')
        logging.info(f'Client address: {self.client_address}')
        print(f'Client address: {self.client_address}')
        self.send_response(200)
        self.end_headers()

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        logging.info(f'PUT request received: {put_data}')
        print(f'PUT request received: {put_data}')
        logging.info(f'Request headers: {self.headers}')
        print(f'Request headers: {self.headers}')
        logging.info(f'Request version: {self.request_version}')
        print(f'Request version: {self.request_version}')
        logging.info(f'Client address: {self.client_address}')
        print(f'Client address: {self.client_address}')
        self.send_response(200)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
