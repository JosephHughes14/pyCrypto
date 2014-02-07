import random


class KeyStore(object):

    def __init__(self, private_key):
        self.private_key = private_key
        self.pub_key = random.random() * private_key

    def gen_pub_key(self):
        return self.pub_key
