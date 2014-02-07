import Queue, threading, time

from key_exchange import KeyExchange
from exception_handler import ExceptionHandler
from channel_manager import ChannelManager
from key_store import KeyStore


class Node(object):

    def __init__(self, inst_id, queue):
        self.key_exchange = KeyExchange()
        self.exception_handler = ExceptionHandler()
        self.channel_manager = ChannelManager()
        self.key_store = KeyStore(11)
        self.inst_id = inst_id
        self.q_in = queue
        self.q_out = queue
        
        self.stop = False

    def start(self):
        while not self.stop:
            print "Node {} still running".format(self.inst_id)
            time.sleep(5)

    def test_method(self):
        print "Made it to the test method for Node {}".format(self.inst_id)
        return True

    def get_pub_key(self):
        pub_key = self.key_store.gen_pub_key()
        print "Pub Key : {}".format(pub_key)

    def kill(self):
        self.stop = True
        return True

