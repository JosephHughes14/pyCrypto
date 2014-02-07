import socket

class Network(object):

    def __init__(self):
        self.node = []

    def connect(self, node):
        self.node.append(node)
        return True

        #TODO: make this socket based
        #      eventually use IP
        #s = socket.socket(
        #        socket.AF_INET,
        #        socket.SOCK_STREAM
        #        )
        #s.bind((self.ip_addr, self.port))


