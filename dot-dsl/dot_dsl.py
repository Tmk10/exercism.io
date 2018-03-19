NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        try:
            self.src = src
            self.dst = dst
            self.attrs = attrs
        except ValueError("Message"):
            raise

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=[]):
        if not isinstance(data, list):
            raise TypeError("Wrong type of input")
        self.attrs = {}
        self.nodes = []
        self.edges = []
        for item in data:
            if len(item) < 2:
                raise TypeError("Wrong argument")
            elif len(item) !=0 and item[0] not in range(3):
                raise ValueError("No object type like {}".format(item[0]))
            elif item[0] == NODE:
                if divmod(len(item[1:]), 2)[1] != 0:
                    raise ValueError("Wrong number of arguments")
                self.nodes.append(Node(item[1], item[2]))
            elif item[0] == EDGE:
                if len(item) < 4:
                    raise ValueError("Wrong number arguments")
                self.edges.append(Edge(item[1], item[2], item[3]))
            elif item[0] == ATTR:
                if divmod(len(item[1:]), 2)[1] != 0:
                    raise ValueError("Wrong number of arguments")
                self.attrs[item[1]] = item[2]



