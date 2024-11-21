from http.server import BaseHTTPRequestHandler, HTTPServer
import json


users = [
   
]
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500}
]

class CRUDHandler(BaseHTTPRequestHandler):
  def __set_headers(self, status=200):
    self.send_response(status)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

  def __path_parser(self):
    parsed_path = self.path.strip('/').split('/')
    return parsed_path
  
  def do_GET(self):
    parsed_path = self.__path_parser()
    if len(parsed_path) == 1:
      if parsed_path[0] == 'users':
        self.__set_headers()
        self.wfile.write(json.dumps(users).encode())
      elif parsed_path[0] == 'products':
        self.__set_headers()
        self.wfile.write(json.dumps(products).encode())
      else:
        self.__set_headers(400)
        self.wfile.write(json.dumps({'error': 'path not found...'}).encode())
    elif len(parsed_path) == 2:
      self.__set_headers()
      resource, resource_id = parsed_path

      result = next(u for u in eval(resource) if u['id'] == int(resource_id)) 
      self.wfile.write(json.dumps(result).encode())
    else:
      self.__set_headers(404)
      self.wfile.write(json.dumps({'error': 'nor found...'}))

  def do_POST(self):
    parsed_path = self.__path_parser()
    if len(parsed_path) == 1:
      self.__set_headers()

      content_length = int(self.headers['Content-length'])
      body = json.loads(self.rfile.read(content_length))

      resource = parsed_path[0]

      new_id = max([u['id'] + 1 for u in eval(resource)]) if eval(resource) else 1
      body.update({'id': new_id})

      eval(resource).append(body)

      self.wfile.write(json.dumps(eval(resource)).encode())




      

def run(server_class=HTTPServer, server_handler=CRUDHandler, port=8000):
  server_address = ('', port)

  httpd = server_class(server_address, server_handler)

  print(f"Server runing on port: {port}")
  httpd.serve_forever()

if __name__ == '__main__':
  run()