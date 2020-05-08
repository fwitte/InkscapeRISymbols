#!/usr/bin/python

import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw

from drawRIComponents import component

from numpy import sqrt, sin, cos, pi


class node(component):
    # ---------------------------------------------
    def drawBasic(self, parent, position=[0, 0], label='Node',
                 direction='right', angleDeg=0, nodeType='node'):
        """Draw a source, sink and cyclecloser.

        parent: parent object
        position: position [x,y]

        label: label of the object (it can be repeated)
        angleDeg: rotation angle in degrees counter-clockwise (default 0)
        """
        group = self.createGroup(parent, label)
        elem = self.createGroup(group)

        if nodeType == 'source':
            # left side
            inkDraw.line.relCoords(
                elem, [[0, self.componentExtent]],
                [position[0],position[1] - self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            # diagonally top right
            inkDraw.line.relCoords(
                elem, [[self.componentExtent, - self.componentExtent / 2]],
                [position[0], position[1] + self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            # diagonally down left
            inkDraw.line.relCoords(
                elem, [[self.componentExtent, self.componentExtent / 2]],
                [position[0], position[1] - self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            # connector right
            inkDraw.line.relCoords(
                elem, [[self.connectorLength, 0]],
                [position[0] + self.componentExtent, position[1]],
                lineStyle=self.lineStyle
                )

        elif nodeType == 'sink':
            # left side
            inkDraw.line.relCoords(
                elem, [[0, self.componentExtent]],
                [position[0] + self.componentExtent * 1.5,
                position[1] - self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            # diagonally top right
            inkDraw.line.relCoords(
                elem, [[self.componentExtent, - self.componentExtent / 2]],
                [position[0] + self.connectorLength, position[1]],
                lineStyle=self.lineStyle
            )

            # diagonally down left
            inkDraw.line.relCoords(
                elem, [[self.componentExtent, self.componentExtent / 2]],
                [position[0] + self.connectorLength, position[1]],
                lineStyle=self.lineStyle
            )

            # connector right
            inkDraw.line.relCoords(
                elem, [[self.connectorLength, 0]],
                position,
                lineStyle=self.lineStyle
            )

        elif nodeType == 'cyclecloser':
            # construction like a source
            # left side
            inkDraw.line.relCoords(
                elem, [[0, self.componentExtent]],
                [position[0],position[1] - self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            # diagonally top right
            inkDraw.line.relCoords(
                elem, [[self.componentExtent, - self.componentExtent / 2]],
                [position[0], position[1] + self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            # diagonally down left
            inkDraw.line.relCoords(
                elem, [[self.componentExtent, self.componentExtent / 2]],
                [position[0], position[1] - self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            # connector right
            inkDraw.line.relCoords(
                elem, [[self.connectorLength, 0]],
                [position[0] + self.componentExtent, position[1]],
                lineStyle=self.lineStyle
                )

            # feature cc
            # left side
            inkDraw.line.relCoords(
                elem, [[0, self.componentExtent]],
                [position[0] - self.componentExtent,
                position[1] - self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            # diagonally top right
            inkDraw.line.relCoords(
                elem, [[self.componentExtent, - self.componentExtent / 2]],
                [position[0] - self.componentExtent,
                position[1] + self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            # diagonally down left
            inkDraw.line.relCoords(
                elem, [[self.componentExtent, self.componentExtent / 2]],
                [position[0] - self.componentExtent,
                 position[1] - self.componentExtent / 2],
                lineStyle=self.lineStyle
            )
            
            # connector right
            inkDraw.line.relCoords(
                elem, [[- self.connectorLength, 0]],
                [position[0] - self.componentExtent, position[1]],
                lineStyle=self.lineStyle
            )

        return group

    # ---------------------------------------------
    def drawNode(self, parent, position=[0, 0], label='Node',
                 direction='right', angleDeg=0, nodeType='node'):
        """Draw a node.

        parent: parent object
        position: position [x,y]

        label: label of the object (it can be repeated)
        angleDeg: rotation angle in degrees counter-clockwise (default 0)
        """
        group = self.createGroup(parent, label)
        elem = self.createGroup(group)

        # create node
        inkDraw.circle.centerRadius(
            elem, [0, 0],
            self.scale * 0.5, offset=position, label='circle',
            lineStyle=inkDraw.lineStyle.set(fillColor='#000000')
        )

        # connector left
        inkDraw.line.relCoords(
            elem, [[- self.connectorLength, 0]], position,
            lineStyle=self.lineStyle
            )

        # connector right
        inkDraw.line.relCoords(
            elem, [[self.connectorLength, 0]], position,
            lineStyle=self.lineStyle
            )

        # connector up
        inkDraw.line.relCoords(
            elem, [[0, - self.connectorLength]], position,
            lineStyle=self.lineStyle)

        # connector down
        inkDraw.line.relCoords(
            elem, [[0, self.connectorLength]], position,
            lineStyle=self.lineStyle)

        return group

    # ---------------------------------------------
    def drawDrum(self, parent, position=[0, 0], label='Drum',
                 direction='right', angleDeg=0, nodeType='drum'):
        """Draw a drum.

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

        # draw horizontal diameter
        inkDraw.line.relCoords(
            elem, [[self.componentExtent, 0]], position,
            lineStyle=self.lineStyle)

        # draw upper vertical connector
        inkDraw.line.relCoords(
            elem, [[0, - self.connectorLength]],
            [position[0] + self.radius, position[1] - self.radius],
            lineStyle=self.lineStyle)

        # draw lower vertical connector
        inkDraw.line.relCoords(
            elem, [[0, self.connectorLength]],
            [position[0] + self.radius, position[1] + self.radius],
            lineStyle=self.lineStyle)

        # change direction to the users choice
        if direction == 'right':
            # draw upper diagonal connector
            inkDraw.line.relCoords(
                elem, [[sqrt(2)/2 * self.connectorLength,
                        - sqrt(2)/2 * self.connectorLength]],
                [position[0] + self.radius * (1 + cos(pi/4)),
                 position[1] - self.radius * sin(pi/4)],
                lineStyle=self.lineStyle)

            # draw lower diagonal connector
            inkDraw.line.relCoords(
                elem, [[sqrt(2)/2 * self.connectorLength,
                        sqrt(2)/2 * self.connectorLength]],
                [position[0] + self.radius * (1 + cos(pi/4)),
                 position[1] + self.radius * sin(pi/4)],
                lineStyle=self.lineStyle)

            # change label position depending on chosen direction
            text_x_offset = (position[0] - self.connectorLength)

        elif direction == 'left':
            # draw upper diagonal connector
            inkDraw.line.relCoords(
                elem, [[- sqrt(2)/2 * self.connectorLength,
                        - sqrt(2)/2 * self.connectorLength]],
                [position[0] + self.radius * (1 - cos(pi/4)),
                 position[1] - self.radius * sin(pi/4)],
                lineStyle=self.lineStyle)

            # draw lower diagonal connector
            inkDraw.line.relCoords(
                elem, [[- sqrt(2)/2 * self.connectorLength,
                        sqrt(2)/2 * self.connectorLength]],
                [position[0] + self.radius * (1 - cos(pi/4)),
                 position[1] + self.radius * sin(pi/4)],
                lineStyle=self.lineStyle)

            # change label position depending on chosen direction
            text_x_offset = (position[0]
                             + self.componentExtent
                             + self.connectorLength)

        # change rotation to user defined angle
        if angleDeg != 0:
            self.rotateElement(group, position, angleDeg)

        pos_text = [text_x_offset, position[1]]

        inkDraw.text.write(
            self, label, pos_text, group, fontSize=self.fontSize,
            justification=direction, textStyle=self.textStyle
        )

        return group
