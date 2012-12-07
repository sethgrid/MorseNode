class MorseNode(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def addChild(self, child):
        self.children.append(child)
        return child

    def display(self):
        print "Data: %s" % self.data
        print "Children: %s" % self.children
        for child in self.children:
            child.display()

