"""
Written by BCl0C, whose code is very damn terrible :).

version 24102024 -> graph class basic ass implementation, bidirectional only.

    Graph class
        introduction
            Graph class was made as basis for graph processing for learning purposes.
            It means i plan to implement all the basic functions and some utils in the process :0
            I'll be using class notes and the book Algorithm Design as support :>
            That's that.

            Will first implement a non-directional version, then i will attempt to implement a
            directional graph. Initally, not class based approach too, very monolitic stuff. Then,
            we'll see about doing something using more classes, like connections and nodes and, finally, 
            a graph class: a small collection of both. 

        initialization of a graph 
            basic usage:
                somegraph = graph([20 30, 30 2, 2 20]) -> this would create a "node" for every unique number and a connection for every unique pair. 
                                                            (As of 22102024, these graphs are NOT directional, meaning 20 30 = 30 20)
                                                        -> this means that it will create n nodes where n is the max number specified. If you need
                                                            23 nodes, for example, pass 23 as the max numbered connection and this will assume you have 23 nodes
                                                            to deal with

            
        notes on the implementation:
            bfs:
                bfs is implemented with a queue, in which the queue is a list and its methods are supposedly enough to deal with the algorithm.
                also, graph has a __visited private variable which stores what exactly was visited for both the bfs and the dfs algorithms.

                running bfs on an initialized graph such as:
                    somegraph.bfsSimple() 
                should return a 3d list structure of the layers.

            dfs: 
                not yet implemented :)
                

        
"""
import numpy as np

def numberDetect(someString: str) -> list: #passed on test battery 1 and is working as intended.
    """
        numberDetect

        input:
            a string with numbers
        output:
            a list of all numbers in the string, if all goes well.

        Usage:
            numberDetect("1283021,84021401") -> [1283021, 84021401]
            numberDetect("ndiwoandiwoan2dnwaodnwi31ohohoh09") -> [2, 31, 9]

        separator usage:
            anything is usable as a separator as long as it is not -, since this will
            be interpreted as a negative number. 
    """
    """
        notes:
            this function will check char for char in a string trying desperately to find a number
            v1 complete, now works
            v2 simplified -> somehow the initial checks for the last digit 
                are meaningless.
                Will probably fuck me over someway somehow when i least expect.
                then i will return to the overcomplicated version, for now this
                is working fine.
            v3 now detects negatives at the cost of - no longer being understood as a separator.
    """
    #initialization

    numberlist = [] #this will hold the extracted numbers
    extracting = "" #this should collect the numbers and stuff for later typecasting.

    #check for every char inside the string and stuff.
    for char in someString:
        if char.isdigit() or char == "-":
            extracting += char
        #when we find something that ain't a number
        elif len(extracting) > 0: #we check to see if we extracted something
            try:
                numberlist.append(int(extracting))
            except:
                print("extracting error, verify usage of - as a separator inside string")
            extracting = ""
    if len(extracting) > 0: #TODO -> fix this algorithm so we don't need the try-excepet chain.
        try: 
            numberlist.append(int(extracting)) #this avoid forgetting the last number and stuff :0
        except:
            print("tried to collect not number. ignored!")
    return numberlist

#tree class moved away from this file
class graph():
    def __init__(self, connectionsInit: list, **kwargs) -> None:
        """
            connectionsInit MUST be a list of numbers separated SOMEHOW.
            this works in pairs, if you fuckup a pair, putting a triad or something, the
            third number gets ignored.
            if connection passed smaller than two, no connection gets made.
            beware of this, it may fuckup what you were trying to do and stuff :)

            example:
                somegraph = graph(["12 30", "11 15", "20 41", "11 11"]) -> this will work fine and create a bunch of connections.

        """
        self.__visited = []                                                                  # <- this will be used when searching and stuff.
        self.__queue =  []                                                                   # <- and so will this!
        self.numNodes = max(max(connectionsInit)) + 1                                           #this depends on an implementation where max will actually go through lists recursively.
        if "debug" in kwargs:
            print(self.numNodes)
        self.connections = [[0 for i in range(self.numNodes)] for i in range(self.numNodes)] #generate the 2d matrix, this is our graph representation.
        
        #this block will operate through every connection passed and assemble our graph.
            #ah yes, if you want this step to run faster, be a good boy and pass a list with bunch of lists with two integers each :)

        for connection in connectionsInit:
            if "debug" in kwargs:
                print("initializing a new connection!")
                print(connection)
            if connection[0] > self.numNodes - 1 or connection[1] > self.numNodes:
                print("out of bounds observed. ignoring...")
                continue 
            self.addConnection(connection)
        self.connectionsCorrector()
       
    def printConnections(self) -> None:
        "prints the connections matrix"
        for connection in self.connections:
            print(connection)

    def __enqueue(self, node: int) -> int:
        """
            enqueue: adds an index to queue

            return codes:
                0 -> success code
                -1 -> failure, somehow. Usually, too much memory being used and stuff. 
        
        
        """
        try:
            self.__queue.append(node)
            return 0 #sucess code
        except:
            return -1
        
    def __dequeue(self, node: int) -> int:
        """
            dequeue: returns the dequeued index

            return codes:
                the expected index -> success code
                -1 -> failure, somehow, usually queue empty
        """
        try:
            return self.__queue.pop(0)
        except:
            return -1
    
    def queueIsEmpty(self):
        """
            returns False when internal queue got something inside
            else returns True
        """
        if len(self.__queue) > 0:
            return False
        return True
    def clearQueue(self):
        self.__queue.clear()
        
    def addConnection(self, someconnection:list):
        """
            adds new connection.
            input should be formatted the same as one would format the initialization input.
            still works with string detection, though.

            what works the same too:
                if you pass a smaller than two connection it gets ignored.
                if you pass a connection greater than two, only the first two numbers gets connected, rest is ignored.
            what does not:
                passing something that would generate a access error gets ignored.
        """
        if not someconnection[0] > self.numNodes - 1 or not someconnection[1] > self.numNodes - 1:        
            if type(someconnection) == str: #when type is string, this will call numberDetect :0
                newConnection: list =  numberDetect(someconnection)
                if len(newConnection) > 1: #if this is not true, connection is never made.
                    self.connections[newConnection[0]][newConnection[1]] = self.connections[newConnection[1]][newConnection[0]] = 1
            elif type(someconnection) == list: #meaning, theoretically, this happened -> ["diwaond1dniwoad2", [2, 3], "39201SEPARATOR4"].
                if len(someconnection) > 1:
                    self.connections[someconnection[0]][self.connections[1]] = self.connections[someconnection[1]][someconnection[0]] = 1

    def severConnection(self, toBeErased: list) -> None: 
        """
            Erases a connection from the graph.

            Input:
                [x,y] connection to be erased
                Not adapted to work with strings!!
            output:
                no output! :0

        """
        self.connections[toBeErased[0]][toBeErased[1]] = self.connections[toBeErased[1]][toBeErased[0]] = 0 

    
    def connectionsCorrector(self) -> None:
        """
            Makes sure no such connections as x<->x!
        """
        for i in range(self.numNodes):
            self.connections[i][i] = 0 

                
    def nodeIsConnected(self, x:int, y:int) -> int:
        """
            this supposedly works the same for directional graphs.
            Don't know, didn't bother to test, beware, yadda yadda.

            usage:
                (assume a graph with connections 1<->2 and 2<->3)
                graph.nodeIsConnected(1, 2) -> true
                graph.nodeIsConnected(3, 1) -> false
                graph.nodeIsConnected(4, 1) -> prints out of bounds, returns false. 

            codes:
                1  -> is connected!
                0  -> is NOT connected!
                -1 -> parameters passed out of graph bounds!
        """
        if x > self.numNodes or y > self.numNodes:
            print("out of bounds!")
            print("x: ", x, "y: ", y)
            print("max x-y expected: ", self.numNodes)
            return -1
        if self.connections[x][y]:
            return 1
        
        return 0
    
    def clearVisited(self):
        self.__visited.clear() #simple as

    def isVisited(self,nodePosit: int):
        if nodePosit in self.__visited:
            return True
        return False
    
    def visit(self, nodePosit: int) -> None:
        if nodePosit not in self.__visited:
            self.__visited.append(nodePosit)
        
    
    def getVisited(self) -> list:
        """
            get visited -> returns the visited nodes from last method runned.

            usage:
                #run something on the graph that needs the visited
                somegraph.bfs()
                #then, we'd like to see the order of visited things!
                visits = somegraph.getVisited()
                print(visits)
                $[1,2,3,5,6,...] -> this would most probably be very different if we runned a dfs on whatever this bfs runned on. 
                    #on this example, the graph might look something like 1->2;1->3;1->5;2->6 and so on. 

        """
        return self.__visited

    def cleanup(self) -> None:
        self.clearQueue()
        self.clearVisited()

    def bfsSimple(self): 
        """
            bfs method
                provides a basic breadth-first searching algorithm
                is prepared to handle the graph class and will probably not work with
                a simple 2d matrix, since it uses the visited private attribute.
            input:
                start -> must be an int, represents the starting index of the search. If n
                end -> execution stops when reaching this value. If left untouched, will not stopped until entire graph was visited.
            usage:
                #initialize a graph
                somesimplegraph = graph([[1,2],[2,3],[3,4],[1,3]])
                #then, search through it:
                path1 = somesimplegraph.bfs() 
            
            about the return value:
                this will return a list organized by layers.
                Example 1:
                    say a given graph is connected like 1->2, 1->3, 2->4, 3->4
                    then, calling a bfs on this graph should return:
                    [[[1],[2,3],[4]]]
                    We would know the connections by calling the original graph again.
                Reading this information is as follows
                GRAPH0
                    [
                        [TREE0
                            [LAYER0],
                            [LAYER1],
                            ...
                        ]
                        [TREE1
                            [LAYER0],
                            [LAYER1],
                        ...]
                    ]
                Where if a given graph got more than 1 tree, there are unconnected paths and
                every layer 0 got no more than 1 node, the root.
                This 3d structure should be useful to find the precise layers and how many trees 
                are inside this graph, precisely.
            
            about the implementation:
                it uses a queue implementation bc i really don't wanna find
                out this Mike Foxtrot Foxtrotted Up during the recursion and 
                stuff since its a class. 
                Will test if it does when we implement dfs. That oughta Foxtrot up
                quite bad. 
        """
        self.cleanup() #makes sure initial queues are clean and stuff.
        analisys = []
        tree = []
        layer = []
        for i in range(len(self.connections)):
            tree.clear()
            lastnode: int
            if not self.isVisited(i): #means we process for all indexes not visited. After first execution, will always search for not visited indexes.
                self.visit(i)
                self.__enqueue(i)
                tree.append([i]) #adds root as first layer of the tree 
                lastnode = i
            while not self.queueIsEmpty():
                thisNode = self.__dequeue()
                for z in len(self.connections[thisNode]):
                    if self.connections[thisNode][z] and not self.isVisited(z):
                        self.visit(z)
                        self.__enqueue(z)
                        
                tree.append(layer)
            if len(tree) > 0: #added because an empty tree might be added in case that for passes through something already visited :0
                analisys.append(tree)



                
            
                
                
def getRandomGraph(seed: int = 3) -> graph:
    pass

def generateGridGraph(resolution) -> graph:
    pass
        
if __name__ == "__main__":
    #EXECUTING THIS FILE AS MAIN RESULTS IN A BATTERY OF TESTS! :)
    #GRAB POPCORN AND STUFF!!! :O
    print("executed as main, running testings")
    print("TESTING 1: numberDetect testing")
    failed = 0
    i = -1
    b = [[839213, 8021],
         [83, 84, 85, 86],
         [90, 90, 90, 80, 34, 63, 888, 4, 4, 4, 4],
         [81, 90, 88, 4018, 8, 3],
         [5241, 5801],
         [-43, -88]
        ]
    a = []
    a.append(numberDetect("839213, 8021"))
    a.append(numberDetect("83, 84, 85, 86"))
    a.append(numberDetect("90,90,90    80, 34, 63    888, 4 4 4 4"))
    a.append(numberDetect("nidowa81nidw90kek88,4018omi8three3"))
    a.append(numberDetect("ndiwoa5241dniwoa5801oiwaio"))
    a.append(numberDetect("-43zetta-88"))

    ##this basic template can easily be used to auto check a large number of stuff :)
    for expectation, reality in zip(a, b):
        i += 1 #used for failure
        if expectation != reality:
            failed = 1
            break
    if failed == 1:
        print("found error in" , i , "position :/")
        print("expectation: " , b[i])
        print("reality: " ,  a[i])
    else:
        print("test 1 passed successfully!")
        print("Gathered numbers:")
        print(a)
        print("expected numbers:")
        print(b)
    
    print("test 1 finished...")

    print("TESTING 2: no connection graph initialization")
    numNodes = max(
        max(
                [
                    [1,2],
                    [2,3],
                    [4,5],
                    [1,1,1,1,6]
                ]
            )
        ) #testing max recursiveness. 
    print(numNodes)
    print([[0 for i in range(numNodes)] for i in range(numNodes)]) #per tested, max needs to be max(max()) to extract actual 2d value!
    print("testing 2 finished...")
    print("TESTING 3: usage of popleft list queue")
    somelist: list = [1,2,3]
    print("original list: " , somelist)
    somelist.append(4)
    print("print list after append: ")
    print(somelist)
    #print(somelist.popleft()) #ah yeah, this does NOT work :/
    print("poping first item (pop left): ")
    print(somelist.pop(0)) #this should, though...
    print("list object after 'popage': ")
    print(somelist)
    print("testing 3 finished!")
    print("TESTING 4: graph initialization")
    newgraph = graph([[0,1], [1,2], [2,0]], debug=1)
    newgraph.printConnections()
    print("testing 4 finished...")

