# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class AdjListGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        self.vertexDictionary = {} #create the adjacency dictionary of coordinate as the key and a list as the value



        
    def addVertex(self, label:Coordinates):
        if label not in self.vertexDictionary: #if the coord hasn't been added already
            self.vertexDictionary[label] = {} #create a blank dictionary as the value with the coord as the key




    def addVertices(self, vertLabels:List[Coordinates]):
        for label in vertLabels:#iterate through the list
            self.addVertex(label)#run the addVertex function on each coordinate in the list



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        if vert1.isAdjacent(vert2): #check if the points are adjacent
            self.vertexDictionary[vert1][vert2] = addWall #append each point to the other's adjacency dictionary with the value of the relationship being whether there is a wall or not
            self.vertexDictionary[vert2][vert1] = addWall
            return True
        return False
        


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        if wallStatus:#check whether to add wall
            if self.hasEdge(vert1, vert2):#check whether the points are an edge
                self.vertexDictionary[vert1][vert2] = True #append each point to the other's adjacency dictionary with the value of the relationship being whether there is a wall or not
                self.vertexDictionary[vert2][vert1] = True
                return True
        else:
            if self.hasEdge(vert1, vert2):#check whether the points are an edge
                self.vertexDictionary[vert1][vert2] = False #append each point to the other's adjacency dictionary with the value of the relationship being whether there is a wall or not
                self.vertexDictionary[vert2][vert1] = False
        return False
        pass



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if self.hasEdge(vert1, vert2): #check if an edge exists
            self.vertexDictionary[vert1].remove(vert2) #remove vert2 from vert1's list and vice versa
            self.vertexDictionary[vert2].remove(vert1)
            return True
        else:
            return False
        


    def hasVertex(self, label:Coordinates)->bool:
        if label in self.vertexDictionary:
            return True
        else:
            return False
        pass



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if vert1 in self.vertexDictionary[vert2] and vert2 in self.vertexDictionary[vert1]:
            return True
        else:
            return False
 


    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if vert1 in self.neighbours(vert2): #check if verticies are next to each other
            if self.vertexDictionary[vert1][vert2] == True and self.vertexDictionary[vert2][vert1] == True: #if the value of the relationship is true there is a wall
                return True
            else:
                return False
        else: #if they are not adjacent there is no wall
            return False
        
    


    def neighbours(self, label:Coordinates)->List[Coordinates]:
        neighbourList = [] #create empty list
        for temp in self.vertexDictionary[label]: #check each vertex to see if it's adjacent
            neighbourList.append(temp) #if so add to the list
        return neighbourList
        