#!/usr/bin/python

import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw
import numpy as np

from drawRIComponents import component


class compressor(component):
    # ---------------------------------------------
    def drawCompressor(self, parent, position=[0, 0], label='Compressor',
                       direction='right', angleDeg=0,
                       compressorType='generic'):
        """Draw a generic compressor.

        parent: parent object
        position: position [x,y]

        label: label of the object (it can be repeated)
        angleDeg: rotation angle in degrees counter-clockwise (default 0)
        """
        self.radius = self.componentExtent / 2

        group = self.createGroup(parent, label)
        elem = self.createGroup(group)

        inkDraw.line.relCoords(
            elem, [[self.connectorLength, 0]], position,
            lineStyle=self.lineStyle)

        inkDraw.circle.centerRadius(
            elem, [self.connectorLength + self.radius, 0], self.radius,
            offset=position, label='circle', lineStyle=self.lineStyle
        )

        inkDraw.line.relCoords(
            elem, [[self.connectorLength, 0]],
            [position[0] + self.connectorLength + self.radius * 2,
             position[1]],
            lineStyle=self.lineStyle
        )

        x0 = 0.135 * self.radius
        y0 = np.cos(np.arcsin(1 - 0.135)) * self.radius
        dx = 1.46 * self.radius
        dy = np.cos(np.arcsin(1 - 0.405)) * self.radius - y0

        if direction == 'left':
            inkDraw.line.relCoords(
                elem, [[dx, dy]],
                [position[0] + self.connectorLength + x0, position[1] + y0],
                lineStyle=self.lineStyle
            )
            inkDraw.line.relCoords(
                elem, [[dx, -dy]],
                [position[0] + self.connectorLength + x0, position[1] - y0],
                lineStyle=self.lineStyle
            )
        elif direction == 'right':
            inkDraw.line.relCoords(
                elem, [[-dx, dy]],
                [position[0] + self.connectorLength + self.componentExtent - x0, position[1] + y0],
                lineStyle=self.lineStyle
            )
            inkDraw.line.relCoords(
                elem, [[-dx, -dy]],
                [position[0] + self.connectorLength + self.componentExtent - x0, position[1] - y0],
                lineStyle=self.lineStyle
            )

        if angleDeg != 0:
            self.rotateElement(group, position, angleDeg)

        pos_text = [
            position[0] + self.connectorLength + self.radius,
            position[1] - self.componentExtent / (4 * self.scale) -
            self.textOffset * self.scale]

        inkDraw.text.write(
            self, label, pos_text, group, fontSize=self.fontSize,
            justification='center', textStyle=self.textStyle
        )

        return group
