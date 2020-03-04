class BinarySearchTree:
    def __init__(self, key, rightNode = None , leftNode = None):
        self.key = key
        self.rightNode = rightNode
        self.leftNode = leftNode

class BSTContainer:

    def __init__(self, key):
        self.rootNode = BinarySearchTree(key)

    def insertNode(self, rtNode, givenKey):

        if rtNode == None:
            rtNode = BinarySearchTree(givenKey)

        elif rtNode.key > givenKey:
            rtNode.leftNode = self.insertNode(rtNode.leftNode, givenKey)

        elif rtNode.key <= givenKey:
            rtNode.rightNode = self.insertNode(rtNode.rightNode, givenKey)

        return rtNode

    def inOrderTrav(self, rtNode):

        if rtNode == None:
            return

        self.inOrderTrav(rtNode.leftNode)
        print("Node: ", rtNode.key)
        self.inOrderTrav(rtNode.rightNode)

    def preOrderTrav(self, rtNode):

        if rtNode == None:
            return

        print("Node: ", rtNode.key)
        self.inOrderTrav(rtNode.leftNode)
        self.inOrderTrav(rtNode.rightNode)

    def postOrderTrav(self, rtNode):

        if rtNode == None:
            return

        self.inOrderTrav(rtNode.leftNode)
        self.inOrderTrav(rtNode.rightNode)
        print("Node: ", rtNode.key)

    def searchNode(self, rtNode, searchKey):

        if rtNode == None:
            return
        if rtNode.key == searchKey:
            print("Key Found In Tree")
            return

        self.searchNode(rtNode.leftNode, searchKey)
        self.searchNode(rtNode.rightNode, searchKey)

    def bfsTraverse(self):
        objects = []
        objects.append(self.rootNode)

        while len(objects) != 0:
            print(objects[0].key)

            if objects[0].leftNode != None:
                objects.append(objects[0].leftNode)
            if objects[0].rightNode != None:
                objects.append(objects[0].rightNode)

            objects.remove(objects[0])


obj = BSTContainer(key = 10)
obj.insertNode(rtNode = obj.rootNode,givenKey = 5)
obj.insertNode(rtNode = obj.rootNode,givenKey = 3)
obj.insertNode(rtNode = obj.rootNode,givenKey = 15)
obj.insertNode(rtNode = obj.rootNode,givenKey = 12)

obj.inOrderTrav(rtNode = obj.rootNode)
obj.searchNode(rtNode = obj.rootNode,searchKey = 15)
obj.bfsTraverse()
