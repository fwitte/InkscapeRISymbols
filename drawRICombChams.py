#!/usr/bin/python

import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw

from drawRIComponents import component

from numpy import sqrt, sin, cos, pi

class combustion_chamber(component):
    # ---------------------------------------------
    def drawCombCham(self, parent, position=[0, 0], label='comb_cham',
                     angleDeg=0, direction='top', comb_chamType='comb_cham'):
        """Draw a combustion chamber.

        parent: parent object
        position: position [x,y]

        label: label of the object (it can be repeated)
        angleDeg: rotation angle in degrees counter-clockwise (default 0)
        """
        group = self.createGroup(parent, label)
        elem = self.createGroup(group)

        # define radius of main circle
        self.radius = self.componentExtent / 2

        # draw main circle
        inkDraw.circle.centerRadius(
            elem, [self.radius, 0], self.radius * 0.8,
            offset=position, label='circle', lineStyle=self.lineStyle
        )

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

        # diagonally top right
        inkDraw.line.relCoords(
            elem, [[self.radius * 0.8 * 2 / sqrt(2),
                    - self.radius * 0.8 * 2 / sqrt(2)]],
            [position[0] + self.radius * (0.8 * (1 - cos(pi/4)) + 0.2),
             position[1] + self.radius * 0.8 * sin(pi/4)],
            lineStyle=self.lineStyle
        )

        # diagonally down left
        inkDraw.line.relCoords(
            elem, [[self.radius * 0.8 * 2 / sqrt(2),
                    self.radius * 0.8 * 2 / sqrt(2)]],
            [position[0] + self.radius * (0.8 * (1 - cos(pi/4)) + 0.2),
             position[1] - self.radius * 0.8 * sin(pi/4)],
            lineStyle=self.lineStyle
        )

        # connector left
        inkDraw.line.relCoords(
            elem, [[- self.connectorLength, 0]],
            position,
            lineStyle=self.lineStyle
            )

        # connector right
        inkDraw.line.relCoords(
            elem, [[self.connectorLength, 0]],
            [position[0] + self.componentExtent, position[1]],
            lineStyle=self.lineStyle
            )

        if direction == 'top':
            # connector up
            inkDraw.line.relCoords(
                elem, [[0, - self.connectorLength]],
                [position[0] + self.radius, position[1] - self.radius],
                lineStyle=self.lineStyle
            )

        elif direction == 'down':
            # connector up
            inkDraw.line.relCoords(
                elem, [[0, + self.connectorLength]],
                [position[0] + self.radius, position[1] + self.radius],
                lineStyle=self.lineStyle
            )

        # Roating components
        if angleDeg != 0:
            self.rotateElement(group, position, angleDeg)

        # Labeling
        pos_text = [
            position[0] + self.componentExtent,
            position[1] - self.componentExtent]

        inkDraw.text.write(
            self, label, pos_text, group, fontSize=self.fontSize,
            justification='left', textStyle=self.textStyle
        )

        return group
