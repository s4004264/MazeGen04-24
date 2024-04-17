# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class AdjMatGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        self.vertexDictionary = {}
        self.matrix = []
        



    def addVertex(self, label:Coordinates):
        if label not in self.vertexDictionary: #constant time hash lookup
            self.vertexDictionary[label] = len(self.vertexDictionary) #use the vertex as a key with it's value being it's position in the dictionary
            for i in range(len(self.matrix)):
                self.matrix[i].append(0) #add a 0 to the end of each row, increasing the length by 1
            newRow = [] #create a temp new row to append to the matrix once filled
            if not self.matrix:
                self.matrix.append([0])
            else:
                for i in range(len(self.matrix[0])):
                    newRow.append(0) #fill the temp row
                self.matrix.append(newRow) #append the row to the matrix to make it a square again
        



    def addVertices(self, vertLabels:List[Coordinates]):
        for label in vertLabels:#iterate through the list
            self.addVertex(label)#run the addVertex function on each coordinate in the list
        



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        if vert1 in self.vertexDictionary and vert2 in self.vertexDictionary: #check if the points even exist in the first place
            index1 = self.vertexDictionary[vert1] #get the index of the points from the dictionary
            index2 = self.vertexDictionary[vert2]
            if not addWall: #make sure to not set two verticies with a wall in between to 1
                self.matrix[index1][index2] = 1 #set both [x][y] and [y][x] to 1 as it's an undirected adjacency matrix
                self.matrix[index2][index1] = 1
                return True
        return False
                
    


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        if wallStatus:#check whether to add wall
            if vert1 in self.vertexDictionary and vert2 in self.vertexDictionary:#check whether the points even exist
                index1 = self.vertexDictionary[vert1] #get the index of the points from the dictionary
                index2 = self.vertexDictionary[vert2]
                if vert1.isAdjacent(vert2):#check whether the points are adjacent
                    self.matrix[index1][index2] = 0 #set both to 0 
                    self.matrix[index2][index1] = 0
                    return True
        else:
            if vert1 in self.vertexDictionary and vert2 in self.vertexDictionary:#check whether the points even exist
                index1 = self.vertexDictionary[vert1] #get the index of the points from the dictionary
                index2 = self.vertexDictionary[vert2]
                if vert1.isAdjacent(vert2):#check whether the points are adjacent
                    self.matrix[index1][index2] = 1 #set both to 1
                    self.matrix[index2][index1] = 1
        return False

        



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if self.hasEdge(vert1, vert2):
            index1 = self.vertexDictionary[vert1] #get the index of the points from the dictionary
            index2 = self.vertexDictionary[vert2]
            self.matrix[index1][index2] = 0 #set both [x][y] and [y][x] to 0
            self.matrix[index2][index1] = 0
            return True
        else:
            return False
        
        


    def hasVertex(self, label:Coordinates)->bool:
        if label in self.vertexDictionary:
            return True
        else:
            return False
        



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        index1 = self.vertexDictionary[vert1] #get the index of the points from the dictionary
        index2 = self.vertexDictionary[vert2]
        if self.matrix[index1][index2] == 1 and self.matrix[index2][index1] == 1: #check whether the points are an edge from the matrix
            return True
        else:
            return False
        



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if vert1 in self.neighbours(vert2): #check if verticies are next to each other
            if not self.hasEdge(vert1, vert2): #even though they are next to each other if they don't have an edge then there's a wall there
                return True
            else:
                return False
        else:
            return False
        



    def neighbours(self, label:Coordinates)->List[Coordinates]:
        neighbourList = [] #create empty list
        for temp in self.vertexDictionary: #check each vertex to see if it's adjacent
            if label.isAdjacent(temp):
                neighbourList.append(temp) #if so add to the list
        return neighbourList
        
        