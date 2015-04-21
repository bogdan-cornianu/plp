class MyMeta(type):
    def __init__(self, name, bases, attrs):
        print "meta init"


class UseMyMeta(object):
    __metaclass__ = MyMeta


m = MyMeta()
