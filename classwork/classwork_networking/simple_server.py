from http.server import BaseHTTPRequestHandler, HTTPServer
import json

users = []
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self, ):
    """Handle GET requests."""
    self.send_response(200)
    self.send_header('Content-type', 'text/html')

    self.end_headers()
    # with open('index.html', mode='r') as html:
    #   some_file = html.read()
    self.wfile.write(bytes(str(users), encoding='utf-8'))

  def do_POST(self):
    """Handle POST requests."""
    content_length = int(self.headers.get('Content-length', 64))

    post_data = self.rfile.read(content_length)

    try:
      post_data_json = json.loads(post_data)
      for user in users:
        if post_data_json['email'] in user.values():
          print(post_data_json['email'])
          self.send_response(400)
          self.send_header('Content-type', 'application/json')
          self.end_headers()   
          self.wfile.write(b'{Message: User already exist...}')
          return
      users.append(post_data_json)   
    except json.JSONDecodeError as e:
      print(e)

    
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

    self.wfile.write(post_data)




HOST = '127.0.0.1'
PORT = 8000


def run():
  server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
  print(f"Starting server at http://{HOST}:{PORT}")
  server.serve_forever()
    
if __name__ == '__main__':
  run()