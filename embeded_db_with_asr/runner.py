#!/usr/bin/python3
import http.server, ssl

import argparse
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-p", "--port", help = "port number")

# Read arguments from command line
args = parser.parse_args()

if args.port:
    print("using port: % s" % args.port)
    port = int(args.port)
else:
    port = 8000
server_address = ('0.0.0.0', port)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='cert.pem', keyfile='key.pem', server_side=True)
print(f"Serving HTTPS on {server_address[0]}:{server_address[1]}")
httpd.serve_forever()
