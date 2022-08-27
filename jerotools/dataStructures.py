class nodeG():
    def __init__(self,destino, weight):
        self.destino=destino
        self.weight=weight
        self.next=None
class nodeLl:
    def __init__(self, val):
        self.val = val
        self.next = None
class binTreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class nAryTree:
	def __init__(self,val):
		self.key=val
		self.child=[]

def nodeExists(node, val):
    if (node == None):
        return False
    elif (node.val == val):
        return True
    #siga buscando en el lado izquierod
    if nodeExists(node.left, val):
        return True
    #busque en el lado derecho
    return nodeExists(node.right, val)
		
class graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.graph={}
        
        for vertice in range(nVertices):
            self.graph[vertice]=[] 
            
    def addEdges(self,source,dest, weight):
        vertice=nodeG(dest, weight) 
        vertice.next=self.graph[source]
        self.graph[source]= vertice

	def printGraph(self):
		for vertice in self.g: #Cambiar la funcion imprimir que imprima todos los destinos. Falta eso
			print("Dato: "+str(vertice)+" Peso: "+str(self.graph[vertice].weight)+ " ->  " + str(self.graph[vertice].destino)) 
        

class linkedList:
    def __init__(self):
        self.head = None
    def add(self,data):
        newNode=nodeLl(data)
        if self.head:
            current=self.head
            while current.next:
                current=current.next
            current.next=newNode
        else:
            self.head=newNode
    def madd(self,*data):
        for i in data:
            newNode=nodeLl(i)
            if self.head:
                current=self.head
                while current.next:
                    current=current.next
                current.next=newNode
            else:
                self.head=newNode
