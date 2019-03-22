import numpy

class Scene(object):
    def __init__(self, _xSize, _ySize):
        self.xSize = _xSize
        self.ySize = _ySize

    def generate(self):
        self.scene = numpy.zeros(self.xSize, self.ySize)




