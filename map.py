#!/usr/bin/python
class Map:
    StreetCorners = {}
    FireLocation = 0

    def addStreet(self, corner1, corner2):
        if corner1 in self.StreetCorners.keys():
            self.StreetCorners[corner1].append(corner2)
        else:
            self.StreetCorners[corner1] = [corner2]

        if corner2 in self.StreetCorners.keys():
            self.StreetCorners[corner2].append(corner1)
        else:
            self.StreetCorners[corner2] = [corner1]

    def setFileLocation(self, fireLocation):
        self.FireLocation = fireLocation

    def __str__(self):
        print self.StreetCorners
        return ''
            
