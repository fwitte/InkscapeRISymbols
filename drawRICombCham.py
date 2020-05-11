#!/usr/bin/python

import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw

from drawRIComponents import component


class combustion_chamber(component):
    # ---------------------------------------------
    def drawCombCham(self, parent, position=[0, 0], label='comb_cham',
                    angleDeg=0, comb_chamType='comb_cham'):
        """Draw a combustion chamber.

        parent: parent object
        position: position [x,y]

        label: label of the object (it can be repeated)
        angleDeg: rotation angle in degrees counter-clockwise (default 0)
        """
        group = self.createGroup(parent, label)
        elem = self.createGroup(group)

        # left side
        inkDraw.line.relCoords(
            elem, [[0, self.componentExtent]],
            [position[0],
            position[1] - self.componentExtent / 2],
            lineStyle=self.lineStyle
        )

        # top
        inkDraw.line.relCoords(
            elem, [[self.componentExtent, 0]],
            [position[0],
            position[1] - self.componentExtent / 2],
            lineStyle=self.lineStyle
        )

        # bottom
        inkDraw.line.relCoords(
            elem, [[self.componentExtent, 0]],
            [position[0],
            position[1] + self.componentExtent / 2],
            lineStyle=self.lineStyle
        )

        # right side
        inkDraw.line.relCoords(
            elem, [[0, self.componentExtent]],
            [position[0] + self.componentExtent,
            position[1] - self.componentExtent / 2],
            lineStyle=self.lineStyle
        )

        return group
