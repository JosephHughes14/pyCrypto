import time, unittest, threading, Queue, sys

sys.path.append('../src')

from node import Node


class SkeletonTest(unittest.TestCase):
    
    def setUp(self):

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
    
    def test_1(self):

        result = self.node[0].test_method()
        self.assertTrue(result)

        result = self.node[1].test_method()
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()

