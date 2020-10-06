from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

import sys

# port = int(sys.argv[1])
port = 3000 

class SocketServer(WebSocket):

    def handleMessage(self):
        # echo message back to client
        print(self.data)
        self.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')
        print('*** Connected ***')

    def handleClose(self):
        print(self.address, 'closed')
        print("*** Connection closed ***")

server = SimpleWebSocketServer('', port, SocketServer)
server.serveforever()