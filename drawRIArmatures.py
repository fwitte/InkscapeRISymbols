#!/usr/bin/python

import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw

from drawRIComponents import component


class armature(component):
    # ---------------------------------------------
    def drawValve(self, parent, position=[0, 0], label='Valve',
                  direction='right', angleDeg=0, armatureType='valve'):
        """Draw a valve.

        parent: parent object
        position: position [x,y]

        label: label of the object (it can be repeated)
        angleDeg: rotation angle in degrees counter-clockwise (default 0)
        """
        group = self.createGroup(parent, label)
        elem = self.createGroup(group)

        inkDraw.line.relCoords(
            elem, [[self.connectorLength, 0]], position,
            lineStyle=self.lineStyle)

        inkDraw.line.relCoords(
            elem, [[0, self.componentExtent / 2]],
            [position[0] + self.connectorLength,
             position[1] - self.componentExtent / 4],
            lineStyle=self.lineStyle
        )

        inkDraw.line.relCoords(
            elem, [[self.componentExtent, -self.componentExtent / 2]],
            [position[0] + self.connectorLength,
             position[1] + self.componentExtent / 4],
            lineStyle=self.lineStyle
        )

        inkDraw.line.relCoords(
            elem, [[self.componentExtent, self.componentExtent / 2]],
            [position[0] + self.connectorLength,
             position[1] - self.componentExtent / 4],
            lineStyle=self.lineStyle
        )

        inkDraw.line.relCoords(
            elem, [[0, self.componentExtent / 2]],
            [position[0] + self.connectorLength + self.componentExtent,
             position[1] - self.componentExtent / 4],
            lineStyle=self.lineStyle
        )

        inkDraw.line.relCoords(
            elem, [[self.connectorLength, 0]],
            [position[0] + self.connectorLength + self.componentExtent,
             position[1]],
            lineStyle=self.lineStyle)

        if armatureType == 'three way valve':
            inkDraw.line.relCoords(
                elem, [[self.componentExtent / 2, 0]],
                [position[0] + self.connectorLength + self.componentExtent / 4,
                 position[1] + self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            inkDraw.line.relCoords(
                elem, [[self.componentExtent / 4, - self.componentExtent / 2]],
                [position[0] + self.connectorLength + self.componentExtent / 4,
                 position[1] + self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            inkDraw.line.relCoords(
                elem, [[- self.componentExtent / 4,
                        - self.componentExtent / 2]],
                [position[0] + self.connectorLength + self.componentExtent
                 / 4 * 3,
                 position[1] + self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            inkDraw.line.relCoords(
                elem, [[0, self.componentExtent / 2]],
                [position[0] + self.connectorLength + self.componentExtent / 2,
                 position[1] + self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

        if armatureType == 'ball valve':
            inkDraw.circle.centerRadius(
                elem, [self.connectorLength + self.componentExtent / 2, 0],
                self.scale * 0.5, offset=position, label='circle',
                lineStyle=inkDraw.lineStyle.set(fillColor='#000000')
            )

        if armatureType == 'check valve':
            inkDraw.circle.centerRadius(
                elem, [self.connectorLength + self.componentExtent / 2, 0],
                self.scale * 0.5, offset=position, label='circle',
                lineStyle=inkDraw.lineStyle.set(fillColor='#000000')
            )

            if direction == 'right':
                inkDraw.circle.centerRadius(
                    elem, [self.connectorLength, - self.componentExtent / 4],
                    self.scale * 0.5, offset=position, label='circle',
                    lineStyle=inkDraw.lineStyle.set(fillColor='#000000')
                )
            elif direction == 'left':
                inkDraw.circle.centerRadius(
                    elem, [self.connectorLength + self.componentExtent,
                           - self.componentExtent / 4],
                    self.scale * 0.5, offset=position, label='circle',
                    lineStyle=inkDraw.lineStyle.set(fillColor='#000000')
                )

        if armatureType == 'three way ball valve':
            inkDraw.line.relCoords(
                elem, [[self.componentExtent / 2, 0]],
                [position[0] + self.connectorLength + self.componentExtent / 4,
                 position[1] + self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            inkDraw.line.relCoords(
                elem, [[self.componentExtent / 4, - self.componentExtent / 2]],
                [position[0] + self.connectorLength + self.componentExtent / 4,
                 position[1] + self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            inkDraw.line.relCoords(
                elem, [[- self.componentExtent / 4,
                        - self.componentExtent / 2]],
                [position[0] + self.connectorLength + self.componentExtent
                 / 4 * 3,
                 position[1] + self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            inkDraw.line.relCoords(
                elem, [[0, self.componentExtent / 2]],
                [position[0] + self.connectorLength + self.componentExtent / 2,
                 position[1] + self.componentExtent / 2],
                lineStyle=self.lineStyle
            )

            inkDraw.circle.centerRadius(
                elem, [self.connectorLength + self.componentExtent / 2, 0],
                self.scale * 0.5, offset=position, label='circle',
                lineStyle=inkDraw.lineStyle.set(fillColor='#000000')
            )

        if armatureType == 'gate valve':
            inkDraw.line.relCoords(
                elem, [[0, - self.componentExtent / 2]],
                [position[0] + self.connectorLength + self.componentExtent / 2,
                 position[1] + self.componentExtent / 4],
                lineStyle=self.lineStyle
            )

        if angleDeg != 0:
            self.rotateElement(group, position, angleDeg)

        pos_text = [
            position[0] + self.connectorLength + self.componentExtent / 2,
            position[1] - self.componentExtent / (4 * self.scale) -
            self.textOffset * self.scale]

        inkDraw.text.write(
            self, label, pos_text, group, fontSize=self.fontSize,
            justification='center', textStyle=self.textStyle
        )

        return group

    # ---------------------------------------------
    def drawExpansionValve(self, parent, position=[0, 0],
                           label='Expansion Valve', direction='right',
                           angleDeg=0):
        """Draw an expansion valve.

        parent: parent object
        position: position [x,y]

        label: label of the object (it can be repeated)
        angleDeg: rotation angle in degrees counter-clockwise (default 0)
        """
        group = self.createGroup(parent, label)
        elem = self.createGroup(group)

        # draw component orientation based on users choice
        if direction == 'right':
            # draw left vertical line
            inkDraw.line.relCoords(
                elem, [[0, self.componentExtent / 3]],
                [position[0] + self.connectorLength,
                 position[1] - self.componentExtent / 6],
                lineStyle=self.lineStyle
            )

            # draw right vertical line
            inkDraw.line.relCoords(
                elem, [[0, self.componentExtent / 3 * 2]],
                [position[0] + self.connectorLength + self.componentExtent,
                 position[1] - self.componentExtent / 3],
                lineStyle=self.lineStyle
            )

            # draw ascending diagonal
            inkDraw.line.relCoords(
                elem, [[self.componentExtent, -self.componentExtent / 2]],
                [position[0] + self.connectorLength,
                 position[1] + self.componentExtent / 6],
                lineStyle=self.lineStyle
            )

            # draw decending diagonal
            inkDraw.line.relCoords(
                elem, [[self.componentExtent, self.componentExtent / 2]],
                [position[0] + self.connectorLength,
                 position[1] - self.componentExtent / 6],
                lineStyle=self.lineStyle
            )

        elif direction == 'left':
            # draw left vertical line
            inkDraw.line.relCoords(
                elem, [[0, self.componentExtent / 3 * 2]],
                [position[0] + self.connectorLength,
                 position[1] - self.componentExtent / 3],
                lineStyle=self.lineStyle
            )

            # draw right vertical line
            inkDraw.line.relCoords(
                elem, [[0, self.componentExtent / 3]],
                [position[0] + self.connectorLength + self.componentExtent,
                 position[1] - self.componentExtent / 6],
                lineStyle=self.lineStyle
            )

            # draw ascending diagonal
            inkDraw.line.relCoords(
                elem, [[self.componentExtent, -self.componentExtent / 2]],
                [position[0] + self.connectorLength,
                 position[1] + self.componentExtent / 3],
                lineStyle=self.lineStyle
            )

            # draw decending diagonal
            inkDraw.line.relCoords(
                elem, [[self.componentExtent, self.componentExtent / 2]],
                [position[0] + self.connectorLength,
                 position[1] - self.componentExtent / 3],
                lineStyle=self.lineStyle
            )

        # draw left connector
        inkDraw.line.relCoords(
            elem, [[self.connectorLength, 0]], position,
            lineStyle=self.lineStyle)

        # draw right connector
        inkDraw.line.relCoords(
            elem, [[self.connectorLength, 0]],
            [position[0] + self.connectorLength + self.componentExtent,
             position[1]],
            lineStyle=self.lineStyle)

        # rotate component depending on users choice
        if angleDeg != 0:
            self.rotateElement(group, position, angleDeg)

        # label position
        pos_text = [
            position[0] + self.connectorLength + self.componentExtent / 2,
            position[1] - self.componentExtent / (4 * self.scale) -
            self.textOffset * self.scale]

        # draw label
        inkDraw.text.write(
            self, label, pos_text, group, fontSize=self.fontSize,
            justification='center', textStyle=self.textStyle
        )

        return group
