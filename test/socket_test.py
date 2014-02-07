import time, unittest, threading, Queue, sys

sys.path.append('../src')

from node import Node
from network import Network


class SocketTest(unittest.TestCase):
    
    def setUp(self):

        self.network = Network()

        #start two
        self.q = Queue.Queue(maxsize=0)
        self.node = []

        self.node_1 = Node(0, self.q)
        self.node.append(self.node_1)

        self.node_2 = Node(1, self.q)
        self.node.append(self.node_2)

        for n in self.node:
            t = threading.Thread(target=n.start)
            t.daemon = True
            t.start()
            result = self.network.connect(n) 
            self.assertTrue(result)
    
    def test_1(self):
        self.assertEqual(len(self.network.node), 2)

    def tearDown(self):
        for node in self.node:
            result = node.kill()
            self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()

