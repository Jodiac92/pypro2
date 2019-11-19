# web server
from http.server import CGIHTTPRequestHandler, HTTPServer

port = 7878

class Handler(CGIHTTPRequestHandler):
    cg_directories = ['/cgi-bin']
    
serv = HTTPServer(('192.168.0.24', port), Handler)

print('웹 서비스 시작.....')
serv.serve_forever()