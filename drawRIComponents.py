#!/usr/bin/python

import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw


class component(inkBase.inkscapeMadeEasy):
    # ---------------------------------------------
    def setDimensions(self, lineStyle=inkDraw.lineStyle.set(0.5),
                      connectorLength=5, componentExtent=10, scale=1):
        """Set the dimensions of a component.

        lineStyle: linestyle
        connectorLength: length of the connectors
        componentExtent: base extent of the component
        scale: scaling factor (integer values >0 only)
        """
        self.lineStyle = lineStyle
        self.connectorLength = connectorLength * scale
        self.componentExtent = componentExtent * scale
        self.scale = scale
