
class Node:
    def __init__(self):
        self.data=None
        self.neighbors=[]

class Graph:
    def __init__(self):
        self.root=None
        self.nodes=[]

    def searchForExisitingNode(self, SearchNodeData, SearchNode):
        for x in self.nodes:
            if x.data==SearchNodeData:
                x.neighbors.append(SearchNode)
                return True
        return False

    def getNeighborNodes(self, nodes):
        nodesList = ""
        for x in nodes:            
            nodesList += str(x.data + ",")
        return nodesList    

    def buildGraph(self):
        nodesToAdd=[]
        rootData = input("Enter root data : ")
        rootNode = Node()
        rootNode.data = rootData
        self.root = rootNode
        nodesToAdd.append(rootNode)

        while len(nodesToAdd)>0:
            node = nodesToAdd.pop(0)
            self.nodes.append(node)

            if not node.neighbors:
                neighborCount = int(input("Enter no of neighbors of node {} : ".format(node.data)))
            else:
                nodesList = self.getNeighborNodes(node.neighbors)    
                neighborCount = int(input("Enter no of neighbors of node {} other than {} : ".format(node.data, nodesList)))
            
            for _ in range(neighborCount):
                neighborData = input("Enter neighbor data : ")
                if not self.searchForExisitingNode(neighborData, node):
                    newNode = Node()
                    newNode.data = neighborData
                    newNode.neighbors.append(node)
                    node.neighbors.append(newNode)
                    nodesToAdd.append(newNode)
                    self.nodes.append(newNode)

    def bfs(self):
        root = self.root
        visited,temp = [],[]
        temp.append(root)
        print("BFS : ")
        while len(temp)>0:
            node = temp.pop(0)
            visited.append(node)
            print(node.data, end=" ")
            for x in node.neighbors:
                if x not in visited:
                    temp.append(x)                

graph = Graph()
graph.buildGraph()
graph.bfs()
                   
