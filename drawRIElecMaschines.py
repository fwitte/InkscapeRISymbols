#!/usr/bin/python

import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw

from drawRIComponents import component

from numpy import sqrt, sin, cos, pi

class elec_maschine(component):
    # ---------------------------------------------
    def drawElecMaschine(self, parent, position=[0, 0], label='elec_maschine',
                    direction='right', elec_maschineType='elec_maschine'):
        """Draw a generator and electrical motor.

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
            elem, [self.radius, 0], self.radius,
            offset=position, label='circle', lineStyle=self.lineStyle
        )

        # choose elec maschine type
        if elec_maschineType == 'generator':
            pos_text = [position[0] + self.radius, position[1] + 1.5]

            inkDraw.text.write(
                self, 'G', pos_text, group, fontSize=self.fontSize,
                justification='center', textStyle=self.textStyle
            )

        elif elec_maschineType == 'motor':
            pos_text = [position[0] + self.radius, position[1] + 1.5]

            inkDraw.text.write(
                self, 'M', pos_text, group, fontSize=self.fontSize,
                justification='center', textStyle=self.textStyle
            )

        # direction
        if direction == 'right':
            inkDraw.line.relCoords(
                elem, [[- self.connectorLength - self.radius * (1-cos(pi/24)), 0]],
                [position[0] + self.radius * (1-cos(pi/24)),
                 position[1] - self.radius * sin(pi/24)],
                lineStyle=self.lineStyle
            )

            inkDraw.line.relCoords(
                elem, [[- self.connectorLength - self.radius * (1-cos(pi/24)), 0]],
                [position[0] + self.radius * (1-cos(pi/24)),
                 position[1] + self.radius * sin(pi/24)],
                lineStyle=self.lineStyle
            )

        elif direction == 'left':
            inkDraw.line.relCoords(
                elem, [[self.connectorLength + self.radius * (1-cos(pi/24)), 0]],
                [position[0] + self.componentExtent - self.radius * (1-cos(pi/24)),
                 position[1] - self.radius * sin(pi/24)],
                lineStyle=self.lineStyle
            )

            inkDraw.line.relCoords(
                elem, [[self.connectorLength + self.radius * (1-cos(pi/24)), 0]],
                [position[0] + self.componentExtent - self.radius * (1-cos(pi/24)),
                 position[1] + self.radius * sin(pi/24)],
                lineStyle=self.lineStyle
            )

        return group
