#!/usr/bin/python

import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw

from drawRIComponents import component

from numpy import sqrt, sin, cos, pi


class heat_exchanger(component):
    # ---------------------------------------------
    def drawGeneric(self, parent, position=[0, 0], label='Heat Exchanger',
                    direction='right', angleDeg=0,
                    heat_exchangerType='generic'):
        """Draw a heat exchanger.

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

        # draw upper connector
        inkDraw.line.relCoords(
            elem, [[0, - self.connectorLength]],
            [position[0] + self.radius, position[1] - self.radius],
            lineStyle=self.lineStyle)

        # draw lower connector
        inkDraw.line.relCoords(
            elem, [[0, self.connectorLength]],
            [position[0] + self.radius, position[1] + self.radius],
            lineStyle=self.lineStyle)

        # change direction to the users choice
        if direction == 'right':
            # draw upper diagonal line
            inkDraw.line.relCoords(
                elem, [[self.componentExtent / 3,
                        - self.componentExtent / 4]],
                [position[0] + self.componentExtent / 3, position[1]],
                lineStyle=self.lineStyle)

            # draw upper horizontal line + connector
            inkDraw.line.relCoords(
                elem,
                [[self.connectorLength + self.componentExtent * 4 / 6, 0]],
                [position[0] - self.connectorLength,
                 position[1] - self.componentExtent / 4],
                lineStyle=self.lineStyle)

            # draw lower diagonal line
            inkDraw.line.relCoords(
                elem, [[self.componentExtent / 3,
                        self.componentExtent / 4]],
                [position[0] + self.componentExtent / 3, position[1]],
                lineStyle=self.lineStyle)

            # draw lower horizontal line + connector
            inkDraw.line.relCoords(
                elem,
                [[self.connectorLength + self.componentExtent * 4 / 6, 0]],
                [position[0] - self.connectorLength,
                 position[1] + self.componentExtent / 4],
                lineStyle=self.lineStyle)

            # adjust label position
            text_x_offset = (position[0] + self.componentExtent
                             + self.connectorLength)
            just = 'left'

        elif direction == 'left':
            # draw upper diagonal line
            inkDraw.line.relCoords(
                elem, [[- self.componentExtent / 3,
                        - self.componentExtent / 4]],
                [position[0] + self.componentExtent * 2 / 3, position[1]],
                lineStyle=self.lineStyle)

            # draw upper horizontal line + connector
            inkDraw.line.relCoords(
                elem,
                [[self.connectorLength + self.componentExtent * 4 / 6, 0]],
                [position[0] + self.componentExtent / 3,
                 position[1] - self.componentExtent / 4],
                lineStyle=self.lineStyle)

            # draw lower diagonal line
            inkDraw.line.relCoords(
                elem, [[- self.componentExtent / 3,
                        self.componentExtent / 4]],
                [position[0] + self.componentExtent * 2 / 3, position[1]],
                lineStyle=self.lineStyle)

            # draw lower horizontal line + connector
            inkDraw.line.relCoords(
                elem,
                [[self.connectorLength + self.componentExtent * 4 / 6, 0]],
                [position[0] + self.componentExtent / 3,
                 position[1] + self.componentExtent / 4],
                lineStyle=self.lineStyle)

            # adjust label position
            text_x_offset = position[0] - self.connectorLength
            just = 'right'

        # change rotation to user defined angle
        if angleDeg != 0:
            self.rotateElement(group, position, angleDeg)

        pos_text = [text_x_offset, position[1]]

        inkDraw.text.write(
            self, label, pos_text, group, fontSize=self.fontSize,
            justification=just, textStyle=self.textStyle
        )

        return group

    def drawGenericX(self, parent, position=[0, 0], label='Heat Exchanger',
                     direction='right', angleDeg=0,
                     heat_exchangerType='generic'):
        """Draw a heat exchanger.

        parent: parent object
        position: position [x,y]

        label: label of the object (it can be repeated)
        angleDeg: rotation angle in degrees counter-clockwise (default 0)
        """
        group = self.createGroup(parent, label)
        elem = self.createGroup(group)

        # draw main square
        # left vertical line
        inkDraw.line.relCoords(
            elem, [[0, - self.componentExtent]],
            [position[0], position[1] + self.componentExtent / 2],
            lineStyle=self.lineStyle)

        # right vertical line
        inkDraw.line.relCoords(
            elem, [[0, - self.componentExtent]],
            [position[0] + self.componentExtent,
             position[1] + self.componentExtent / 2],
            lineStyle=self.lineStyle)

        # upper horizontal line
        inkDraw.line.relCoords(
            elem, [[self.componentExtent, 0]],
            [position[0], position[1] - self.componentExtent / 2],
            lineStyle=self.lineStyle)

        # lower horizontal line
        inkDraw.line.relCoords(
            elem, [[self.componentExtent, 0]],
            [position[0], position[1] + self.componentExtent / 2],
            lineStyle=self.lineStyle)

        # draw connectors
        # left connector
        inkDraw.line.relCoords(
            elem, [[- self.connectorLength, 0]], position,
            lineStyle=self.lineStyle)

        # right connector
        inkDraw.line.relCoords(
            elem, [[self.connectorLength, 0]],
            [position[0] + self.componentExtent, position[1]],
            lineStyle=self.lineStyle)

        # upper connector
        inkDraw.line.relCoords(
            elem, [[0, - self.connectorLength]],
            [position[0] + self.componentExtent / 2,
             position[1] - self.componentExtent / 2],
            lineStyle=self.lineStyle)

        # lower connector
        inkDraw.line.relCoords(
            elem, [[0, self.connectorLength]],
            [position[0] + self.componentExtent / 2,
             position[1] + self.componentExtent / 2],
            lineStyle=self.lineStyle)

        # draw heat receiving medium
        # centered vertical line
        inkDraw.line.relCoords(
            elem, [[0, - self.componentExtent / 3 * 2]],
            [position[0] + self.componentExtent / 2,
             position[1] + self.componentExtent / 3],
            lineStyle=self.lineStyle)

        # change direction to the users choice
        if direction == 'right':

            # left diagonal line
            inkDraw.line.relCoords(
                elem, [[self.componentExtent / 2, - self.componentExtent / 3]],
                position, lineStyle=self.lineStyle)

            # right diagonal line
            inkDraw.line.relCoords(
                elem, [[self.componentExtent / 2, - self.componentExtent / 3]],
                [position[0] + self.componentExtent / 2,
                 position[1] + self.componentExtent / 3],
                lineStyle=self.lineStyle)

            # adjust label position
            text_x_offset = position[0] - self.connectorLength / 2

        elif direction == 'left':

            # left diagonal line
            inkDraw.line.relCoords(
                elem, [[self.componentExtent / 2, self.componentExtent / 3]],
                position, lineStyle=self.lineStyle)

            # right diagonal line
            inkDraw.line.relCoords(
                elem, [[self.componentExtent / 2, self.componentExtent / 3]],
                [position[0] + self.componentExtent / 2,
                 position[1] - self.componentExtent / 3],
                lineStyle=self.lineStyle)

            # adjust label position
            text_x_offset = (position[0] + self.componentExtent
                             + self.connectorLength / 2)

        # change rotation to user defined angle
        if angleDeg != 0:
            self.rotateElement(group, position, angleDeg)

        pos_text = [text_x_offset,
                    (position[1] - self.componentExtent / 2
                     - self.connectorLength / 2)]

        inkDraw.text.write(
            self, label, pos_text, group, fontSize=self.fontSize,
            justification=direction, textStyle=self.textStyle
        )

        return group
