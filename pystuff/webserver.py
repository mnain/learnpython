#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from SocketServer import ThreadingMixIn
from  BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from time import sleep, strftime

_counter = 0

class ThreadingServer(ThreadingMixIn, HTTPServer):
    pass

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        global _counter
        #print dir(self.request)
        #print "request: "+str(self.request)
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        # sleep(5)
        response = str(_counter) + ' ' + strftime('%H:%M:%S')
        _counter = _counter + 1
        self.send_header('Content-length', len(response))
        self.end_headers()
        self.wfile.write(response)

if __name__ == "__main__":
    _counter = 0
    try:
        ThreadingServer(('', 8000), RequestHandler).serve_forever()
    except:
        print "That's all..."

