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
    if len(extracting) > 0: numberlist.append(int(extracting)) #this avoid forgetting the last number and stuff :0
    return numberlist

class tree(): 
    def __init__() -> None:
        pass


class graph():
    def __init__(self, connectionsInit: list) -> None:
        """
            connectionsInit MUST be a list of numbers separated SOMEHOW.
            this works in pairs, if you fuckup a pair, putting a triad or something, the
            third number gets ignored.
            if connection passed smaller than two, no connection gets made.
            beware of this, it may fuckup what you were trying to do and stuff :)

            example:
                somegraph = graph(["12 30", "11 15", "20 41", "11 11"]) -> this will work fine and create a bunch of connections.

        """
        #self.numNodes = numNodes                                                       #would be necessary in a c implementation. Not quite inside python.
        self.__visited = []                                                                 #this will be used when searching and stuff. 
        self.numNodes = max(max(connectionsInit))                                                #this depends on an implementation where max will actually go through lists recursively.
        self.connections = [[0 for i in range(self.numNodes)] for i in range(self.numNodes)] #generate the 2d matrix, this is our graph representation.
        
        #this block will operate through every connection passed and assemble our graph.
            #ah yes, if you want this step to run faster, be a good boy and pass a list with bunch of lists with two integers each :)

        for connection in connectionsInit:
            if connection[0] > self.numNodes - 1 or connection[1] > self.numNodes:
                print("out of bounds observed. ignoring...")
                continue 
            if type(connection) == str: #when type is string, this will call numberDetect :0
                newConnection: list =  numberDetect(connection)
                if len(newConnection) > 1: #if this is not true, connection is never made.
                    self.connections[newConnection[0]][newConnection[1]] = self.connections[newConnection[1]][newConnection[0]] = 1
            elif type(connection) == list: #meaning, theoretically, this happened -> ["diwaond1dniwoad2", [2, 3], "39201SEPARATOR4"].
                if len(connection) > 1:
                    self.connections[connection[0]][self.connections[1]] = self.connections[connection[1]][connection[0]] = 1

    def addConnection(self, someconnection:list):
        """
            adds new connection(s).
            input should be formatted the same as one would format the initialization input.
                then something as [[1,2],[2,3],[3,4],...]

            what works the same too:
                if you pass a smaller than two connection it gets ignored.
                if you pass a connection greater than two, only the first two numbers gets connected, rest is ignored.
            what does not:
                passing something that would generate a access error gets ignored.
        """
        for connection in someconnection:
            if connection[0] > self.numNodes or connection[1] > self.numNodes - 1:
                continue #meaning it would fuckup and therefore it gets very fucking ignored :)
            if type(connection) == str: #when type is string, this will call numberDetect :0
                newConnection: list =  numberDetect(connection)
                if len(newConnection) > 1: #if this is not true, connection is never made.
                    self.connections[newConnection[0]][newConnection[1]] = self.connections[newConnection[1]][newConnection[0]] = 1
            elif type(connection) == list: #meaning, theoretically, this happened -> ["diwaond1dniwoad2", [2, 3], "39201SEPARATOR4"].
                if len(connection) > 1:
                    self.connections[connection[0]][self.connections[1]] = self.connections[connection[1]][connection[0]] = 1

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
    
    def visited(self,nodePosit: int):
        if nodePosit in self.__visited:
            return True
        return False
    
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

    
    def bfs(self, start: int = 0, end: int = -1): 
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
                this will return a new graph with some cut connections.
                Useful to find least distance paths.
            
            about the implementation:
                it uses a queue implementation bc i really don't wanna find
                out this Mike Foxtrot Foxtrotted Up during the recursion and 
                stuff since its a class. 
                Will test if it does when we implement dfs. That oughta Foxtrot up
                quite bad. 
        """

        self.__visited.clear()       #clears last run of any algorithm
        self.__visited.append(start) #start always gets visited first
        queue = []
        if end == -1: #means it should run for the entire graph
            queue.append(start)
            for i in range(len(self.connections)):
                pass
        else:
            pass

        
                

def getRandomGraph(seed: int = 3) -> graph:
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


