"""
Written by BCl0C, whose code is very damn terrible :).

version 24102024 -> graph class basic ass implementation, bidirectional only.
version 27102024 -> most of bfs implemented, not yet useful.
version 30102024 -> bfs implemented, working, returns a useful 

Who exactly is "we" as used along most of the documentation and commentary:
    "We" is no less than us, you, the reader and me, the terrible ass programmer. 
    When used, "We" refers to our cooperative effort to understand What In the FOXTROT
    is going on.

    Example:
        Then, we may use this piece of code here to get what we need. 
    
    This is made so you can always feel my presence onto your walls.

0th warning:
    As one might've noticed, lots of curse words are used during 
    commenting of the code. 
    To avoid major consequences, they are censored using a modified NATO phonetic
    alphabet (papa -> phantom)
    keep this in mind whenever finding something like FOXTROTUNIFORM in the code, 
    this was a curse phrase. And one of the most common, at that, since it describes
    what happens when someone misuses the code or follow the instructions wrong.

    A compreehensive list of usual usage of this is as follows:
        FOXTROTUNIFORM -> the result of bad or incorrect usage, which makes me proud,
            since i go by badCode;
        BETAALPHAMIKEFOXTROT -> someone despicable;
        CHARLIEFOXTROT -> similar to foxtrot uniform;
        MIKEFOXTROTUNIFORM -> A bigger foxtrot uniform.

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
                                                            (As of 27102024, these graphs are NOT directional, meaning 20 30 = 30 20)
                                                        -> this means that it will create n nodes where n is the max number specified. If you need
                                                            23 nodes, for example, pass 23 as the max numbered connection and this will assume you have 23 nodes
                                                            to deal with

            
        notes on the implementation:
            bfs:
                bfs is implemented with a queue, in which the queue is a list and 
                its methods are supposedly enough to deal with the algorithm.
                also, graph has a __visited private variable which stores what exactly was
                visited for both the bfs and the dfs algorithms.

                running bfs on an initialized graph such as:
                    somegraph.bfsSimple() 
                should return a 3d list structure of the layers.
                    which is generated from the visited list.
            
            layerfinder:
                it is the function that actually finds the layers and organizes the 
                3d structure.
                Might need more versions, since one could modify the visited 
                structure, which would majorly FOXTROT UNIFORM the entire algorithm.

            dfs: 
                not yet implemented :)

            why the visit method is not private:
                ah yes, this is useful to prevent bfs from going somewhere unwanted.
                the expense would be that layerfinder would MIKEFOXTROTUNIFORM and provide 
                unreliable output...
        
    Utils: what are they, where they live and how to bury them many feet under.
        numberDetect
            Attempts to find numbers inside a string. Might not work with some special
            string forms, have not found them yet and therefore have no way to fix it 
            to run better. 

        recursiveMax
            attempts to find the greatest number inside a n-dimensional list, meaning
                [[[[...[some Foxtrot number]...]]]]
            Since max would simply return the list containing such a number, probably
            by scanning memory and then giving you a pointer to the bloody list.
            Not very great for graph purposes, since to know how many such nodes exist,
            we use the greatest index possible.

        curseUser
            Attempts to hurt the psychological aspects of the user by attacking
            his mental state.
            Calls the user a f-bamf (FOXTROT BETA ALFA MIKE FOXTROT).
            By all means, if you see the curse user message, do not attempt
            to use the function that generated it.
            It is most probably something not done.
    
"""

def curseUser():
    """
        sends a nice curse to the user when he tries to use something not ready.
    """
    print("why In The foxtrot(!) ye're trying to use the prototype, not even close to be completed function,\n\
           ye mikeFoxtrot, ye Foxtrot Beta Alpha Mike Foxtrot (F-BAMF!)")
    
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

def recursiveMax(nDimensionalList: list) -> int: #TODO -> TEST TO SEE IF PYTHON WILL DESTROY THE DATA INSIDE NDIMENSIONALLIST IN THIS ALGORITHM!!!!.
    """
    Simple ass algorithm to find the max number inside a ndimensional list.
    Uses max recursively.
    Useful to assemble graph structure without need to pass a number of nodes.
    
    usage:
        recursiveMax([[1,2,3],[4,5,6]]) -> 6
            in comparison, while very Foxtrot cool that 
            calling max on this same list would return:
                [4,5,6]
            this would FoxtrotUniform later algorithms, 
            such as the initialization of the graph object.

    Expectations on how this works:
        Since calling len() on a type int is a bad foxtrot'ng idea,
        one might use this to his advantage to create a breakpoint.
    
    Other possible implementations:
    
    possible expansions:
    """

    try:
        g = max(nDimensionalList)
    except:
        return nDimensionalList #if failure in the above, usually caused by finding an int.
    return recursiveMax(g)
    

#tree class moved away from this file

#### GRAPH CLASS ###########

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
            
            input: 
                a list of connections properly formatted.
            
            output:
                a graph object
            
            keywords:
                debug -> will activate some of the debugging messages and stuff.
            

        """
        self.__visited = []                                                                  # <- this will be used when searching and stuff.
        self.__queue =  []                                                                   # <- and so will this!
        self.numNodes = max(max(connectionsInit)) + 1                                           #this depends on an implementation where max will actually go through lists recursively.
        if "debug" in kwargs:
            print(self.numNodes)
        self.connections = [[0 for i in range(self.numNodes)] for i in range(self.numNodes)] #generate the 2d matrix, this is our graph representation.
        
        # this block will operate through every connection
        # passed and assemble our graph.
        # ah yes, if you want this step to run faster, 
        # be a good boy and pass a list with bunch of 
        # lists with two integers each :)
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
        """
            prints the connections matrix and stuff. 
            simple as.
        """
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
        
    def __dequeue(self) -> int:
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
        if not someconnection[0] > self.numNodes - 1 or not someconnection[1] > self.numNodes - 1:      #this would generate the big ass access error :>  
            if type(someconnection) == str:                                                             #when type is string, this will call numberDetect :0
                newConnection: list =  numberDetect(someconnection)
                if len(newConnection) > 1:                           #connections are made when at least two ints detected!
                    self.connections[newConnection[0]][newConnection[1]] = \
                    self.connections[newConnection[1]][newConnection[0]] = 1
            elif type(someconnection) == list:                       #meaning, theoretically, this happened -> ["diwaond1dniwoad2", [2, 3], "39201SEPARATOR4"].
                if len(someconnection) > 1:
                    self.connections[someconnection[0]][someconnection[1]] = \
                    self.connections[someconnection[1]][someconnection[0]] = 1

    def severConnection(self, toBeErased: list) -> None: 
        """
            Erases a connection from the graph. Bidirectionally.

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

    def bfsSimple(self) -> list: 
        """
            bfs method
                provides a basic breadth-first searching algorithm
                is prepared to handle the graph class and will probably not work with
                a simple 2d matrix, since it uses the visited private attribute.
            input:
                noinput! -> this function will visit the entire graph finding whatever it can.
            usage:
                #initialize a graph
                somesimplegraph = graph([[1,2],[2,3],[3,4],[1,3]])
                #then, search through it:
                path1 = somesimplegraph.bfs() 
            
            about the return value:
                This was the original idea:
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
                I've decided to discard this bullshit return value, now it should return the non-discarded connections as such:
                    [[1,4],[1,2],[1,5],[2,6],...]
                    this may be used to create a new and simplified graph!
            
            about the implementation:
                it uses a queue implementation bc i really don't wanna find
                out this Mike Foxtrot Foxtrotted Up during the recursion and 
                stuff since its a class. 
                Will test if it does when we implement dfs. That oughta Foxtrot up
                quite bad. 
        """
        self.cleanup()                          #makes sure initial queues are clean and stuff.
        bfsconnections = []
        for i in range(len(self.connections)):
            if not self.isVisited(i):           #means we process for all indexes not visited. After first execution, will always search for not visited indexes.
                self.visit(i)
                self.__enqueue(i)
            while not self.queueIsEmpty():
                thisNode = self.__dequeue()
                for z in range(len(self.connections[thisNode])):
                    if self.connections[thisNode][z] and not self.isVisited(z):
                        self.visit(z)
                        self.__enqueue(z)
                        bfsconnections.append([thisNode, z]) 
        return bfsconnections #THERE MUCH SIMPLER NOW!!!!
    
    def bfsStart(self, start: int): 
        """
            basically the same as bfs simple, basic change is we do not have something 
            like the funky range used in bfs simple, this guy here will assemble a single
            tree. As soon as the queue dries up, so does the rest of the algorithm.

            Also, this will only create a single tree, not searching unconnected nodes to the 
            root passed, meaning that start parameter. 

            input:
                start: int 
                    -> index of node to be used as tree root
            
            output:
                bfsconnections: list
                    -> list of connections found, may be passed onto a new graph object.

        """
        self.cleanup()
        bfsconnections = []
        self.visit(start)
        self.__enqueue(start) 
        while not self.queueIsEmpty():
            thisNode = self.__dequeue()
            for z in len(self.connections[thisNode]):
                if self.connections[thisNode][z] and not self.isVisited(z):
                    self.visit(z)
                    self.__enqueue(z)
                    bfsconnections.append([thisNode, z]) 
        return bfsconnections #THERE MUCH SIMPLER NOW!!!!
    
    def bfsStartEnd(self, start: int, end: int):
        """
            This one will assemble no more than a tree and will end 
            as soon as it finds the MikeFoxtrot it needs. 

            If it can't find the mikeFoxtrot, it will return the 
            complete root to leaf of a tree on the graph.
            At the very least, it is both somewhat easy to verify
            if it found the desired node.
            
            usage:
                path = g.bfsStartEnd(0, 5)
                if 5 in path:
                    print("Found!")

            input:
                start -> the node to be searched first, the tree root. 
                end   -> the node to stop execution after finding. 

            notes on implementation:
                see that there is no more than a single for in the code
                below.
                That will prevent the algorithm from searching one more tree.     
    
                
        """
        self.cleanup()
        bfsconnections = []
        self.visit(start)
        self.__enqueue(start) 
        while not self.queueIsEmpty():
            thisNode = self.__dequeue()
            if thisNode == end:
                self.visit(thisNode)
                break #if we found our guy, no point in continuing, if he got enqueued, his connection was very much found and stuff. 
            for z in len(self.connections[thisNode]):
                if self.connections[thisNode][z] and not self.isVisited(z):
                    self.visit(z)
                    self.__enqueue(z)
                    bfsconnections.append([thisNode, z]) 
        return bfsconnections #THERE MUCH SIMPLER NOW!!!!
    
    def bfs(self, start: int = 0, end: int = 0): #general bfs, prepared to receive both a start end
        if start == 0:
            self.bfsSimple()
        elif start != 0:
            self.bfsStart(start)
        elif start*end != 0:
            self.bfsStartEnd(start, end)

    def dfsSimple(self): #TODO
        """
            much of the same as bfsSimple, though now we run a dfs on this badman.
            this function WILL run for all possible paths.

            input:
                noinput :> -> requires only a graph object
            output:
                dfsConnections -> a list of connections, made from running the algorithm.
                    may be transplanted onto a new graph with some severed connections and 
                    stuff!
            
            notes:
                though in class professor taught us the recursive version, i took upon myself
                to see an iterative version through. For this, we'll be using only the pseudo code
                and stuff. 
        """
        curseUser() #not ready for usage, therefore cursing the user, as usual.
        return ["leSsex"]
        self.cleanup()
        dfsConnections = []
        for i in range(len(self.connections)): #this guy checks for roots and stuff. As it runs first, setting the starter node is merely a factor of setting the starting length.
            if not self.isVisited(i):
                self.visit(i)
                self.__enqueue(i)
            while not self.queueIsEmpty(): #runs when queue not empty! -> this guy visits a lot, so it is supposed to take the longest.
                this = self.__dequeue()                     
        pass

    
#### END OF GRAPH CLASS ####

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
    """
    max behaviour veredict:
        it seems to search for the list with the greatest number, but no such thing as 
    """
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
    
    print("TESTING 5: running a bfs on the graph")
    print(newgraph.bfsSimple())

    print("TESTING 6: recursiveMax")
    somerandomasslist = [[[1],[2]],[[3],[4]],[[5],[6]]] #terrible 3d list :0
    print(recursiveMax(somerandomasslist))
    print(somerandomasslist)


