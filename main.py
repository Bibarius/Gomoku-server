from http.server import *
import os

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path[1:]
        if not path:
            f = open("index.html", "rb")
            File = f.read()
            self.send_response(200)
            self.send_header('Content-Lenth', str(len(File)))
            self.end_headers()
            self.wfile.write(File)

        else:
            try:                
                f = open(path, 'rb')
            except FileNotFoundError:
                print('requested file ' + path + ' wasnt found on server')
                return 1
            File = f.read()
            self.send_response(200)

            if path.find('css'):
                self.send_header('Content-Type', 'text/css')

            self.send_header('Content-Lenth', str(len(File)))
            self.end_headers()
            self.wfile.write(File)



if __name__ == "__main__":
    os.chdir(os.getcwd() + '/frontend')
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
    