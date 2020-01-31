#!/usr/bin/python
import os
from map import Map
import copy

folderAddress = "."
fileName = "test.txt"

class ImportFile:
    AbsoluteAddress = ""

    def __init__(self, folder, filename):
        self.AbsoluteAddress = os.path.join(folder,filename)
        print(self.AbsoluteAddress)

    def openFile(self):
        self.FileObject = open(self.AbsoluteAddress,"r")

    def closeFile(self):
        self.FileObject.close

    def getMaps(self):
        self.openFile()
        mapList = []
        map = self.readMap()
        while map != None:
            mapList.append(copy.deepcopy(map))
            map = self.readMap()
        self.closeFile()
        return mapList

    def readMap(self):
        map = Map()

        fireLocation = self.FileObject.readline().split()
        if(len(fireLocation) == 0):
            return None

        map.setFileLocation(int(fireLocation[0]))
        line = self.FileObject.readline()
        while line:
            corners = line.split()
            if(corners[0] == '0' or corners[1] == '0'):
                return map
            else:
                map.addStreet(int(corners[0]), int(corners[1]))
            line = self.FileObject.readline()
        return None

importTest = ImportFile(folderAddress,fileName)
maps = importTest.getMaps()
print(maps)
for map in maps:
    print map


        


