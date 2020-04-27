#!/usr/bin/python

import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw

from drawRIComponents import component


class pump(component):
    # ---------------------------------------------
    def drawPump(self, parent, position=[0, 0], label='Pump',
                 direction='right', angleDeg=0,
                 pumpType='generic'):
        """Draw a generic pump.

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
            [position[0] + self.connectorLength + self.radius * 2, position[1]],
            lineStyle=self.lineStyle
        )

        dx = 0.9 * self.radius
        dy = np.cos(np.arcsin(0.1)) * self.radius

        if direction == 'left':
            inkDraw.line.relCoords(
                elem, [[dx, dy]],
                [position[0] + self.connectorLength, position[1]],
                lineStyle=self.lineStyle
            )
            inkDraw.line.relCoords(
                elem, [[dx, -dy]],
                [position[0] + self.connectorLength, position[1]],
                lineStyle=self.lineStyle
            )
        elif direction == 'right':
            inkDraw.line.relCoords(
                elem, [[-dx, dy]],
                [position[0] + self.connectorLength + self.componentExtent, position[1]],
                lineStyle=self.lineStyle
            )
            inkDraw.line.relCoords(
                elem, [[-dx, -dy]],
                [position[0] + self.connectorLength + self.componentExtent, position[1]],
                lineStyle=self.lineStyle
            )

        self.drawPumpTypeSymbol(elem, direction, position, pumpType)

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

    def drawPumpTypeSymbol(self, elem, direction, position, pumpType):
        """Draw the symbol for the type of the pump.

        elem: elemnt group
        direction: direction the pump is facing
        position: position [x, y]
        pumpType: Type of the pump
        """

        if pumpType == 'centrifugal':
            inkDraw.line.relCoords(
                elem, [[self.componentExtent, 0]],
                [position[0] + self.connectorLength, position[1]],
                lineStyle=self.lineStyle)
            return

        if direction == 'left':
            if pumpType == 'piston':
                inkDraw.line.relCoords(
                    elem, [[-self.radius / 2, 0]],
                    [
                        position[0] + self.connectorLength + self.radius,
                        position[1]
                    ], lineStyle=self.lineStyle)
                inkDraw.line.relCoords(
                    elem, [[0, self.radius / 2]],
                    [
                        position[0] + self.connectorLength + self.radius,
                        position[1] - self.radius / 4],
                    lineStyle=self.lineStyle)

            elif pumpType == 'membrane':
                arcradius = self.componentExtent * 0.75
                inkDraw.arc.startEndRadius(
                    elem, [0, self.radius], [0, -self.radius], arcradius,
                    [
                        position[0] + self.connectorLength + self.radius,
                        position[1]
                    ], lineStyle=self.lineStyle
                )

        elif direction == 'right':
            if pumpType == 'piston':
                inkDraw.line.relCoords(
                    elem, [[self.radius / 2, 0]],
                    [
                        position[0] + self.connectorLength + self.radius,
                        position[1]
                    ], lineStyle=self.lineStyle)
                inkDraw.line.relCoords(
                    elem, [[0, self.radius / 2]],
                    [
                        position[0] + self.connectorLength + self.radius,
                        position[1] - self.radius / 4],
                    lineStyle=self.lineStyle)

            elif pumpType == 'membrane':
                arcradius = self.componentExtent * 0.75
                inkDraw.arc.startEndRadius(
                    elem, [0, self.radius], [0, -self.radius], arcradius,
                    [
                        position[0] + self.connectorLength + self.radius,
                        position[1]
                    ],
                    lineStyle=self.lineStyle, flagRightOf=False
                )
