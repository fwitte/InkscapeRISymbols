#!/usr/bin/python

import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw

from drawRIComponents import component


class piping(component):
    # ---------------------------------------------
    def drawPipe(self, parent, position=[0, 0], label='Pipe',
                 direction='right', angleDeg=0):
        """Draw a generic pipe.

        parent: parent object
        position: position [x,y]

        label: label of the object (it can be repeated)
        angleDeg: rotation angle in degrees counter-clockwise (default 0)
        """

    # ---------------------------------------------
    def drawHose(self, parent, position=[0, 0], label='Hose',
                 direction='right', angleDeg=0):
        """Draw a hose.

        parent: parent object
        position: position [x,y]

        label: label of the object (it can be repeated)
        angleDeg: rotation angle in degrees counter-clockwise (default 0)
        """
