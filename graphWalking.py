import queue
class Node:
    def __init__(self):
        self.data=None
        self.neighbors=[]

class Graph:
    
    def __init__(self):
        self.root=None

    def getNodeData(self,nodesList):
        nodeData=""
        for x in nodesList:
            nodeData+=("," + str(x.data))
        return nodeData[1:]        


    def insert(self):
        nodes=queue.Queue()
        rootData=int(input("Enter root node : "))
        node = Node()
        node.data=rootData
        self.root=node
        nodes.put(node)              
        while not nodes.empty():
            nodeExists=False
            node = nodes.get()
            if len(node.neighbors)==0:
                connections=int(input("Enter the number of connections from/to node {} : ".format(node.data)))
            else:
                connections=int(input("Enter the number of connections from/to node {} other than node(s) {} : ".format(node.data, self.getNodeData(node.neighbors))))
            for _ in range(connections):
                connectionNodeData=int(input("Enter connection node data : "))
                if connectionNodeData==0:
                    break
                for n in nodes.queue:
                    if n.data==connectionNodeData:
                        n.neighbors.append(node)
                        nodeExists=True
                if nodeExists==False:    
                    connectionNode = Node()
                    connectionNode.data=connectionNodeData
                    connectionNode.neighbors.append(node)
                    node.neighbors.append(connectionNode)
                    nodes.put(connectionNode)

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
graph.insert()
graph.bfs()

