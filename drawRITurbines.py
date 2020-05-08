#!/usr/bin/python

import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw

from drawRIComponents import component
import numpy as np

class turbine(component):
    # ---------------------------------------------
    def drawTurbine(self, parent, position=[0, 0], label='Turbine',
                    connection='crossed', mirroring='mirOff',
                    extraction='extrOff', turbineType='turbine'):
        """Draw a turbine.

        parent: parent object
        position: position [x,y]

        label: label of the object (it can be repeated)
        angleDeg: rotation angle in degrees counter-clockwise (default 0)
        """
        group = self.createGroup(parent, label)
        elem = self.createGroup(group)

        # left side
        inkDraw.line.relCoords(
            elem, [[0, self.componentExtent * 1.5]],
            position, lineStyle=self.lineStyle
        )

        # diagonally top right
        inkDraw.line.relCoords(
            elem, [[self.componentExtent * 1.5, - self.componentExtent / 2]],
            position,
            lineStyle=self.lineStyle
        )

        # diagonally down left
        inkDraw.line.relCoords(
            elem, [[self.componentExtent * 1.5, self.componentExtent / 2]],
            [position[0],
             position[1] + self.componentExtent * 1.5],
            lineStyle=self.lineStyle
        )

        # right side
        inkDraw.line.relCoords(
            elem, [[0, self.componentExtent * 2.5]],
            [position[0] + self.componentExtent * 1.5,
            position[1] - self.componentExtent / 2],
            lineStyle=self.lineStyle
        )

        # label position
        pos_text = [
            position[0] + self.componentExtent * 1.5 + (3 * self.scale),
            position[1] + self.componentExtent / (4 * self.scale) -
            self.textOffset * self.scale]

        inkDraw.text.write(
            self, label, pos_text, group, fontSize=self.fontSize,
            justification='left', textStyle=self.textStyle
        )

        if connection == 'crossed':
            if mirroring == 'mirOff':
                # inlet crossed - no mirror
                inkDraw.line.relCoords(
                    elem, [[0, - self.connectorLength]],
                    position,
                    lineStyle=self.lineStyle
                )

                # outlet crossed - no mirror
                inkDraw.line.relCoords(
                    elem, [[0, self.connectorLength]],
                    [position[0] + self.componentExtent * 1.5,
                    position[1] + self.componentExtent * 2],
                    lineStyle=self.lineStyle
                )

            if mirroring == 'mirOn':
                # inlet crossed - mirror
                inkDraw.line.relCoords(
                    elem, [[0, + self.connectorLength]],
                    [position[0],
                    position[1] + self.componentExtent * 1.5],
                    lineStyle=self.lineStyle
                )

                # outlet crossed - mirror
                inkDraw.line.relCoords(
                    elem, [[0, - self.connectorLength]],
                    [position[0] + self.componentExtent * 1.5,
                    position[1] - self.componentExtent / 2],
                    lineStyle=self.lineStyle
                )

        if connection == 'equal':
            if mirroring == 'mirOff':
                # inlet equal - no mirror
                inkDraw.line.relCoords(
                    elem, [[0, self.connectorLength]],
                    [position[0],
                    position[1] + self.componentExtent * 1.5],
                    lineStyle=self.lineStyle
                )

                # outlet equal - no mirror
                inkDraw.line.relCoords(
                    elem, [[0, self.connectorLength]],
                    [position[0] + self.componentExtent * 1.5,
                    position[1] + self.componentExtent * 2],
                    lineStyle=self.lineStyle
                )

            if mirroring == 'mirOn':
                # inlet equal - mirror
                inkDraw.line.relCoords(
                    elem, [[0, - self.connectorLength]],
                    position,
                    lineStyle=self.lineStyle
                )

                # outlet equal - mirror
                inkDraw.line.relCoords(
                    elem, [[0, - self.connectorLength]],
                    [position[0] + self.componentExtent * 1.5,
                    position[1] - self.componentExtent / 2],
                    lineStyle=self.lineStyle
                )

        if extraction == 'extrTop':
            inkDraw.line.relCoords(
                elem, [[0, - self.connectorLength]],
                [position[0] + self.connectorLength * 1.5,
                position[1] - self.connectorLength / 2],
                lineStyle=self.lineStyle
            )

        if extraction == 'extrDown':
            inkDraw.line.relCoords(
                elem, [[0, + self.connectorLength]],
                [position[0] + self.connectorLength * 1.5,
                position[1] + self.componentExtent * 1.5
                 + self.connectorLength / 2],
                lineStyle=self.lineStyle
            )

        return group
